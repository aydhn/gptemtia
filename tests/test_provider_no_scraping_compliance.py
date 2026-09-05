from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_no_scraping_compliance import (
    build_provider_no_scraping_compliance_report,
    summarize_provider_no_scraping_compliance,
)


def test_provider_no_scraping_compliance():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_no_scraping_compliance_report(profile)

    assert not df.empty
    assert (df["raw_score"] == 1.0).all()
    assert summary["all_compliant"] is True
    assert summary["non_compliant_count"] == 0
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
