from portfolio_research.concentration_risk import (
    calculate_hhi_concentration,
    calculate_top_n_weight,
    identify_concentration_warnings
)
from portfolio_research.portfolio_config import get_default_portfolio_research_profile

def test_concentration_risk():
    w = {"A": 0.8, "B": 0.2}

    hhi = calculate_hhi_concentration(w)
    assert abs(hhi - 0.68) < 0.0001

    top = calculate_top_n_weight(w, 1)
    assert top == 0.8

    profile = get_default_portfolio_research_profile()
    warns = identify_concentration_warnings(w, None, profile)
    assert len(warns) > 0
