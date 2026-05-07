import pytest
import pandas as pd
from backtesting.drawdown_metrics import (
    calculate_drawdown_series,
    calculate_max_drawdown,
    calculate_drawdown_durations,
    calculate_top_drawdowns,
    calculate_underwater_periods,
    build_drawdown_analysis,
)


def test_calculate_drawdown_series():
    eq = pd.DataFrame({"equity": [100, 110, 90, 105, 120]})
    dd = calculate_drawdown_series(eq)
    assert "drawdown" in dd.columns
    assert "drawdown_pct" in dd.columns
    assert "is_underwater" in dd.columns
    assert dd["drawdown"].iloc[2] == -20.0
    assert dd["drawdown_pct"].iloc[2] == pytest.approx(-0.1818, 0.01)


def test_calculate_max_drawdown():
    eq = pd.DataFrame({"equity": [100, 110, 90, 105, 120]})
    res = calculate_max_drawdown(eq)
    assert res["max_drawdown"] == 20.0


def test_calculate_drawdown_durations():
    eq = pd.DataFrame({"equity": [100, 110, 90, 105, 120]})
    dd = calculate_drawdown_series(eq)
    dur = calculate_drawdown_durations(dd)
    assert not dur.empty
    assert "max_drawdown" in dur.columns
    assert "duration_bars" in dur.columns


def test_build_drawdown_analysis():
    eq = pd.DataFrame({"equity": [100, 110, 90, 105, 120]})
    dd_df, summary = build_drawdown_analysis(eq)
    assert not dd_df.empty
    assert "max_drawdown" in summary
    assert "longest_drawdown_bars" in summary
    assert "avg_recovery_bars" in summary
