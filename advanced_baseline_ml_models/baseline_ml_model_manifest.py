# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Manifest.

Constructs and verifies the full integrity manifest for Phase 138.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_models import BaselineMlModelManifest


def create_baseline_ml_model_manifest(
    manifest_name: str = "baseline_ml_model_manifest",
    model_contract_count: int = 10,
    harness_contract_count: int = 5,
    disabled_execution_report_count: int = 5,
    finding_count: int = 0,
    manual_review_count: int = 5,
    readiness_score: float = 1.0,
    manual_review_required: bool = True,
) -> BaselineMlModelManifest:
    """Create a new BaselineMlModelManifest dataclass instance."""
    return BaselineMlModelManifest(
        manifest_name=manifest_name,
        current_phase=138,
        target_final_phase=160,
        next_phase=139,
        model_contract_count=model_contract_count,
        harness_contract_count=harness_contract_count,
        disabled_execution_report_count=disabled_execution_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        status="baseline_contract_placeholder_only",
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
    )


def build_baseline_ml_model_manifest(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manifest DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    manifest_obj = create_baseline_ml_model_manifest()

    rows = [{
        "manifest_name": manifest_obj.manifest_name,
        "current_phase": manifest_obj.current_phase,
        "target_final_phase": manifest_obj.target_final_phase,
        "next_phase": manifest_obj.next_phase,
        "model_contract_count": manifest_obj.model_contract_count,
        "harness_contract_count": manifest_obj.harness_contract_count,
        "disabled_execution_report_count": manifest_obj.disabled_execution_report_count,
        "finding_count": manifest_obj.finding_count,
        "manual_review_count": manifest_obj.manual_review_count,
        "readiness_score": manifest_obj.readiness_score,
        "status": manifest_obj.status,
        "non_signal": manifest_obj.non_signal,
        "source_preserved": manifest_obj.source_preserved,
        "local_only": manifest_obj.local_only,
        "dry_run": manifest_obj.dry_run,
        "non_production": manifest_obj.non_production,
        "research_only": manifest_obj.research_only,
        "official_approval": manifest_obj.official_approval,
        "production_ready": manifest_obj.production_ready,
        "broker_ready": manifest_obj.broker_ready,
        "dataset_materialized": manifest_obj.dataset_materialized,
        "feature_snapshot_materialized": manifest_obj.feature_snapshot_materialized,
        "contains_target_or_prediction": manifest_obj.contains_target_or_prediction,
        "contains_trading_recommendation": manifest_obj.contains_trading_recommendation,
        "contains_full_article_text": manifest_obj.contains_full_article_text,
        "contains_article_body": manifest_obj.contains_article_body,
        "contains_raw_content": manifest_obj.contains_raw_content,
        "contains_scraped_html": manifest_obj.contains_scraped_html,
        "contains_embedding": manifest_obj.contains_embedding,
        "contains_vector": manifest_obj.contains_vector,
        "sentiment_model_output": manifest_obj.sentiment_model_output,
        "real_training_executed": manifest_obj.real_training_executed,
        "model_training_executed": manifest_obj.model_training_executed,
        "model_fit_executed": manifest_obj.model_fit_executed,
        "model_predict_executed": manifest_obj.model_predict_executed,
        "model_inference_executed": manifest_obj.model_inference_executed,
        "model_transform_executed": manifest_obj.model_transform_executed,
        "clustering_executed": manifest_obj.clustering_executed,
        "supervised_execution": manifest_obj.supervised_execution,
        "unsupervised_execution": manifest_obj.unsupervised_execution,
        "ensemble_executed": manifest_obj.ensemble_executed,
        "calibration_executed": manifest_obj.calibration_executed,
        "metric_calculation_executed": manifest_obj.metric_calculation_executed,
        "performance_claim_generated": manifest_obj.performance_claim_generated,
        "artifact_persisted": manifest_obj.artifact_persisted,
        "model_registry_written": manifest_obj.model_registry_written,
        "destructive_action_allowed": manifest_obj.destructive_action_allowed,
        "auto_fix_allowed": manifest_obj.auto_fix_allowed,
        "auto_drop_allowed": manifest_obj.auto_drop_allowed,
        "created_at": manifest_obj.created_at,
    }]

    df = pd.DataFrame(rows)
    summary = summarize_baseline_ml_model_manifest(df)
    return df, summary


def summarize_baseline_ml_model_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline ML model manifest."""
    row = df.iloc[0] if not df.empty else {}
    return {
        "manifest_name": row.get("manifest_name", "baseline_ml_model_manifest"),
        "status": row.get("status", "baseline_contract_placeholder_only"),
        "current_phase": row.get("current_phase", 138),
        "next_phase": row.get("next_phase", 139),

        "target_final_phase": int(row.get("target_final_phase", 160)),
        "model_contract_count": int(row.get("model_contract_count", 10)),
        "harness_contract_count": int(row.get("harness_contract_count", 5)),
        "readiness_score": float(row.get("readiness_score", 1.0)),
        "real_training_executed": bool(row.get("real_training_executed", False)),
        "model_fit_executed": bool(row.get("model_fit_executed", False)),
        "model_predict_executed": bool(row.get("model_predict_executed", False)),
        "metric_calculation_executed": bool(row.get("metric_calculation_executed", False)),
        "artifact_persisted": bool(row.get("artifact_persisted", False)),
        "model_registry_written": bool(row.get("model_registry_written", False)),
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
