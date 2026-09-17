# -*- coding: utf-8 -*-
"""Unit tests for Margin Exposure Placeholders."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.margin_exposure_placeholders import build_margin_exposure_placeholder_registry


def test_build_margin_exposure_placeholder_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_margin_exposure_placeholder_registry(profile)

    assert not df.empty
    assert summary["placeholder_count"] >= 1
    assert summary["is_calculated"] is False
    assert (df["is_placeholder"] == True).all()
    assert (df["is_calculated"] == False).all()
