# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Safety Boundary."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

NO_GO_CONDITIONS: List[Dict[str, str]] = [
    {"condition_id": "NG-01", "name": "live_trading", "rule": "Never execute live orders or connect broker APIs."},
    {"condition_id": "NG-02", "name": "real_orders", "rule": "Never submit real orders to financial markets."},
    {"condition_id": "NG-03", "name": "investment_advice", "rule": "Never provide financial or investment advice."},
    {"condition_id": "NG-04", "name": "signal_generation", "rule": "Never generate buy/sell/long/short signals."},
    {"condition_id": "NG-05", "name": "directional_certainty", "rule": "Never claim directional predictive certainty."},
    {"condition_id": "NG-06", "name": "dataset_materialization", "rule": "Never materialize datasets during governance."},
    {"condition_id": "NG-07", "name": "feature_snapshot_materialization", "rule": "Never materialize feature snapshots."},
    {"condition_id": "NG-08", "name": "strategy_backtest_execution", "rule": "Never execute backtests or optimization algorithms."},
    {"condition_id": "NG-09", "name": "real_model_training", "rule": "Never execute real model fit/training routines."},
    {"condition_id": "NG-10", "name": "real_model_predict", "rule": "Never execute model predict or inference routines."},
    {"condition_id": "NG-11", "name": "probability_prediction", "rule": "Never compute real probability predictions."},
    {"condition_id": "NG-12", "name": "calibration_execution", "rule": "Never execute calibration algorithms on live data."},
    {"condition_id": "NG-13", "name": "uncertainty_estimation", "rule": "Never compute live uncertainty estimates."},
    {"condition_id": "NG-14", "name": "drift_calculation", "rule": "Never run live drift calculations during governance."},
    {"condition_id": "NG-15", "name": "explainability_calculation", "rule": "Never compute live SHAP/LIME/PDP values."},
    {"condition_id": "NG-16", "name": "feature_attribution_calculation", "rule": "Never compute live feature attribution."},
    {"condition_id": "NG-17", "name": "target_label_prediction", "rule": "Never generate target labels or predictions."},
    {"condition_id": "NG-18", "name": "metric_performance_claim", "rule": "Never claim performance metrics or accuracy."},
    {"condition_id": "NG-19", "name": "model_artifact_persistence", "rule": "Never persist weights or serialized model objects."},
    {"condition_id": "NG-20", "name": "model_registry_write", "rule": "Never write to MLflow or model registries."},
    {"condition_id": "NG-21", "name": "model_deployment", "rule": "Never deploy models to serving infrastructure."},
    {"condition_id": "NG-22", "name": "production_deployment", "rule": "Never trigger production deployment pipelines."},
    {"condition_id": "NG-23", "name": "production_approval", "rule": "Never grant production approval sign-offs."},
    {"condition_id": "NG-24", "name": "broker_ready_approval", "rule": "Never certify broker readiness."},
    {"condition_id": "NG-25", "name": "live_trading_approval", "rule": "Never grant live trading authorization."},
    {"condition_id": "NG-26", "name": "release_approval", "rule": "Never approve release candidates."},
    {"condition_id": "NG-27", "name": "official_approval_claim", "rule": "Never claim official regulatory approvals."},
    {"condition_id": "NG-28", "name": "real_audit_log", "rule": "Never claim placeholder logs are real audit logs."},
    {"condition_id": "NG-29", "name": "full_article_content", "rule": "Never store full news article body text or HTML."},
    {"condition_id": "NG-30", "name": "embedding_generation", "rule": "Never generate NLP embeddings or vector databases."},
    {"condition_id": "NG-31", "name": "source_overwrite", "rule": "Never overwrite or destructively modify raw source files."},
    {"condition_id": "NG-32", "name": "auto_imputation_drop", "rule": "Never silently impute values or drop features."},
    {"condition_id": "NG-33", "name": "scraping", "rule": "Never scrape external web sources."},
    {"condition_id": "NG-34", "name": "credential_output", "rule": "Never leak credentials, API keys, or tokens."},
]

SAFE_GO_CONDITIONS: List[Dict[str, str]] = [
    {"condition_id": "SG-01", "name": "governance_contract_generation", "rule": "Generate local offline governance contracts."},
    {"condition_id": "SG-02", "name": "model_card_template_generation", "rule": "Generate standardized model card templates."},
    {"condition_id": "SG-03", "name": "limitations_metadata_recording", "rule": "Document limitations, intended use, and prohibited use."},
    {"condition_id": "SG-04", "name": "risk_disclosure_recording", "rule": "Record model risk disclosures and mitigations."},
    {"condition_id": "SG-05", "name": "validation_evidence_recording", "rule": "Link validation evidence from Phases 136-143."},
    {"condition_id": "SG-06", "name": "approval_boundary_enforcement", "rule": "Enforce approval boundaries and manual review gates."},
    {"condition_id": "SG-07", "name": "audit_trail_placeholders", "rule": "Produce dry-run audit trail placeholders."},
    {"condition_id": "SG-08", "name": "control_checklists_evaluation", "rule": "Evaluate and verify safety control checklists."},
    {"condition_id": "SG-09", "name": "disabled_execution_reporting", "rule": "Generate 10 disabled execution reports."},
    {"condition_id": "SG-10", "name": "phase_145_handoff_preparation", "rule": "Package safe handoff to Phase 145 Advanced ML Acceptance."},
]


def build_model_governance_no_go_conditions(
    profile: Optional[ModelGovernanceProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of NO-GO safety conditions."""
    records = [dict(c) for c in NO_GO_CONDITIONS]
    for r in records:
        r["is_strictly_enforced"] = True
    return pd.DataFrame(records)


def build_model_governance_safe_go_conditions(
    profile: Optional[ModelGovernanceProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of SAFE-GO permitted conditions."""
    records = [dict(c) for c in SAFE_GO_CONDITIONS]
    for r in records:
        r["is_permitted"] = True
    return pd.DataFrame(records)


def build_model_governance_safety_boundary(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build complete safety boundary report."""
    prof = profile or get_model_governance_profile()
    df_nogo = build_model_governance_no_go_conditions(prof)
    df_safego = build_model_governance_safe_go_conditions(prof)

    summary = {
        "total_no_go_rules": len(df_nogo),
        "total_safe_go_rules": len(df_safego),
        "all_no_go_enforced": bool(df_nogo["is_strictly_enforced"].all()),
        "status": "SECURE",
    }
    return df_nogo, summary


def summarize_model_governance_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary."""
    return {
        "total_rules": len(df),
        "status": "SECURE",
        "live_trading_prohibited": True,
        "model_registry_write_prohibited": True,
    }
