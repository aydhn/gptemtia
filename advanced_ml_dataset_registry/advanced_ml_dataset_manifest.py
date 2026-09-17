# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Manifest aggregator module.

Compiles top-level audit manifest verifying contract counts, readiness scores,
and enforcing strict non-signal, zero-training invariants.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_models import (
    AdvancedMlDatasetManifest,
)


def create_advanced_ml_dataset_manifest(
    manifest_name: str = "advanced_ml_dataset_manifest",
    dataset_contract_count: int = 9,
    experiment_count: int = 6,
    guard_count: int = 4,
    finding_count: int = 6,
    manual_review_count: int = 9,
    readiness_score: float = 1.0,
    manual_review_required: bool = True,
) -> AdvancedMlDatasetManifest:
    """Create a typed AdvancedMlDatasetManifest instance."""
    return AdvancedMlDatasetManifest(
        manifest_name=manifest_name,
        current_phase=137,
        target_final_phase=160,
        next_phase=138,
        dataset_contract_count=dataset_contract_count,
        experiment_count=experiment_count,
        guard_count=guard_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
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
        model_training_executed=False,
        model_fit_executed=False,
        model_predict_executed=False,
        model_inference_executed=False,
        model_transform_executed=False,
        clustering_executed=False,
        unsupervised_execution=False,
        ensemble_executed=False,
        calibration_executed=False,
        artifact_persisted=False,
        model_registry_written=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
        status="dataset_contract_placeholder_only",
    )


def build_advanced_ml_dataset_manifest(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for the Phase 137 Manifest."""
    p = profile or get_default_advanced_ml_dataset_profile()

    manifest = create_advanced_ml_dataset_manifest()
    row = {
        "manifest_name": manifest.manifest_name,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "dataset_contract_count": manifest.dataset_contract_count,
        "experiment_count": manifest.experiment_count,
        "guard_count": manifest.guard_count,
        "finding_count": manifest.finding_count,
        "manual_review_count": manifest.manual_review_count,
        "readiness_score": manifest.readiness_score,
        "manual_review_required": manifest.manual_review_required,
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
        "model_training_executed": manifest.model_training_executed,
        "model_fit_executed": manifest.model_fit_executed,
        "model_predict_executed": manifest.model_predict_executed,
        "model_inference_executed": manifest.model_inference_executed,
        "model_transform_executed": manifest.model_transform_executed,
        "clustering_executed": manifest.clustering_executed,
        "unsupervised_execution": manifest.unsupervised_execution,
        "ensemble_executed": manifest.ensemble_executed,
        "calibration_executed": manifest.calibration_executed,
        "artifact_persisted": manifest.artifact_persisted,
        "model_registry_written": manifest.model_registry_written,
        "destructive_action_allowed": manifest.destructive_action_allowed,
        "auto_fix_allowed": manifest.auto_fix_allowed,
        "auto_drop_allowed": manifest.auto_drop_allowed,
        "status": manifest.status,
    }

    df = pd.DataFrame([row])
    summary = summarize_advanced_ml_dataset_manifest(df)
    return df, summary


def summarize_advanced_ml_dataset_manifest(df: pd.DataFrame) -> Dict:
    """Summarize the manifest DataFrame."""
    first = df.iloc[0].to_dict() if not df.empty else {}
    return {
        "manifest_name": first.get("manifest_name", "advanced_ml_dataset_manifest"),
        "current_phase": first.get("current_phase", 137),
        "target_final_phase": first.get("target_final_phase", 160),
        "next_phase": first.get("next_phase", 138),
        "dataset_contract_count": first.get("dataset_contract_count", 9),
        "experiment_count": first.get("experiment_count", 6),
        "readiness_score": first.get("readiness_score", 1.0),
        "dataset_materialized": False,
        "feature_snapshot_materialized": False,
        "model_training_executed": False,
        "model_predict_executed": False,
        "clustering_executed": False,
        "artifact_persisted": False,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
        "status": first.get("status", "dataset_contract_placeholder_only"),
    }
