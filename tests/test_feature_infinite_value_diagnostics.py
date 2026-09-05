import numpy as np
import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_infinite_value_diagnostics import (
    build_feature_infinite_value_diagnostics_report,
    detect_infinite_values,
    summarize_feature_infinite_value,
)


def test_detect_infinite_values():
    df = pd.DataFrame({
        "feat_clean": [1.0, 2.0, 3.0, 4.0],
        "feat_pos_inf": [1.0, np.inf, 3.0, 4.0],
        "feat_neg_inf": [1.0, -np.inf, 3.0, 4.0],
    })
    res = detect_infinite_values(df, ["feat_clean", "feat_pos_inf", "feat_neg_inf"])
    assert len(res) == 3

    clean_row = res[res["column"] == "feat_clean"].iloc[0]
    assert clean_row["total_inf_count"] == 0
    assert clean_row["status"] == "diagnostic_pass"

    pos_row = res[res["column"] == "feat_pos_inf"].iloc[0]
    assert pos_row["pos_inf_count"] == 1
    assert pos_row["total_inf_count"] == 1
    assert pos_row["status"] == "diagnostic_fail"
    assert pos_row["manual_review_required"] == True

    summary = summarize_feature_infinite_value(res)
    assert summary["features_with_inf"] == 2
    assert summary["status"] == "diagnostic_fail"
