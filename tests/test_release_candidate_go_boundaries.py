# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Go Boundaries."""

from advanced_final_hardening.release_candidate_go_boundaries import (
    build_release_candidate_go_boundary_registry,
)


def test_build_release_candidate_go_boundaries():
    df, summary = build_release_candidate_go_boundary_registry()
    assert not df.empty
    assert summary["go_boundary_count"] >= 1
    assert summary["all_safe_go"] is True
    assert (df["boundary_type"] == "go").all()
