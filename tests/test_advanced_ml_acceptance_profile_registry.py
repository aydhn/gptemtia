# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Acceptance Profile Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_profile_registry import (
    build_advanced_ml_acceptance_profile_registry,
    summarize_advanced_ml_acceptance_profiles,
)


def test_build_profile_registry():
    df, summary = build_advanced_ml_acceptance_profile_registry()
    assert not df.empty
    assert len(df) >= 3
    assert summary["current_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 146
    assert summary["non_signal"] is True

    s = summarize_advanced_ml_acceptance_profiles(df)
    assert s["profile_count"] >= 3
    assert s["non_signal"] is True
