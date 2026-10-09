# -*- coding: utf-8 -*-
"""Tests for Risk Reporting Readiness Scoring."""

import pytest
import pandas as pd
from advanced_risk_reporting.risk_reporting_readiness_scoring import (
    classify_risk_reporting_readiness_score,
    calculate_risk_reporting_readiness_score,
    build_risk_reporting_readiness_score_report,
)
from advanced_risk_reporting.risk_reporting_config import RiskReportingProfile


def test_classify_risk_reporting_readiness_score():
    """Test classification logic based on threshold limits."""
    # Test blocked (< 0.25)
    assert classify_risk_reporting_readiness_score(0.0) == "blocked"
    assert classify_risk_reporting_readiness_score(0.24) == "blocked"

    # Test incomplete (< 0.50)
    assert classify_risk_reporting_readiness_score(0.25) == "incomplete"
    assert classify_risk_reporting_readiness_score(0.49) == "incomplete"

    # Test manual review (< 0.75)
    assert classify_risk_reporting_readiness_score(0.50) == "contract_ready_with_manual_review"
    assert classify_risk_reporting_readiness_score(0.74) == "contract_ready_with_manual_review"

    # Test ready (>= 0.75)
    assert classify_risk_reporting_readiness_score(0.75) == "risk_reporting_contract_ready_non_production"
    assert classify_risk_reporting_readiness_score(1.0) == "risk_reporting_contract_ready_non_production"


def test_calculate_risk_reporting_readiness_score_empty_findings():
    """Test calculation with empty findings."""
    empty_df = pd.DataFrame()
    result = calculate_risk_reporting_readiness_score(empty_df)

    assert result.readiness_score == 1.0
    assert result.classification == "risk_reporting_contract_ready_non_production"
    assert result.is_contract_ready is True
    assert result.current_phase == 155


def test_calculate_risk_reporting_readiness_score_with_findings():
    """Test calculation with severity labels."""
    findings_data = {
        "severity_label": ["BLOCKER", "BLOCKER", "WARNING", "INFO"]
    }
    df = pd.DataFrame(findings_data)

    # 2 blockers = -0.80, 1 warning = -0.10. Base = 1.0 -> 0.10
    result = calculate_risk_reporting_readiness_score(df)
    assert result.readiness_score == 0.10
    assert result.classification == "blocked"
    assert result.is_contract_ready is False


def test_calculate_risk_reporting_readiness_score_floor():
    """Test score doesn't drop below 0.0."""
    findings_data = {
        "severity_label": ["BLOCKER", "BLOCKER", "BLOCKER"]
    }
    df = pd.DataFrame(findings_data)

    # 3 blockers = -1.20. Base = 1.0 -> max(0.0, 1.0 - 1.2) -> 0.0
    result = calculate_risk_reporting_readiness_score(df)
    assert result.readiness_score == 0.0


def test_calculate_risk_reporting_readiness_score_custom_profile():
    """Test calculation with a custom profile threshold."""
    profile = RiskReportingProfile(
        profile_name="test_profile",
        description="test",
        min_readiness_score=0.80
    )

    findings_data = {
        "severity_label": ["WARNING", "WARNING", "WARNING"]
    }
    df = pd.DataFrame(findings_data)

    # 3 warnings = -0.30. Base = 1.0 -> 0.70.
    result = calculate_risk_reporting_readiness_score(df, profile=profile)
    assert result.readiness_score == 0.70
    assert result.classification == "contract_ready_with_manual_review"
    assert result.is_contract_ready is False  # 0.70 < 0.80


def test_build_risk_reporting_readiness_score_report():
    """Test building report dataframes and dictionaries."""
    df, summary = build_risk_reporting_readiness_score_report()

    assert not df.empty
    assert "readiness_score" in df.columns
    assert "classification" in df.columns

    assert summary["readiness_score"] == 1.0
    assert summary["classification"] == "risk_reporting_contract_ready_non_production"
    assert summary["is_contract_ready"] is True
    assert "meets_threshold" in summary
