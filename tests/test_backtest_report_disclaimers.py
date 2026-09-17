# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Report Disclaimers."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_report_disclaimers import (
    build_backtest_report_disclaimer_registry,
    DISCLAIMER_TEXT,
    REPORT_DISCLAIMERS,
)


def test_build_backtest_report_disclaimers():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_report_disclaimer_registry(profile)

    assert not df.empty
    assert len(df) == 2
    assert "disclaimer_id" in df.columns
    assert (df["mandatory"] == True).all()
    assert summary["mandatory_count"] == 2
    assert "Phase 150 Backtest Governance" in DISCLAIMER_TEXT
    assert len(REPORT_DISCLAIMERS) == 2
