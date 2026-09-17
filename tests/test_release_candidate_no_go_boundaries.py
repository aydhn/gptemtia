# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate No-Go Boundaries."""

from advanced_final_hardening.release_candidate_no_go_boundaries import (
    build_release_candidate_no_go_boundary_registry,
)


def test_build_release_candidate_no_go_boundaries():
    df, summary = build_release_candidate_no_go_boundary_registry()
    assert not df.empty
    assert summary["no_go_boundary_count"] >= 1
    assert summary["all_enforced"] is True
    assert (df["enforced"] == True).all()
