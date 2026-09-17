import pytest
import pandas as pd
from advanced_backtest_acceptance.phase_148_stress_testing_acceptance import (
    build_phase_148_stress_testing_acceptance_registry,
    PHASE_148_CHECKS,
)

def test_phase_148_stress_testing_acceptance():
    df, summary = build_phase_148_stress_testing_acceptance_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(PHASE_148_CHECKS)
    assert summary["phase_ref"] == "Phase 148"
    assert summary["all_passed"] is True
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["passed"] == True).all()
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert (df["non_signal"] == True).all()
