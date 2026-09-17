# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Component Registry."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_registry import (
    COMPONENTS,
    build_portfolio_acceptance_component_registry,
    summarize_portfolio_acceptance_components,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    COMPONENT_REGISTRY_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def test_component_registry_structure():
    """Verify component registry builds expected DataFrame and summary."""
    df, summary = build_portfolio_acceptance_component_registry()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(COMPONENTS)
    assert len(df) == 5  # Phases 153 to 157

    expected_cols = {
        "component_id",
        "component_name",
        "phase_number",
        "module_name",
        "description",
        "status",
        "current_phase",
    }
    assert expected_cols.issubset(df.columns)

    assert isinstance(summary, dict)
    assert summary["domain"] == COMPONENT_REGISTRY_DOMAIN
    assert summary["total_components"] == len(COMPONENTS)
    assert summary["all_contract_only"] is True
    assert summary["all_non_production"] is True
    assert summary["none_production_ready"] is True
    assert set(summary["phases_covered"]) == {153, 154, 155, 156, 157}
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY


def test_component_registry_custom_profile():
    """Verify registry with custom profile."""
    profile = get_portfolio_acceptance_profile()
    df, summary = build_portfolio_acceptance_component_registry(profile)

    assert (df["current_phase"] == 157).all()
    assert all(df["status"] == PORTFOLIO_ACCEPTANCE_READY)


def test_summarize_components_empty():
    """Verify summarizing empty df."""
    empty_df = pd.DataFrame()
    summary = summarize_portfolio_acceptance_components(empty_df)
    assert summary["total_components"] == 0
    assert summary["all_contract_only"] is True
