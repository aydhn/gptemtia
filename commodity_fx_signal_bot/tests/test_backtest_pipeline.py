import pytest
import pandas as pd
from backtesting.backtest_pipeline import BacktestPipeline
from config.settings import settings
from backtesting.backtest_config import get_default_backtest_profile
from config.symbols import SymbolSpec


class MockDataLake:
    def load_processed_ohlcv(self, symbol, timeframe):
        return pd.DataFrame(
            {"open": [1], "high": [2], "low": [0.5], "close": [1.5]},
            index=pd.DatetimeIndex(["2020-01-01"]),
        )

    def load_sizing_candidates(self, symbol, timeframe):
        return pd.DataFrame()

    def load_level_candidates(self, symbol, timeframe):
        return pd.DataFrame(
            {
                "report_builder = ReportBuilder()ed_level_filters": [True],
                "directional_bias": ["long"],
                "theoretical_stop_level": [0.5],
                "theoretical_target_level": [2.0],
            },
            index=pd.DatetimeIndex(["2020-01-01"]),
        )


def test_backtest_pipeline():
    prof = get_default_backtest_profile()
    pipeline = BacktestPipeline(MockDataLake(), settings, prof)

    spec = SymbolSpec("GC=F", "Gold", "metals", "precious", "USD")
    trades, summary = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert summary["profile"] == prof.name
