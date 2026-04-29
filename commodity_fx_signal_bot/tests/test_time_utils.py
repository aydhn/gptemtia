from datetime import datetime, timedelta, timezone

from core.time_utils import (
    ensure_timezone_aware,
    floor_datetime_to_timeframe,
    is_weekend,
    local_now,
    timeframe_to_timedelta,
    utc_now,
)


def test_utc_now():
    now = utc_now()
    assert now.tzinfo == timezone.utc


def test_local_now():
    now = local_now()
    assert now.tzinfo is not None


def test_ensure_timezone_aware():
    dt = datetime(2024, 1, 1)
    aware_dt = ensure_timezone_aware(dt)
    assert aware_dt.tzinfo == timezone.utc


def test_timeframe_to_timedelta():
    td = timeframe_to_timedelta("1h")
    assert td == timedelta(hours=1)


def test_floor_datetime_to_timeframe():
    dt = datetime(2024, 1, 1, 15, 45, tzinfo=timezone.utc)
    floored = floor_datetime_to_timeframe(dt, "1h")
    assert floored.hour == 15
    assert floored.minute == 0
    assert floored.second == 0


def test_is_weekend():
    # 2024-01-06 is a Saturday
    dt_sat = datetime(2024, 1, 6, tzinfo=timezone.utc)
    # 2024-01-08 is a Monday
    dt_mon = datetime(2024, 1, 8, tzinfo=timezone.utc)
    assert is_weekend(dt_sat) is True
    assert is_weekend(dt_mon) is False
