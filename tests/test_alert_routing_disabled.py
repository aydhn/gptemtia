# -*- coding: utf-8 -*-
"""Unit tests for Alert Routing Disabled."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.alert_routing_disabled import build_alert_routing_disabled_registry


def test_build_alert_routing_disabled_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_alert_routing_disabled_registry(profile)

    assert not df.empty
    assert summary["is_disabled"] is True
    assert summary["component_count"] >= 1
    assert (df["is_disabled"] == True).all()
    assert (df["status"] == "execution_contract_only").all()
