import pytest
from datetime import datetime, timezone
from core.market_calendar import MarketCalendar


def test_market_calendar_is_open():
    calendar = MarketCalendar()

    # A Saturday
    saturday = datetime(2024, 1, 6, 12, 0, tzinfo=timezone.utc)
    # A Monday
    monday = datetime(2024, 1, 8, 12, 0, tzinfo=timezone.utc)

    # Forex is 24/5 (closed weekends)
    assert calendar.is_market_open("forex_major", dt=saturday) is False
    assert calendar.is_market_open("forex_major", dt=monday) is True

    # Metals (futures_extended) closed weekends
    assert calendar.is_market_open("metals", dt=saturday) is False
    assert calendar.is_market_open("metals", dt=monday) is True


def test_market_calendar_describe():
    calendar = MarketCalendar()
    desc = calendar.describe_session("forex_major")
    assert isinstance(desc, str)
    assert "forex_24_5" in desc


def test_market_calendar_unknown():
    calendar = MarketCalendar()
    # Unknown asset class defaults to open to not block
    assert (
        calendar.is_market_open(
            "unknown_asset", dt=datetime(2024, 1, 8, tzinfo=timezone.utc)
        )
        is True
    )

    desc = calendar.describe_session("unknown_asset")
    assert desc == "Unknown Session"
