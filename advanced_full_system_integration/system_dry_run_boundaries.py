# -*- coding: utf-8 -*-
"""Phase 158: System Dry-Run Boundaries.

Enforces zero-execution, dry-run guarantees across all subsystems.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

DRY_RUN_RULES = [
    ("DRB-158-001", "dry_run_boundary", "enforce_dry_run_default", "execution", True, "Default mode must be dry-run across all subsystems."),
    ("DRB-158-002", "dry_run_boundary", "block_real_broker_socket", "network", False, "Opening real broker sockets or websockets is blocked."),
    ("DRB-158-003", "dry_run_boundary", "block_real_order_routing", "order", False, "Routing orders to trading venues is blocked."),
    ("DRB-158-004", "dry_run_boundary", "block_real_account_mutation", "account", False, "Mutating real account balances or positions is blocked."),
    ("DRB-158-005", "dry_run_boundary", "allow_in_memory_simulation", "simulation", True, "Isolated in-memory test fixtures are permitted."),
]


def build_system_dry_run_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system dry-run boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in DRY_RUN_RULES:
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
