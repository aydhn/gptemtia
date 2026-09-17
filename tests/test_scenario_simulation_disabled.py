# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Scenario Simulation Disabled Report."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.scenario_simulation_disabled import (
    build_scenario_simulation_disabled_report,
    validate_no_scenario_simulation_request,
)


def test_scenario_simulation_disabled():
    prof = get_default_stress_testing_profile()
    df, summary = build_scenario_simulation_disabled_report(prof)
    assert not df.empty
    assert summary["is_blocked"] is True
    assert summary["enforced"] is True
    assert summary["non_signal"] is True

    res = validate_no_scenario_simulation_request("simulate_scenario")
    assert res["is_safe"] is False
