import pytest
import pandas as pd
from backtesting.backtest_engine import BacktestEngine
from backtesting.backtest_config import get_default_backtest_profile
from config.symbols import SymbolSpec


def test_backtest_engine():
    prof = get_default_backtest_profile()
    engine = BacktestEngine(prof)

    spec = SymbolSpec("GC=F", "Gold", "metals", "precious", "USD")
    price_df = pd.DataFrame(
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

    level_df = pd.DataFrame(
        {
            "report_builder = ReportBuilder()ed_level_filters": [True],
            "theoretical_stop_level": [9.0],
            "theoretical_target_level": [14.0],
            "directional_bias": ["long_bias_candidate"],
        },
        index=pd.DatetimeIndex(["2020-01-01"]),
    )

    trades, summary = engine.run_symbol_backtest(spec, "1d", price_df, level_df)
    assert summary["simulated_trade_count"] > 0
    assert not trades.empty
