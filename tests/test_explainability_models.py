# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Models."""

import pytest
from advanced_explainability_attribution.explainability_models import (
    ExplainabilityProfileItem,
    ExplainabilityReportContract,
    FeatureAttributionContract,
    ExplanationPlaceholderItem,
    AttributionMethodPolicy,
    ExplainabilityReadinessScore,
    ExplainabilityManifest,
)


def test_explainability_models():
    prof_item = ExplainabilityProfileItem(
        profile_name="test_prof",
        display_name="Test Profile",
        description="Testing profile item",
    )
    assert prof_item.current_phase == 143
    assert prof_item.non_signal is True

    rep_contract = ExplainabilityReportContract(
        contract_name="test_report_contract",
        explanation_family="global_explanation",
        candidate_model_contract_ref="cand_v1",
        ensemble_contract_ref="ens_v1",
        dataset_contract_ref="ds_v1",
        featurestore_contract_ref="fs_v1",
        drift_contract_ref="drift_v1",
        calibration_uncertainty_contract_ref="calib_v1",
        required_no_lookahead_guard_ref="guard_look_v1",
        required_metadata_only_news_guard_ref="guard_meta_v1",
        required_source_preservation_guard_ref="guard_source_v1",
    )
    assert rep_contract.explainability_calculation_allowed is False
    assert rep_contract.non_signal_required is True

    feat_contract = FeatureAttributionContract(
        contract_name="test_feat_contract",
        method_name="shap",
        attribution_scope="global",
        target_feature_set_ref="fs_v1",
    )
    assert feat_contract.shap_execution_allowed is False

    score = ExplainabilityReadinessScore(
        score_id="test_score",
        readiness_score=1.0,
        classification="ready",
    )
    assert score.readiness_score == 1.0

    with pytest.raises(ValueError):
        ExplainabilityReadinessScore(
            score_id="invalid",
            readiness_score=1.5,
            classification="invalid",
        )
