# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Strategy Contracts."""

from advanced_ensemble_model_registry.ensemble_strategy_contracts import (
    build_ensemble_strategy_contracts,
    validate_ensemble_strategy_contracts,
    validate_ensemble_strategy_contract,
    summarize_ensemble_strategy_contracts,
)


def test_ensemble_strategy_contracts():
    df, summary = build_ensemble_strategy_contracts()
    assert len(df) == 7
    assert summary["total_strategies"] == 7
    assert summary["all_execution_disabled"] is True
    assert summary["all_voting_disabled"] is True
    assert summary["all_blending_disabled"] is True
    assert summary["all_stacking_disabled"] is True
    assert validate_ensemble_strategy_contracts(df, summary) is True


def test_validate_ensemble_strategy_contract():
    valid = {
        "ensemble_strategy_name": "test_strategy",
        "ensemble_execution_allowed": False,
        "voting_execution_allowed": False,
        "blending_execution_allowed": False,
        "stacking_execution_allowed": False,
        "calibration_allowed": False,
        "prediction_allowed": False,
        "signal_generation_allowed": False,
        "artifact_persistence_allowed": False,
        "non_signal_required": True,
    }
    assert validate_ensemble_strategy_contract(valid)["is_valid"] is True

    bad = dict(valid, ensemble_execution_allowed=True)
    assert validate_ensemble_strategy_contract(bad)["is_valid"] is False
