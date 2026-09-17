# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Component Registry."""

import pytest
from advanced_ml_acceptance.advanced_ml_component_registry import (
    build_advanced_ml_component_registry,
    summarize_advanced_ml_components,
)


def test_build_component_registry():
    df, summary = build_advanced_ml_component_registry()
    assert not df.empty
    assert len(df) == 10
    assert summary["current_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 146
    assert summary["total_components"] == 10
    assert summary["non_signal"] is True

    s = summarize_advanced_ml_components(df)
    assert s["component_count"] == 10
    assert s["all_contract_only"] is True
    assert s["non_signal"] is True
