"""Unit tests for Phase 119 markdown report builder."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_asset_alignment_report_builder import (
    build_cross_asset_alignment_disclaimer,
    build_cross_asset_alignment_profile_markdown_report,
    build_cross_asset_alignment_domain_markdown_report,
    build_cross_domain_matrix_markdown_report,
    build_cross_asset_alignment_validation_markdown_report,
    build_cross_asset_alignment_health_markdown_report,
    build_cross_asset_alignment_safety_markdown_report,
    build_phase_120_handoff_markdown_report,
    CROSS_ASSET_ALIGNMENT_DISCLAIMER,
)


def test_disclaimer_content():
    disc = build_cross_asset_alignment_disclaimer()
    assert "Phase 119" in disc
    assert "Canlı emir" in disc
    assert "kesin AL/SAT" in disc
    assert "yatırım tavsiyesi" in disc
    assert "trade sinyali" in disc


def test_profile_markdown_report():
    summary = {"active_profile": "balanced_local_cross_asset_alignment", "total_profiles": 3, "status": "READY"}
    df = pd.DataFrame([{"profile_name": "p1", "current_phase": 119}])
    md = build_cross_asset_alignment_profile_markdown_report(summary, df)
    assert "# Phase 119: Cross-Asset Alignment Profile Report" in md
    assert CROSS_ASSET_ALIGNMENT_DISCLAIMER in md
    assert "balanced_local_cross_asset_alignment" in md


def test_matrix_markdown_report():
    summary = {"total_rows": 10, "total_columns": 8, "contract_name": "cross_domain_research", "status": "READY"}
    md = build_cross_domain_matrix_markdown_report(summary)
    assert "# Phase 119: Cross-Domain Aligned Feature Matrix Report" in md
    assert "cross_domain_research" in md
