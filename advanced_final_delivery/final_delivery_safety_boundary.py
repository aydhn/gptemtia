# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Safety Boundary.

Builds consolidated safety boundary conditions, separating NO-GO prohibitions from SAFE-GO actions.
"""

from typing import Dict, List, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_SAFETY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)
from advanced_final_delivery.final_delivery_no_go_boundaries import NO_GO_RULES
from advanced_final_delivery.final_delivery_go_boundaries import SAFE_GO_ACTIONS


def build_final_delivery_no_go_conditions(
    profile: FinalDeliveryProfile | None = None,
) -> List[Dict]:
    """Return list of enforced no-go rule dictionaries."""
    return [{"rule_name": r[0], "description": r[1], "enforced": True} for r in NO_GO_RULES]


def build_final_delivery_safe_go_conditions(
    profile: FinalDeliveryProfile | None = None,
) -> List[Dict]:
    """Return list of permitted safe-go action dictionaries."""
    return [{"action_name": a[0], "description": a[1], "permitted": True} for a in SAFE_GO_ACTIONS]


def build_final_delivery_safety_boundary(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build consolidated safety boundary DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for r_name, desc in NO_GO_RULES:
        rows.append({
            "boundary_item": r_name,
            "boundary_type": "NO_GO",
            "description": desc,
            "enforced": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_SAFETY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    for a_name, desc in SAFE_GO_ACTIONS:
        rows.append({
            "boundary_item": a_name,
            "boundary_type": "SAFE_GO",
            "description": desc,
            "enforced": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_SAFETY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_rules": len(rows),
        "no_go_count": len(NO_GO_RULES),
        "safe_go_count": len(SAFE_GO_ACTIONS),
        "safety_status": "SAFETY_BOUNDARY_ENFORCED",
        "all_enforced": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary
