import pandas as pd
from portfolio_research.portfolio_config import get_default_portfolio_research_profile
from portfolio_research.portfolio_quality import (
    check_returns_matrix_quality,
    check_correlation_matrix_quality,
    check_basket_definitions_quality,
    check_for_forbidden_trade_terms_in_portfolio_research,
    build_portfolio_quality_report
)

def test_quality_checks():
    profile = get_default_portfolio_research_profile()

    ret = pd.DataFrame()
    q = check_returns_matrix_quality(ret, profile)
    assert not q["valid"]

    corr = pd.DataFrame({"A": [1.0, None], "B": [None, 1.0]})
    q = check_correlation_matrix_quality(corr)
    assert not q["valid"]

    q = check_basket_definitions_quality([], profile)
    assert not q["valid"]

    term_q = check_for_forbidden_trade_terms_in_portfolio_research(text="THIS IS A LIVE ORDER")
    assert not term_q["valid"]

    full_q = build_portfolio_quality_report({"dummy": 1})
    assert "passed" in full_q
