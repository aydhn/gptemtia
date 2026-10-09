# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Overfitting Guards."""

from advanced_risk_reporting.risk_reporting_config import (
    get_default_risk_reporting_profile,
)
from advanced_risk_reporting.risk_reporting_overfitting_guards import (
    build_risk_reporting_overfitting_guard_registry,
)


def test_build_risk_reporting_overfitting_guard_registry():
    profile = get_default_risk_reporting_profile()

    df_og, s_og = build_risk_reporting_overfitting_guard_registry(profile)
    assert not df_og.empty
    assert s_og["all_active"] is True
    assert (df_og["is_active"]).all()
    assert s_og["guard_count"] == len(df_og)
    assert "risk_reporting_overfitting_guard" in df_og["guard_name"].values
    assert df_og["domain"].iloc[0] == "overfitting_guard"

    # Test default profile handling
    df_og_default, s_og_default = build_risk_reporting_overfitting_guard_registry(None)
    assert not df_og_default.empty
    assert s_og_default["guard_count"] == len(df_og_default)
