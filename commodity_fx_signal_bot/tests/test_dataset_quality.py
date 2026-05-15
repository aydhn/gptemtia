import pandas as pd
import numpy as np
from ml.dataset_quality import check_dataset_min_rows, check_feature_nan_ratio, check_target_class_balance, check_feature_variance, build_dataset_quality_report
from ml.dataset_config import get_default_ml_dataset_profile

def test_check_dataset_min_rows():
    df = pd.DataFrame({"A": range(50)})
    res = check_dataset_min_rows(df, 100)
    assert not res["passed"]

def test_check_feature_nan_ratio():
    X = pd.DataFrame({"A": [1, np.nan, np.nan, np.nan]})
    res = check_feature_nan_ratio(X, 0.5)
    assert not res["passed"]
    assert res["ratio"] == 0.75

def test_check_target_class_balance():
    y = pd.Series(["up", "up", "down", "flat"])
    res = check_target_class_balance(y)
    assert res["balance"]["up"] == 0.5

def test_check_feature_variance():
    X = pd.DataFrame({"A": [1, 1, 1], "B": [1, 2, 3]})
    res = check_feature_variance(X)
    assert res["low_variance_count"] == 1
    assert "A" in res["low_variance_columns"]

def test_build_dataset_quality_report():
    X = pd.DataFrame({"f1": range(200)})
    y = pd.DataFrame({"target": ["up"]*200})
    dataset = pd.concat([X, y], axis=1)
    dataset.index = pd.date_range("2020-01-01", periods=200)

    prof = get_default_ml_dataset_profile()
    report = build_dataset_quality_report(X, y, dataset, prof)

    assert report["passed"]
