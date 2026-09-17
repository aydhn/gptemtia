# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Broker Execution Disabled Report.

Documents and validates that broker API integration and execution are disabled.
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
    EXECUTION_BLOCKED_NO_BROKER,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_broker_execution_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build broker execution disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "broker_api_binding", "disabled": True, "reason": "Broker API connection disabled"},
        {"action": "broker_order_dispatch", "disabled": True, "reason": "Broker order routing disabled"},
        {"action": "broker_account_sync", "disabled": True, "reason": "Broker account sync disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "broker_execution_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_BROKER,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_broker_execution_request(request: Union[dict, str]) -> dict:
    """Validate request does not request broker execution."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(broker_order|broker_exec|broker_api|connect_broker)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "broker_blocked": blocked,
        "message": "Broker execution blocked by policy" if blocked else "Request verified no broker",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_BROKER,
    }
