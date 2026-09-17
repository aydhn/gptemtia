# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Backtest Execution Disabled Report."""

from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_execution_disabled import (
    build_backtest_execution_disabled_report,
    validate_no_backtest_execution_request,
)


def test_build_execution_disabled_report():
    prof = get_default_realistic_backtest_profile()
    df, summary = build_backtest_execution_disabled_report(prof)
    assert not df.empty
    assert summary["is_blocked"] is True
    assert summary["policy_active"] is True
    assert summary["non_signal"] is True
    assert (df["is_blocked"] == True).all()


def test_validate_no_backtest_execution_request():
    res_clean = validate_no_backtest_execution_request("inspect_contracts")
    assert res_clean["permitted"] is True

    res_blocked = validate_no_backtest_execution_request("run_backtest")
    assert res_blocked["permitted"] is False
