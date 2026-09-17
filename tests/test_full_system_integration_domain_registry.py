# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Domain Registry."""

import pytest
import pandas as pd
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.full_system_integration_domain_registry import (
    build_full_system_integration_domain_registry,
)


def test_domain_registry():
    profile = get_default_full_system_integration_profile()
    df, summary = build_full_system_integration_domain_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 10
    assert "domain_id" in df.columns
    assert "domain_name" in df.columns
    assert "layer" in df.columns
    assert "scope" in df.columns

    assert summary["active_profile"] == profile.profile_name
    assert summary["total_domains"] == len(df)
    assert summary["non_signal"] is True
