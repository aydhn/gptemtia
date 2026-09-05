from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_findings import (
    build_provider_benchmark_findings_registry,
    summarize_provider_benchmark_findings,
    create_provider_benchmark_finding,
)


def test_provider_benchmark_findings():
    profile = get_default_provider_benchmark_profile()
    df, summary = build_provider_benchmark_findings_registry(profile)

    assert not df.empty
    assert "finding_id" in df.columns
    assert "severity_label" in df.columns
    assert summary["current_phase"] == 115
    assert summary["target_final_phase"] == 160

    f = create_provider_benchmark_finding(
        provider_name="p",
        provider_domain="d",
        metric_label="m",
        severity_label="s",
        status_label="st",
        message="msg",
        recommendation="rec",
        manual_review_required=True,
    )
    assert f.manual_review_required is True
