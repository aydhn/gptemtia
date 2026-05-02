import pandas as pd
import numpy as np
import pytest
from macro.fx_macro_features import (
    calculate_fx_returns,
    calculate_fx_trend_features,
    calculate_fx_volatility_features,
    build_fx_macro_feature_frame,
)


def test_calculate_fx_returns():
    s = pd.Series(
        range(100, 400), index=pd.date_range("2020-01-01", periods=300, freq="D")
    )
    df = calculate_fx_returns(s, windows=(21, 63))
    assert "return_21d" in df.columns
    assert "return_63d" in df.columns


def test_calculate_fx_trend_features():
    s = pd.Series(
        range(100, 400), index=pd.date_range("2020-01-01", periods=300, freq="D")
    )
    df = calculate_fx_trend_features(s)
    assert "sma_50" in df.columns
    assert "sma_200" in df.columns
    assert "above_sma_200" in df.columns


def test_calculate_fx_volatility_features():
    s = pd.Series(
        np.random.normal(10, 1, 300),
        index=pd.date_range("2020-01-01", periods=300, freq="D"),
    )
    df = calculate_fx_volatility_features(s)
    assert "vol_21d" in df.columns


def test_build_fx_macro_feature_frame():
    df = pd.DataFrame(
        {"value": range(100, 400)},
        index=pd.date_range("2020-01-01", periods=300, freq="D"),
    )
    res, summ = build_fx_macro_feature_frame(df, "usdtry")
    assert "usdtry_return_21d" in res.columns
    assert "usdtry_above_sma_200" in res.columns
