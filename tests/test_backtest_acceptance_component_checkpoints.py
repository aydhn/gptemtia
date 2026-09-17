import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_component_checkpoints import (
    build_backtest_acceptance_component_checkpoint_registry,
    validate_backtest_acceptance_component_checkpoint,
    summarize_backtest_acceptance_component_checkpoints,
    CHECKPOINTS,
)

def test_backtest_acceptance_component_checkpoints():
    df, summary = build_backtest_acceptance_component_checkpoint_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(CHECKPOINTS)
    assert summary["total_checkpoints"] == len(CHECKPOINTS)
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True

    # Invariants
    assert (df["contract_only"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["manual_review_required"] == True).all()
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert (df["live_ready"] == False).all()
    assert (df["signal_ready"] == False).all()
    assert (df["strategy_approved"] == False).all()

    # Test checkpoint validation helper
    chk_record = CHECKPOINTS[0]
    validation = validate_backtest_acceptance_component_checkpoint(chk_record)
    assert validation["is_valid"] is True
    assert validation["production_ready"] is False
    assert validation["broker_ready"] is False

    invalid_record = {"checkpoint_id": "CHK-INVALID"}
    validation_invalid = validate_backtest_acceptance_component_checkpoint(invalid_record)
    assert validation_invalid["is_valid"] is False
    assert len(validation_invalid["missing_keys"]) > 0

    # Test summary helper
    summ = summarize_backtest_acceptance_component_checkpoints(df)
    assert summ["checkpoint_count"] == len(CHECKPOINTS)
    assert summ["all_contract_only"] is True
    assert summ["all_non_production"] is True
    assert summ["all_manual_review_required"] is True
    assert summ["non_signal"] is True
