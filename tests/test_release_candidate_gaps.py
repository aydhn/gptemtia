# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Gaps."""

from advanced_final_hardening.release_candidate_gaps import (
    build_release_candidate_gap_registry,
)


def test_build_release_candidate_gaps():
    df, summary = build_release_candidate_gap_registry()
    assert not df.empty
    assert summary["gap_count"] >= 1
    assert summary["open_gap_count"] == 0
    assert (df["is_open"] == False).all()
