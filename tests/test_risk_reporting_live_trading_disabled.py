# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Reporting Live Trading Disabled."""

import pandas as pd
from advanced_risk_reporting.risk_reporting_live_trading_disabled import (
    build_risk_reporting_live_trading_disabled_report,
    validate_no_risk_reporting_live_trading_request,
)
from advanced_risk_reporting.risk_reporting_config import RiskReportingProfile


def test_build_risk_reporting_live_trading_disabled_report_default():
    df, summary = build_risk_reporting_live_trading_disabled_report()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]["component_name"] == "live_trading_engine"
    assert bool(df.iloc[0]["is_disabled"]) is True
    assert df.iloc[0]["status"] == "execution_contract_only"
    assert summary["is_disabled"] is True
    assert summary["status"] == "execution_blocked_no_live_trading"


def test_build_risk_reporting_live_trading_disabled_report_custom_profile():
    profile = RiskReportingProfile(
        profile_name="test_profile",
        description="test description",
        current_phase=155,
        target_final_phase=160,
        next_phase=156,
        non_production=True,
    )
    df, summary = build_risk_reporting_live_trading_disabled_report(profile=profile)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]["current_phase"] == 155
    assert df.iloc[0]["target_final_phase"] == 160
    assert df.iloc[0]["next_phase"] == 156


def test_validate_no_risk_reporting_live_trading_request_safe():
    request_str = "Run a historical backtest."
    result = validate_no_risk_reporting_live_trading_request(request_str)
    assert result["is_blocked"] is False
    assert result["is_safe"] is True
    assert result["action"] == "ALLOW"
    assert result["reason"] == "No violation"


def test_validate_no_risk_reporting_live_trading_request_prohibited_string():
    request_str = "Please LIVE_TRADE the following signals."
    result = validate_no_risk_reporting_live_trading_request(request_str)
    assert result["is_blocked"] is True
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
    assert result["reason"] == "Live trading strictly prohibited"


def test_validate_no_risk_reporting_live_trading_request_prohibited_dict():
    request_dict = {"instruction": "place_order for AAPL", "amount": 100}
    result = validate_no_risk_reporting_live_trading_request(request_dict)
    assert result["is_blocked"] is True
    assert result["is_safe"] is False
    assert result["action"] == "BLOCK"
    assert result["reason"] == "Live trading strictly prohibited"
