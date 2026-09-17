# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Feature Store Explainability Linkage."""

import pytest
from advanced_explainability_attribution.featurestore_explainability_linkage import (
    build_featurestore_explainability_linkage_registry,
    summarize_featurestore_explainability_linkage,
)


def test_featurestore_explainability_linkage():
    df, summary = build_featurestore_explainability_linkage_registry()
    assert len(df) == 5
    assert summary["all_linkage_contract"] is True
    assert summary["all_no_lookahead_enforced"] is True
    assert summary["all_metadata_only_enforced"] is True
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True
