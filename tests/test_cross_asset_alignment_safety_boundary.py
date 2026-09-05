"""Unit tests for Phase 119 safety boundary conditions (31 No-Go, 15 Safe-Go)."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_asset_alignment_safety_boundary import (
    build_cross_asset_alignment_no_go_conditions,
    build_cross_asset_alignment_safe_go_conditions,
    build_cross_asset_alignment_safety_boundary,
    NO_GO_ITEMS,
    SAFE_GO_ITEMS,
)


def test_no_go_conditions_count():
    assert len(NO_GO_ITEMS) == 31
    df = build_cross_asset_alignment_no_go_conditions()
    assert len(df) == 31
    assert bool(df["enforced"].all()) is True


def test_safe_go_conditions_count():
    assert len(SAFE_GO_ITEMS) == 15
    df = build_cross_asset_alignment_safe_go_conditions()
    assert len(df) == 15
    assert bool(df["enabled"].all()) is True


def test_safety_boundary_summary():
    df, summary = build_cross_asset_alignment_safety_boundary()
    assert len(df) == 46
    assert summary["no_go_count"] == 31
    assert summary["safe_go_count"] == 15
    assert summary["all_no_go_enforced"] is True
    assert summary["all_safe_go_enabled"] is True
    assert summary["safety_status"] == "SECURE"
