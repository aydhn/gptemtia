# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Credential Output Disabled Report.

Documents and validates that API keys, tokens, and secrets are never printed or leaked.
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


def build_final_delivery_credential_output_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build credential output disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "api_key_output", "disabled": True, "reason": "API key printing strictly prohibited"},
        {"action": "token_output", "disabled": True, "reason": "Auth token printing strictly prohibited"},
        {"action": "secret_output", "disabled": True, "reason": "Secret printing strictly prohibited"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "credential_output_disabled": True,
        "actions_blocked": len(rows),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_credential_output_request(request: Union[dict, str]) -> dict:
    """Validate that credentials or secrets are not requested."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(api_key|secret_key|auth_token|private_key|password)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "credential_blocked": blocked,
        "message": "Credential request blocked by policy" if blocked else "Request verified no credentials",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else "BLOCKED_BY_CREDENTIAL_POLICY",
    }
