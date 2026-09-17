# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Portfolio Optimization Profiles, Domains and Scopes."""

from advanced_portfolio_optimization.portfolio_optimization_config import (
    get_default_portfolio_optimization_profile,
)
from advanced_portfolio_optimization.portfolio_optimization_profile_registry import (
    build_portfolio_optimization_profile_registry,
    summarize_portfolio_optimization_profiles,
)
from advanced_portfolio_optimization.portfolio_optimization_domain_registry import (
    build_portfolio_optimization_domain_registry,
)
from advanced_portfolio_optimization.portfolio_optimization_scope_registry import (
    build_portfolio_optimization_scope_registry,
)


def test_profile_registry_builder():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_profile_registry(profile)
    assert not df.empty
    assert len(df) >= 3
    assert summary["profile_count"] >= 3
    assert (df["allow_live_trading"] == False).all()
    assert (df["allow_portfolio_optimization"] == False).all()


def test_domain_registry_builder():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_domain_registry(profile)
    assert not df.empty
    assert len(df) >= 10
    assert summary["domain_count"] >= 10
    assert (df["non_production"] == True).all()


def test_scope_registry_builder():
    profile = get_default_portfolio_optimization_profile()
    df, summary = build_portfolio_optimization_scope_registry(profile)
    assert not df.empty
    assert len(df) >= 4
    assert summary["scope_count"] >= 4
