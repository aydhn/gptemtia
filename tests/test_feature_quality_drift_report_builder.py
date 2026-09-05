"""Tests for advanced_feature_quality_drift.feature_quality_drift_report_builder."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_quality_drift_report_builder import (
    DISCLAIMER,
    build_feature_quality_drift_disclaimer,
    build_feature_quality_drift_profile_markdown_report,
    build_quality_metric_markdown_report,
    build_drift_metric_markdown_report,
    build_missingness_markdown_report,
    build_distribution_drift_markdown_report,
    build_factor_quality_markdown_report,
    build_macro_cross_asset_quality_markdown_report,
    build_quality_findings_markdown_report,
    build_drift_findings_markdown_report,
    build_quality_drift_score_markdown_report,
    build_quality_drift_manifest_markdown_report,
    build_quality_drift_health_markdown_report,
    build_quality_drift_safety_markdown_report,
    build_phase_124_handoff_markdown_report,
)


def test_build_feature_quality_drift_disclaimer():
    disc = build_feature_quality_drift_disclaimer()
    assert "UYARI VE BİLGİLENDİRME:" in disc
    assert "Phase 123" in disc
    assert "AL/SAT" in disc


def test_markdown_reports_include_disclaimer():
    summary = {
        "active_profile": "research_balanced",
        "total_profiles": 3,
        "current_phase": 123,
        "target_final_phase": 160,
        "next_phase": 124,
        "non_signal": True,
        "local_only": True,
        "research_only": True,
        "status": "diagnostic_pass",
    }
    df = pd.DataFrame([{"col1": "val1", "col2": 10}])

    rep1 = build_feature_quality_drift_profile_markdown_report(summary, df)
    assert "Phase 123: Feature Quality and Drift Profile Registry" in rep1
    assert "UYARI VE BİLGİLENDİRME:" in rep1
    assert "Configured Diagnostic Profiles" in rep1

    rep2 = build_quality_metric_markdown_report(summary, df)
    assert "Phase 123: Feature Quality Metric Registry" in rep2
    assert "UYARI VE BİLGİLENDİRME:" in rep2

    rep3 = build_drift_metric_markdown_report(summary, df)
    assert "Phase 123: Feature Drift Metric Registry" in rep3

    rep4 = build_missingness_markdown_report(summary, df)
    assert "Phase 123: Feature Missingness Diagnostics Report" in rep4

    rep5 = build_distribution_drift_markdown_report(summary, df)
    assert "Phase 123: Feature Distribution Drift Report" in rep5

    rep6 = build_factor_quality_markdown_report(summary, df)
    assert "Phase 123: Factor Family Quality Report" in rep6

    rep7 = build_macro_cross_asset_quality_markdown_report(summary, df)
    assert "Phase 123: Macro, Calendar, News & Cross-Asset Quality Report" in rep7

    rep8 = build_quality_findings_markdown_report(summary, df)
    assert "Phase 123: Feature Quality Findings Registry Report" in rep8

    rep9 = build_drift_findings_markdown_report(summary, df)
    assert "Phase 123: Feature Drift Findings Registry Report" in rep9

    rep10 = build_quality_drift_score_markdown_report(summary, df)
    assert "Phase 123: Feature Quality & Drift Score Report" in rep10

    rep11 = build_quality_drift_manifest_markdown_report(summary, df)
    assert "Phase 123: Feature Quality & Drift Manifest Report" in rep11

    rep12 = build_quality_drift_health_markdown_report(summary, df)
    assert "Phase 123: Feature Quality & Drift Health Check Report" in rep12

    rep13 = build_quality_drift_safety_markdown_report(summary, df)
    assert "Phase 123: Feature Quality & Drift Safety Boundary Report" in rep13

    rep14 = build_phase_124_handoff_markdown_report(summary, df)
    assert "Phase 123 -> Phase 124: Feature Store Integration Handoff Report" in rep14
