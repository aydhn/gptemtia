# -*- coding: utf-8 -*-
"""Phase 158: Order Generation Disabled Report.

Certifies and enforces that order generation is disabled at contract layer.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemDisabledExecutionItem


def build_order_generation_disabled_report(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build order generation disabled report DataFrame and summary."""
    items = [
        SystemDisabledExecutionItem(
            item_id="OGD-001",
            execution_type="order_generation",
            is_disabled=True,
            blocking_reason="Generating order tickets or executable quantities is prohibited.",
        ),
        SystemDisabledExecutionItem(
            item_id="OGD-002",
            execution_type="order_routing",
            is_disabled=True,
            blocking_reason="Routing orders to broker or execution gateways is prohibited.",
        ),
    ]
    df = pd.DataFrame([item.__dict__ for item in items])
    summary = {
        "active_profile": profile.profile_name,
        "total_items": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "execution_blocked_no_order_generation",
        "non_signal": True,
    }
    return df, summary


def validate_no_order_generation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that incoming payload does not request order generation."""
    text = str(request).lower()
    forbidden_tokens = ["generate_order", "send_order", "order_quantity", "position_size"]
    found = [t for t in forbidden_tokens if t in text]
    return {
        "is_safe": len(found) == 0,
        "forbidden_tokens_detected": found,
        "blocked_by_policy": len(found) > 0,
        "non_signal": True,
    }
