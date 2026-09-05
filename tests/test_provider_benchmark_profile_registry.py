from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_profile_registry import (
    build_provider_benchmark_profile_registry,
    summarize_provider_benchmark_profile_registry,
)


def test_provider_benchmark_profile_registry():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
    assert summary["all_local_only"] is True
    assert summary["all_non_production"] is True
