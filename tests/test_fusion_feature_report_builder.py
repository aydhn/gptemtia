"""Tests for Fusion Feature Report Builder."""

from advanced_feature_fusion.fusion_feature_report_builder import (
    build_fusion_feature_markdown_report,
    build_fusion_feature_text_report,
)


def test_markdown_report_builder():
    summary_data = {
        "status": "HEALTHY",
        "current_phase": 120,
        "next_phase": 121,
        "target_final_phase": 160,
        "readiness_score": 1.0,
        "handoff_ready": True,
        "domain_count": 35,
        "metadata_feature_count": 17,
        "contract_count": 5,
        "policy_count": 5,
    }
    md = build_fusion_feature_markdown_report(summary_data)
    assert "# Phase 120" in md
    assert "DISCLAIMER" in md
    assert "HEALTHY" in md
    assert "Phase 121" in md


def test_text_report_builder():
    summary_data = {
        "status": "HEALTHY",
        "current_phase": 120,
        "next_phase": 121,
        "target_final_phase": 160,
        "readiness_score": 1.0,
        "handoff_ready": True,
        "domain_count": 35,
        "metadata_feature_count": 17,
    }
    txt = build_fusion_feature_text_report(summary_data)
    assert "PHASE 120" in txt
    assert "DISCLAIMER" in txt
    assert "Zero Trade Signals: ENFORCED" in txt
