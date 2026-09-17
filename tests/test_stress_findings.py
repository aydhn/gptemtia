# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Findings Registry."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_findings import (
    build_stress_findings_registry,
    create_stress_finding,
)


def test_findings_registry():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_findings_registry(prof)
    assert not df.empty
    assert summary["total_findings"] == len(df)
    assert summary["non_signal"] is True

    f = create_stress_finding(
        finding_type="test_finding",
        domain="test_domain",
        severity_label="INFO",
        message="test msg",
        recommendation="test rec",
    )
    assert f.finding_type == "test_finding"
