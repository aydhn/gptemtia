# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Findings."""

from advanced_final_hardening.release_candidate_findings import (
    build_release_candidate_findings_registry,
)


def test_build_release_candidate_findings():
    df, summary = build_release_candidate_findings_registry()
    assert not df.empty
    assert summary["finding_count"] >= 1
    assert summary["all_manual_review_required"] is True
    assert (df["severity_label"] != "CRITICAL").all()
