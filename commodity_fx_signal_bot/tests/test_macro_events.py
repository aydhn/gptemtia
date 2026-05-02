import pandas as pd

from macro.macro_events import (
    build_macro_event_frame,
    detect_benchmark_outperformance_events,
    detect_fx_macro_events,
    detect_inflation_events,
)


def test_detect_inflation_events():
    df = pd.DataFrame(
        {
            "TR_CPI_yoy_rising": [1, 0],
            "TR_CPI_yoy_falling": [0, 1],
            "TR_CPI_yoy_falling": [0, 1],
        }
    )
    res = detect_inflation_events(df)
    assert "event_macro_tr_inflation_rising" in res.columns
    assert res["event_macro_tr_inflation_rising"].iloc[0] == 1


def test_detect_fx_macro_events():
    df = pd.DataFrame(
        {"usdtry_depreciation_pressure": [1, 0], "usdtry_return_252d": [0.30, 0.10]}
    )
    res = detect_fx_macro_events(df)
    assert "event_macro_usdtry_strong_12m" in res.columns
    assert res["event_macro_usdtry_strong_12m"].iloc[0] == 1


def test_build_macro_event_frame():
    df = pd.DataFrame(
        {
            "TR_CPI_yoy_rising": [1, 0],
            "TR_CPI_yoy_falling": [0, 1],
            "usdtry_depreciation_pressure": [1, 0],
        }
    )
    res, summ = build_macro_event_frame(df)
    assert "event_macro_tr_inflation_rising" in res.columns

    # Event columns must not be named buy/sell
    for col in res.columns:
        assert "buy" not in col.lower()
        assert "sell" not in col.lower()
