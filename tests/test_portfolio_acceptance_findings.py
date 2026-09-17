# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Findings Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_findings import (
    DEFAULT_FINDINGS,
    create_portfolio_acceptance_finding,
    build_portfolio_acceptance_findings_registry,
    summarize_portfolio_acceptance_findings,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    FINDING_DOMAIN,
    SEVERITY_INFO,
    SEVERITY_WARNING,
    SEVERITY_CRITICAL,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_findings_registry_structure():
    """Verify findings registry builds valid DataFrame and summary."""
    df, summary = build_portfolio_acceptance_findings_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(DEFAULT_FINDINGS)

    expected_cols = {
        "finding_id",
        "finding_type",
        "phase_ref",
        "severity_label",
        "message",
        "recommendation",
        "manual_review_required",
        "is_blocking",
        "current_phase",
        "status",
    }
    assert expected_cols.issubset(df.columns)
    assert not any(df["is_blocking"])
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)

    assert isinstance(summary, dict)
    assert summary["domain"] == FINDING_DOMAIN
    assert summary["total_findings"] == len(DEFAULT_FINDINGS)
    assert summary["blocking_findings_count"] == 0
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_create_finding_valid():
    """Verify creating a valid finding."""
    f = create_portfolio_acceptance_finding(
        finding_type="test_finding",
        phase_ref="Phase 157",
        severity_label=SEVERITY_WARNING,
        message="Test warning message",
        recommendation="Review contracts manually.",
    )
    assert f.finding_type == "test_finding"
    assert f.phase_ref == "Phase 157"
    assert f.is_blocking is False
    assert f.manual_review_required is True


def test_create_finding_forbidden_recommendation():
    """Verify attempting automated forbidden actions raises ValueError."""
    with pytest.raises(ValueError, match="Prohibited remediation"):
        create_portfolio_acceptance_finding(
            finding_type="unsafe_fix",
            phase_ref="Phase 157",
            severity_label=SEVERITY_CRITICAL,
            message="Attempting auto fix",
            recommendation="auto-rebalance the portfolio positions immediately",
        )


def test_findings_with_extra():
    """Verify adding extra findings."""
    extra = create_portfolio_acceptance_finding(
        finding_type="extra_check",
        phase_ref="Phase 157",
        severity_label=SEVERITY_INFO,
        message="Additional informational check",
        recommendation="Log information.",
    )
    df, summary = build_portfolio_acceptance_findings_registry(extra_findings=[extra])
    assert len(df) == len(DEFAULT_FINDINGS) + 1
    assert summary["total_findings"] == len(DEFAULT_FINDINGS) + 1


def test_findings_empty():
    """Verify summarize with empty DataFrame."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_findings(empty_df)
    assert summary["total_findings"] == 0
    assert summary["blocking_findings_count"] == 0
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY
