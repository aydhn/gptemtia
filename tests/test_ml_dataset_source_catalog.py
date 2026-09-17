"""Test suite for Phase 137 ML Dataset Source Catalog."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_source_catalog import (
    build_ml_dataset_source_catalog_registry,
    summarize_ml_dataset_source_catalog,
)


def test_build_source_catalog():
    df, summary = build_ml_dataset_source_catalog_registry()
    assert not df.empty
    assert summary["total_sources"] >= 5
    assert summary["all_metadata_reference_only"] is True
    assert summary["materialized"] is False
