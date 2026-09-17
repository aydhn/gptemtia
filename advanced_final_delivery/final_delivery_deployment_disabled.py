# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Deployment Disabled Report.

Documents and validates that production deployment and release publication are disabled.
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
    EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_deployment_disabled_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build deployment disabled report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = [
        {"action": "production_deploy", "disabled": True, "reason": "Production deployment disabled"},
        {"action": "cloud_release_deploy", "disabled": True, "reason": "Cloud release publishing disabled"},
        {"action": "model_deploy", "disabled": True, "reason": "Model serving deployment disabled"},
    ]

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "deployment_disabled": True,
        "actions_blocked": len(rows),
        "execution_code": EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_no_final_delivery_deployment_request(request: Union[dict, str]) -> dict:
    """Validate request does not request deployment."""
    text = " ".join(str(v) for v in request.values()) if isinstance(request, dict) else str(request)
    blocked = bool(re.search(r"\b(deploy_production|deploy_release|publish_cloud|push_docker)\b", text.lower()))
    return {
        "is_safe": not blocked,
        "deployment_blocked": blocked,
        "message": "Deployment blocked by policy" if blocked else "Request verified no deployment",
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if not blocked else EXECUTION_BLOCKED_NO_PRODUCTION_DEPLOYMENT,
    }
