import numpy as np
import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_all_nan_diagnostics import (
    build_feature_all_nan_diagnostics_report,
    detect_all_nan_features,
    summarize_feature_all_nan,
)


def test_detect_all_nan_features():
    df = pd.DataFrame({
        "feat_valid": [1.0, np.nan, 3.0],
        "feat_all_nan": [np.nan, np.nan, np.nan],
    })
    res = detect_all_nan_features(df, ["feat_valid", "feat_all_nan"])
    assert len(res) == 2

    valid_row = res[res["column"] == "feat_valid"].iloc[0]
    assert valid_row["all_nan_flag"] == False
    assert valid_row["status"] == "diagnostic_pass"

    nan_row = res[res["column"] == "feat_all_nan"].iloc[0]
    assert nan_row["all_nan_flag"] == True
    assert nan_row["status"] == "diagnostic_fail"
    assert nan_row["manual_review_required"] == True

    summary = summarize_feature_all_nan(res)
    assert summary["all_nan_count"] == 1
    assert summary["status"] == "diagnostic_fail"
