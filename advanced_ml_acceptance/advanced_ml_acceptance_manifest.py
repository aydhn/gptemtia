# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Manifest."""

from dataclasses import asdict
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    MANIFEST_DOMAIN,
    ACCEPTANCE_READY,
)
from advanced_ml_acceptance.advanced_ml_acceptance_models import AdvancedMlAcceptanceManifest


def create_advanced_ml_acceptance_manifest(
    manifest_name: str = "manifest_phase_145_advanced_ml_acceptance",
    component_count: int = 10,
    accepted_component_count: int = 10,
    blocker_count: int = 0,
    warning_count: int = 0,
    gap_count: int = 0,
    finding_count: int = 0,
    manual_review_count: int = 10,
    readiness_score: float = 1.0,
    manual_review_required: bool = True,
) -> AdvancedMlAcceptanceManifest:
    """Instantiate a fully populated AdvancedMlAcceptanceManifest."""
    return AdvancedMlAcceptanceManifest(
        manifest_name=manifest_name,
        manifest_id="manifest_phase_145_advanced_ml_acceptance",
        current_phase=145,
        target_final_phase=160,
        next_phase=146,
        component_count=component_count,
        accepted_component_count=accepted_component_count,
        blocker_count=blocker_count,
        warning_count=warning_count,
        gap_count=gap_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
        advanced_ml_block_completed=True,
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
        backtest_executed=False,
        walk_forward_executed=False,
        transaction_cost_calculated=False,
        slippage_calculated=False,
        benchmark_calculated=False,
        metric_calculation_executed=False,
        performance_claim_generated=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        phase_146_handoff_ready=True,
    )


def build_advanced_ml_acceptance_manifest(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for acceptance manifest."""
    manifest = create_advanced_ml_acceptance_manifest()
    manifest_dict = asdict(manifest)

    records = [manifest_dict]
    df = pd.DataFrame(records)

    summary: Dict[str, Any] = {
        "domain": MANIFEST_DOMAIN,
        "manifest_name": manifest.manifest_name,
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "advanced_ml_block_completed": manifest.advanced_ml_block_completed,
        "component_count": manifest.component_count,
        "accepted_component_count": manifest.accepted_component_count,
        "readiness_score": manifest.readiness_score,
        "manual_review_required": manifest.manual_review_required,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "non_signal": manifest.non_signal,
        "phase_146_handoff_ready": manifest.phase_146_handoff_ready,
        "status": ACCEPTANCE_READY,
    }
    return df, summary


def summarize_advanced_ml_acceptance_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manifest DataFrame."""
    if df.empty:
        return {"manifest_ready": False, "non_signal": True}
    row = df.iloc[0]
    return {
        "manifest_name": row.get("manifest_name", ""),
        "advanced_ml_block_completed": bool(row.get("advanced_ml_block_completed", False)),
        "component_count": int(row.get("component_count", 0)),
        "readiness_score": float(row.get("readiness_score", 0.0)),
        "production_ready": bool(row.get("production_ready", False)),
        "broker_ready": bool(row.get("broker_ready", False)),
        "phase_146_handoff_ready": bool(row.get("phase_146_handoff_ready", False)),
        "non_signal": True,
    }
