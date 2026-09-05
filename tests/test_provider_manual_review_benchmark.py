from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_manual_review_benchmark import (
    build_provider_manual_review_benchmark_report,
    summarize_provider_manual_review_benchmark,
)


def test_provider_manual_review_benchmark():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_manual_review_benchmark_report(profile)

    assert not df.empty
    assert "raw_score" in df.columns
    assert summary["destructive_action_allowed"] is False
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
