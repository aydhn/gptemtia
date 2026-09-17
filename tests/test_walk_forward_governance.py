# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Walk-Forward Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.walk_forward_governance import (
    build_walk_forward_governance_registry,
    WALK_FORWARD_GOVERNANCE_ITEMS,
)


def test_build_walk_forward_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_walk_forward_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "governance_id" in df.columns
    assert "title" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert summary["total_items"] == 3
    assert summary["execution_disabled"] is True
    assert len(WALK_FORWARD_GOVERNANCE_ITEMS) == 3
