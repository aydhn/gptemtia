import pytest
import pandas as pd
from backtesting.lifecycle_engine import TradeLifecycleEngine
from backtesting.backtest_config import get_default_backtest_profile


def test_simulate_lifecycle_target_touch():
    prof = get_default_backtest_profile()
    engine = TradeLifecycleEngine(prof)

    df = pd.DataFrame(
        {
            "open": [10, 11, 12, 13],
            "high": [11, 12, 15, 14],
            "low": [9, 10, 11, 12],
            "close": [10.5, 11.5, 14.5, 13.5],
        },
        index=pd.DatetimeIndex(
            ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04"]
        ),
    )

    cand = pd.Series(
        {
            "directional_bias": "long_bias_candidate",
            "theoretical_stop_level": 9.0,
            "theoretical_target_level": 14.0,
            "theoretical_units": 1,
            "theoretical_notional": 10,
        },
        name=pd.Timestamp("2020-01-01"),
    )

    trade, status = engine.simulate_candidate_lifecycle("GC=F", "1d", cand, df)
    assert status["status"] == "success"
    assert trade.exit_reason == "target_touch_simulated"
    assert trade.result_label == "win"
