# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Acceptance Report Builder."""

import pytest
import pandas as pd
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_advanced_ml_acceptance_disclaimer,
    build_advanced_ml_acceptance_profile_markdown_report,
    build_advanced_ml_component_markdown_report,
    build_advanced_ml_readiness_score_markdown_report,
    build_advanced_ml_acceptance_manifest_markdown_report,
    build_advanced_ml_acceptance_full_markdown_report,
)
from reports.report_builder import (
    build_advanced_ml_acceptance_text_report,
    build_advanced_ml_readiness_score_text_report,
)


def test_disclaimer_content():
    disc = build_advanced_ml_acceptance_disclaimer()
    assert "Phase 145" in disc
    assert "Canlı emir" in disc
    assert "değildir" in disc


def test_markdown_and_text_reports():
    summary = {
        "active_profile": "balanced_local_advanced_ml_acceptance",
        "current_phase": 145,
        "target_final_phase": 160,
        "next_phase": 146,
        "total_profiles": 3,
        "total_components": 10,
        "readiness_score": 1.0,
        "classification": "advanced_ml_contract_acceptance_ready_non_production",
        "meets_threshold": True,
        "manifest_id": "manifest_phase_145",
        "status": "ACCEPTED",
    }
    df = pd.DataFrame([{"col1": "val1"}])

    md_prof = build_advanced_ml_acceptance_profile_markdown_report(summary, df)
    assert "# Phase 145" in md_prof
    assert "balanced_local_advanced_ml_acceptance" in md_prof

    txt_prof = build_advanced_ml_acceptance_text_report(summary, df)
    assert "Phase 145" in txt_prof

    full_md = build_advanced_ml_acceptance_full_markdown_report({"components": df}, summary)
    assert "# Phase 145: Consolidated Advanced ML Acceptance Report" in full_md
    assert "Production Ready: `False`" in full_md
