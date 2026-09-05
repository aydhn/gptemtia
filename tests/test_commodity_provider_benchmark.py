from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.commodity_provider_benchmark import (
    build_commodity_provider_benchmark_report,
    summarize_commodity_provider_benchmark,
)


def test_commodity_provider_benchmark():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_commodity_provider_benchmark_report(profile)

    assert not df.empty
    assert summary["domain"] == "provider_domain_commodity"
    assert summary["mean_domain_score"] > 0.0
    assert summary["no_scraping_compliant"] is True
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
