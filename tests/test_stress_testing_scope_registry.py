# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Scope Registry."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_scope_registry import (
    build_stress_testing_scope_registry,
)


def test_scope_registry():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_scope_registry(prof)
    assert not df.empty
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
