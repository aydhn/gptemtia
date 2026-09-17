# -*- coding: utf-8 -*-
"""Unit tests for Phase 157 Portfolio Acceptance Profile Registry."""

import pandas as pd
from advanced_portfolio_acceptance.portfolio_acceptance_profile_registry import (
    build_portfolio_acceptance_profile_registry,
    summarize_portfolio_acceptance_profile_registry,
)


def test_profile_registry():
    df, summary = build_portfolio_acceptance_profile_registry()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert summary["total_profiles"] >= 3
    assert summary["all_dry_run"] is True
    assert summary["all_local_only"] is True
    assert summary["all_non_production"] is True
    assert summary["all_live_trading_disabled"] is True
