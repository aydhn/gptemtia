# -*- coding: utf-8 -*-
"""Phase 144: Model Governance Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)
from advanced_model_governance.model_governance_models import ModelGovernanceManifest


def create_model_governance_manifest(
    manifest_name: str = "manifest_phase_144_model_governance",
    governance_contract_count: int = 7,
    model_card_count: int = 7,
    disabled_execution_report_count: int = 10,
    finding_count: int = 4,
    manual_review_count: int = 10,
    readiness_score: float = 1.0,
    manual_review_required: bool = True,
) -> ModelGovernanceManifest:
    """Factory for ModelGovernanceManifest instance with strict invariants."""
    return ModelGovernanceManifest(
        manifest_id=manifest_name,
        current_phase=144,
        target_final_phase=160,
        next_phase=145,
        non_signal=True,
        source_preserved=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        production_approved=False,
        broker_ready_approved=False,
        live_trading_approved=False,
        release_approved=False,
        real_audit_log=False,
        dataset_materialized=False,
        feature_snapshot_materialized=False,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        contains_full_article_text=False,
        contains_article_body=False,
        contains_raw_content=False,
        contains_scraped_html=False,
        contains_embedding=False,
        contains_vector=False,
        sentiment_model_output=False,
        real_training_executed=False,
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        model_inference_executed=False,
        probability_prediction_executed=False,
        calibration_executed=False,
        uncertainty_estimation_executed=False,
        drift_calculation_executed=False,
        explainability_calculation_executed=False,
        feature_attribution_calculation_executed=False,
        metric_calculation_executed=False,
        performance_claim_generated=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        governance_contract_count=governance_contract_count,
        model_card_count=model_card_count,
        disabled_execution_report_count=disabled_execution_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
    )


def build_model_governance_manifest(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model governance manifest."""
    prof = profile or get_model_governance_profile()
    manifest_obj = create_model_governance_manifest()

    data = manifest_obj.__dict__
    df = pd.DataFrame([data])
    summary = summarize_model_governance_manifest(df)
    return df, summary


def summarize_model_governance_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model governance manifest."""
    row = df.iloc[0] if not df.empty else {}
    return {
        "manifest_id": str(row.get("manifest_id", "manifest_phase_144_model_governance")),
        "current_phase": int(row.get("current_phase", 144)),
        "next_phase": int(row.get("next_phase", 145)),
        "target_final_phase": int(row.get("target_final_phase", 160)),
        "non_signal": bool(row.get("non_signal", True)),
        "source_preserved": bool(row.get("source_preserved", True)),
        "official_approval": bool(row.get("official_approval", False)),
        "production_ready": bool(row.get("production_ready", False)),
        "broker_ready": bool(row.get("broker_ready", False)),
        "production_approved": bool(row.get("production_approved", False)),
        "broker_ready_approved": bool(row.get("broker_ready_approved", False)),
        "live_trading_approved": bool(row.get("live_trading_approved", False)),
        "model_registry_written": bool(row.get("model_registry_written", False)),
        "artifact_persisted": bool(row.get("artifact_persisted", False)),
        "model_deployed": bool(row.get("model_deployed", False)),
        "status": "MANIFEST_VERIFIED",
    }
