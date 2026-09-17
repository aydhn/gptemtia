# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Output Contracts."""

from advanced_ensemble_model_registry.ensemble_output_contracts import (
    build_ensemble_output_contracts,
    validate_ensemble_output_contracts,
    summarize_ensemble_output_contracts,
)


def test_ensemble_output_contracts():
    contracts = build_ensemble_output_contracts()
    assert len(contracts) == 6
    assert "voting_output_contract" in contracts
    assert "blending_output_contract" in contracts
    assert "stacking_output_contract" in contracts
    assert validate_ensemble_output_contracts(contracts) is True

    summary = summarize_ensemble_output_contracts(contracts)
    assert summary["total_contracts"] == 6
    assert summary["all_predictions_blocked"] is True
    assert summary["all_signals_blocked"] is True
    assert summary["all_non_signal"] is True
