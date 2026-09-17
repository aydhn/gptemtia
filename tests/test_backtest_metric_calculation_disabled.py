# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Metric Calculation Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_metric_calculation_disabled import (
    build_backtest_metric_calculation_disabled_report,
    validate_no_metric_calculation_request,
)


def test_build_backtest_metric_calculation_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_metric_calculation_disabled_report(profile)

    assert not df.empty
    assert len(df) == 4
    assert (df["calculation_permitted"] == False).all()
    assert summary["all_calculations_disabled"] is True
    assert summary["total_disabled_calculations"] == 4


def test_validate_no_metric_calculation_request():
    blocked = validate_no_metric_calculation_request("calculate_sharpe for gold strategy")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_metric_calculation_request("view metric definition schema")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
