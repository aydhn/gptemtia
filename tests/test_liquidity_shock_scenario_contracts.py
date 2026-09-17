# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Liquidity Shock Scenario Contracts."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.liquidity_shock_scenario_contracts import (
    build_liquidity_shock_scenario_contract_registry,
)


def test_liquidity_shock_contracts():
    prof = get_default_stress_testing_profile()
    df, summary = build_liquidity_shock_scenario_contract_registry(prof)
    assert not df.empty
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
