from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_domain_registry import (
    build_provider_benchmark_domain_registry,
    summarize_provider_benchmark_domain_registry,
)


def test_provider_benchmark_domain_registry():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_domain_registry(profile)

    assert not df.empty
    assert len(df) >= 27
    assert "domain_label" in df.columns
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
