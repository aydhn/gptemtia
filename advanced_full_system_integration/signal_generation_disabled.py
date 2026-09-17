# -*- coding: utf-8 -*-
"""Phase 158: Signal Generation Disabled Report.

Certifies and enforces that signal generation is disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_signal_generation_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build signal generation disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="SGD-001",
            execution_type="trade_signal_generation",
            is_disabled=True,
            blocking_reason="Generating actionable trade signals is disabled.",
        ),
        SystemDisabledExecutionItem(
            item_id="SGD-002",
            execution_type="directional_recommendations",
            is_disabled=True,
            blocking_reason="Generating long/short trading directives is disabled.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_signal_generation",
        "non_signal": True,
    }
    return df, summary


def validate_no_signal_generation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request trade signals."""
    text = str(request).lower()
    forbidden_tokens = ["generate_signal", "buy", "sell", "long", "short"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
