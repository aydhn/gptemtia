# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Model Training Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_model_training_disabled import (
    build_backtest_model_training_disabled_report,
    validate_no_backtest_model_training_request,
)


def test_build_backtest_model_training_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_model_training_disabled_report(profile)

    assert not df.empty
    assert len(df) >= 3
    assert (df["training_permitted"] == False).all()
    assert summary["all_model_training_disabled"] is True


def test_validate_no_backtest_model_training_request():
    blocked = validate_no_backtest_model_training_request("train_model on dataset splits")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_backtest_model_training_request("verify model registry metadata")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
