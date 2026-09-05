import numpy as np
import pandas as pd
import pytest
from advanced_feature_quality_drift.feature_rolling_stability import (
    build_feature_rolling_stability_report,
    calculate_rolling_stability,
    summarize_feature_rolling_stability,
)


def test_calculate_rolling_stability():
    np.random.seed(42)
    # 100 rows, window 30
    df = pd.DataFrame({"feat_stable": np.random.randn(100)})
    res = calculate_rolling_stability(df, ["feat_stable"], window=30)
    assert len(res) == 1
    row = res.iloc[0]
    assert 0.0 <= row["stability_score"] <= 1.0


def test_rolling_stability_insufficient_rows():
    df = pd.DataFrame({"feat_stable": [1.0, 2.0, 3.0]})
    res = calculate_rolling_stability(df, ["feat_stable"], window=30)
    assert res.iloc[0]["status"] == "diagnostic_manual_review_required"
    assert res.iloc[0]["manual_review_required"] == True
