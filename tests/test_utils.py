from test_jobs.utils import format_trip_count


def test_format_trip_count_plural():
    assert format_trip_count(3) == "3 trips"


def test_format_trip_count_singular():
    assert format_trip_count(1) == "1 trip"


def test_format_trip_count_zero():
    assert format_trip_count(0) == "0 trips"


def test_format_trip_count_negative_raises():
    import pytest

    with pytest.raises(ValueError):
        format_trip_count(-1)
