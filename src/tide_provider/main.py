import csv
import dataclasses
import os
import re
from datetime import date, datetime, time, timedelta, timezone, tzinfo
from enum import Enum, IntEnum
from pathlib import Path
from typing import Optional, Self

from tide_provider.api import ApiClient, TidalDataExtremum

# Input example: "+ 1:00"
timezone_modifier_pattern = re.compile(
    r"^(?P<operator>[+-])\s*(?P<hours>\d+):(?P<minutes>\d+)$"
)


class LineCode(Enum):
    WithoutHeights = "VB1"
    WithHeights = "VB2"


@dataclasses.dataclass
class GaugeNumber:
    country_code: str
    underline: str
    # while this column (8) should be a number by definition, it's usually an underline
    number_or_underline: str
    number: int
    letter_or_underline: str

    @classmethod
    def from_str(cls, s: str):
        return cls(
            country_code=s[0:2],
            underline=s[2],
            number_or_underline=s[3],
            number=int(s[4:7]),
            letter_or_underline=s[7],
        )


class MoonPhase(IntEnum):
    NewMoon = 0
    FirstQuarterMoon = 1
    FullMoon = 2
    LastQuarterMoon = 3


# We're ignoring `K` since we're never downloading curve data
class WaterLevel(Enum):
    # Niedrigwasser
    LowWater = "N"
    # Hochwasser
    HighWater = "H"


class DayOfTheWeek(Enum):
    Monday = "Mo"
    Tuesday = "Di"
    Wednesday = "Mi"
    Thursday = "Do"
    Friday = "Fr"
    Saturday = "Sa"
    Sunday = "So"


def parse_date(s: str) -> date:
    clean = s.replace(" ", "")
    return datetime.strptime(clean, "%d.%m.%Y").date()


def parse_time(s: str) -> time:
    # hours are not 0 padded
    return datetime.strptime(s.replace(" ", "0"), "%H:%M").time()


def parse_timezone_info(timezone_modifier: str) -> tzinfo:
    match = timezone_modifier_pattern.match(timezone_modifier)
    if match is None:
        raise ValueError(f"Invalid timezone_modifier: {timezone_modifier}")

    delta = timedelta(
        hours=int(match.group("hours")),
        minutes=int(match.group("minutes")),
    )

    if match.group("operator") == "-":
        delta = -delta

    return timezone(offset=delta)


@dataclasses.dataclass
class TimeZoneModifier:
    modifier: str

    @classmethod
    def from_str(cls, s: str) -> Self:
        return cls(modifier=s.replace(" ", ""))


class TransitDirection(IntEnum):
    HighWaterUpperTransit = 1
    LowWaterUpperTransit = 2
    HighWaterLowerTransit = 3
    LowWaterLowerTransit = 4


@dataclasses.dataclass
class TideInformation:
    line_code: LineCode
    gauge_number: GaugeNumber
    moon_phase: Optional[MoonPhase]
    water_level: WaterLevel
    day_of_the_week: DayOfTheWeek
    date: date
    time: time
    height: str
    # can be between 1 - 7, should this be an `Enum` with self-made names?
    quality: Optional[int]
    day_of_the_year: int
    timezone_info: tzinfo
    transit_number: int
    transit_direction: TransitDirection
    julian_date: float

    @classmethod
    def from_row(cls, _row: list[str]) -> Self:
        moon_phase = MoonPhase(int(_row[2].strip())) if _row[2].strip() else None
        quality = int(_row[8].strip()) if _row[8].strip() else None

        return cls(
            line_code=LineCode(_row[0]),
            gauge_number=GaugeNumber.from_str(_row[1]),
            moon_phase=moon_phase,
            water_level=WaterLevel(_row[3]),
            day_of_the_week=DayOfTheWeek(_row[4]),
            date=parse_date(_row[5]),
            time=parse_time(_row[6]),
            height=_row[7].strip(),
            quality=quality,
            day_of_the_year=int(_row[9].strip()),
            timezone_info=parse_timezone_info(_row[10]),
            transit_number=int(_row[11].strip()),
            transit_direction=TransitDirection(int(_row[12].strip())),
            julian_date=float(_row[13].strip()),
        )

    @property
    def datetime(self) -> datetime:
        return datetime.combine(
            self.date,
            self.time,
            self.timezone_info,
        )

    def to_dto(self) -> TidalDataExtremum:
        return {
            "isHighTide": self.water_level == WaterLevel.HighWater,
            "time": self.datetime.astimezone(timezone.utc).isoformat(),
            "height": self.height,
        }


def parse_info(file_path: Path) -> list[TideInformation]:
    infos = []
    with open(file_path, encoding="ISO-8859-1") as f:
        spamreader = csv.reader(f, delimiter="#")
        seen_data_delim = False
        for row in spamreader:
            if "EEE" in row:
                # signalizes the end
                break
            elif seen_data_delim and row:
                infos.append(TideInformation.from_row(row))
            else:
                seen_data_delim = "LLL" in row

    return infos


def find_lowest_height_info_index(infos: list) -> int:
    lowest = float(infos[0]["height"])
    lowest_index = 0
    for idx, info in enumerate(infos):
        height = float(info["height"])
        if height < lowest:
            lowest = height
            lowest_index = idx

    return lowest_index


def parse_canada_info(file_path: Path) -> list[TidalDataExtremum]:
    infos = []
    with open(file_path, encoding="UTF-8") as f:
        spamreader = csv.reader(f, delimiter=",")
        is_first_line = True
        for row in spamreader:
            if is_first_line:
                is_first_line = False
                continue
            dt = datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S")
            isotime = dt.astimezone(timezone.utc).isoformat()
            height = row[1]
            infos.append({"time": isotime, "height": height})

    is_high_tide = find_lowest_height_info_index(infos) % 2 == 1
    for info in infos:
        info["isHighTide"] = is_high_tide
        is_high_tide = not is_high_tide

    # PyCharm can't (reliably) detect the later addition of the `isHighTide` field
    # noinspection PyTypeChecker
    return infos


def main():
    print(*parse_info(Path("resources/cuxhaven_2023.txt")), sep="\n")


def publish():
    token = os.getenv("WOOG_API_TOKEN")
    if not token:
        raise ValueError("Missing WOOG_API_TOKEN env var")

    resources = Path("resources")
    with ApiClient(token) as client:
        for lake_id, file_name in (
            ("d074654c-dedd-46c3-8042-af55c93c910e", "cuxhaven_2023.txt"),
            ("18e6931a-3729-4ad9-8301-03c5980f82b6", "husum_2023.txt"),
        ):
            infos = parse_info(resources / file_name)
            print(
                "Uploading data from",
                file_name,
                "(This will take about a minutes)",
            )
            client.push_tidal_data(lake_id, [info.to_dto() for info in infos])


if __name__ == "__main__":
    main()
