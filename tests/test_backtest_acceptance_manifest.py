import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_manifest import (
    build_backtest_acceptance_manifest,
)

def test_backtest_acceptance_manifest():
    df, summary = build_backtest_acceptance_manifest()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == 1
    assert summary["backtest_block_completed"] is True
    assert summary["phase_153_handoff_ready"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    row = df.iloc[0]
    assert row["current_phase"] == 152
    assert row["target_final_phase"] == 160
    assert row["next_phase"] == 153
    assert bool(row["backtest_block_completed"]) is True
    assert bool(row["phase_153_handoff_ready"]) is True
    assert bool(row["source_preserved"]) is True
    assert bool(row["local_only"]) is True
    assert bool(row["dry_run"]) is True
    assert bool(row["non_production"]) is True

    # Check all negative invariant flags
    assert bool(row["production_ready"]) is False
    assert bool(row["broker_ready"]) is False
    assert bool(row["live_trading_ready"]) is False
    assert bool(row["official_approval"]) is False
    assert bool(row["backtest_executed"]) is False
    assert bool(row["benchmark_executed"]) is False
    assert bool(row["metric_calculated"]) is False
    assert bool(row["result_claim_generated"]) is False
    assert bool(row["performance_claim_generated"]) is False
    assert bool(row["strategy_approved"]) is False
    assert bool(row["capital_allocation_generated"]) is False
    assert bool(row["portfolio_constructed"]) is False
    assert bool(row["position_sizing_generated"]) is False
    assert bool(row["optimizer_executed"]) is False
    assert bool(row["model_training_executed"]) is False
    assert bool(row["prediction_generated"]) is False
    assert bool(row["target_label_generated"]) is False
    assert bool(row["broker_order_sent"]) is False
    assert bool(row["live_order_sent"]) is False
    assert bool(row["artifact_persisted"]) is False
    assert bool(row["model_registry_written"]) is False
    assert bool(row["model_deployed"]) is False
    assert bool(row["production_deployed"]) is False
