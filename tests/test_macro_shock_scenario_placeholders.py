# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Macro Shock Scenario Placeholders."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.macro_shock_scenario_placeholders import (
    build_macro_shock_scenario_placeholder_registry,
)


def test_macro_shock_placeholders():
    prof = get_default_stress_testing_profile()
    df, summary = build_macro_shock_scenario_placeholder_registry(prof)
    assert not df.empty
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
