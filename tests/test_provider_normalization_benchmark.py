from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_normalization_benchmark import (
    build_provider_normalization_benchmark_report,
    summarize_provider_normalization_benchmark,
)


def test_provider_normalization_benchmark():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_normalization_benchmark_report(profile)

    assert not df.empty
    assert "raw_score" in df.columns
    assert summary["mean_normalization_score"] > 0.0
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
