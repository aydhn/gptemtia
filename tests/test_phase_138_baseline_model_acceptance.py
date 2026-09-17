# -*- coding: utf-8 -*-
"""Unit tests for Phase 138 Baseline Model Acceptance."""

import pytest
from advanced_ml_acceptance.phase_138_baseline_model_acceptance import (
    build_phase_138_baseline_model_acceptance_registry,
    summarize_phase_138_baseline_model_acceptance,
)


def test_phase_138_acceptance():
    df, summary = build_phase_138_baseline_model_acceptance_registry()
    assert not df.empty
    assert len(df) >= 7
    assert summary["phase_ref"] == "Phase 138"
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "ACCEPTED"

    s = summarize_phase_138_baseline_model_acceptance(df)
    assert s["check_count"] >= 7
    assert s["all_passed"] is True
