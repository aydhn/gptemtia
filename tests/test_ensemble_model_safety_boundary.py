# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Safety Boundary."""

import pytest
from advanced_ensemble_model_registry.ensemble_model_safety_boundary import (
    enforce_ensemble_model_safety_boundary,
    assert_ensemble_model_safety_boundary,
    summarize_ensemble_model_safety_boundary,
)


def test_ensemble_model_safety_boundary():
    safe_dict = {
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
        "real_training_executed": False,
        "model_predict_executed": False,
        "ensemble_executed": False,
        "calibration_executed": False,
        "artifact_persisted": False,
        "model_registry_written": False,
    }
    assert enforce_ensemble_model_safety_boundary(safe_dict) is True
    assert_ensemble_model_safety_boundary(safe_dict)

    unsafe_dict = dict(safe_dict, real_training_executed=True)
    assert enforce_ensemble_model_safety_boundary(unsafe_dict) is False
    with pytest.raises(ValueError):
        assert_ensemble_model_safety_boundary(unsafe_dict)

    summary = summarize_ensemble_model_safety_boundary()
    assert summary["enforced"] is True
    assert summary["phase"] == 140
