import pytest
import pandas as pd
from portfolio_regime.regime_config import PortfolioRegimeProfile
from portfolio_regime.regime_report_builder import (
    build_regime_portfolio_markdown_report,
    build_macro_scenario_markdown_report,
    build_stress_test_markdown_report,
    build_drawdown_cluster_markdown_report,
    build_risk_regime_exposure_markdown_report
)

def test_report_builders():
    profile = PortfolioRegimeProfile(name="test", description="")
    df = pd.DataFrame({"A": [1]})

    rep1 = build_regime_portfolio_markdown_report({}, {"symbol_returns": df}, profile)
    assert "offline" in rep1.lower()

    rep2 = build_macro_scenario_markdown_report({}, df, profile)
    assert "offline" in rep2.lower()

    rep3 = build_stress_test_markdown_report({}, {"scenario_stress": df}, profile)
    assert "offline" in rep3.lower()

    rep4 = build_drawdown_cluster_markdown_report({}, df, profile)
    assert "offline" in rep4.lower()

    rep5 = build_risk_regime_exposure_markdown_report({}, df, profile)
    assert "offline" in rep5.lower()
