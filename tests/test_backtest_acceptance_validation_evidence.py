import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_validation_evidence import (
    build_backtest_acceptance_validation_evidence_registry,
    EVIDENCE_ITEMS,
)

def test_backtest_acceptance_validation_evidence():
    df, summary = build_backtest_acceptance_validation_evidence_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(EVIDENCE_ITEMS)
    assert summary["total_evidence_items"] == len(EVIDENCE_ITEMS)
    assert summary["all_verified"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["verified"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
