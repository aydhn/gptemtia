from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_weight_registry import (
    build_provider_benchmark_weight_registry,
    summarize_provider_benchmark_weight_registry,
)


def test_provider_benchmark_weight_registry():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_weight_registry(profile)

    assert not df.empty
    assert "weight" in df.columns
    assert (df["weight"] >= 0.0).all()
    assert (df["weight"] <= 1.0).all()
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
