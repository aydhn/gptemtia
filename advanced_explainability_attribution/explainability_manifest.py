# -*- coding: utf-8 -*-
"""Phase 143: Explainability Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)
from advanced_explainability_attribution.explainability_models import ExplainabilityManifest


def build_explainability_manifest(
    profile: Optional[ExplainabilityProfile] = None,
    explainability_contract_count: int = 7,
    attribution_contract_count: int = 8,
    disabled_execution_report_count: int = 36,
    finding_count: int = 4,
    manual_review_count: int = 4,
    readiness_score: float = 1.0,
) -> ExplainabilityManifest:
    """Build the comprehensive Phase 143 Explainability Manifest."""
    prof = profile or get_explainability_profile()

    return ExplainabilityManifest(
        manifest_id="manifest_phase_143_explainability_attribution",
        current_phase=143,
        target_final_phase=160,
        next_phase=144,
        explainability_contract_count=explainability_contract_count,
        attribution_contract_count=attribution_contract_count,
        disabled_execution_report_count=disabled_execution_report_count,
        finding_count=finding_count,
        manual_review_count=manual_review_count,
        readiness_score=readiness_score,
        manual_review_required=True,
        # Invariant safety flags
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
        probability_prediction_executed=False,
        calibration_executed=False,
        uncertainty_estimation_executed=False,
        drift_calculation_executed=False,
        explainability_calculation_executed=False,
        feature_attribution_calculation_executed=False,
        feature_importance_calculation_executed=False,
        shap_executed=False,
        lime_executed=False,
        permutation_importance_executed=False,
        pdp_executed=False,
        ice_executed=False,
        surrogate_model_executed=False,
        counterfactual_generated=False,
        explanation_model_action_generated=False,
        metric_calculation_executed=False,
        performance_claim_generated=False,
        artifact_persisted=False,
        model_registry_written=False,
        destructive_action_allowed=False,
        auto_fix_allowed=False,
        auto_drop_allowed=False,
    )


def summarize_explainability_manifest(manifest: ExplainabilityManifest) -> Dict[str, Any]:
    """Summarize the explainability manifest."""
    return {
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "next_phase": manifest.next_phase,
        "target_final_phase": manifest.target_final_phase,
        "explainability_contract_count": manifest.explainability_contract_count,
        "attribution_contract_count": manifest.attribution_contract_count,
        "disabled_execution_report_count": manifest.disabled_execution_report_count,
        "finding_count": manifest.finding_count,
        "manual_review_count": manifest.manual_review_count,
        "readiness_score": manifest.readiness_score,
        "all_invariants_preserved": (
            manifest.non_signal
            and manifest.source_preserved
            and manifest.local_only
            and manifest.dry_run
            and manifest.non_production
            and manifest.research_only
            and not manifest.official_approval
            and not manifest.production_ready
            and not manifest.broker_ready
            and not manifest.real_training_executed
            and not manifest.model_predict_executed
            and not manifest.shap_executed
            and not manifest.lime_executed
            and not manifest.permutation_importance_executed
            and not manifest.pdp_executed
            and not manifest.ice_executed
            and not manifest.surrogate_model_executed
            and not manifest.counterfactual_generated
            and not manifest.explanation_model_action_generated
            and not manifest.contains_trading_recommendation
        ),
    }
