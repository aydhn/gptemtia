import pytest
import pandas as pd
from backtesting.data_adapter import BacktestDataAdapter


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
            {"passed_level_filters": [True]}, index=pd.DatetimeIndex(["2020-01-01"])
        )


def test_data_adapter_success():
    adapter = BacktestDataAdapter(MockDataLake())
    from config.symbols import SymbolSpec

    spec = SymbolSpec("GC=F", "Gold", "metals", "precious", "USD")
    price_df, p_status = adapter.load_price_frame(spec, "1d")
    assert not price_df.empty
    assert p_status["status"] == "success"

    level_df, l_status = adapter.load_level_candidates(spec, "1d")
    assert not level_df.empty
