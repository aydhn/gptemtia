import pytest
from advanced_feature_quality_drift.factor_availability import (
    build_factor_availability_report,
    summarize_factor_availability,
)


def test_factor_availability_report():
    df, summary = build_factor_availability_report()
    assert not df.empty
    assert summary["total_families"] == 10
    assert summary["fully_available_families"] == 10
    assert summary["status"] == "diagnostic_pass"

    for _, row in df.iterrows():
        assert row["production_ready"] is False
        assert row["official_approval"] is False
        assert row["phase_124_store_ready"] is True
