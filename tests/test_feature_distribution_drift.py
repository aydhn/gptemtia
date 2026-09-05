import numpy as np
import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_distribution_drift import (
    build_feature_distribution_drift_report,
    compare_feature_distribution_baseline,
    summarize_feature_distribution_drift,
)


def test_compare_feature_distribution_baseline():
    np.random.seed(42)
    baseline_df = pd.DataFrame({"feat_test": np.random.normal(0.0, 1.0, 50)})
    # Shifted current by +2.0 std
    current_df = pd.DataFrame({"feat_test": np.random.normal(2.0, 1.0, 50)})

    res = compare_feature_distribution_baseline(current_df, baseline_df, ["feat_test"])
    assert len(res) == 1
    row = res.iloc[0]
    assert row["mean_abs_delta"] > 1.0
    assert row["drift_status"] == "diagnostic_fail"
    assert row["manual_review_required"] == True

    summary = summarize_feature_distribution_drift(res)
    assert summary["critical_drift_count"] == 1
    assert summary["status"] == "diagnostic_fail"


def test_distribution_drift_insufficient_rows():
    b_df = pd.DataFrame({"feat_test": [1.0, 2.0]})
    c_df = pd.DataFrame({"feat_test": [1.0, 2.0]})
    res = compare_feature_distribution_baseline(c_df, b_df, ["feat_test"])
    assert res.iloc[0]["drift_status"] == "diagnostic_manual_review_required"
    assert res.iloc[0]["manual_review_required"] == True
