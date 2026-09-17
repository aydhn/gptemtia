# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Result Release Boundaries."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_result_release_boundaries import (
    build_backtest_result_release_boundary_registry,
    RELEASE_BOUNDARIES,
)


def test_build_backtest_result_release_boundaries():
    profile = get_default_backtest_governance_profile()
    df, summary = build_backtest_result_release_boundary_registry(profile)

    assert not df.empty
    assert len(df) == 3
    assert "boundary_id" in df.columns
    assert (df["public_release_allowed"] == False).all()
    assert (df["marketing_release_allowed"] == False).all()
    assert summary["public_release_blocked"] is True
    assert len(RELEASE_BOUNDARIES) == 3
