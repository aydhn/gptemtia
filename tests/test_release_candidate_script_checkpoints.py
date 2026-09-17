# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Script Checkpoints."""

from advanced_final_hardening.release_candidate_script_checkpoints import (
    build_release_candidate_script_checkpoint_registry,
)


def test_build_release_candidate_script_checkpoints():
    df, summary = build_release_candidate_script_checkpoint_registry()
    assert not df.empty
    assert summary["checkpoint_count"] >= 1
    assert summary["all_available"] is True
    assert (df["status"] == "release_candidate_contract_ready").all()
