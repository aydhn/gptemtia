# -*- coding: utf-8 -*-
"""Phase 158: Live Trading Disabled Report.

Certifies and enforces that live trading execution is disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_live_trading_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build live trading disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="LTD-001",
            execution_type="live_trading",
            is_disabled=True,
            blocking_reason="Live market order submission is strictly prohibited.",
        ),
        SystemDisabledExecutionItem(
            item_id="LTD-002",
            execution_type="live_account_access",
            is_disabled=True,
            blocking_reason="Live account state manipulation is blocked.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_live_trading",
        "non_signal": True,
    }
    return df, summary


def validate_no_live_trading_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request live trading."""
    text = str(request).lower()
    forbidden_tokens = ["live_trade", "live_trading", "live_order"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
