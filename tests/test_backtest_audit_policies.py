# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Audit Policies."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_audit_policies import (
    build_backtest_audit_policy_registry,
    AUDIT_POLICIES,
)


def test_build_backtest_audit_policies():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_audit_policy_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "policy_id" in df.columns
    assert "name" in df.columns
    assert (df["status"] == "ACTIVE").all()
    assert (df["non_signal"] == True).all()
    assert (df["local_only"] == True).all()
    assert summary["total_policies"] == 3
    assert len(AUDIT_POLICIES) == 3
