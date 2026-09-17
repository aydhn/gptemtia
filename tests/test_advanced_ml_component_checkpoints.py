# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Component Checkpoints."""

import pytest
from advanced_ml_acceptance.advanced_ml_component_checkpoints import (
    build_advanced_ml_component_acceptance_checkpoint_registry,
    validate_component_checkpoint,
    summarize_advanced_ml_component_checkpoints,
)


def test_build_component_checkpoints():
    df, summary = build_advanced_ml_component_acceptance_checkpoint_registry()
    assert not df.empty
    assert len(df) == 10
    assert summary["current_phase"] == 145
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 146
    assert summary["total_checkpoints"] == 10

    for _, row in df.iterrows():
        assert row["contract_only"] is True
        assert row["non_production"] is True
        assert row["production_ready"] is False
        assert row["broker_ready"] is False
        assert row["signal_ready"] is False

    s = summarize_advanced_ml_component_checkpoints(df)
    assert s["checkpoint_count"] == 10
    assert s["all_contract_only"] is True
    assert s["all_non_production"] is True
