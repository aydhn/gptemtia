# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Report Builder."""

from advanced_calibration_uncertainty.calibration_uncertainty_report_builder import (
    CALIBRATION_UNCERTAINTY_DISCLAIMER,
    build_calibration_uncertainty_disclaimer,
    build_calibration_uncertainty_profile_markdown_report,
    build_probability_calibration_contract_markdown_report,
    build_calibration_uncertainty_consolidated_markdown_report,
    build_calibration_uncertainty_consolidated_text_report,
)


def test_report_builder_disclaimer():
    disc = build_calibration_uncertainty_disclaimer()
    assert "Phase 141" in disc
    assert "yatırım tavsiyesi" in disc.lower()


def test_consolidated_reports():
    dummy = {
        "phase": 141,
        "profile": {"name": "test_prof"},
        "calibration_contract_count": 5,
        "uncertainty_contract_count": 5,
        "readiness_score": 1.0,
        "health_status": "HEALTHY",
        "validation_status": "VALID",
    }
    md = build_calibration_uncertainty_consolidated_markdown_report(dummy)
    assert "# Phase 141" in md
    assert "test_prof" in md

    txt = build_calibration_uncertainty_consolidated_text_report(dummy)
    assert "PHASE 141" in txt
    assert "test_prof" in txt
