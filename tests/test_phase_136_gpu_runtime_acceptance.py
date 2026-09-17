# -*- coding: utf-8 -*-
"""Unit tests for Phase 136 GPU Runtime Acceptance."""

import pytest
from advanced_ml_acceptance.phase_136_gpu_runtime_acceptance import (
    build_phase_136_gpu_runtime_acceptance_registry,
    summarize_phase_136_gpu_runtime_acceptance,
)


def test_phase_136_acceptance():
    df, summary = build_phase_136_gpu_runtime_acceptance_registry()
    assert not df.empty
    assert len(df) >= 7
    assert summary["phase_ref"] == "Phase 136"
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "ACCEPTED"

    s = summarize_phase_136_gpu_runtime_acceptance(df)
    assert s["check_count"] >= 7
    assert s["all_passed"] is True
