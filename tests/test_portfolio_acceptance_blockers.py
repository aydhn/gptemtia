# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Blocker Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_blockers import (
    KNOWN_BLOCKER_TYPES,
    create_portfolio_acceptance_blocker,
    build_portfolio_acceptance_blocker_registry,
    summarize_portfolio_acceptance_blockers,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    BLOCKER_DOMAIN,
    SEVERITY_CRITICAL,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_blocker_registry_structure():
    """Verify blocker registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_blocker_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(KNOWN_BLOCKER_TYPES)

    expected_cols = {
        "blocker_type",
        "phase_ref",
        "severity_label",
        "is_active",
        "message",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)

    # In clean default state, zero active blockers
    assert not any(df["is_active"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == BLOCKER_DOMAIN
    assert summary["total_monitored_blocker_types"] == len(KNOWN_BLOCKER_TYPES)
    assert summary["active_blockers_count"] == 0
    assert summary["has_active_blockers"] is False
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_create_portfolio_acceptance_blocker():
    """Verify creation of a blocker finding."""
    blk = create_portfolio_acceptance_blocker(
        blocker_type="missing_manifest",
        phase_ref="Phase 153",
        severity_label=SEVERITY_CRITICAL,
        message="Manifest missing in Phase 153",
    )
    assert blk.finding_type == "missing_manifest"
    assert blk.phase_ref == "Phase 153"
    assert blk.severity_label == SEVERITY_CRITICAL
    assert blk.is_blocking is True
    assert blk.manual_review_required is True


def test_blocker_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_blockers(empty_df)
    assert summary["total_monitored_blocker_types"] == 0
    assert summary["active_blockers_count"] == 0
    assert summary["has_active_blockers"] is False
