# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Validation."""

import pytest
from advanced_explainability_attribution.explainability_validation import validate_explainability_layer


def test_explainability_validation():
    val = validate_explainability_layer()
    assert val["status"] == "PASS"
    assert val["all_passed"] is True
    assert val["current_phase"] == 143
    assert val["next_phase"] == 144
