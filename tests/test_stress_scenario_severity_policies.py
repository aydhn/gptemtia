# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Severity Policies."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_scenario_severity_policies import (
    build_stress_scenario_severity_policy_registry,
)


def test_severity_policies():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_scenario_severity_policy_registry(prof)
    assert not df.empty
    assert summary["total_severity_levels"] == len(df)
    assert summary["non_signal"] is True
