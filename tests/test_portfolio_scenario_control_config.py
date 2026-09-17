# -*- coding: utf-8 -*-
import pytest
from advanced_portfolio_scenario_control.portfolio_scenario_control_config import (
    get_default_portfolio_scenario_control_profile,
    get_portfolio_scenario_control_profile,
    list_portfolio_scenario_control_profiles,
    PortfolioScenarioControlProfile,
)

def test_config_profiles():
    prof = get_default_portfolio_scenario_control_profile()
    assert prof.profile_name == "balanced_local_portfolio_scenario_control_contracts"
    assert prof.current_phase == 156
    assert prof.target_final_phase == 160
    assert prof.next_phase == 157
    assert prof.allow_live_trading is False
    assert prof.allow_scenario_execution is False
    assert prof.validate() is True

    names = list_portfolio_scenario_control_profiles()
    assert len(names) >= 4
    for n in names:
        p = get_portfolio_scenario_control_profile(n)
        assert p.validate() is True

def test_config_validation_failure():
    with pytest.raises(ValueError):
        p = PortfolioScenarioControlProfile(
            profile_name="bad", description="bad", allow_live_trading=True
        )
        p.validate()
