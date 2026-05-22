import pandas as pd
import numpy as np
from synthetic_indices.composite_index_builder import CompositeIndexBuilder
from synthetic_indices.index_models import SyntheticIndexDefinition

# Simple mock for DataLake
class MockDataLake:
    def load_ohlcv(self, symbol: str, timeframe: str):
        dates = pd.date_range("2023-01-01", periods=5)
        # Create a simple upward trend for testing
        close = pd.Series([100.0, 101.0, 102.0, 103.0, 104.0], index=dates, name="close")
        return pd.DataFrame({"close": close})

def test_composite_index_builder():
    lake = MockDataLake()
    builder = CompositeIndexBuilder(lake)

    class MockSpec:
         def __init__(self, sym):
             self.symbol = sym

    specs = [MockSpec("A"), MockSpec("B")]

    close_df, summary = builder.load_close_prices(specs, "1d")
    assert not close_df.empty
    assert "A" in close_df.columns

    returns_df, ret_summary = builder.build_returns_matrix(close_df, method="log")
    assert not returns_df.empty
    assert len(returns_df) == 4 # One less due to shift

    dfn = SyntheticIndexDefinition(
        index_id="test_idx",
        index_name="Test",
        index_type="custom",
        timeframe="1d",
        symbols=["A", "B"],
        weights={"A": 0.5, "B": 0.5},
        weighting_scheme="equal_weight",
        base_value=100.0,
        created_at_utc="now",
        methodology="Test",
        warnings=[]
    )

    series, series_summary = builder.build_index_series(dfn, returns_df)
    assert series.observation_count == 4
    assert series.level_series.iloc[0] > 0

    map_series, map_summary = builder.build_index_series_for_definitions([dfn], returns_df)
    assert "test_idx" in map_series
