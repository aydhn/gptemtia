# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Input Contracts."""

import pytest
from advanced_explainability_attribution.attribution_input_contracts import (
    build_attribution_input_contract_registry,
    summarize_attribution_input_contracts,
)


def test_attribution_input_contracts():
    df, summary = build_attribution_input_contract_registry()
    assert len(df) >= 5
    assert summary["all_no_lookahead_enforced"] is True
    assert summary["all_metadata_only_enforced"] is True
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True
