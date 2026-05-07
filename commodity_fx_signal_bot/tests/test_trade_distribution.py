import pytest
import pandas as pd
from backtesting.trade_distribution import (
    calculate_trade_return_distribution,
    calculate_trade_pnl_distribution,
    calculate_holding_period_distribution,
    calculate_exit_reason_distribution,
    calculate_result_label_distribution,
    calculate_trade_streaks,
    build_trade_distribution_report,
)


def test_trade_distributions():
    trades = pd.DataFrame(
        {
            "return_pct": [0.1, -0.05, 0.02, 0.05],
            "net_pnl": [10.0, -5.0, 2.0, 5.0],
            "holding_bars": [5, 2, 3, 4],
            "exit_reason": ["take_profit", "stop_loss", "time_limit", "take_profit"],
            "result_label": ["win", "loss", "win", "win"],
        }
    )

    ret_dist = calculate_trade_return_distribution(trades)
    assert "mean_return" in ret_dist
    assert "best_trade" in ret_dist

    pnl_dist = calculate_trade_pnl_distribution(trades)
    assert "mean_pnl" in pnl_dist

    hold_dist = calculate_holding_period_distribution(trades)
    assert "avg_holding_bars" in hold_dist

    exit_dist = calculate_exit_reason_distribution(trades)
    assert not exit_dist.empty

    res_dist = calculate_result_label_distribution(trades)
    assert not res_dist.empty

    streaks = calculate_trade_streaks(trades)
    assert "max_win_streak" in streaks

    report = build_trade_distribution_report(trades)
    assert "mean_return" in report
    assert "exit_reason_distribution" in report
