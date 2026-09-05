"""Unit tests for Phase 119 feature matrix join policies."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.feature_matrix_join_policies import (
    build_feature_matrix_join_policy_registry,
    JOIN_POLICIES_CATALOG,
)


def test_join_policies_catalog():
    assert len(JOIN_POLICIES_CATALOG) == 5
    df, summary = build_feature_matrix_join_policy_registry()
    assert len(df) == 5
    assert summary["total_policies"] == 5
    assert summary["all_backward_direction"] is True
    assert summary["non_signal"] is True
    assert summary["status"] == "READY"


def test_join_direction_strict():
    df, _ = build_feature_matrix_join_policy_registry()
    for _, row in df.iterrows():
        assert row["direction"] in ["backward", "exact", "bucket", "link"]
        assert row["direction"] != "forward"
        assert row["direction"] != "nearest"
