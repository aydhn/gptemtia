"""Phase 136: GPU ML Runtime Manifest.

Master integrity manifest recording all Phase 136 compliance invariants,
capability counts, readiness scores, and execution boundaries.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    MANIFEST_DOMAIN,
    RUNTIME_READY,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_models import GpuMlRuntimeManifest
from advanced_gpu_ml_runtime.ml_runtime_findings import build_ml_runtime_findings_registry
from advanced_gpu_ml_runtime.ml_runtime_readiness_scoring import calculate_ml_runtime_readiness_score


def create_gpu_ml_runtime_manifest(
    manifest_name: str,
    capability_report_count: int,
    safety_contract_count: int,
    input_contract_count: int,
    finding_count: int,
    manual_review_count: int,
    readiness_score: float,
    manual_review_required: bool = True,
) -> GpuMlRuntimeManifest:
    """Create and return a validated GpuMlRuntimeManifest."""
    return GpuMlRuntimeManifest(
        manifest_name=manifest_name,
        current_phase=136,
        target_final_phase=160,
        next_phase=137,
        non_signal=True,
        source_preserved=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
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
        capability_report_count=capability_report_count,
        safety_contract_count=safety_contract_count,
        input_contract_count=input_contract_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=manual_review_required,
    )


def build_gpu_ml_runtime_manifest(
    profile: Optional[GpuMlRuntimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for master GPU ML runtime manifest."""
    active = profile or get_gpu_ml_runtime_profile()

    findings_df, _ = build_ml_runtime_findings_registry(active)
    score_obj = calculate_ml_runtime_readiness_score(findings_df, active)

    manifest_obj = create_gpu_ml_runtime_manifest(
        manifest_name="gpu_ml_runtime_manifest",
        capability_report_count=score_obj.hardware_discovery_count + score_obj.gpu_capability_count + score_obj.cpu_capability_count + score_obj.memory_capability_count,
        safety_contract_count=score_obj.safety_contract_count,
        input_contract_count=score_obj.input_contract_count,
        finding_count=score_obj.finding_count,
        manual_review_count=score_obj.manual_review_count,
        readiness_score=score_obj.readiness_score,
        manual_review_required=True,
    )

    rows = [
        {
            "manifest_name": manifest_obj.manifest_name,
            "current_phase": manifest_obj.current_phase,
            "target_final_phase": manifest_obj.target_final_phase,
            "next_phase": manifest_obj.next_phase,
            "non_signal": manifest_obj.non_signal,
            "source_preserved": manifest_obj.source_preserved,
            "local_only": manifest_obj.local_only,
            "dry_run": manifest_obj.dry_run,
            "non_production": manifest_obj.non_production,
            "research_only": manifest_obj.research_only,
            "official_approval": manifest_obj.official_approval,
            "production_ready": manifest_obj.production_ready,
            "broker_ready": manifest_obj.broker_ready,
            "contains_target_or_prediction": manifest_obj.contains_target_or_prediction,
            "contains_trading_recommendation": manifest_obj.contains_trading_recommendation,
            "contains_full_article_text": manifest_obj.contains_full_article_text,
            "contains_article_body": manifest_obj.contains_article_body,
            "contains_raw_content": manifest_obj.contains_raw_content,
            "contains_scraped_html": manifest_obj.contains_scraped_html,
            "contains_embedding": manifest_obj.contains_embedding,
            "contains_vector": manifest_obj.contains_vector,
            "sentiment_model_output": manifest_obj.sentiment_model_output,
            "model_training_executed": manifest_obj.model_training_executed,
            "model_fit_executed": manifest_obj.model_fit_executed,
            "model_predict_executed": manifest_obj.model_predict_executed,
            "model_inference_executed": manifest_obj.model_inference_executed,
            "model_transform_executed": manifest_obj.model_transform_executed,
            "clustering_executed": manifest_obj.clustering_executed,
            "unsupervised_execution": manifest_obj.unsupervised_execution,
            "ensemble_executed": manifest_obj.ensemble_executed,
            "calibration_executed": manifest_obj.calibration_executed,
            "artifact_persisted": manifest_obj.artifact_persisted,
            "model_registry_written": manifest_obj.model_registry_written,
            "destructive_action_allowed": manifest_obj.destructive_action_allowed,
            "auto_fix_allowed": manifest_obj.auto_fix_allowed,
            "auto_drop_allowed": manifest_obj.auto_drop_allowed,
            "capability_report_count": manifest_obj.capability_report_count,
            "safety_contract_count": manifest_obj.safety_contract_count,
            "input_contract_count": manifest_obj.input_contract_count,
            "finding_count": manifest_obj.finding_count,
            "manual_review_count": manifest_obj.manual_review_count,
            "readiness_score": manifest_obj.readiness_score,
            "manual_review_required": manifest_obj.manual_review_required,
            "status_label": RUNTIME_READY,
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_gpu_ml_runtime_manifest(df)
    summary["domain"] = MANIFEST_DOMAIN
    summary["active_profile"] = active.profile_name
    return df, summary


def summarize_gpu_ml_runtime_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize master manifest DataFrame."""
    score = 0.0
    if not df.empty and "readiness_score" in df.columns:
        score = float(df.iloc[0]["readiness_score"])
    return {
        "manifest_name": "gpu_ml_runtime_manifest",
        "current_phase": 136,
        "next_phase": 137,
        "target_final_phase": 160,
        "readiness_score": score,
        "manifest_valid": True,
        "model_training_executed": False,
        "model_predict_executed": False,
        "clustering_executed": False,
        "artifact_persisted": False,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
