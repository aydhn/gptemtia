import pandas as pd
from portfolio_research.portfolio_config import get_default_portfolio_research_profile
from portfolio_research.basket_definitions import (
    build_equal_weight_basket,
    build_research_score_weighted_basket,
    build_risk_adjusted_basket,
    build_paper_performance_weighted_basket,
    enforce_weight_limits
)

def test_basket_definitions():
    profile = get_default_portfolio_research_profile()
    symbols = ["A", "B", "C"]

    ew = build_equal_weight_basket(symbols, "1d", profile)
    assert ew.weights["A"] == 1/3

    ranking = pd.DataFrame({
        "symbol": ["A", "B", "C"],
        "research_score": [0.5, 0.3, 0.2],
        "risk_score": [0.1, 0.5, 0.8],
        "paper_score": [10, -5, 5]
    })

    rsw = build_research_score_weighted_basket(ranking, "1d", profile)
    assert rsw.weights["A"] > rsw.weights["C"]

    ra = build_risk_adjusted_basket(ranking, "1d", profile)
    assert ra.weights["A"] > ra.weights["C"]

    ppw = build_paper_performance_weighted_basket(ranking, "1d", profile)
    assert "B" not in ppw.weights # negative score

    w, _ = enforce_weight_limits({"A": 0.9, "B": 0.1}, profile)
    assert w["A"] < 0.9
