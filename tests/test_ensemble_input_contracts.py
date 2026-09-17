# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Input Contracts."""

from advanced_ensemble_model_registry.ensemble_input_contracts import (
    build_ensemble_input_contracts,
    validate_ensemble_input_contracts,
    summarize_ensemble_input_contracts,
)


def test_ensemble_input_contracts():
    contracts = build_ensemble_input_contracts()
    assert len(contracts) == 6
    assert "voting_input_contract" in contracts
    assert "blending_input_contract" in contracts
    assert "stacking_input_contract" in contracts
    assert validate_ensemble_input_contracts(contracts) is True

    summary = summarize_ensemble_input_contracts(contracts)
    assert summary["total_contracts"] == 6
    assert summary["all_no_lookahead"] is True
    assert summary["all_non_signal"] is True
