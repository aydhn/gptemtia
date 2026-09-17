# -*- coding: utf-8 -*-
"""Unit tests for Phase 143 Explainability Health."""

import pytest
from advanced_explainability_attribution.explainability_health import check_explainability_health


def test_explainability_health():
    health = check_explainability_health()
    assert health["status"] == "healthy"
    assert health["is_healthy"] is True
    assert health["failed_checks"] == 0
    assert health["current_phase"] == 143
    assert health["next_phase"] == 144
