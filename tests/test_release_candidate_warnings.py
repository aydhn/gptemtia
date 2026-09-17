# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Release Candidate Warnings."""

from advanced_final_hardening.release_candidate_warnings import (
    build_release_candidate_warning_registry,
)


def test_build_release_candidate_warnings():
    df, summary = build_release_candidate_warning_registry()
    assert not df.empty
    assert summary["warning_count"] >= 1
    assert summary["all_acknowledged"] is True
    assert (df["is_acknowledged"] == True).all()
