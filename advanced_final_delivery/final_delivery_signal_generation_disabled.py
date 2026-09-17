# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Signal Generation Disabled Report.

Documents and validates that signal generation is strictly disabled.
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
    EXECUTION_BLOCKED_NO_SIGNAL_GENERATION,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_signal_generation_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build signal generation disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "signal_emission", "disabled": True, "reason": "Trading signal emission disabled"},
        {"action": "directional_signal", "disabled": True, "reason": "Long/short directional bias disabled"},
        {"action": "trade_recommendation", "disabled": True, "reason": "Buy/sell trade recommendation disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "signal_generation_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_SIGNAL_GENERATION,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_signal_generation_request(request: Union[dict, str]) -> dict:
    """Validate request does not request signal generation."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(generate_signal|emit_signal|buy_signal|sell_signal)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "signal_blocked": blocked,
        "message": "Signal generation blocked by policy" if blocked else "Request verified no signal generation",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_SIGNAL_GENERATION,
    }
