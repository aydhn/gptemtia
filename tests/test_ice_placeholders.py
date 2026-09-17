# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 ICE Placeholders."""

import pytest
from advanced_explainability_attribution.ice_placeholders import (
    build_ice_placeholder_registry,
    summarize_ice_placeholders,
)


def test_ice_placeholders():
    df, summary = build_ice_placeholder_registry()
    assert len(df) >= 3
    assert summary["all_placeholder_only"] is True
    assert summary["all_ice_executed_false"] is True
    assert summary["all_non_signal"] is True
