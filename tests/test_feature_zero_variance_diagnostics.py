import numpy as np
import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_zero_variance_diagnostics import (
    build_feature_zero_variance_diagnostics_report,
    detect_zero_variance_features,
    summarize_feature_zero_variance,
)


def test_detect_zero_variance_features():
    df = pd.DataFrame({
        "feat_varying": [1.0, 2.0, 3.0, 4.0, 5.0],
        "feat_constant": [42.0, 42.0, 42.0, 42.0, 42.0],
    })
    res = detect_zero_variance_features(df, ["feat_varying", "feat_constant"])
    assert len(res) == 2

    var_row = res[res["column"] == "feat_varying"].iloc[0]
    assert var_row["zero_variance_flag"] == False
    assert var_row["status"] == "diagnostic_pass"

    const_row = res[res["column"] == "feat_constant"].iloc[0]
    assert const_row["zero_variance_flag"] == True
    assert const_row["status"] == "diagnostic_fail"
    assert const_row["manual_review_required"] == True

    summary = summarize_feature_zero_variance(res)
    assert summary["zero_variance_count"] == 1
    assert summary["status"] == "diagnostic_fail"
