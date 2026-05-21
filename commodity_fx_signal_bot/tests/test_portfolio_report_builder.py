import pandas as pd
from portfolio_research.portfolio_config import get_default_portfolio_research_profile
from portfolio_research.portfolio_report_builder import (
    build_portfolio_markdown_report,
    build_correlation_markdown_report,
    build_virtual_basket_markdown_report
)

def test_report_builder():
    profile = get_default_portfolio_research_profile()

    md = build_portfolio_markdown_report({"timeframe": "1d"}, {}, profile)
    assert "Portfolio Research Report" in md
    assert "YASAL UYARI" in md

    corr_md = build_correlation_markdown_report({}, pd.DataFrame(), pd.DataFrame(), profile)
    assert "Correlation Analysis Report" in corr_md

    vb_md = build_virtual_basket_markdown_report({}, pd.DataFrame(), pd.DataFrame(), profile)
    assert "Virtual Basket Report" in vb_md
