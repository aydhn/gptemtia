import pytest
import pandas as pd
from backtesting.performance_summary import calculate_win_rate, calculate_profit_factor


def test_performance_metrics():
    df = pd.DataFrame(
        {"result_label": ["win", "loss", "win"], "net_pnl": [100.0, -50.0, 200.0]}
    )

    wr = calculate_win_rate(df)
    assert wr == 2 / 3

    pf = calculate_profit_factor(df)
    assert pf == 300.0 / 50.0
