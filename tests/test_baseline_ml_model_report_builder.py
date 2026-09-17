# -*- coding: utf-8 -*-
"""Unit tests for baseline ML model report builder."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_ml_model_report_builder import (
    BASELINE_ML_MODEL_REPORT_DISCLAIMER,
    build_baseline_ml_model_disclaimer,
    _df_to_markdown,
    build_baseline_ml_model_profile_markdown_report,
    build_baseline_model_contract_markdown_report,
    build_dry_run_training_harness_markdown_report,
    build_disabled_execution_markdown_report,
    build_baseline_metric_placeholder_markdown_report,
    build_baseline_model_input_guard_markdown_report,
    build_baseline_model_findings_markdown_report,
    build_baseline_model_readiness_score_markdown_report,
    build_baseline_ml_model_manifest_markdown_report,
    build_baseline_ml_model_validation_markdown_report,
    build_baseline_ml_model_safety_markdown_report,
    build_phase_139_handoff_markdown_report,
)


def test_build_baseline_ml_model_disclaimer():
    disclaimer = build_baseline_ml_model_disclaimer()
    assert "YASAL UYARI VE GÜVENLİK SINIRI" in disclaimer
    assert "Phase 138" in disclaimer
    assert "AL/SAT" in disclaimer


def test_df_to_markdown_fallback():
    df = pd.DataFrame({"col_a": [1, 2], "col_b": ["x", "y"]})
    md = _df_to_markdown(df)
    assert "| col_a | col_b |" in md
    assert "| 1 | x |" in md

    empty_df = pd.DataFrame()
    assert _df_to_markdown(empty_df) == ""


def test_markdown_report_builders():
    summary = {"total_contracts": 10, "all_real_training_blocked": True}
    df = pd.DataFrame([{"contract_id": "c1", "status": "CONTRACT_ONLY"}])

    md_contract = build_baseline_model_contract_markdown_report(summary, df)
    assert "# Phase 138: Baseline Model Contracts Registry Report" in md_contract
    assert "c1" in md_contract

    md_harness = build_dry_run_training_harness_markdown_report({"total_harness_contracts": 5})
    assert "Dry-Run Training Harness" in md_harness

    md_safety = build_baseline_ml_model_safety_markdown_report({"safety_status": "SECURE"})
    assert "Safety Boundary Report" in md_safety

    md_handoff = build_phase_139_handoff_markdown_report({"handoff_status": "READY_FOR_PHASE_139"})
    assert "Phase 139" in md_handoff
