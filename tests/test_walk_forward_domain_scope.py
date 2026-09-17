# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Walk-Forward Domain and Scope Registries."""

from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_domain_registry import (
    build_walk_forward_domain_registry,
    summarize_walk_forward_domains,
)
from advanced_walk_forward_validation.walk_forward_scope_registry import (
    build_walk_forward_scope_registry,
    summarize_walk_forward_scope,
)


def test_domain_registry():
    prof = get_default_walk_forward_profile()
    df, summary = build_walk_forward_domain_registry(prof)
    assert not df.empty
    assert len(df) >= 30
    assert "domain_name" in df.columns
    assert summary["total_domains"] >= 30
    assert summary["non_signal"] is True

    s2 = summarize_walk_forward_domains(df)
    assert s2["total_domains"] == len(df)


def test_scope_registry():
    prof = get_default_walk_forward_profile()
    df, summary = build_walk_forward_scope_registry(prof)
    assert not df.empty
    assert len(df) >= 10
    assert "scope_name" in df.columns
    assert summary["total_scope_items"] >= 10
    assert summary["non_signal"] is True

    s2 = summarize_walk_forward_scope(df)
    assert s2["total_scope_items"] == len(df)
