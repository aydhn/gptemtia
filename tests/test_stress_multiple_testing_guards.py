# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Multiple Testing Guards."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_multiple_testing_guards import (
    build_stress_multiple_testing_guard_registry,
)


def test_multiple_testing_guards():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_multiple_testing_guard_registry(prof)
    assert not df.empty
    assert summary["guard_active"] is True
    assert summary["non_signal"] is True
