# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Order Generation Disabled Report.

Documents and validates that automated order creation is disabled.
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
    EXECUTION_BLOCKED_NO_ORDER_GENERATION,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_order_generation_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build order generation disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "order_creation", "disabled": True, "reason": "Automated order creation disabled"},
        {"action": "order_sizing", "disabled": True, "reason": "Automated lot sizing disabled"},
        {"action": "order_routing", "disabled": True, "reason": "Automated order routing disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "order_generation_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_ORDER_GENERATION,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_order_generation_request(request: Union[dict, str]) -> dict:
    """Validate request does not request order generation."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(generate_order|send_order|create_order|place_order)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "order_blocked": blocked,
        "message": "Order generation blocked by policy" if blocked else "Request verified no order generation",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_ORDER_GENERATION,
    }
