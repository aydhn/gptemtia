# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Historical Stress Scenario Contracts."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.historical_stress_scenario_contracts import (
    build_historical_stress_scenario_contract_registry,
)


def test_historical_contracts():
    prof = get_default_stress_testing_profile()
    df, summary = build_historical_stress_scenario_contract_registry(prof)
    assert not df.empty
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
