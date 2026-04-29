from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from config.scan_config import ScanProfile
from config.symbols import SymbolSpec
from core.market_calendar import MarketCalendar
from core.time_utils import ensure_timezone_aware, utc_now


class ScanScheduler:
    def __init__(self, profile: ScanProfile, calendar: MarketCalendar):
        self.profile = profile
        self.calendar = calendar

    def should_scan_now(
        self,
        asset_class: str,
        last_scan_time: Optional[datetime],
        now: Optional[datetime] = None,
    ) -> bool:
        """
        Determines if a scan should happen now for a given asset class based on the profile's scan interval
        and market open status.
        """
        if now is None:
            now = utc_now()
        now = ensure_timezone_aware(now)

        if not self.calendar.is_market_open(asset_class, now):
            return False

        if last_scan_time is None:
            return True

        last_scan_time = ensure_timezone_aware(last_scan_time)
        time_since_last_scan = now - last_scan_time
        interval = timedelta(minutes=self.profile.scan_interval_minutes)

        return time_since_last_scan >= interval

    def build_scan_plan(
        self,
        symbols: List[SymbolSpec],
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        """
        Builds a scan plan for a given list of symbols based on the current profile and market state.
        """
        if now is None:
            now = utc_now()
        now = ensure_timezone_aware(now)

        eligible_symbols = []
        skipped_symbols = []
        by_asset_class: Dict[str, int] = {}

        for spec in symbols:
            # Skip disabled symbols entirely
            if not spec.enabled:
                continue

            # Allow synthetic benchmarks even if analysis_enabled is False,
            # or skip if analysis_enabled is False and not a benchmark
            is_synthetic_benchmark = (
                spec.asset_class == "benchmark" and spec.data_source == "synthetic"
            )
            if not spec.analysis_enabled and not is_synthetic_benchmark:
                continue

            # Skip synthetic benchmarks from active live scanning (they don't need continuous data fetching)
            # as per instruction: "synthetic benchmarkları canlı tarama planına alma"
            if is_synthetic_benchmark:
                skipped_symbols.append(spec.symbol)
                continue

            if not self.calendar.is_market_open(spec.asset_class, now):
                skipped_symbols.append(spec.symbol)
                continue

            if len(eligible_symbols) >= self.profile.max_symbols_per_cycle:
                skipped_symbols.append(spec.symbol)
                continue

            eligible_symbols.append(spec.symbol)
            by_asset_class[spec.asset_class] = (
                by_asset_class.get(spec.asset_class, 0) + 1
            )

        return {
            "profile": self.profile.name,
            "now": str(now),
            "scan_interval_minutes": self.profile.scan_interval_minutes,
            "total_symbols": len(symbols),
            "eligible_symbols": eligible_symbols,
            "skipped_symbols": skipped_symbols,
            "by_asset_class": by_asset_class,
            "timeframes": list(self.profile.timeframes),
            "notes": "Plan generated successfully.",
        }
