# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Governance Domain Registry."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_domain_registry import (
    build_backtest_governance_domain_registry,
    summarize_backtest_governance_domains,
    DOMAINS,
)


def test_build_backtest_governance_domain_registry():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_governance_domain_registry(profile)

    assert not df.empty
    assert len(df) == 27
    assert "domain_name" in df.columns
    assert (df["non_signal"] == True).all()
    assert (df["local_only"] == True).all()
    assert (df["execution_allowed"] == False).all()
    assert summary["all_non_signal"] is True
    assert summary["all_local_only"] is True
    assert len(DOMAINS) == 27
