from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_manual_review_queue import (
    build_provider_benchmark_manual_review_queue,
    summarize_provider_benchmark_manual_review_queue,
)


def test_provider_benchmark_manual_review_queue():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_manual_review_queue(None, profile)

    assert not df.empty
    assert "review_id" in df.columns
    assert (df["destructive_action_allowed"] == False).all()
    assert summary["all_non_destructive"] is True
    assert summary["destructive_actions_prevented"] is True
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
