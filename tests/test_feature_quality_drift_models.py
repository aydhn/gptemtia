import pytest
from advanced_feature_quality_drift.feature_quality_drift_models import (
    FeatureQualityDriftProfileItem,
    FeatureQualityMetric,
    FeatureDriftMetric,
    FeatureQualityThreshold,
    FeatureDriftThreshold,
    FeatureQualityFinding,
    FeatureDriftFinding,
    FeatureQualityScore,
    FeatureDriftScore,
    FeatureQualityDriftManifest,
)


def test_feature_quality_drift_models():
    # Profile item
    item = FeatureQualityDriftProfileItem(
        profile_name="test_profile",
        description="Test profile description",
    )
    assert item.non_signal is True
    assert item.official_approval is False

    # Metric
    q_met = FeatureQualityMetric(
        metric_id="missingness_ratio",
        metric_name="Missingness Ratio",
        domain="missingness_domain",
        description="Missingness check",
        metric_type="ratio",
        severity="quality_medium",
    )
    assert q_met.non_signal is True
    assert q_met.destructive_action_allowed is False

    # Threshold
    q_thr = FeatureQualityThreshold(
        threshold_id="thresh_1",
        metric_id="missingness_ratio",
        warning_threshold=0.25,
        critical_threshold=0.50,
    )
    assert q_thr.auto_drop_allowed is False
    assert q_thr.auto_fix_allowed is False

    # Score
    q_score = FeatureQualityScore(
        profile_name="test_profile",
        overall_quality_score=0.95,
        missingness_score=1.0,
        infinite_value_score=1.0,
        zero_variance_score=0.9,
        duplicate_score=0.95,
        namespace_score=1.0,
    )
    assert 0.0 <= q_score.overall_quality_score <= 1.0
    assert q_score.official_approval is False

    # Manifest
    man = FeatureQualityDriftManifest(
        manifest_id="manifest_1",
        matrix_or_factor_name="matrix_1",
        feature_count=10,
    )
    assert man.non_signal is True
    assert man.source_preserved is True
    assert man.auto_drop_allowed is False


def test_feature_quality_drift_models_invariants_failure():
    with pytest.raises(ValueError):
        FeatureQualityScore(
            profile_name="bad_score",
            overall_quality_score=1.5,
            missingness_score=1.0,
            infinite_value_score=1.0,
            zero_variance_score=1.0,
            duplicate_score=1.0,
            namespace_score=1.0,
        )

    with pytest.raises(ValueError):
        FeatureQualityThreshold(
            threshold_id="bad_thresh",
            metric_id="m1",
            warning_threshold=0.2,
            critical_threshold=0.5,
            auto_drop_allowed=True,
        )
