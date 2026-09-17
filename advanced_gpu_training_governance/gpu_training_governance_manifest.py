# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_models import (
    GpuTrainingGovernanceManifest,
)


def create_gpu_training_governance_manifest(
    manifest_name: str = "gpu_training_governance_manifest",
    resource_policy_count: int = 4,
    harness_contract_count: int = 5,
    disabled_execution_report_count: int = 5,
    finding_count: int = 3,
    manual_review_count: int = 8,
    readiness_score: float = 1.0,
    manual_review_required: bool = True,
    profile_name: str = "balanced_local_gpu_training_governance",
) -> GpuTrainingGovernanceManifest:
    """Create a structured, validated GpuTrainingGovernanceManifest instance."""
    return GpuTrainingGovernanceManifest(
        manifest_name=manifest_name,
        current_phase=139,
        target_final_phase=160,
        next_phase=140,
        active_profile=profile_name,
        non_signal=True,
        source_preserved=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
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
        model_transform_executed=False,
        clustering_executed=False,
        supervised_execution=False,
        unsupervised_execution=False,
        ensemble_executed=False,
        calibration_executed=False,
        metric_calculation_executed=False,
        performance_claim_generated=False,
        artifact_persisted=False,
        model_registry_written=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        resource_policy_count=resource_policy_count,
        harness_contract_count=harness_contract_count,
        disabled_execution_report_count=disabled_execution_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
    )


def build_gpu_training_governance_manifest(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build governance manifest DataFrame and summary."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    manifest = create_gpu_training_governance_manifest(
        profile_name=active_profile.name,
    )

    row = {
        "manifest_name": manifest.manifest_name,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "active_profile": manifest.active_profile,
        "non_signal": manifest.non_signal,
        "source_preserved": manifest.source_preserved,
        "local_only": manifest.local_only,
        "dry_run": manifest.dry_run,
        "non_production": manifest.non_production,
        "research_only": manifest.research_only,
        "official_approval": manifest.official_approval,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "dataset_materialized": manifest.dataset_materialized,
        "feature_snapshot_materialized": manifest.feature_snapshot_materialized,
        "contains_target_or_prediction": manifest.contains_target_or_prediction,
        "contains_trading_recommendation": manifest.contains_trading_recommendation,
        "contains_full_article_text": manifest.contains_full_article_text,
        "contains_article_body": manifest.contains_article_body,
        "contains_raw_content": manifest.contains_raw_content,
        "contains_scraped_html": manifest.contains_scraped_html,
        "contains_embedding": manifest.contains_embedding,
        "contains_vector": manifest.contains_vector,
        "sentiment_model_output": manifest.sentiment_model_output,
        "real_training_executed": manifest.real_training_executed,
        "model_training_executed": manifest.model_training_executed,
        "model_fit_executed": manifest.model_fit_executed,
        "model_predict_executed": manifest.model_predict_executed,
        "model_inference_executed": manifest.model_inference_executed,
        "model_transform_executed": manifest.model_transform_executed,
        "clustering_executed": manifest.clustering_executed,
        "supervised_execution": manifest.supervised_execution,
        "unsupervised_execution": manifest.unsupervised_execution,
        "ensemble_executed": manifest.ensemble_executed,
        "calibration_executed": manifest.calibration_executed,
        "metric_calculation_executed": manifest.metric_calculation_executed,
        "performance_claim_generated": manifest.performance_claim_generated,
        "artifact_persisted": manifest.artifact_persisted,
        "model_registry_written": manifest.model_registry_written,
        "destructive_action_allowed": manifest.destructive_action_allowed,
        "auto_fix_allowed": manifest.auto_fix_allowed,
        "auto_drop_allowed": manifest.auto_drop_allowed,
        "resource_policy_count": manifest.resource_policy_count,
        "harness_contract_count": manifest.harness_contract_count,
        "disabled_execution_report_count": manifest.disabled_execution_report_count,
        "finding_count": manifest.finding_count,
        "manual_review_count": manifest.manual_review_count,
        "readiness_score": manifest.readiness_score,
        "manual_review_required": manifest.manual_review_required,
        "created_at": manifest.created_at,
    }

    df = pd.DataFrame([row])
    summary = summarize_gpu_training_governance_manifest(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_governance_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance manifest DataFrame."""
    if df.empty:
        return {"manifest_valid": False, "non_signal": True}
    row = df.iloc[0]
    return {
        "manifest_name": str(row.get("manifest_name", "")),
        "current_phase": int(row.get("current_phase", 139)),
        "next_phase": int(row.get("next_phase", 140)),
        "target_final_phase": int(row.get("target_final_phase", 160)),
        "real_training_executed": bool(row.get("real_training_executed", False)),
        "model_fit_executed": bool(row.get("model_fit_executed", False)),
        "model_predict_executed": bool(row.get("model_predict_executed", False)),
        "target_label_generated": bool(row.get("contains_target_or_prediction", False)),
        "artifact_persisted": bool(row.get("artifact_persisted", False)),
        "model_registry_written": bool(row.get("model_registry_written", False)),
        "readiness_score": float(row.get("readiness_score", 1.0)),
        "dry_run": True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
