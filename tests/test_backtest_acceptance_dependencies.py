import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_dependencies import (
    build_backtest_acceptance_dependency_registry,
    DEPENDENCIES,
)

def test_backtest_acceptance_dependencies():
    df, summary = build_backtest_acceptance_dependency_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(DEPENDENCIES)
    assert summary["total_dependencies"] == len(DEPENDENCIES)
    assert summary["all_satisfied"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["satisfied"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
