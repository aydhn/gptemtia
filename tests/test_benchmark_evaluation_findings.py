# -*- coding: utf-8 -*-
"""Phase 151 Unit Tests: Benchmark Evaluation Findings."""

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_findings import (
    build_benchmark_evaluation_findings_registry,
    create_benchmark_evaluation_finding,
)


def test_benchmark_evaluation_findings():
    profile = get_default_benchmark_evaluation_profile()
    df, s = build_benchmark_evaluation_findings_registry(profile)

    assert not df.empty
    assert "finding_id" in df.columns
    assert s["has_blockers"] is False
    assert s["non_signal"] is True

    f = create_benchmark_evaluation_finding(
        finding_type="test_finding",
        domain="benchmark_evaluation_domain",
        severity_label="INFO",
        message="Test message",
        recommendation="Test recommendation",
    )
    assert f.finding_type == "test_finding"
    assert f.is_blocker is False
