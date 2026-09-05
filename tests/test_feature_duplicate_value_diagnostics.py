import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_duplicate_value_diagnostics import (
    build_feature_duplicate_value_diagnostics_report,
    detect_duplicate_value_features,
    summarize_feature_duplicate_value,
)


def test_detect_duplicate_value_features():
    # 95 out of 100 identical values -> duplicate_ratio = 0.95 -> warning
    vals = [0.0] * 95 + [1.0, 2.0, 3.0, 4.0, 5.0]
    df = pd.DataFrame({"feat_dup": vals, "feat_clean": list(range(100))})

    res = detect_duplicate_value_features(df, ["feat_dup", "feat_clean"])
    assert len(res) == 2

    dup_row = res[res["column"] == "feat_dup"].iloc[0]
    assert dup_row["duplicate_ratio"] == 0.95
    assert dup_row["status"] == "diagnostic_pass_with_warnings"
    assert dup_row["manual_review_required"] == True

    clean_row = res[res["column"] == "feat_clean"].iloc[0]
    assert clean_row["duplicate_ratio"] == 0.01
    assert clean_row["status"] == "diagnostic_pass"
