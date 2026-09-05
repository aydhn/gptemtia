from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.cross_domain_provider_benchmark import (
    build_cross_domain_provider_benchmark_report,
    summarize_cross_domain_provider_benchmark,
)


def test_cross_domain_provider_benchmark():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_cross_domain_provider_benchmark_report(profile)

    assert not df.empty
    assert summary["domain"] == "provider_domain_cross_domain"
    assert summary["mean_cross_domain_score"] > 0.0
    assert summary["all_alignments_pass"] is True
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
