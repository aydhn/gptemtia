# -*- coding: utf-8 -*-
"""Phase 158: Broker Execution Disabled Report.

Certifies and enforces that broker API execution is disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_broker_execution_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build broker execution disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="BED-001",
            execution_type="broker_api_calls",
            is_disabled=True,
            blocking_reason="Broker execution interfaces are not connected.",
        ),
        SystemDisabledExecutionItem(
            item_id="BED-002",
            execution_type="broker_authentication",
            is_disabled=True,
            blocking_reason="No broker credentials or tokens permitted.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_broker",
        "non_signal": True,
    }
    return df, summary


def validate_no_broker_execution_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request broker execution."""
    text = str(request).lower()
    forbidden_tokens = ["broker_order", "send_order", "broker_api"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
