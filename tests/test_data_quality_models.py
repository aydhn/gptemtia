import pytest
from advanced_data_quality.data_quality_models import (
    DataQualityProfileItem,
    DataQualityDomain,
    QualityRule,
    QualityFinding,
    ManualReviewItem,
    ProviderQualityScore,
    DatasetQualityScore,
    build_data_quality_profile_id,
    build_data_quality_domain_id,
    build_quality_rule_id,
    build_quality_finding_id,
    build_manual_review_id,
    build_provider_quality_score_id,
    build_dataset_quality_score_id,
)


def test_data_quality_models_and_ids():
    p_id = build_data_quality_profile_id("test profile")
    assert p_id == "dqp_test_profile"

    d_id = build_data_quality_domain_id("schema_domain")
    assert d_id == "dqd_schema_domain"

    r_id = build_quality_rule_id("rule_a", "domain_b")
    assert r_id == "rule_domain_b_rule_a"

    f_id = build_quality_finding_id("r1", "fx_quote", "bid")
    assert f_id == "find_r1_fx_quote_bid"

    m_id = build_manual_review_id(f_id)
    assert m_id == f"rev_{f_id}"

    # ManualReviewItem must enforce destructive_action_allowed is False
    item = ManualReviewItem(
        review_id="rev_1",
        finding_id="find_1",
        dataset_type="dataset_fx_ohlcv",
        provider_name="test_p",
        priority="quality_high",
        review_reason="test",
        suggested_action="test",
        destructive_action_allowed=False,
        status_label="quality_manual_review_required"
    )
    d = item.to_dict()
    assert d["destructive_action_allowed"] is False
