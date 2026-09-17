# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Scope Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    ACCEPTANCE_SCOPE_DOMAIN,
    ACCEPTANCE_READY,
)

SCOPE_ITEMS: List[Dict[str, Any]] = [
    {"scope_id": "SCP-01", "scope_item": "phase_136_145_block_acceptance", "description": "Consolidated acceptance for Phase 136 to 144 Advanced ML components.", "allowed": True},
    {"scope_id": "SCP-02", "scope_item": "local_offline_only", "description": "Execution constrained strictly to local/offline research environment.", "allowed": True},
    {"scope_id": "SCP-03", "scope_item": "dry_run_only", "description": "Deterministic, dry-run compliant contracts and assertions.", "allowed": True},
    {"scope_id": "SCP-04", "scope_item": "non_production_boundary", "description": "Zero production authorization, deployment, or exposure.", "allowed": True},
    {"scope_id": "SCP-05", "scope_item": "no_live_trading", "description": "Strict prohibition of live capital, orders, or exchange connectivity.", "allowed": False},
    {"scope_id": "SCP-06", "scope_item": "no_broker_execution", "description": "Zero broker API calls, credentials, or execution routing.", "allowed": False},
    {"scope_id": "SCP-07", "scope_item": "no_investment_advice", "description": "Zero financial, buy/sell, or directional advice generation.", "allowed": False},
    {"scope_id": "SCP-08", "scope_item": "no_production_approval", "description": "No release approval, compliance signoff, or production status.", "allowed": False},
    {"scope_id": "SCP-09", "scope_item": "no_backtest_execution", "description": "No backtest, walk-forward, or cost execution in Phase 145.", "allowed": False},
    {"scope_id": "SCP-10", "scope_item": "no_model_training", "description": "No model fitting, parameter optimization, or training loops.", "allowed": False},
    {"scope_id": "SCP-11", "scope_item": "no_prediction_inference", "description": "No model inference, prediction, or probability generation.", "allowed": False},
    {"scope_id": "SCP-12", "scope_item": "no_artifact_persistence", "description": "No model weight saving, pickle dump, or tensor serialization.", "allowed": False},
    {"scope_id": "SCP-13", "scope_item": "no_model_registry_write", "description": "No registry publish, catalog write, or model deployment.", "allowed": False},
    {"scope_id": "SCP-14", "scope_item": "no_web_scraping", "description": "No HTTP scraping, HTML parsing, or web extraction.", "allowed": False},
    {"scope_id": "SCP-15", "scope_item": "no_credential_output", "description": "No secret, token, key, or sensitive credential leakage.", "allowed": False},
    {"scope_id": "SCP-16", "scope_item": "phase_146_handoff_only", "description": "Safe handoff to Phase 146 realistic backtest contract planning.", "allowed": True},
]


def build_advanced_ml_acceptance_scope_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for advanced ML acceptance scope."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for item in SCOPE_ITEMS:
        row = dict(item)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": ACCEPTANCE_SCOPE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_scope_items": len(df),
        "allowed_items": int(df["allowed"].sum()),
        "prohibited_items": int((~df["allowed"]).sum()),
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_advanced_ml_acceptance_scope(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize scope DataFrame."""
    return {
        "total_scope_items": len(df),
        "allowed_count": int(df["allowed"].sum()) if not df.empty and "allowed" in df.columns else 0,
        "prohibited_count": int((~df["allowed"]).sum()) if not df.empty and "allowed" in df.columns else 0,
        "non_signal": True,
    }
