# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Profile Registry."""

import pytest
from advanced_explainability_attribution.explainability_profile_registry import (
    build_explainability_profile_registry,
    summarize_explainability_profiles,
)


def test_explainability_profile_registry():
    df, summary = build_explainability_profile_registry()
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["all_dry_run"] is True
    assert summary["all_non_signal"] is True
    assert summary["current_phase"] == 143
    assert summary["next_phase"] == 144
    assert summary["target_final_phase"] == 160
