import pytest
import pandas as pd
from advanced_feature_validation.no_leakage_guard import run_no_leakage_guard


def test_no_leakage_guard():
    clean_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "feat_val": [1, 2, 3, 4, 5],
    })
    res_clean = run_no_leakage_guard(clean_df)
    assert res_clean["guard_status"] == "PASSED"
    assert res_clean["leakage_detected"] is False

    leaky_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=5),
        "future_return_5d": [0.01, 0.02, 0.03, 0.04, 0.05],
    })
    res_leaky = run_no_leakage_guard(leaky_df)
    assert res_leaky["guard_status"] == "VIOLATION"
    assert res_leaky["leakage_detected"] is True
