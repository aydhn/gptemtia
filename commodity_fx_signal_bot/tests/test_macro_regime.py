import pandas as pd

from macro.macro_regime import (
    classify_fx_pressure_regime,
    classify_inflation_regime,
    classify_macro_regime,
)


def test_classify_inflation_regime():
    df = pd.DataFrame(
        {
            "TR_CPI_yoy_rising": [1, 0],
            "TR_CPI_yoy_falling": [0, 1],
            "TR_CPI_yoy_falling": [0, 1],
        }
    )
    res = classify_inflation_regime(df)
    assert res["macro_tr_inflation_rising"].iloc[0] == 1
    assert res["macro_tr_inflation_falling"].iloc[1] == 1


def test_classify_fx_pressure_regime():
    df = pd.DataFrame({"usdtry_depreciation_pressure": [1, 0]})
    res = classify_fx_pressure_regime(df)
    assert res["macro_try_depreciation_pressure"].iloc[0] == 1


def test_classify_macro_regime():
    df = pd.DataFrame(
        {
            "TR_CPI_yoy_rising": [1, 0],
            "TR_CPI_yoy_falling": [0, 1],
            "TR_CPI_yoy": [0.25, 0.10],
            "usdtry_depreciation_pressure": [1, 0],
        }
    )
    res, summ = classify_macro_regime(df)
    assert res["macro_primary_label"].iloc[0] == "high_local_inflation_fx_pressure"
    assert res["macro_confidence"].iloc[0] == 0.9
