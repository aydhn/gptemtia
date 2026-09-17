# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Manual Review Gates."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_manual_review_gates import (
    build_backtest_manual_review_gate_registry,
    REVIEW_GATES,
)


def test_build_backtest_manual_review_gates():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_manual_review_gate_registry(profile)

    assert not df.empty
    assert len(df) == 10
    assert "gate_name" in df.columns
    assert (df["requires_human_signoff"] == True).all()
    assert (df["auto_pass_prohibited"] == True).all()
    assert summary["all_require_human_signoff"] is True
    assert summary["total_gates"] == 10
    assert len(REVIEW_GATES) == 10
