# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Health Checks."""

from advanced_ensemble_model_registry.ensemble_model_health import (
    check_ensemble_model_health,
    validate_ensemble_model_health_report,
    summarize_ensemble_model_health_report,
)


def test_ensemble_model_health():
    health = check_ensemble_model_health()
    assert health["status"] == "HEALTHY"
    assert health["passed_checks"] == health["total_checks"]
    assert health["non_signal"] is True
    assert validate_ensemble_model_health_report(health) is True

    summary = summarize_ensemble_model_health_report(health)
    assert summary["all_passed"] is True
