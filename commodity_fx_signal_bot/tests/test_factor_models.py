from factor_research.factor_models import build_factor_id, build_factor_neutral_basket_id

def test_models():
    assert build_factor_id("Test Factor", "trend") == "trend_test_factor"
    assert build_factor_neutral_basket_id("1d", ["AAPL", "MSFT"]) == "neutral_basket_1d_AAPL_MSFT"
