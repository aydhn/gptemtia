# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Readiness Scoring."""

from advanced_final_hardening.release_candidate_readiness_scoring import (
    build_release_candidate_readiness_score_report,
)


def test_build_release_candidate_readiness_scoring():
    df, summary = build_release_candidate_readiness_score_report()
    assert not df.empty
    assert summary["readiness_score"] >= 0.85
    assert summary["threshold_met"] is True
    assert (df["readiness_score"] >= 0.80).all()
