# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Broker Execution Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_broker_execution_disabled import (
    build_backtest_broker_execution_disabled_report,
    validate_no_backtest_broker_execution_request,
)


def test_build_backtest_broker_execution_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_broker_execution_disabled_report(profile)

    assert not df.empty
    assert len(df) >= 3
    assert (df["broker_permitted"] == False).all()
    assert summary["all_broker_execution_disabled"] is True


def test_validate_no_backtest_broker_execution_request():
    blocked = validate_no_backtest_broker_execution_request("connect to ibkr_client gateway")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_backtest_broker_execution_request("inspect mock broker contract models")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
