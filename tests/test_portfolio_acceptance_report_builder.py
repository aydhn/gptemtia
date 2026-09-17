# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Report Builder."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    DISCLAIMER_TEXT,
    build_portfolio_acceptance_disclaimer,
    build_portfolio_acceptance_profile_markdown_report,
    build_portfolio_acceptance_component_markdown_report,
    build_portfolio_phase_acceptance_markdown_report,
    build_portfolio_acceptance_dependency_markdown_report,
    build_portfolio_validation_evidence_markdown_report,
    build_portfolio_acceptance_boundary_markdown_report,
    build_portfolio_acceptance_findings_markdown_report,
    build_portfolio_acceptance_readiness_score_markdown_report,
    build_portfolio_acceptance_manifest_markdown_report,
    build_portfolio_acceptance_validation_markdown_report,
    build_portfolio_acceptance_safety_markdown_report,
    build_phase_158_handoff_markdown_report,
)


def test_disclaimer():
    """Verify standard disclaimer is returned and non-empty."""
    disc = build_portfolio_acceptance_disclaimer()
    assert disc == DISCLAIMER_TEXT
    assert "NON-PRODUCTION / RESEARCH-ONLY" in disc


def test_markdown_reports():
    """Verify all report builder functions generate markdown containing disclaimers."""
    summary = {
        "active_profile": "portfolio_acceptance_default",
        "total_profiles": 1,
        "all_dry_run": True,
        "all_local_only": True,
        "all_non_production": True,
        "status": "PORTFOLIO_ACCEPTANCE_READY",
        "phase_number": 153,
        "total_criteria": 10,
        "satisfied_criteria": 10,
        "all_satisfied": True,
        "total_components": 5,
        "total_dependencies": 8,
        "total_boundaries": 12,
        "total_rules": 16,
        "total_findings": 2,
        "readiness_score": 0.95,
        "classification": "portfolio_acceptance_contract_ready_non_production",
        "meets_threshold": True,
        "handoff_accepted": True,
        "from_phase": 157,
        "to_phase": 158,
    }
    df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])

    reports = [
        build_portfolio_acceptance_profile_markdown_report(summary, df),
        build_portfolio_acceptance_component_markdown_report(summary, df),
        build_portfolio_phase_acceptance_markdown_report(summary, df),
        build_portfolio_acceptance_dependency_markdown_report(summary, df),
        build_portfolio_validation_evidence_markdown_report(summary, df),
        build_portfolio_acceptance_boundary_markdown_report(summary, df),
        build_portfolio_acceptance_findings_markdown_report(summary, df),
        build_portfolio_acceptance_readiness_score_markdown_report(summary, df),
        build_portfolio_acceptance_manifest_markdown_report(summary, df),
        build_portfolio_acceptance_validation_markdown_report(summary, df),
        build_portfolio_acceptance_safety_markdown_report(summary, df),
        build_phase_158_handoff_markdown_report(summary, df),
    ]

    for rep in reports:
        assert isinstance(rep, str)
        assert len(rep) > 100
        assert DISCLAIMER_TEXT in rep
        assert "Phase 157" in rep
