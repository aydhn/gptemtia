import pytest
import pandas as pd
from mtf.mtf_quality import check_mtf_nan_ratio, check_mtf_index_integrity


def test_check_mtf_nan_ratio():
    df = pd.DataFrame({"a": [1, None, None, None]})
    res = check_mtf_nan_ratio(df, 0.5)
    assert res["passed"] == False
    assert res["total_nan_ratio"] == 0.75


def test_check_mtf_index_integrity():
    df = pd.DataFrame({"a": [1, 2]}, index=pd.date_range("2023-01-01", periods=2))
    res = check_mtf_index_integrity(df)
    assert res["passed"] == True

    df2 = pd.DataFrame({"a": [1, 2]}, index=[1, 1])
    res2 = check_mtf_index_integrity(df2)
    assert res2["passed"] == False
