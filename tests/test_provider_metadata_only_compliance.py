from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_metadata_only_compliance import (
    build_provider_metadata_only_compliance_report,
    summarize_provider_metadata_only_compliance,
)


def test_provider_metadata_only_compliance():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_metadata_only_compliance_report(profile)

    assert not df.empty
    assert (df["raw_score"] >= 0.90).all()
    assert summary["all_zero_full_text"] is True
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160
