# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Report Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_report_contracts import build_risk_report_contract_registry


def test_build_risk_report_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_report_contract_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert summary["contract_count"] >= 8
    assert summary["all_contracts_disallow_live_trading"] is True
    assert summary["all_contracts_disallow_execution"] is True
    assert summary["manual_review_required_all"] is True
    assert "contract_name" in df.columns
    assert "live_trading_allowed" in df.columns
    assert (df["live_trading_allowed"] == False).all()
