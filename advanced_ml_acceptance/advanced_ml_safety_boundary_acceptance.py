# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Safety Boundary Acceptance Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    SAFETY_BOUNDARY_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)

SAFETY_BOUNDARIES: List[Dict[str, Any]] = [
    {"boundary_id": "SB-01", "name": "live_trading_boundary", "boundary_rule": "Strict prohibition of live capital, order routing, and broker APIs.", "enforced": True},
    {"boundary_id": "SB-02", "name": "broker_integration_boundary", "boundary_rule": "Zero broker execution bindings allowed in Phase 145.", "enforced": True},
    {"boundary_id": "SB-03", "name": "investment_advice_boundary", "boundary_rule": "No buy/sell signals, directional targets, or financial advice.", "enforced": True},
    {"boundary_id": "SB-04", "name": "training_execution_boundary", "boundary_rule": "Real model training loops completely disabled.", "enforced": True},
    {"boundary_id": "SB-05", "name": "prediction_inference_boundary", "boundary_rule": "Real inference and model predictions disabled.", "enforced": True},
    {"boundary_id": "SB-06", "name": "backtest_execution_boundary", "boundary_rule": "Real backtest, walk-forward, and slippage calculations disabled in Phase 145.", "enforced": True},
    {"boundary_id": "SB-07", "name": "dataset_materialization_boundary", "boundary_rule": "Dataset and feature snapshot disk materialization disabled.", "enforced": True},
    {"boundary_id": "SB-08", "name": "model_registry_write_boundary", "boundary_rule": "Writing to model registry or artifact publishing disabled.", "enforced": True},
    {"boundary_id": "SB-09", "name": "model_deployment_boundary", "boundary_rule": "Model deployment and production release disabled.", "enforced": True},
    {"boundary_id": "SB-10", "name": "source_preservation_boundary", "boundary_rule": "Source records in DataLake are immutable and never overwritten.", "enforced": True},
    {"boundary_id": "SB-11", "name": "metadata_only_news_boundary", "boundary_rule": "News is restricted to metadata only; full text and scraping prohibited.", "enforced": True},
]


def build_advanced_ml_safety_boundary_acceptance_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for safety boundary acceptance."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for b in SAFETY_BOUNDARIES:
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
        "domain": SAFETY_BOUNDARY_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_boundaries": len(df),
        "enforced_boundaries": int(df["enforced"].sum()),
        "all_enforced": bool(df["enforced"].all()),
        "non_signal": True,
        "status": "SECURE",
    }
    return df, summary


def summarize_advanced_ml_safety_boundary_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundaries DataFrame."""
    return {
        "boundary_count": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else False,
        "non_signal": True,
    }
