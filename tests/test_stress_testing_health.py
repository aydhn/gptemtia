# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Health Check."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_health import (
    check_stress_testing_health,
)


def test_health_check():
    prof = get_default_stress_testing_profile()
    df, summary = check_stress_testing_health(prof)
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["overall_status"] == "HEALTHY"
