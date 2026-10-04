# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting Portfolio Construction Dependencies Registry."""

import pandas as pd
from advanced_risk_reporting.risk_reporting_config import RiskReportingProfile
from advanced_risk_reporting.risk_reporting_portfolio_construction_dependencies import (
    build_risk_reporting_portfolio_construction_dependency_registry,
)


def test_build_risk_reporting_portfolio_construction_dependency_registry_default():
    """Test building the registry with the default profile."""
    df, summary = build_risk_reporting_portfolio_construction_dependency_registry()

    assert not df.empty
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1

    assert "dependency_name" in df.columns
    assert "source_phase" in df.columns
    assert "target_phase" in df.columns
    assert "contract_type" in df.columns
    assert "status" in df.columns
    assert "current_phase" in df.columns
    assert "target_final_phase" in df.columns
    assert "next_phase" in df.columns

    assert df.iloc[0]["dependency_name"] == "portfolio_construction_contracts_dependency"
    assert df.iloc[0]["source_phase"] == 153
    assert df.iloc[0]["target_phase"] == 155
    assert df.iloc[0]["contract_type"] == "portfolio_construction_spec"
    assert df.iloc[0]["status"] == "AVAILABLE_CONTRACT_ONLY"

    assert "dependency_count" in summary
    assert "is_satisfied" in summary
    assert summary["dependency_count"] == 1
    assert summary["is_satisfied"] is True


def test_build_risk_reporting_portfolio_construction_dependency_registry_custom():
    """Test building the registry with a custom profile."""
    custom_profile = RiskReportingProfile(
        profile_name="custom_test_profile",
        description="Custom profile for testing",
        current_phase=155,
        target_final_phase=160,
        next_phase=156,
        allow_live_trading=False,
    )

    df, summary = build_risk_reporting_portfolio_construction_dependency_registry(custom_profile)

    assert not df.empty
    assert isinstance(df, pd.DataFrame)

    assert df.iloc[0]["current_phase"] == 155
    assert df.iloc[0]["target_final_phase"] == 160
    assert df.iloc[0]["next_phase"] == 156

    assert summary["dependency_count"] == 1
    assert summary["is_satisfied"] is True
