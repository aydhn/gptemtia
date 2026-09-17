# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Scenario Leakage Guards."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_leakage_guards import (
    build_stress_scenario_leakage_guard_registry,
    validate_stress_scenario_leakage_request,
)


def test_scenario_leakage_guards():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_scenario_leakage_guard_registry(prof)
    assert not df.empty
    assert summary["guard_active"] is True
    assert summary["non_signal"] is True

    res = validate_stress_scenario_leakage_request("clean request")
    assert res["is_safe"] is True
