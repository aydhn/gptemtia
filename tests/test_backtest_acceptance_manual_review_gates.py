import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_manual_review_gates import (
    build_backtest_acceptance_manual_review_gate_registry,
    REVIEW_GATES,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    ACCEPTANCE_MANUAL_REVIEW_REQUIRED,
)

def test_backtest_acceptance_manual_review_gates():
    df, summary = build_backtest_acceptance_manual_review_gate_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(REVIEW_GATES)
    assert summary["total_gates"] == len(REVIEW_GATES)
    assert summary["all_require_review"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["manual_review_required"] == True).all()
    assert (df["status"] == ACCEPTANCE_MANUAL_REVIEW_REQUIRED).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
