import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_warnings import (
    build_backtest_acceptance_warning_registry,
    create_backtest_acceptance_warning,
    STANDARD_WARNINGS,
)

def test_backtest_acceptance_warnings():
    df, summary = build_backtest_acceptance_warning_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(STANDARD_WARNINGS)
    assert summary["total_warnings"] == len(STANDARD_WARNINGS)
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()
    assert (df["manual_review_required"] == True).all()

    # Factory test
    w = create_backtest_acceptance_warning(
        warning_type="contract_only_acceptance",
        phase_ref="Phase 152",
        severity_label="INFO",
        message="Notice regarding contracts",
        recommendation="Maintain contracts",
    )
    assert w.finding_type == "contract_only_acceptance"
    assert w.manual_review_required is True
    assert w.non_signal is True
