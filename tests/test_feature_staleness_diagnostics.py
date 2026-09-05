import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_staleness_diagnostics import (
    build_feature_staleness_diagnostics_report,
    detect_stale_features,
    summarize_feature_staleness,
)


def test_detect_stale_features():
    # 40 consecutive frozen values -> warning threshold exceeded
    frozen = [5.0] * 40 + [1.0, 2.0, 3.0]
    df = pd.DataFrame({"feat_stale": frozen, "feat_fresh": list(range(43))})

    res = detect_stale_features(df, feature_columns=["feat_stale", "feat_fresh"], warning_bars=30, critical_bars=60)
    assert len(res) == 2

    stale_row = res[res["column"] == "feat_stale"].iloc[0]
    assert stale_row["max_consecutive_unchanged"] == 40
    assert stale_row["status"] == "diagnostic_pass_with_warnings"
    assert stale_row["manual_review_required"] == True

    fresh_row = res[res["column"] == "feat_fresh"].iloc[0]
    assert fresh_row["max_consecutive_unchanged"] == 1
    assert fresh_row["status"] == "diagnostic_pass"
