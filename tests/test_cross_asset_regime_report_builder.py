"""Tests for Cross-Asset Regime Report Builder."""

import pandas as pd
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_cross_asset_regime_disclaimer,
    build_cross_asset_regime_profile_markdown_report,
    build_cross_asset_entity_pair_markdown_report,
    build_cross_asset_manifest_markdown_report,
    build_phase_132_handoff_markdown_report,
)


def test_cross_asset_regime_disclaimer():
    disc = build_cross_asset_regime_disclaimer()
    assert "YASAL VE OPERASYONEL FERAGATNAME" in disc
    assert "Phase 131" in disc
    assert "kesin AL/SAT" in disc


def test_markdown_report_generation():
    summary = {
        "active_profile": "test_profile",
        "current_phase": 131,
        "target_final_phase": 160,
        "total_profiles": 1,
    }
    df = pd.DataFrame([{"col1": "val1", "col2": "val2"}])
    report = build_cross_asset_regime_profile_markdown_report(summary, df)
    assert "# Phase 131: Cross-Asset Regime Profile Registry Report" in report
    assert "test_profile" in report
    assert "| col1 | col2 |" in report
