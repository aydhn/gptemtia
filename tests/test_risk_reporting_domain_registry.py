# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Reporting Domain Registry."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_domain_registry import build_risk_reporting_domain_registry


def test_build_risk_reporting_domain_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_domain_registry(profile)

    assert not df.empty
    assert len(df) >= 4
    assert summary["domain_count"] >= 4
    assert "domain_name" in df.columns
    assert "status" in df.columns
    assert (df["status"] == "active").all()
