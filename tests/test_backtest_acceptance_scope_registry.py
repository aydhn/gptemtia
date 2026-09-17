import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_scope_registry import (
    build_backtest_acceptance_scope_registry,
    SCOPE_ITEMS,
)

def test_backtest_acceptance_scope_registry():
    df, summary = build_backtest_acceptance_scope_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(SCOPE_ITEMS)
    assert summary["total_scope_items"] == len(SCOPE_ITEMS)
    assert summary["all_safe"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Check that safety items are in scope and flagged properly
    assert (df["in_scope"] == True).all()
    assert (df["is_safe"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
