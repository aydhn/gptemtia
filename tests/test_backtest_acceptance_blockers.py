import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_blockers import (
    build_backtest_acceptance_blocker_registry,
    create_backtest_acceptance_blocker,
    BLOCKER_TYPES,
)

def test_backtest_acceptance_blockers():
    df, summary = build_backtest_acceptance_blocker_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert summary["total_blockers"] == 0
    assert summary["has_blockers"] is False
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
    assert set(BLOCKER_TYPES).issubset(set(summary["supported_blocker_types"]))

    # Test factory
    blocker = create_backtest_acceptance_blocker(
        blocker_type="missing_manifest",
        phase_ref="Phase 146",
        severity_label="CRITICAL",
        message="Manifest missing in test environment",
        recommendation="Run phase 146 manifest script",
    )
    assert blocker.finding_type == "missing_manifest"
    assert blocker.phase_ref == "Phase 146"
    assert blocker.severity_label == "CRITICAL"
    assert blocker.manual_review_required is True
    assert blocker.non_signal is True
