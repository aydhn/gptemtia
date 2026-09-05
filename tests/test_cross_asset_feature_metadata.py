"""Unit tests for Phase 119 cross-asset feature metadata."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.cross_asset_feature_metadata import build_cross_asset_feature_metadata_registry


def test_cross_asset_feature_metadata_registry():
    df, summary = build_cross_asset_feature_metadata_registry()
    assert len(df) == 6
    assert summary["total_features"] == 6
    assert summary["all_non_signal"] is True
    assert summary["all_lookahead_checked"] is True
    assert summary["status"] == "READY"

    domains = set(summary["domains"])
    assert "fx" in domains
    assert "commodity" in domains
    assert "macro" in domains
    assert "calendar" in domains
    assert "news" in domains
