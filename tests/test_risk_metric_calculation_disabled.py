# -*- coding: utf-8 -*-
"""Unit tests for Risk Metric Calculation Disabled Report."""

import pytest
import pandas as pd
from dataclasses import replace
from advanced_risk_reporting.risk_metric_calculation_disabled import (
    build_risk_metric_calculation_disabled_report,
    validate_no_risk_metric_calculation_request,
)
from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile

def test_build_risk_metric_calculation_disabled_report_default():
    """Test building report with default profile."""
    df, summary = build_risk_metric_calculation_disabled_report()
    assert not df.empty
    assert "is_disabled" in df.columns
    assert (df["is_disabled"] == True).all()
    assert "current_phase" in df.columns
    assert summary["is_disabled"] is True
    assert summary["status"] == "execution_blocked_no_metric_calculation"

def test_build_risk_metric_calculation_disabled_report_custom_profile():
    """Test building report with a specific profile."""
    profile = get_default_risk_reporting_profile()
    profile = replace(profile, current_phase="Phase_155")

    df, summary = build_risk_metric_calculation_disabled_report(profile)
    assert not df.empty
    assert (df["current_phase"] == "Phase_155").all()
    assert summary["is_disabled"] is True

def test_validate_no_risk_metric_calculation_request_allow():
    """Test validation allows safe requests."""
    safe_requests = [
        "get_portfolio_summary",
        {"action": "view_report"},
        "calculate_something_else",
        {"command": "status"},
    ]

    for req in safe_requests:
        res = validate_no_risk_metric_calculation_request(req)
        assert res["is_safe"] is True
        assert res["is_blocked"] is False
        assert res["action"] == "ALLOW"
        assert res["reason"] == "No violation"

def test_validate_no_risk_metric_calculation_request_block():
    """Test validation blocks prohibited requests."""
    blocked_requests = [
        "calculate_var",
        "please calculate_expected_shortfall",
        {"command": "calculate_volatility"},
        {"request": "calculate_drawdown"},
        "CALCULATE_METRIC for portfolio",
    ]

    for req in blocked_requests:
        res = validate_no_risk_metric_calculation_request(req)
        assert res["is_safe"] is False
        assert res["is_blocked"] is True
        assert res["action"] == "BLOCK"
        assert res["reason"] == "Risk metric calculation strictly disabled"
