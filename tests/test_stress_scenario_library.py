# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Scenario Library."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_library import (
    build_stress_scenario_library_registry,
)


def test_stress_scenario_library():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_scenario_library_registry(prof)
    assert not df.empty
    assert summary["total_library_scenarios"] == len(df)
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
