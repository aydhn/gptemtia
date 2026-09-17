# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Contracts."""

from advanced_final_hardening.release_candidate_contracts import (
    build_release_candidate_contract_registry,
)


def test_build_release_candidate_contracts():
    df, summary = build_release_candidate_contract_registry()
    assert not df.empty
    assert summary["candidate_contract_count"] >= 1
    assert summary["all_production_ready_false"] is True
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert (df["status"] == "release_candidate_contract_ready").all()
