# -*- coding: utf-8 -*-
"""Unit tests for Limit Monitoring Output Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.limit_monitoring_output_contracts import build_limit_monitoring_output_contract_registry


def test_build_limit_monitoring_output_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_limit_monitoring_output_contract_registry(profile)

    assert not df.empty
    assert summary["output_contract_count"] >= 1
    assert summary["status"] == "limit_monitoring_contract_ready"
    assert (df["actual_breach_detected"] == False).all()
    assert (df["live_alert_dispatched"] == False).all()
