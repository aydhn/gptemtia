# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Metric Placeholders."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_metric_placeholders import (
    build_stress_metric_placeholder_registry,
)


def test_stress_metric_placeholders():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_metric_placeholder_registry(prof)
    assert not df.empty
    assert summary["all_calculation_blocked"] is True
    assert summary["zero_performance_claims"] is True
    assert summary["non_signal"] is True
