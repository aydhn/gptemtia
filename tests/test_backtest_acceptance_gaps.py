import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_gaps import (
    build_backtest_acceptance_gap_registry,
    create_backtest_acceptance_gap,
    GAP_TYPES,
)

def test_backtest_acceptance_gaps():
    df, summary = build_backtest_acceptance_gap_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert summary["total_gaps"] == 0
    assert summary["has_gaps"] is False
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert set(GAP_TYPES).issubset(set(summary["supported_gap_types"]))

    # Test factory
    gap = create_backtest_acceptance_gap(
        gap_type="optional_doc_missing",
        phase_ref="Phase 147",
        severity_label="LOW",
        message="Optional doc file not yet generated",
        recommendation="Generate optional doc during next review",
    )
    assert gap.finding_type == "optional_doc_missing"
    assert gap.phase_ref == "Phase 147"
    assert gap.severity_label == "LOW"
    assert gap.manual_review_required is True
    assert gap.non_signal is True
