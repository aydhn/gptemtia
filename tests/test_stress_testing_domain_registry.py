# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Domain Registry."""

from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_domain_registry import (
    build_stress_testing_domain_registry,
)


def test_domain_registry():
    prof = get_default_stress_testing_profile()
    df, summary = build_stress_testing_domain_registry(prof)
    assert not df.empty
    assert summary["total_domains"] >= 30
    assert summary["all_non_signal"] is True
