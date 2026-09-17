import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_safety_boundary_registry import (
    build_backtest_acceptance_safety_boundary_registry,
    SAFETY_BOUNDARIES,
)

def test_backtest_acceptance_safety_boundary_registry():
    df, summary = build_backtest_acceptance_safety_boundary_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(SAFETY_BOUNDARIES)
    assert summary["total_boundaries"] == len(SAFETY_BOUNDARIES)
    assert summary["all_enforced"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["enforced"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
