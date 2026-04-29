from datetime import datetime
from typing import Optional

from config.market_sessions import get_market_session
from core.time_utils import (
    ensure_timezone_aware,
    is_weekend,
    timeframe_to_timedelta,
    utc_now,
)


class MarketCalendar:
    def __init__(self):
        pass

    def is_market_open(
        self,
        asset_class: str,
        dt: Optional[datetime] = None,
    ) -> bool:
        """
        Approximate check if the market is open.
        """
        if dt is None:
            dt = utc_now()
        dt = ensure_timezone_aware(dt)

        try:
            session = get_market_session(asset_class)
        except Exception:
            return True  # Fallback if unknown

        # Check weekend trading
        if not session.weekend_trading and is_weekend(dt):
            return False

        if session.trades_24h:
            return True

        # For simplicity in this phase, if it's not 24h but weekday, we just say True
        # Actual intraday session hour checking requires more complex parsing of typical_open/typical_close
        # which can be added later if needed. For now, non-24h weekday is assumed "partially open"
        # and we don't strict filter by hours in this phase unless requested.
        return True

    def next_reasonable_scan_time(
        self,
        asset_class: str,
        timeframe: str,
        dt: Optional[datetime] = None,
    ) -> datetime:
        """
        Calculates the next reasonable time to scan based on session and timeframe.
        """
        if dt is None:
            dt = utc_now()
        dt = ensure_timezone_aware(dt)

        # Simplistic implementation: just add timeframe timedelta
        # Real implementation might skip weekends if market is closed
        return dt + timeframe_to_timedelta(timeframe)

    def describe_session(self, asset_class: str) -> str:
        """
        Returns a description of the market session.
        """
        try:
            session = get_market_session(asset_class)
            parts = [f"Session: {session.session_name} ({session.timezone})"]
            if session.trades_24h:
                parts.append("24 Hours")
            else:
                parts.append(f"Hours: {session.typical_open} - {session.typical_close}")
            if session.weekend_trading:
                parts.append("Weekend Trading: Yes")
            else:
                parts.append("Weekend Trading: No")
            if session.notes:
                parts.append(f"Notes: {session.notes}")
            return " | ".join(parts)
        except Exception:
            return "Unknown Session"
