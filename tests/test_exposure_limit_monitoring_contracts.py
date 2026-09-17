# -*- coding: utf-8 -*-
"""Unit tests for Exposure Limit Monitoring Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.exposure_limit_monitoring_contracts import build_exposure_limit_monitoring_contract_registry


def test_build_exposure_limit_monitoring_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_exposure_limit_monitoring_contract_registry(profile)

    assert not df.empty
    assert summary["contract_count"] >= 1
    assert summary["is_enforced_live"] is False
    assert (df["is_enforced_live"] == False).all()
    assert (df["allows_execution"] == False).all()
    assert (df["allows_alerting"] == False).all()
