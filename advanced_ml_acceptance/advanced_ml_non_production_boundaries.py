# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Non-Production Boundary Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    NON_PRODUCTION_BOUNDARY_DOMAIN,
    ACCEPTANCE_READY,
)

NON_PRODUCTION_BOUNDARIES: List[Dict[str, Any]] = [
    {"boundary_id": "NPB-01", "name": "research_only_execution", "description": "All logic executed exclusively within local/offline research sandbox.", "active": True},
    {"boundary_id": "NPB-02", "name": "no_production_readiness_claims", "description": "System never claims production readiness or commercial suitability.", "active": True},
    {"boundary_id": "NPB-03", "name": "no_broker_readiness_claims", "description": "System never claims broker certification or exchange readiness.", "active": True},
    {"boundary_id": "NPB-04", "name": "no_official_approval_claims", "description": "System never claims regulatory or official audit approval.", "active": True},
    {"boundary_id": "NPB-05", "name": "no_live_trading_approval", "description": "Live trading approval is permanently denied.", "active": True},
    {"boundary_id": "NPB-06", "name": "no_production_deployment", "description": "Automated deployment to staging/production clusters disabled.", "active": True},
    {"boundary_id": "NPB-07", "name": "non_signal_guarantee", "description": "Readiness scores and acceptance reports are never presented as trading signals.", "active": True},
]


def build_advanced_ml_non_production_boundary_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for non-production boundaries."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for b in NON_PRODUCTION_BOUNDARIES:
        row = dict(b)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": NON_PRODUCTION_BOUNDARY_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_boundaries": len(df),
        "active_boundaries": int(df["active"].sum()),
        "all_active": bool(df["active"].all()),
        "non_signal": True,
        "status": "ENFORCED",
    }
    return df, summary


def summarize_advanced_ml_non_production_boundaries(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize non-production boundaries DataFrame."""
    return {
        "boundary_count": len(df),
        "all_active": bool(df["active"].all()) if not df.empty and "active" in df.columns else False,
        "non_signal": True,
    }
