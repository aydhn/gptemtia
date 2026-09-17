# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Reporting Profile Registry."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.risk_reporting_profile_registry import build_risk_reporting_profile_registry


def test_build_risk_reporting_profile_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert summary["profile_count"] >= 3
    assert summary["active_profile"] == profile.profile_name
    assert summary["all_profiles_non_production"] is True
    assert "profile_name" in df.columns
    assert "current_phase" in df.columns
    assert (df["current_phase"] == 155).all()
