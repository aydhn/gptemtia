# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Portfolio Exposure Summary Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.portfolio_exposure_summary_contracts import build_portfolio_exposure_summary_contract_registry


def test_build_portfolio_exposure_summary_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_portfolio_exposure_summary_contract_registry(profile)

    assert not df.empty
    assert summary["summary_contract_count"] >= 1
    assert summary["all_placeholder"] is True
    assert summary["zero_calculated"] is True
    assert "contract_name" in df.columns
    assert "allows_execution" in df.columns
    assert (df["allows_execution"] == False).all()
