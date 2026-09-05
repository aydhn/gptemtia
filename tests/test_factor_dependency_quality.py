import pytest
from advanced_feature_quality_drift.factor_dependency_quality import (
    build_factor_dependency_quality_report,
    summarize_factor_dependency_quality,
)


def test_factor_dependency_quality_report():
    df, summary = build_factor_dependency_quality_report()
    assert not df.empty
    assert summary["total_dependencies"] == 7
    assert summary["passed_dependencies"] == 7
    assert summary["failed_dependencies"] == 0
    assert summary["status"] == "diagnostic_pass"

    phases = list(df["phase_ref"])
    assert 116 in phases
    assert 117 in phases
    assert 118 in phases
    assert 119 in phases
    assert 120 in phases
    assert 121 in phases
    assert 122 in phases
