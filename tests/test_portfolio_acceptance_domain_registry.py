# -*- coding: utf-8 -*-
"""Unit tests for Phase 157 Portfolio Acceptance Domain Registry."""

import pandas as pd
from advanced_portfolio_acceptance.portfolio_acceptance_domain_registry import (
    build_portfolio_acceptance_domain_registry,
)


def test_domain_registry():
    df, summary = build_portfolio_acceptance_domain_registry()
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 20
    assert summary["total_domains"] == len(df)
    assert (df["current_phase"] == 157).all()
