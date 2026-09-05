from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_scoring import (
    build_provider_benchmark_score_report,
    summarize_provider_benchmark_scores,
    calculate_provider_benchmark_score,
)
from advanced_provider_benchmark.provider_benchmark_weight_registry import (
    build_provider_benchmark_weight_registry,
)


def test_provider_benchmark_scoring():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_score_report(profile)

    assert not df.empty
    assert "total_score" in df.columns
    assert (df["total_score"] >= 0.0).all()
    assert (df["total_score"] <= 1.0).all()
    assert (df["official_approval"] == False).all()
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert summary["official_approval_guarantee"] is False
    assert summary["production_ready_guarantee"] is False
    assert summary["broker_ready_guarantee"] is False
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160


def test_calculate_single_score():
    profile = get_default_provider_benchmark_profile()
    weights_df, _ = build_provider_benchmark_weight_registry(profile)
    score_obj = calculate_provider_benchmark_score(
        records_df=None,
        provider_name="test_provider",
        provider_domain="provider_domain_fx",
        weights_df=weights_df,
        profile=profile,
    )
    assert 0.0 <= score_obj.total_score <= 1.0
    assert score_obj.official_approval is False
