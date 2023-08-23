import csv
import dataclasses
from datetime import datetime
from enum import IntEnum, Enum
from typing import Self, Optional


class LineCode(Enum):
    # data without heights
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


@dataclasses.dataclass
class Date:
    date: datetime

    @classmethod
    def from_str(cls, s: str) -> Self:
        clean: str = s.replace(" ", "")
        return cls(date=datetime.strptime(clean, "%d.%m.%Y"))


@dataclasses.dataclass
class Time:
    time: datetime

    @classmethod
    def from_str(cls, s: str) -> Self:
        # hours are not 0 padded
        return cls(time=datetime.strptime(s.replace(" ", "0"), "%H:%M"))


@dataclasses.dataclass
class TimeZoneModifier:
    modifier: str

    @classmethod
    def from_str(cls, s: str) -> Self:
        return cls(modifier=s.replace(" ", ""))


class TransitDirection(IntEnum):
    HighWaterUpperTransit = 1
    LowWaterUpperTransit = 2
    HightWaterLowerTransit = 3
    LowWaterLowerTransit = 4


@dataclasses.dataclass
class TideInformation:
    line_code: LineCode
    # honestly, no idea. empty in the example data
    gauge_number: GaugeNumber
    moon_phase: Optional[MoonPhase]
    water_level: WaterLevel
    day_of_the_week: DayOfTheWeek
    date: Date
    time: Time
    height: float
    # can be between 1 - 7, should this be an `Enum` with self-made names?
    quality: Optional[int]
    day_of_the_year: int
    time_zone_modifier: TimeZoneModifier
    transit_number: int
    transit_direction: TransitDirection
    julian_date: float

    @classmethod
    def from_row(cls, _row: list[str]):
        moon_phase = MoonPhase(int(_row[2].strip())) if _row[2].strip() else None
        quality = int(_row[8].strip()) if _row[8].strip() else None

        return cls(
            line_code=LineCode(_row[0]),
            gauge_number=GaugeNumber.from_str(_row[1]),
            moon_phase=moon_phase,
            water_level=WaterLevel(_row[3]),
            day_of_the_week=DayOfTheWeek(_row[4]),
            date=Date.from_str(_row[5]),
            time=Time.from_str(_row[6]),
            height=float(_row[7].strip()),
            quality=quality,
            day_of_the_year=int(_row[9].strip()),
            time_zone_modifier=TimeZoneModifier.from_str(_row[10]),
            transit_number=int(_row[11].strip()),
            transit_direction=TransitDirection(int(_row[12].strip())),
            julian_date=float(_row[13].strip()),
        )


infos = []
with open("resources/cuxhaven_2023.txt", encoding="ISO-8859-1") as f:
    spamreader = csv.reader(f, delimiter="#")
    seen_data_delim = False
    for row in spamreader:
        if "EEE" in row:
            # signalises the end
            break
        elif seen_data_delim and row:
            infos.append(TideInformation.from_row(row))
        else:
            seen_data_delim = "LLL" in row

print(*infos, sep="\n")
