import pytest
import pandas as pd
from backtesting.equity_curve import build_equity_curve


def test_build_equity_curve():
    df = pd.DataFrame(
        {"exit_timestamp": ["2020-01-02", "2020-01-03"], "net_pnl": [100.0, -50.0]}
    )
    eq = build_equity_curve(df, 1000.0)
    assert not eq.empty
    assert eq["equity"].iloc[0] == 1100.0
    assert eq["equity"].iloc[1] == 1050.0
