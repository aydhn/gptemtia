import pytest
from advanced_provider_benchmark.provider_benchmark_models import (
    ProviderBenchmarkProfileItem,
    ProviderBenchmarkDomain,
    BenchmarkMetric,
    BenchmarkWeight,
    ProviderBenchmarkRecord,
    ProviderBenchmarkFinding,
    ProviderBenchmarkManualReviewItem,
    ProviderBenchmarkScore,
    build_provider_benchmark_profile_id,
    build_provider_benchmark_domain_id,
    build_benchmark_metric_id,
    build_benchmark_weight_id,
    build_provider_benchmark_record_id,
    build_provider_benchmark_finding_id,
    build_provider_benchmark_review_id,
    build_provider_benchmark_score_id,
)


def test_provider_benchmark_models():
    prof_item = ProviderBenchmarkProfileItem(
        profile_id="p1",
        profile_name="prof1",
        current_phase=115,
        target_final_phase=160,
        next_phase=116,
        local_only=True,
        non_production=True,
        research_only=True,
        dry_run=True,
        status_label="benchmark_pass",
        warnings=[],
    )
    assert prof_item.to_dict()["current_phase"] == 115

    score = ProviderBenchmarkScore(
        score_id="s1",
        provider_name="fx_prov",
        provider_domain="provider_domain_fx",
        total_score=0.88,
        coverage_score=0.9,
        capability_score=0.85,
        quality_score=0.92,
        normalization_score=0.91,
        traceability_score=0.9,
        compliance_score=1.0,
        manual_review_penalty=0.0,
        status_label="benchmark_pass",
        official_approval=False,
        production_ready=False,
        broker_ready=False,
        notes="note",
    )
    assert score.to_dict()["total_score"] == 0.88
    assert score.official_approval is False

    with pytest.raises(ValueError):
        ProviderBenchmarkScore(
            score_id="s2",
            provider_name="p",
            provider_domain="d",
            total_score=0.8,
            coverage_score=0.8,
            capability_score=0.8,
            quality_score=0.8,
            normalization_score=0.8,
            traceability_score=0.8,
            compliance_score=1.0,
            manual_review_penalty=0.0,
            status_label="benchmark_pass",
            official_approval=True,
            production_ready=False,
            broker_ready=False,
            notes="",
        )

    with pytest.raises(ValueError):
        ProviderBenchmarkManualReviewItem(
            review_id="r1",
            finding_id="f1",
            provider_name="p",
            provider_domain="d",
            review_reason="r",
            suggested_action="s",
            destructive_action_allowed=True,
            status_label="pending",
        )

    assert build_provider_benchmark_profile_id("test") == "pb_profile::test"
    assert build_provider_benchmark_domain_id("test") == "pb_domain::test"
    assert build_benchmark_metric_id("test") == "pb_metric::test"
    assert build_benchmark_weight_id("m", "d") == "pb_weight::m::d"
    assert build_provider_benchmark_record_id("p", "m") == "pb_rec::p::m"
    assert build_provider_benchmark_finding_id("p", "m") == "pb_find::p::m"
    assert build_provider_benchmark_review_id("f") == "pb_review::f"
    assert build_provider_benchmark_score_id("p", "d") == "pb_score::p::d"
