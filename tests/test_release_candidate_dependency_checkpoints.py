# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Dependency Checkpoints."""

from advanced_final_hardening.release_candidate_dependency_checkpoints import (
    build_release_candidate_dependency_checkpoint_registry,
)


def test_build_release_candidate_dependency_checkpoints():
    df, summary = build_release_candidate_dependency_checkpoint_registry()
    assert not df.empty
    assert summary["checkpoint_count"] >= 1
    assert summary["all_resolved"] is True
    assert (df["status"] == "release_candidate_contract_ready").all()
