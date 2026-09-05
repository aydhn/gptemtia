import pytest
from advanced_feature_quality_drift.factor_family_drift import (
    build_factor_family_drift_report,
    summarize_factor_family_drift,
)


def test_factor_family_drift_report():
    df, summary = build_factor_family_drift_report()
    assert not df.empty
    assert summary["total_families"] == 10
    assert summary["stable_families_count"] == 10
    assert summary["status"] == "diagnostic_pass"

    for _, row in df.iterrows():
        assert row["non_signal"] is True
        assert row["status"] == "diagnostic_pass"
