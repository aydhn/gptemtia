# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Correlation Breakdown Scenario Placeholders."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.correlation_breakdown_scenario_placeholders import (
    build_correlation_breakdown_scenario_placeholder_registry,
)


def test_correlation_breakdown_placeholders():
    prof = get_default_stress_testing_profile()
    df, summary = build_correlation_breakdown_scenario_placeholder_registry(prof)
    assert not df.empty
    assert summary["all_execution_blocked"] is True
    assert summary["non_signal"] is True
