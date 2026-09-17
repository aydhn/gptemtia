# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Split Governance."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.split_governance import (
    build_split_governance_registry,
    SPLIT_RULES,
)


def test_build_split_governance():
    profile = get_default_backtest_governance_profile()
    df, summary = build_split_governance_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "rule_id" in df.columns
    assert "rule_name" in df.columns
    assert (df["execution_allowed"] == False).all()
    assert (df["status"] == "ACTIVE").all()
    assert summary["total_split_rules"] == 3
    assert summary["random_splits_prohibited"] is True
    assert len(SPLIT_RULES) == 3
