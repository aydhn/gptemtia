# -*- coding: utf-8 -*-
"""Phase 158: Production Deployment Disabled Report.

Certifies and enforces that production deployments and claims are disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_production_deployment_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build production deployment disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="PDD-001",
            execution_type="production_deployment",
            is_disabled=True,
            blocking_reason="Phase 158 is non-production research layer.",
        ),
        SystemDisabledExecutionItem(
            item_id="PDD-002",
            execution_type="production_ready_claim",
            is_disabled=True,
            blocking_reason="Claims of production-readiness are strictly prohibited.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_deployment",
        "non_signal": True,
    }
    return df, summary


def validate_no_production_deployment_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request production deployment."""
    text = str(request).lower()
    forbidden_tokens = ["deploy", "production_ready", "broker_ready", "live_ready", "approve"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
