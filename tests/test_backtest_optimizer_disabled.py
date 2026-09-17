# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Optimizer Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_optimizer_disabled import (
    build_backtest_optimizer_disabled_report,
    validate_no_backtest_optimizer_request,
)


def test_build_backtest_optimizer_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_optimizer_disabled_report(profile)

    assert not df.empty
    assert len(df) >= 3
    assert (df["optimization_permitted"] == False).all()
    assert summary["all_optimizers_disabled"] is True


def test_validate_no_backtest_optimizer_request():
    blocked = validate_no_backtest_optimizer_request("grid_search over parameter space")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_backtest_optimizer_request("inspect fixed parameter contracts")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
