# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Acceptance Scope Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_scope_registry import (
    build_advanced_ml_acceptance_scope_registry,
    summarize_advanced_ml_acceptance_scope,
)


def test_build_scope_registry():
    df, summary = build_advanced_ml_acceptance_scope_registry()
    assert not df.empty
    assert len(df) >= 10
    assert summary["current_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 146
    assert summary["non_signal"] is True
    assert summary["allowed_items"] > 0
    assert summary["prohibited_items"] > 0

    s = summarize_advanced_ml_acceptance_scope(df)
    assert s["total_scope_items"] >= 10
    assert s["non_signal"] is True
