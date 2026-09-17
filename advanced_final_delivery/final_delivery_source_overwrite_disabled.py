# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Source Overwrite Disabled Report.

Documents and validates that source overwriting and destructive actions are disabled.
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
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_source_overwrite_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build source overwrite disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "source_overwrite", "disabled": True, "reason": "Overwriting source files is prohibited"},
        {"action": "destructive_deletion", "disabled": True, "reason": "Deleting repository files is prohibited"},
        {"action": "destructive_migration", "disabled": True, "reason": "Destructive database migrations are prohibited"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "source_overwrite_disabled": True,
        "actions_blocked": len(rows),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_source_overwrite_request(request: Union[dict, str]) -> dict:
    """Validate that source overwrite or destructive actions are not requested."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(overwrite_source|delete_file|destructive_clean|purge_raw)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "overwrite_blocked": blocked,
        "message": "Source overwrite blocked by policy" if blocked else "Request verified no source overwrite",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else "BLOCKED_BY_SOURCE_PRESERVATION",
    }
