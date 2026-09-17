# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Attribution Quality Gates."""

import pytest
from advanced_explainability_attribution.attribution_quality_gates import (
    build_attribution_quality_gate_registry,
    summarize_attribution_quality_gates,
)


def test_attribution_quality_gates():
    df, summary = build_attribution_quality_gate_registry()
    assert len(df) == 5
    assert summary["all_passed"] is True
    assert summary["all_contract_gate"] is True
    assert summary["all_non_signal"] is True
