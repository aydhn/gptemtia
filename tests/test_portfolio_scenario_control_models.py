# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_models import (
    ScenarioTestingContract, DrawdownControlContract, ControlActionPlaceholder
)

def test_models():
    sc = ScenarioTestingContract(
        contract_id="SC-1", scenario_type="HISTORICAL", name="GFC", description="GFC Shock",
        shock_scope="GLOBAL", severity_level="EXTREME", target_asset_classes=["COMMODITIES"],
        offline_simulation_hook="hook"
    )
    d = sc.to_dict()
    assert d["contract_id"] == "SC-1"
    assert d["execution_allowed"] is False
