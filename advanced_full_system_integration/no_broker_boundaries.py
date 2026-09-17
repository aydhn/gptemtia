# -*- coding: utf-8 -*-
"""Phase 158: No Broker Boundaries.

Enforces zero-broker integration and blocks any broker API authentication or connectivity.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

BROKER_RULES = [
    ("NBR-001", "broker_boundary", "no_broker_api_keys", "credential", False, "Storing or transmitting broker API keys is blocked."),
    ("NBR-002", "broker_boundary", "no_broker_rest_calls", "network", False, "Making outbound HTTP requests to broker endpoints is blocked."),
    ("NBR-003", "broker_boundary", "no_broker_websocket_streams", "network", False, "Opening broker order feed sockets is blocked."),
    ("NBR-004", "broker_boundary", "no_broker_order_submission", "order", False, "Submitting live orders to any exchange or broker is blocked."),
]


def build_no_broker_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build no-broker boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in BROKER_RULES:
        item = SystemBoundaryItem(
            boundary_id=bid,
            boundary_type=btype,
            rule_name=rname,
            action_type=atype,
            is_allowed=is_allowed,
            reason=reason,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "prohibited_actions_count": int((df["is_allowed"] == False).sum()),
        "allowed_actions_count": int((df["is_allowed"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
