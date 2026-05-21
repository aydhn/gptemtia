from portfolio_regime.regime_models import (
    RegimeClassificationResult,
    MacroScenarioDefinition,
    build_scenario_id,
    build_drawdown_cluster_id,
    regime_classification_result_to_dict
)

def test_build_ids():
    assert build_scenario_id("test", 0.05) == "test_0.0500"
    assert build_drawdown_cluster_id("basket", "t1", "t2") == "basket_t1_t2"

def test_to_dict():
    res = RegimeClassificationResult("t", "r", "v", "t", "c", "d", 0.5, 0.5, [])
    d = regime_classification_result_to_dict(res)
    assert d['timestamp'] == "t"
    assert d['regime_label'] == "r"
