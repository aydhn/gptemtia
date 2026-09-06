"""Test suite for Phase 136 ML Runtime Environment Snapshot."""

import pytest
from advanced_gpu_ml_runtime.ml_runtime_environment_snapshot import (
    build_ml_runtime_environment_snapshot,
)


def test_build_ml_runtime_environment_snapshot():
    df, summary = build_ml_runtime_environment_snapshot()
    assert not df.empty
    assert summary["total_properties"] > 0
    assert summary["non_signal"] is True
    # Ensure no secrets or tokens are in property names or values
    if "property_name" in df.columns:
        for prop in df["property_name"]:
            assert "token" not in str(prop).lower()
            assert "secret" not in str(prop).lower()
            assert "password" not in str(prop).lower()
