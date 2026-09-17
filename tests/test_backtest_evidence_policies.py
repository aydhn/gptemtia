# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Evidence Policies."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_evidence_policies import (
    build_backtest_evidence_policy_registry,
    EVIDENCE_POLICIES,
)


def test_build_backtest_evidence_policies():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_evidence_policy_registry(profile)

    assert not df.empty
    assert len(df) == 4
    assert "evidence_id" in df.columns
    assert "name" in df.columns
    assert (df["status"] == "ACTIVE").all()
    assert (df["non_signal"] == True).all()
    assert summary["total_evidence_policies"] == 4
    assert len(EVIDENCE_POLICIES) == 4
