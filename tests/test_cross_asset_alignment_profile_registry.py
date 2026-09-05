"""Unit tests for Phase 119 profile registry builder."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_asset_alignment_profile_registry import (
    build_cross_asset_alignment_profile_registry,
    summarize_cross_asset_alignment_profiles,
)
from advanced_cross_asset_alignment.cross_asset_alignment_config import get_default_cross_asset_alignment_profile


def test_build_profile_registry():
    profile = get_default_cross_asset_alignment_profile()
    df, summary = build_cross_asset_alignment_profile_registry(profile)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["current_phase"] == 119
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 120
    assert summary["local_only"] is True
    assert summary["research_only"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"


def test_profile_registry_columns():
    df, _ = build_cross_asset_alignment_profile_registry()
    required = ["profile_name", "current_phase", "target_final_phase", "next_phase", "dry_run_default", "non_signal", "local_only"]
    for col in required:
        assert col in df.columns
