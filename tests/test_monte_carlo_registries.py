# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Profile, Domain, and Scope Registries."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_profile_registry import build_monte_carlo_profile_registry
from advanced_monte_carlo_robustness.monte_carlo_domain_registry import build_monte_carlo_domain_registry
from advanced_monte_carlo_robustness.monte_carlo_scope_registry import build_monte_carlo_scope_registry


def test_build_monte_carlo_profile_registry():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_profile_registry(profile)
    assert not df.empty
    assert summary["total_profiles"] >= 3
    assert summary["all_local_only"] is True
    assert summary["all_zero_execution"] is True
    assert "profile_name" in df.columns
    assert "non_signal" in df.columns


def test_build_monte_carlo_domain_registry():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_domain_registry(profile)
    assert not df.empty
    assert summary["total_domains"] >= 8
    assert "domain_name" in df.columns


def test_build_monte_carlo_scope_registry():
    profile = get_default_monte_carlo_profile()
    df, summary = build_monte_carlo_scope_registry(profile)
    assert not df.empty
    assert summary["total_scope_items"] >= 5
    assert summary["all_prohibitions_enforced"] is True
    assert "scope_key" in df.columns

