# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Out-of-Sample Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.oos_governance import (
    build_oos_governance_registry,
    OOS_GOVERNANCE_ITEMS,
)


def test_build_oos_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_oos_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "oos_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["status"] == "ACTIVE").all()
    assert summary["total_rules"] == 3
    assert summary["quarantine_active"] is True
    assert len(OOS_GOVERNANCE_ITEMS) == 3
