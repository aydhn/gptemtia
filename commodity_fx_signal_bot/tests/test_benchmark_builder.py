import pandas as pd
import numpy as np
import pytest
from macro.benchmark_builder import (
    build_price_return_index,
    build_equal_weight_basket,
    convert_usd_asset_to_try,
    build_inflation_index,
    calculate_real_return_index,
    build_benchmark_frame,
)


def test_build_price_return_index():
    s = pd.Series([10, 11, 12])
    res = build_price_return_index(s, 100.0)
    assert res.iloc[0] == 100.0
    assert pytest.approx(res.iloc[1]) == 110.0


def test_build_equal_weight_basket():
    s1 = pd.Series([100, 110, 121])  # 10%
    s2 = pd.Series([100, 100, 100])  # 0%
    res = build_equal_weight_basket({"s1": s1, "s2": s2}, 100.0)
    assert res.iloc[0] == 100.0
    assert pytest.approx(res.iloc[1]) == 105.0  # (10% + 0%) / 2 = 5% => 105


def test_convert_usd_asset_to_try():
    usd = pd.Series([1000, 1000])
    try_rate = pd.Series([10, 15])
    res = convert_usd_asset_to_try(usd, try_rate)
    assert res.iloc[0] == 10000
    assert res.iloc[1] == 15000


def test_build_inflation_index():
    s = pd.Series([1.0, 1.1])
    res = build_inflation_index(s)
    assert res.iloc[0] == 100.0
    assert pytest.approx(res.iloc[1]) == 110.0


def test_calculate_real_return_index():
    nom = pd.Series([100, 110])
    inf = pd.Series([100, 110])
    res = calculate_real_return_index(nom, inf)
    assert res.iloc[0] == 100.0
    assert pytest.approx(res.iloc[1]) == 100.0


def test_build_benchmark_frame():
    d = pd.date_range("2020-01-01", periods=10, freq="D")
    inputs = {
        "USDTRY": pd.Series(range(10, 20), index=d),
        "GOLD_USD": pd.Series(range(100, 110), index=d),
        "TR_CPI": pd.Series(range(100, 110), index=d),
    }
    df, summ = build_benchmark_frame(inputs)
    assert "bench_usdtry_index" in df.columns
    assert "bench_gold_try_index" in df.columns
    assert "real_gold_try_vs_tr_cpi" in df.columns
