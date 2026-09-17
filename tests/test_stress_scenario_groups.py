# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Scenario Groups."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_groups import (
    build_stress_scenario_group_registry,
)


def test_stress_scenario_groups():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_scenario_group_registry(prof)
    assert not df.empty
    assert summary["total_scenario_groups"] == len(df)
    assert summary["non_signal"] is True
