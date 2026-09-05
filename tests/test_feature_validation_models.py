import pytest
from advanced_feature_validation.feature_validation_models import (
    FeatureValidationFinding,
    FeatureValidationProfile,
    FeatureValidationRule,
    FeatureMatrixIntegrityManifest,
    FeatureValidationScoreResult,
)


def test_feature_validation_models():
    finding = FeatureValidationFinding(
        finding_id="F-001",
        rule_id="R-001",
        column_name="price",
        severity="HIGH",
        finding_type="LOOKAHEAD",
        message="Lookahead detected",
    )
    assert finding.finding_id == "F-001"
    assert finding.current_phase == 121

    profile = FeatureValidationProfile(
        profile_name="strict",
        description="Strict profile",
        enabled=True,
    )
    assert profile.profile_name == "strict"
    assert profile.non_signal is True

    rule = FeatureValidationRule(
        rule_id="R-001",
        rule_name="No-Lookahead",
        description="Verify no negative shifts",
    )
    assert rule.rule_id == "R-001"

    manifest = FeatureMatrixIntegrityManifest(
        matrix_name="main_matrix",
        total_rows=100,
        total_columns=10,
    )
    assert manifest.matrix_name == "main_matrix"

    scores = FeatureValidationScoreResult(
        overall_score=0.95,
        lookahead_score=1.0,
        forbidden_column_score=1.0,
        integrity_score=0.9,
        numeric_sanity_score=0.95,
        completeness_score=0.9,
        is_passing=True,
    )
    assert scores.overall_score == 0.95
