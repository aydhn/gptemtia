"""Unit tests for Phase 155 Risk Reporting Model Governance Dependencies."""

from unittest.mock import MagicMock

import pandas as pd

from advanced_risk_reporting.risk_reporting_config import (
    RiskReportingProfile,
    get_default_risk_reporting_profile,
)
from advanced_risk_reporting.risk_reporting_model_governance_dependencies import (
    build_risk_reporting_model_governance_dependency_registry,
)


def test_build_risk_reporting_model_governance_dependency_registry_default():
    """Test building the registry with the default profile."""
    df, summary = build_risk_reporting_model_governance_dependency_registry()

    assert not df.empty
    assert isinstance(df, pd.DataFrame)

    # Check default profile properties are mapped
    default_profile = get_default_risk_reporting_profile()
    assert (df["current_phase"] == default_profile.current_phase).all()
    assert (df["target_final_phase"] == default_profile.target_final_phase).all()
    assert (df["next_phase"] == default_profile.next_phase).all()

    # Check the actual rows
    assert "dependency_name" in df.columns
    assert "source_phase" in df.columns
    assert "target_phase" in df.columns
    assert "contract_type" in df.columns
    assert "status" in df.columns

    # Check summary
    assert isinstance(summary, dict)
    assert summary["dependency_count"] == len(df)
    assert summary["is_satisfied"] is True


def test_build_risk_reporting_model_governance_dependency_registry_explicit():
    """Test building the registry with an explicit mocked profile."""
    # Create a mock profile
    mock_profile = MagicMock(spec=RiskReportingProfile)
    mock_profile.current_phase = 144
    mock_profile.target_final_phase = 160
    mock_profile.next_phase = 145

    df, summary = build_risk_reporting_model_governance_dependency_registry(
        profile=mock_profile
    )

    assert not df.empty
    assert isinstance(df, pd.DataFrame)

    # Check mocked profile properties are mapped
    assert (df["current_phase"] == 144).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["next_phase"] == 145).all()

    # Check summary
    assert isinstance(summary, dict)
    assert summary["dependency_count"] == len(df)
    assert summary["is_satisfied"] is True
