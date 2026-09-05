import numpy as np
import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_missingness_diagnostics import (
    build_feature_missingness_diagnostics_report,
    calculate_missingness,
    summarize_feature_missingness,
)


def test_calculate_missingness_accurate():
    df = pd.DataFrame({
        "feat_a": [1.0, 2.0, np.nan, 4.0],  # 25% missing
        "feat_b": [np.nan, np.nan, np.nan, np.nan],  # 100% missing
        "feat_c": [1.0, 2.0, 3.0, 4.0],  # 0% missing
    })
    res = calculate_missingness(df, ["feat_a", "feat_b", "feat_c"])
    assert len(res) == 3

    row_a = res[res["column"] == "feat_a"].iloc[0]
    assert row_a["missing_count"] == 1
    assert row_a["missing_ratio"] == 0.25
    assert row_a["status"] == "diagnostic_pass_with_warnings"

    row_b = res[res["column"] == "feat_b"].iloc[0]
    assert row_b["missing_count"] == 4
    assert row_b["missing_ratio"] == 1.0
    assert row_b["status"] == "diagnostic_fail"
    assert row_b["manual_review_required"] == True

    row_c = res[res["column"] == "feat_c"].iloc[0]
    assert row_c["missing_count"] == 0
    assert row_c["missing_ratio"] == 0.0
    assert row_c["status"] == "diagnostic_pass"


def test_build_feature_missingness_report():
    df_rep, summary = build_feature_missingness_diagnostics_report()
    assert not df_rep.empty
    assert summary["current_phase"] == 123
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
