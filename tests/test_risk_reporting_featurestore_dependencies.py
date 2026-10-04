# -*- coding: utf-8 -*-
"""Unit tests for Risk Reporting FeatureStore Dependencies."""

import pandas as pd
from advanced_risk_reporting.risk_reporting_config import (
    get_default_risk_reporting_profile,
)
from advanced_risk_reporting.risk_reporting_featurestore_dependencies import (
    build_risk_reporting_featurestore_dependency_registry,
)


def test_build_risk_reporting_featurestore_dependency_registry_default_profile():
    df, summary = build_risk_reporting_featurestore_dependency_registry()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == 1

    row = df.iloc[0]
    assert row["dependency_name"] == "featurestore_metadata_dependency"
    assert row["source_phase"] == 134
    assert row["target_phase"] == 155
    assert row["contract_type"] == "featurestore_catalog"
    assert row["status"] == "AVAILABLE_METADATA_ONLY"

    assert isinstance(summary, dict)
    assert summary["dependency_count"] == 1
    assert summary["is_satisfied"] is True

    profile = get_default_risk_reporting_profile()
    assert row["current_phase"] == profile.current_phase
    assert row["target_final_phase"] == profile.target_final_phase
    assert row["next_phase"] == profile.next_phase


def test_build_risk_reporting_featurestore_dependency_registry_explicit_profile():
    profile = get_default_risk_reporting_profile()
    df, summary = build_risk_reporting_featurestore_dependency_registry(profile=profile)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == 1

    row = df.iloc[0]
    assert row["dependency_name"] == "featurestore_metadata_dependency"
    assert row["current_phase"] == profile.current_phase

    assert isinstance(summary, dict)
    assert summary["dependency_count"] == 1
    assert summary["is_satisfied"] is True
