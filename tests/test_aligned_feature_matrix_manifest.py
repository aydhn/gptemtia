"""Unit tests for Phase 119 aligned feature matrix manifests."""

import pytest
import pandas as pd
from advanced_cross_asset_alignment.aligned_feature_matrix_manifest import (
    create_aligned_feature_matrix_manifest,
    build_aligned_feature_matrix_manifest,
    build_aligned_feature_matrix_manifest_registry,
)


def test_create_manifest():
    manifest = create_aligned_feature_matrix_manifest(
        matrix_name="test_mat",
        base_domain="fx",
        aligned_domains=["macro"],
        row_count=50,
        feature_count=5,
        join_policy="join_policy_asof_backward",
    )
    assert manifest.source_preserved is True
    assert manifest.non_signal is True
    assert manifest.contains_target_or_prediction is False


def test_build_manifest_registry():
    df, summary = build_aligned_feature_matrix_manifest()
    assert len(df) == 2
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True
    assert summary["all_no_target_or_prediction"] is True
    assert summary["status"] == "READY"

    # Alias check
    df2, s2 = build_aligned_feature_matrix_manifest_registry()
    assert len(df2) == 2
    assert s2["all_non_signal"] is True
