# -*- coding: utf-8 -*-
"""Unit tests for Monitoring Schedule Placeholders."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.monitoring_schedule_placeholders import build_monitoring_schedule_placeholder_registry


def test_build_monitoring_schedule_placeholder_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_monitoring_schedule_placeholder_registry(profile)

    assert not df.empty
    assert summary["is_disabled"] is True
    assert summary["component_count"] >= 1
    assert (df["is_disabled"] == True).all()
    assert (df["status"] == "execution_contract_only").all()
