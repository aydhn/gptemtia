import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_non_production_boundaries import (
    build_backtest_acceptance_non_production_boundary_registry,
    NON_PROD_BOUNDARIES,
)

def test_backtest_acceptance_non_production_boundaries():
    df, summary = build_backtest_acceptance_non_production_boundary_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(NON_PROD_BOUNDARIES)
    assert summary["total_boundaries"] == len(NON_PROD_BOUNDARIES)
    assert summary["all_active"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["active"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
