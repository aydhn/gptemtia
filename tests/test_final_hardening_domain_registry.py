# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Domain Registry."""

from advanced_final_hardening.final_hardening_domain_registry import (
    build_final_hardening_domain_registry,
)


def test_build_domain_registry():
    df, summary = build_final_hardening_domain_registry()
    assert not df.empty
    assert summary["domain_count"] >= 12
    assert summary["all_domains_ready"] is True
    assert (df["non_signal"] == True).all()
    assert (df["dry_run"] == True).all()
