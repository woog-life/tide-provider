import dataclasses
from pathlib import Path

import pytest
from tide_provider.main import parse_info


@pytest.mark.parametrize(
    "filename,item_count",
    [
        ("cuxhaven_2023.txt", 1411),
        ("husum_2023.txt", 1411),
    ],
)
def test_parse_resources(filename: str, item_count: int):
    path = Path("resources") / filename

    data = parse_info(path)
    assert isinstance(data, list)
    assert len(data) == item_count

    # Inspect a random sample
    item = data[420]

    for field in dataclasses.fields(item):
        name = field.name

        if name in ("moon_phase", "quality"):
            # These are optional
            continue

        value = getattr(item, name)
        assert value, f"Field {name} is not set"

    datetime = item.datetime
    assert datetime is not None
    assert datetime.tzinfo is not None
