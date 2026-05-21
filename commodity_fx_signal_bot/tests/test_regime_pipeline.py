import pytest
from portfolio_regime.regime_pipeline import PortfolioRegimePipeline
from portfolio_regime.regime_config import PortfolioRegimeProfile
from data.storage.data_lake import DataLake
from config.settings import settings
from config.paths import LAKE_DIR

def test_regime_pipeline():
    lake = DataLake(LAKE_DIR)
    profile = PortfolioRegimeProfile(name="test", description="")
    pipeline = PortfolioRegimePipeline(lake, settings, profile)

    # We pass empty specs array for testing
    summary, quality = pipeline.build_regime_portfolio_report([], save=False)
    assert summary is not None
    assert "warnings" in quality

    df, summary = pipeline.build_macro_scenario_sensitivity_report([], save=False)
    assert summary is not None

    tables, summary = pipeline.build_basket_stress_test_report([], save=False)
    assert summary is not None
