# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Governance Scope Registry."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_scope_registry import (
    build_backtest_governance_scope_registry,
    summarize_backtest_governance_scopes,
    SCOPES,
)


def test_build_backtest_governance_scope_registry():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_governance_scope_registry(profile)

    assert not df.empty
    assert len(df) == 16
    assert "scope_name" in df.columns
    assert (df["non_signal"] == True).all()
    assert (df["local_only"] == True).all()
    assert summary["included_scopes_count"] == 8
    assert summary["excluded_scopes_count"] == 8
    assert summary["total_scopes"] == 16
    assert len(SCOPES) == 16
