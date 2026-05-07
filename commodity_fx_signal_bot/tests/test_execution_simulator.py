import pytest
import pandas as pd
from backtesting.execution_simulator import ExecutionSimulator
from backtesting.backtest_config import get_default_backtest_profile


def test_simulate_entry():
    prof = get_default_backtest_profile()
    sim = ExecutionSimulator(prof)

    df = pd.DataFrame(
        {"open": [10, 11, 12], "close": [10.5, 11.5, 12.5]},
        index=pd.DatetimeIndex(["2020-01-01", "2020-01-02", "2020-01-03"]),
    )

    res = sim.simulate_entry(df, pd.Timestamp("2020-01-01"), "long")
    assert res["status"] == "success"
    assert res["entry_timestamp"] == pd.Timestamp("2020-01-02")
    assert res["entry_price"] == 11  # Next bar open
