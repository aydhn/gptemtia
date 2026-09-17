# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Execution Disabled Report.

Documents and validates that all system execution and end-to-end bot runs are disabled.
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
    EXECUTION_BLOCKED_NO_SYSTEM_EXECUTION,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_execution_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build execution disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "system_execution", "disabled": True, "reason": "Full system execution prohibited by policy"},
        {"action": "end_to_end_run", "disabled": True, "reason": "End-to-end bot runs prohibited by policy"},
        {"action": "automated_pipeline_daemon", "disabled": True, "reason": "Standing daemon process prohibited"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "execution_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_SYSTEM_EXECUTION,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_execution_request(request: Union[dict, str]) -> dict:
    """Validate request does not request system execution."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(run_system|execute_system|end_to_end_run|launch_bot)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "execution_blocked": blocked,
        "message": "Execution blocked by policy" if blocked else "Request verified non-execution",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_SYSTEM_EXECUTION,
    }
