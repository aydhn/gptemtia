# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Output Contracts."""

import pytest
from advanced_explainability_attribution.attribution_output_contracts import (
    build_attribution_output_contract_registry,
    summarize_attribution_output_contracts,
)


def test_attribution_output_contracts():
    df, summary = build_attribution_output_contract_registry()
    assert len(df) == 8
    assert summary["all_no_signal"] is True
    assert summary["all_no_real_attribution"] is True
    assert summary["all_no_prediction"] is True
    assert summary["all_contract_only"] is True
