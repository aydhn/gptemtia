from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_capability_benchmark import (
    build_provider_capability_benchmark_report,
    summarize_provider_capability_benchmark,
)


def test_provider_capability_benchmark():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_capability_benchmark_report(profile)

    assert not df.empty
    assert "raw_score" in df.columns
    assert summary["mean_capability_score"] > 0.0
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
