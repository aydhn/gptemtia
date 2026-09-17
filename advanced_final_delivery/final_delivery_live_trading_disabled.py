# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Live Trading Disabled Report.

Documents and validates that live trading operations are strictly disabled.
"""

from typing import Dict, Tuple, Union
import re
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DISABLED_EXECUTION_DOMAIN,
    EXECUTION_BLOCKED_NO_LIVE_TRADING,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_live_trading_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build live trading disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "live_orders", "disabled": True, "reason": "Live order generation strictly prohibited"},
        {"action": "exchange_feed", "disabled": True, "reason": "Live trading exchange sockets strictly prohibited"},
        {"action": "live_account_balance", "disabled": True, "reason": "Live account operations strictly prohibited"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "live_trading_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_LIVE_TRADING,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_live_trading_request(request: Union[dict, str]) -> dict:
    """Validate request does not request live trading."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(live_trade|live_trading|real_order|live_order|place_order)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "live_trading_blocked": blocked,
        "message": "Live trading blocked by policy" if blocked else "Request verified no live trading",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_LIVE_TRADING,
    }
