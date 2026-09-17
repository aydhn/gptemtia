# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Profile Registry."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_profile_registry import (
    build_stress_testing_profile_registry,
)


def test_profile_registry():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_profile_registry(prof)
    assert not df.empty
    assert summary["total_profiles"] == len(df)
    assert summary["all_local_only"] is True
    assert summary["all_non_signal"] is True
