# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Limit Monitoring Contracts."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.limit_monitoring_contracts import build_limit_monitoring_contract_registry


def test_build_limit_monitoring_contract_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_limit_monitoring_contract_registry(profile)

    assert not df.empty
    assert len(df) >= 8
    assert summary["contract_count"] >= 8
    assert summary["all_contracts_placeholder"] is True
    assert summary["zero_live_enforcement"] is True
    assert summary["zero_alerting_allowed"] is True
    assert "contract_name" in df.columns
    assert "limit_family" in df.columns
    assert "allows_execution" in df.columns
    assert (df["allows_execution"] == False).all()
