# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Test Checkpoints."""

from advanced_final_hardening.release_candidate_test_checkpoints import (
    build_release_candidate_test_checkpoint_registry,
)


def test_build_release_candidate_test_checkpoints():
    df, summary = build_release_candidate_test_checkpoint_registry()
    assert not df.empty
    assert summary["checkpoint_count"] >= 1
    assert summary["all_passed"] is True
    assert (df["status"] == "release_candidate_contract_ready").all()
