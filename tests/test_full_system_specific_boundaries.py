# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Specific Boundaries and Policies."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.non_live_signal_output_boundaries import (
    build_non_live_signal_output_boundary_registry,
)
from advanced_full_system_integration.no_broker_boundaries import (
    build_no_broker_boundary_registry,
)
from advanced_full_system_integration.no_live_trading_boundaries import (
    build_no_live_trading_boundary_registry,
)
from advanced_full_system_integration.no_investment_advice_boundaries import (
    build_no_investment_advice_boundary_registry,
)
from advanced_full_system_integration.no_production_deployment_boundaries import (
    build_no_production_deployment_boundary_registry,
)
from advanced_full_system_integration.no_model_registry_write_boundaries import (
    build_no_model_registry_write_boundary_registry,
)
from advanced_full_system_integration.no_artifact_persistence_boundaries import (
    build_no_artifact_persistence_boundary_registry,
)
from advanced_full_system_integration.no_scraping_boundaries import (
    build_no_scraping_boundary_registry,
)
from advanced_full_system_integration.source_preservation_boundaries import (
    build_source_preservation_boundary_registry,
)
from advanced_full_system_integration.metadata_only_news_boundaries import (
    build_metadata_only_news_boundary_registry,
)
from advanced_full_system_integration.forbidden_column_system_policies import (
    build_forbidden_column_system_policy_registry,
    validate_system_forbidden_columns,
    FORBIDDEN_COLUMNS,
)


def test_specific_boundary_builders():
    profile = get_default_full_system_integration_profile()

    builders = [
        build_non_live_signal_output_boundary_registry,
        build_no_broker_boundary_registry,
        build_no_live_trading_boundary_registry,
        build_no_investment_advice_boundary_registry,
        build_no_production_deployment_boundary_registry,
        build_no_model_registry_write_boundary_registry,
        build_no_artifact_persistence_boundary_registry,
        build_no_scraping_boundary_registry,
        build_source_preservation_boundary_registry,
        build_metadata_only_news_boundary_registry,
        build_forbidden_column_system_policy_registry,
    ]

    for builder in builders:
        df, summary = builder(profile)
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert summary["active_profile"] == profile.profile_name
        assert summary["status"] == "full_system_integration_ready"
        assert summary["non_signal"] is True


def test_forbidden_columns_validation():
    clean_cols = ["date", "open", "high", "low", "close", "volume"]
    res_clean = validate_system_forbidden_columns(clean_cols)
    assert res_clean["is_clean"] is True
    assert len(res_clean["forbidden_columns_found"]) == 0

    dirty_cols = ["date", "close", "signal", "live_signal", "target"]
    res_dirty = validate_system_forbidden_columns(dirty_cols)
    assert res_dirty["is_clean"] is False
    assert "signal" in res_dirty["forbidden_columns_found"]
    assert "live_signal" in res_dirty["forbidden_columns_found"]
    assert "target" in res_dirty["forbidden_columns_found"]
