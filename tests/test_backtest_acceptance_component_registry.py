import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_component_registry import (
    build_backtest_acceptance_component_registry,
    summarize_backtest_acceptance_components,
    COMPONENTS,
)

def test_backtest_acceptance_component_registry():
    df, summary = build_backtest_acceptance_component_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(COMPONENTS)
    assert summary["total_components"] == len(COMPONENTS)
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True

    # Invariant safety flags
    assert (df["contract_only"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert (df["signal_ready"] == False).all()
    assert (df["strategy_approved"] == False).all()
    assert (df["non_signal"] == True).all()

    # Summarize function
    summ = summarize_backtest_acceptance_components(df)
    assert summ["component_count"] == len(COMPONENTS)
    assert len(summ["phases_covered"]) == len(COMPONENTS)
    assert summ["all_contract_only"] is True
    assert summ["all_non_production"] is True
    assert summ["non_signal"] is True
