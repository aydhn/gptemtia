# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Deployment Disabled."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_deployment_disabled import (
    build_backtest_deployment_disabled_report,
    validate_no_backtest_deployment_request,
)


def test_build_backtest_deployment_disabled():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_deployment_disabled_report(profile)

    assert not df.empty
    assert len(df) >= 3
    assert (df["deployment_permitted"] == False).all()
    assert summary["all_deployment_disabled"] is True


def test_validate_no_backtest_deployment_request():
    blocked = validate_no_backtest_deployment_request("trigger deploy_production pipeline")
    assert blocked["is_allowed"] is False
    assert blocked["is_blocked"] is True

    allowed = validate_no_backtest_deployment_request("run offline local unit tests")
    assert allowed["is_allowed"] is True
    assert allowed["is_blocked"] is False
