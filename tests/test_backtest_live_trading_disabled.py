# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Live Trading Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_live_trading_disabled import (
    build_backtest_live_trading_disabled_report,
    validate_no_backtest_live_trading_request,
)


def test_build_backtest_live_trading_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_live_trading_disabled_report(profile)

    assert not df.empty
    assert len(df) >= 3
    assert (df["live_permitted"] == False).all()
    assert summary["all_live_trading_disabled"] is True


def test_validate_no_backtest_live_trading_request():
    blocked = validate_no_backtest_live_trading_request("place_order on exchange")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_backtest_live_trading_request("check offline data paths")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
