import pytest
import pandas as pd
from portfolio_regime.regime_data_adapter import PortfolioRegimeDataAdapter
from data.storage.data_lake import DataLake
from config.paths import LAKE_DIR

def test_data_adapter_loads():
    lake = DataLake(LAKE_DIR)
    adapter = PortfolioRegimeDataAdapter(lake)

    returns_df, summary = adapter.load_universe_returns("1d")
    assert isinstance(returns_df, pd.DataFrame)
    assert "status" in summary
    assert "warnings" in summary

    basket_df, summary = adapter.load_virtual_basket_definitions("1d")
    assert isinstance(basket_df, pd.DataFrame)

    macro, summary = adapter.load_macro_context("1d")
    assert isinstance(macro, dict)
