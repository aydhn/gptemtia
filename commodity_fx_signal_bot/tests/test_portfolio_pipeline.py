import pytest
from config.symbols import SymbolSpec
from config.settings import settings
from portfolio_research.portfolio_pipeline import PortfolioResearchPipeline
from portfolio_research.portfolio_config import get_default_portfolio_research_profile

class MockDataLake:
    def __init__(self):
        self.paths = type('obj', (object,), {'processed_ohlcv': type('obj', (object,), {'exists': lambda: False})})

    def load_processed_ohlcv(self, symbol, timeframe):
        import pandas as pd
        import numpy as np
        dates = pd.date_range("2023-01-01", periods=150)
        return pd.DataFrame({"close": np.random.rand(150) + 100}, index=dates)

def test_portfolio_pipeline():
    dl = MockDataLake()
    profile = get_default_portfolio_research_profile()
    pipeline = PortfolioResearchPipeline(dl, settings, profile)

    specs = [
        SymbolSpec(symbol="A", asset_class="C", base_currency="B", quote_currency="Q", currency="USD", name="test", sub_class="test"),
        SymbolSpec(symbol="B", asset_class="C", base_currency="B", quote_currency="Q", currency="USD", name="test", sub_class="test"),
        SymbolSpec(symbol="C", asset_class="C", base_currency="B", quote_currency="Q", currency="USD", name="test", sub_class="test")
    ]

    report, info = pipeline.build_portfolio_research(specs, "1d", save=False)

    assert report.report_id != ""
    assert "quality" in info
