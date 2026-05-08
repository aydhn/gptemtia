import pandas as pd
import numpy as np
import pytest
from ml.target_engineering import calculate_forward_return, calculate_direction_class, calculate_future_volatility, calculate_future_max_drawdown, build_price_based_target_frame
from ml.dataset_config import get_default_ml_dataset_profile

def test_calculate_forward_return():
    close = pd.Series([100, 105, 110, 100, 90])
    ret = calculate_forward_return(close, 1)
    assert ret.iloc[0] == 0.05
    assert ret.iloc[1] == pytest.approx((110-105)/105)
    assert pd.isna(ret.iloc[-1])

def test_calculate_direction_class():
    ret = pd.Series([0.05, -0.05, 0.001, np.nan])
    dc = calculate_direction_class(ret, 0.002)
    assert dc.iloc[0] == "up"
    assert dc.iloc[1] == "down"
    assert dc.iloc[2] == "flat"
    assert dc.iloc[3] == "unknown"

def test_calculate_future_volatility():
    close = pd.Series([100, 105, 110, 100, 90])
    vol = calculate_future_volatility(close, 2)
    assert len(vol) == 5
    assert pd.isna(vol.iloc[-1])

def test_calculate_future_max_drawdown():
    close = pd.Series([100, 110, 90, 80, 100])
    dd = calculate_future_max_drawdown(close, 2)
    assert dd.iloc[0] == -0.10 # from 100 to 90
    assert dd.iloc[1] == pytest.approx((80-110)/110) # from 110 to 80

def test_build_price_based_target_frame():
    df = pd.DataFrame({"close": [100, 105, 110, 100, 90]}, index=pd.date_range("2020-01-01", periods=5))
    profile = get_default_ml_dataset_profile()
    targets, summary = build_price_based_target_frame(df, profile)

    assert "target_forward_return_1" in targets.columns
    assert "target_direction_class_1" in targets.columns
    assert len(targets) == 5
    assert not any(c.startswith("target_") for c in df.columns) # Target should not be in original
