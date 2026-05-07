import pytest
import pandas as pd
from backtesting.backtest_quality import (
    check_trade_timestamp_order,
    check_overlapping_positions,
    check_for_forbidden_live_terms_in_backtest,
)


def test_quality_checks():
    df = pd.DataFrame(
        {
            "symbol": ["GC", "GC"],
            "entry_timestamp": ["2020-01-01", "2020-01-02"],
            "exit_timestamp": ["2020-01-03", "2020-01-04"],
        }
    )

    assert check_trade_timestamp_order(df)["passed"]
    assert not check_overlapping_positions(df)["passed"]  # 02 is before 03

    df2 = pd.DataFrame({"status": ["simulated", "LIVE_ORDER"]})
    assert not check_for_forbidden_live_terms_in_backtest(df2)["passed"]
