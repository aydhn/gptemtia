# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Non-Production Boundaries."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    ACCEPTANCE_READY,
)

NON_PROD_BOUNDARIES: List[Dict[str, Any]] = [
    {"boundary_id": "NPB-152-01", "name": "research_only_environment", "description": "All backtest acceptance logic operates exclusively as an offline research framework.", "active": True},
    {"boundary_id": "NPB-152-02", "name": "dry_run_default", "description": "Operations default to dry-run contracts without stateful execution side-effects.", "active": True},
    {"boundary_id": "NPB-152-03", "name": "no_production_deployment", "description": "Production deployment pipelines, endpoints, or release tags remain strictly disabled.", "active": True},
    {"boundary_id": "NPB-152-04", "name": "local_filesystem_isolation", "description": "Artifacts are stored locally in DataLake without remote cloud publishing.", "active": True},
    {"boundary_id": "NPB-152-05", "name": "zero_broker_coupling", "description": "Zero coupling with real brokers or trading execution services.", "active": True},
]


def build_backtest_acceptance_non_production_boundary_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for non-production boundaries."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for b in NON_PROD_BOUNDARIES:
        records.append({
            "boundary_id": b["boundary_id"],
            "boundary_name": b["name"],
            "description": b["description"],
            "active": b["active"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": NON_PRODUCTION_BOUNDARY_DOMAIN,
        "active_profile": active.profile_name,
        "total_boundaries": len(records),
        "active_boundaries": len([r for r in records if r["active"]]),
        "all_active": all(r["active"] for r in records),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
