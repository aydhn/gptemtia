# -*- coding: utf-8 -*-
"""Unit tests for Attribution Metric Placeholders."""

from advanced_risk_reporting.risk_reporting_config import get_default_risk_reporting_profile
from advanced_risk_reporting.attribution_metric_placeholders import build_attribution_metric_placeholder_registry


def test_build_attribution_metric_placeholder_registry():
    profile = get_default_risk_reporting_profile()
    df, summary = build_attribution_metric_placeholder_registry(profile)

    assert not df.empty
    assert summary["metric_count"] >= 1
    assert summary["all_placeholder"] is True
    assert summary["zero_calculated"] is True
    assert (df["is_placeholder"] == True).all()
    assert (df["is_calculated"] == False).all()
