import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_drift_findings import (
    build_feature_drift_findings_registry,
    summarize_feature_drift_findings,
)


def test_feature_drift_findings_nominal():
    df, summary = build_feature_drift_findings_registry()
    assert not df.empty
    assert summary["critical_drift_findings"] == 0
    assert summary["status"] == "diagnostic_pass"

    for _, row in df.iterrows():
        assert row["non_signal"] is True
        assert row["destructive_action_allowed"] is False
