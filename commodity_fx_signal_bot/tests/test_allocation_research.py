from portfolio_research.portfolio_config import get_default_portfolio_research_profile
from portfolio_research.allocation_research import (
    build_virtual_allocation_table,
    calculate_allocation_quality
)
from portfolio_research.basket_definitions import build_equal_weight_basket

def test_allocation_research():
    profile = get_default_portfolio_research_profile()
    b = build_equal_weight_basket(["A", "B"], "1d", profile)

    df = build_virtual_allocation_table([b])
    assert not df.empty

    q = calculate_allocation_quality(b.weights, None, None, profile)
    assert q["quality_score"] > 0
