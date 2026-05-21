from portfolio_research.portfolio_labels import (
    list_portfolio_report_type_labels,
    list_basket_type_labels,
    list_diversification_labels,
    list_exposure_labels,
    validate_portfolio_report_type,
    validate_basket_type,
    validate_diversification_label,
    validate_exposure_label
)

def test_label_lists_not_empty():
    assert len(list_portfolio_report_type_labels()) > 0
    assert len(list_basket_type_labels()) > 0
    assert len(list_diversification_labels()) > 0
    assert len(list_exposure_labels()) > 0

def test_validate_basket_type():
    validate_basket_type("equal_weight_basket")

def test_validate_diversification_label():
    validate_diversification_label("well_diversified")
