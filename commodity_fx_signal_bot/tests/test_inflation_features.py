import pytest
import pandas as pd
import numpy as np
from macro.inflation_features import (
    calculate_monthly_change,
    calculate_yoy_change,
    calculate_inflation_momentum,
    build_inflation_feature_frame,
)


def test_monthly_change():
    s = pd.Series([100, 101, 103, 102])
    res = calculate_monthly_change(s)
    assert np.isnan(res.iloc[0])
    assert pytest.approx(res.iloc[1]) == 0.01


def test_yoy_change():
    s = pd.Series(range(100, 115))
    res = calculate_yoy_change(s, periods=12)
    assert np.isnan(res.iloc[0])
    assert pytest.approx(res.iloc[12]) == 0.12


def test_inflation_momentum():
    s = pd.Series([0.1, 0.2, 0.3, 0.2, 0.1])
    res = calculate_inflation_momentum(s, window=2)
    assert np.isnan(res.iloc[0])
    assert pytest.approx(res.iloc[2]) == 0.2


def test_build_inflation_feature_frame():
    df = pd.DataFrame(
        {"value": range(100, 120)},
        index=pd.date_range("2020-01-01", periods=20, freq="ME"),
    )
    res, summ = build_inflation_feature_frame(df, "TR_CPI")
    assert "TR_CPI_level" in res.columns
    assert "TR_CPI_mom" in res.columns
    assert "TR_CPI_yoy" in res.columns
    assert "TR_CPI_yoy_rising" in res.columns
