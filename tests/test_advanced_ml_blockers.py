# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Blocker Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_blockers import (
    build_advanced_ml_blocker_registry,
    create_advanced_ml_blocker,
    summarize_advanced_ml_blockers,
)


def test_blocker_registry_clean():
    df, summary = build_advanced_ml_blocker_registry()
    assert summary["has_blockers"] is False
    assert summary["total_blockers"] == 0
    assert summary["status"] == "CLEAN"

    s = summarize_advanced_ml_blockers(df)
    assert s["blocker_count"] == 0


def test_create_blocker():
    blk = create_advanced_ml_blocker(
        blocker_type="missing_phase_module",
        phase_ref="Phase 136",
        severity_label="CRITICAL",
        message="Module missing",
        recommendation="Install module",
    )
    assert blk.finding_type == "missing_phase_module"
    assert blk.severity_label == "CRITICAL"
    assert blk.manual_review_required is True
