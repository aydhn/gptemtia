from portfolio_regime.regime_labels import (
    list_portfolio_regime_labels,
    list_macro_scenario_labels,
    list_stress_severity_labels,
    list_drawdown_cluster_labels,
    validate_portfolio_regime_label,
    validate_macro_scenario_label
)

def test_label_lists_not_empty():
    assert len(list_portfolio_regime_labels()) > 0
    assert len(list_macro_scenario_labels()) > 0
    assert len(list_stress_severity_labels()) > 0
    assert len(list_drawdown_cluster_labels()) > 0

def test_validate_labels():
    validate_portfolio_regime_label("risk_on_regime")
    validate_macro_scenario_label("usdtry_up_scenario")
