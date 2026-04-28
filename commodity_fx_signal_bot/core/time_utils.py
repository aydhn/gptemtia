from datetime import datetime, timedelta, timezone as dt_timezone
from zoneinfo import ZoneInfo
from typing import Optional, Union
import pandas as pd
from config.timeframes import timeframe_to_minutes


def utc_now() -> datetime:
    """Return the current time in UTC."""
    return datetime.now(dt_timezone.utc)


def local_now(timezone: str = "Europe/Istanbul") -> datetime:
    """Return the current time in the specified local timezone."""
    return datetime.now(ZoneInfo(timezone))


def to_utc(dt: datetime) -> datetime:
    """Convert a timezone-aware datetime to UTC."""
    return ensure_timezone_aware(dt).astimezone(dt_timezone.utc)


def ensure_timezone_aware(dt: datetime, timezone: str = "UTC") -> datetime:
    """Ensure a datetime is timezone-aware. If naive, assume the given timezone."""
    if dt.tzinfo is None:
        if timezone == "UTC":
            return dt.replace(tzinfo=dt_timezone.utc)
        return dt.replace(tzinfo=ZoneInfo(timezone))
    return dt


def parse_date_or_datetime(value: Union[str, datetime, pd.Timestamp]) -> datetime:
    """Parse a string or Timestamp to a timezone-aware datetime."""
    if isinstance(value, datetime):
        return ensure_timezone_aware(value)
    if isinstance(value, pd.Timestamp):
        return ensure_timezone_aware(value.to_pydatetime())

    # Try parsing string
    parsed = pd.to_datetime(value)
    return ensure_timezone_aware(parsed.to_pydatetime())


def floor_datetime_to_timeframe(dt: datetime, timeframe: str) -> datetime:
    """Floor a datetime to the nearest lower boundary of the given timeframe."""
    minutes = timeframe_to_minutes(timeframe)
    if minutes >= 1440:  # Daily or higher
        # Simply strip time for 1d. For 1wk/1mo we'd need more complex logic, but this suffices for now
        floored = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        return floored

    # Intraday
    total_minutes = dt.hour * 60 + dt.minute
    floored_total_minutes = (total_minutes // minutes) * minutes
    floored_hour = floored_total_minutes // 60
    floored_minute = floored_total_minutes % 60
    return dt.replace(hour=floored_hour, minute=floored_minute, second=0, microsecond=0)


def timeframe_to_timedelta(timeframe: str) -> timedelta:
    """Convert a timeframe string to a timedelta object."""
    minutes = timeframe_to_minutes(timeframe)
    return timedelta(minutes=minutes)


def calculate_lookback_start(end: datetime, lookback_days: int) -> datetime:
    """Calculate the start date given an end date and lookback period in days."""
    return end - timedelta(days=lookback_days)


def is_weekend(dt: datetime) -> bool:
    """Check if a datetime falls on a weekend (Saturday or Sunday)."""
    # 5 is Saturday, 6 is Sunday in Python's weekday()
    return dt.weekday() >= 5
