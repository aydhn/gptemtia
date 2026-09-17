# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Go/No-Go Decision Boundaries."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_go_no_go_boundaries import (
    build_backtest_go_no_go_boundary_registry,
    validate_backtest_go_no_go_request,
    GO_ACTIVITIES,
    NO_GO_ACTIVITIES,
)


def test_build_backtest_go_no_go_boundaries():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_go_no_go_boundary_registry(profile)

    assert not df.empty
    assert len(df) == 13
    assert "activity_name" in df.columns
    assert "category" in df.columns
    assert (df[df["category"] == "NO_GO"]["permitted"] == False).all()
    assert (df[df["category"] == "GO"]["permitted"] == True).all()
    assert summary["all_no_go_strictly_blocked"] is True
    assert len(GO_ACTIVITIES) == 3
    assert len(NO_GO_ACTIVITIES) == 10


def test_validate_backtest_go_no_go_request():
    blocked_req = validate_backtest_go_no_go_request("proceed with live_trade deployment")
    assert blocked_req["is_permitted"] is False
    assert blocked_req["is_blocked"] is True

    allowed_req = validate_backtest_go_no_go_request("verify contract completeness")
    assert allowed_req["is_permitted"] is True
    assert allowed_req["is_blocked"] is False
