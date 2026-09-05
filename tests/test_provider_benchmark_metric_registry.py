from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_metric_registry import (
    build_provider_benchmark_metric_registry,
    summarize_provider_benchmark_metric_registry,
)


def test_provider_benchmark_metric_registry():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_metric_registry(profile)

    assert not df.empty
    assert len(df) >= 10
    assert "metric_label" in df.columns
    assert "metric_coverage" in df["metric_label"].values
    assert "metric_no_scraping_compliance" in df["metric_label"].values
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
