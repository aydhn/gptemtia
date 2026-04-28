import pytest
from datetime import datetime, timezone
from config.scan_config import get_default_scan_profile, validate_scan_profiles
from core.scan_scheduler import ScanScheduler
from core.market_calendar import MarketCalendar
from config.symbols import SymbolSpec


def test_scan_profiles_validation():
    validate_scan_profiles()


def test_get_default_scan_profile():
    profile = get_default_scan_profile()
    assert profile.name == "balanced_swing"
    assert profile.max_symbols_per_cycle == 80


def test_build_scan_plan():
    profile = get_default_scan_profile()
    calendar = MarketCalendar()
    scheduler = ScanScheduler(profile, calendar)

    symbols = [
        SymbolSpec(
            "GC=F",
            "Gold",
            "metals",
            "precious",
            "USD",
            enabled=True,
            analysis_enabled=True,
        ),
        SymbolSpec(
            "USDTRY=X",
            "USD/TRY bench",
            "benchmark",
            "currency",
            "TRY",
            data_source="synthetic",
            enabled=True,
            analysis_enabled=False,
        ),
        SymbolSpec("UNKNOWN", "Unknown", "unknown", "unknown", "USD", enabled=False),
    ]

    # Run on a Monday
    monday = datetime(2024, 1, 8, 12, 0, tzinfo=timezone.utc)
    plan = scheduler.build_scan_plan(symbols, now=monday)

    assert isinstance(plan, dict)
    assert plan["profile"] == "balanced_swing"
    assert "GC=F" in plan["eligible_symbols"]
    assert "USDTRY=X" in plan["skipped_symbols"]  # Synthetic skipped from live
    assert "UNKNOWN" not in plan["eligible_symbols"]
    assert "UNKNOWN" not in plan["skipped_symbols"]  # Disabled entirely

    assert plan["by_asset_class"]["metals"] == 1
