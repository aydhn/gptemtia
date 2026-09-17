# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Blockers."""

from advanced_final_hardening.release_candidate_blockers import (
    build_release_candidate_blocker_registry,
)


def test_build_release_candidate_blockers():
    df, summary = build_release_candidate_blocker_registry()
    assert not df.empty
    assert summary["total_monitored_blockers"] >= 1
    assert summary["has_active_blockers"] is False
    assert (df["is_active"] == False).all()
