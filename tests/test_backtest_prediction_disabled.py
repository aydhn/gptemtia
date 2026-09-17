# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Prediction Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_prediction_disabled import (
    build_backtest_prediction_disabled_report,
    validate_no_backtest_prediction_request,
)


def test_build_backtest_prediction_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_prediction_disabled_report(profile)

    assert not df.empty
    assert len(df) >= 3
    assert (df["prediction_permitted"] == False).all()
    assert summary["all_predictions_disabled"] is True


def test_validate_no_backtest_prediction_request():
    blocked = validate_no_backtest_prediction_request("predict next day return")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_backtest_prediction_request("inspect offline schema contracts")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
