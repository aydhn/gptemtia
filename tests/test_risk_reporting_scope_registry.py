# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Reporting Scope Registry."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_scope_registry import build_risk_reporting_scope_registry


def test_build_risk_reporting_scope_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_scope_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert summary["scope_count"] >= 3
    assert "scope_name" in df.columns
    assert "is_in_scope" in df.columns
    assert "non_production" in df.columns
    assert (df["non_production"] == True).all()
