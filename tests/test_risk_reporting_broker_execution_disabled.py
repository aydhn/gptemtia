# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Broker Execution Disabled Report."""

import pandas as pd
from advanced_risk_reporting.risk_reporting_broker_execution_disabled import (
    build_risk_reporting_broker_execution_disabled_report,
    validate_no_risk_reporting_broker_execution_request
)
from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile

def test_build_risk_reporting_broker_execution_disabled_report():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_broker_execution_disabled_report(profile)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "component_name" in df.columns
    assert "broker_execution_bridge" in df["component_name"].values
    assert df["is_disabled"].all()
    assert summary["is_disabled"] is True
    assert summary["status"] == "execution_blocked_no_broker"


def test_validate_no_risk_reporting_broker_execution_request_blocked():
    blocked_requests = [
        "connect_broker",
        {"intent": "broker_order"},
        "Connect to ibkr",
        "Send order to binance",
        "metatrader login"
    ]
    for req in blocked_requests:
        res = validate_no_risk_reporting_broker_execution_request(req)
        assert res["is_blocked"] is True
        assert res["is_safe"] is False
        assert res["action"] == "BLOCK"


def test_validate_no_risk_reporting_broker_execution_request_allowed():
    allowed_requests = [
        "generate risk report",
        {"intent": "fetch_data"},
        "calculate metrics",
        "show exposure attribution"
    ]
    for req in allowed_requests:
        res = validate_no_risk_reporting_broker_execution_request(req)
        assert res["is_blocked"] is False
        assert res["is_safe"] is True
        assert res["action"] == "ALLOW"
