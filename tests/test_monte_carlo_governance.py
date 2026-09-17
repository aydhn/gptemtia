# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Monte Carlo Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.monte_carlo_governance import (
    build_monte_carlo_governance_registry,
    MONTE_CARLO_GOVERNANCE_ITEMS,
)


def test_build_monte_carlo_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_monte_carlo_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "governance_id" in df.columns
    assert "name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert summary["execution_disabled"] is True
    assert summary["total_items"] == 3
    assert len(MONTE_CARLO_GOVERNANCE_ITEMS) == 3
