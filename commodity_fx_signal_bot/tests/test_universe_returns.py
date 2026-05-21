import pandas as pd
import numpy as np
from config.symbols import SymbolSpec
from portfolio_research.universe_returns import UniverseReturnsBuilder

class MockDataLake:
    def load_processed_ohlcv(self, symbol, timeframe):
        dates = pd.date_range("2023-01-01", periods=150)
        return pd.DataFrame({"close": np.random.rand(150) + 100}, index=dates)

def test_universe_returns():
    dl = MockDataLake()
    builder = UniverseReturnsBuilder(dl)
    specs = [
        SymbolSpec(symbol="A", asset_class="C", base_currency="B", quote_currency="Q", currency="USD", name="test", sub_class="test"),
        SymbolSpec(symbol="B", asset_class="C", base_currency="B", quote_currency="Q", currency="USD", name="test", sub_class="test")
    ]

    close_df, info = builder.load_close_prices(specs, "1d")
    assert not close_df.empty

    ret_df, ret_info = builder.build_returns_matrix(close_df, method="log")
    assert not ret_df.empty

    align_df, align_info = builder.align_universe_returns(ret_df, min_observations=120)
    assert "A" in align_df.columns
