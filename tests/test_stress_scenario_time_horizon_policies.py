# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Time Horizon Policies."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_time_horizon_policies import (
    build_stress_scenario_time_horizon_policy_registry,
)


def test_time_horizon_policies():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_scenario_time_horizon_policy_registry(prof)
    assert not df.empty
    assert summary["total_time_horizons"] == len(df)
    assert summary["non_signal"] is True
