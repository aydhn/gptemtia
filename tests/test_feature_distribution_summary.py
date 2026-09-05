import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_distribution_summary import (
    build_distribution_summary,
    build_feature_distribution_summary_report,
    summarize_feature_distribution_summary,
)


def test_build_distribution_summary():
    df = pd.DataFrame({
        "feat_vals": [1.0, 2.0, 3.0, 4.0, 5.0],
    })
    res = build_distribution_summary(df, ["feat_vals"])
    assert len(res) == 1
    row = res.iloc[0]
    assert row["mean"] == 3.0
    assert row["median"] == 3.0
    assert row["min"] == 1.0
    assert row["max"] == 5.0
    assert "skewness" in row
    assert "kurtosis" in row

    summary = summarize_feature_distribution_summary(res)
    assert summary["total_features"] == 1
    assert summary["features_with_data"] == 1
