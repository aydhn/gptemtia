# -*- coding: utf-8 -*-
from advanced_portfolio_scenario_control.portfolio_scenario_control_labels import (
    ContractStatus, ScenarioType, DrawdownTier, ControlActionType
)

def test_labels():
    assert ContractStatus.CONTRACT_ONLY == "CONTRACT_ONLY"
    assert ScenarioType.HISTORICAL_CRISIS == "HISTORICAL_CRISIS"
    assert DrawdownTier.NORMAL == "NORMAL"
    assert ControlActionType.EXPOSURE_REDUCTION == "EXPOSURE_REDUCTION"
