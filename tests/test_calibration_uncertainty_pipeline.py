# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Pipeline."""

from advanced_calibration_uncertainty.calibration_uncertainty_pipeline import (
    CalibrationUncertaintyPipeline,
    run_calibration_uncertainty_pipeline,
)


def test_pipeline_execution():
    res = run_calibration_uncertainty_pipeline()
    assert res["phase"] == 141
    assert res["next_phase"] == 142
    assert res["target_final_phase"] == 160
    assert res["calibration_contract_count"] >= 5
    assert res["uncertainty_contract_count"] >= 5
    assert res["health_status"] == "HEALTHY"
    assert res["validation_status"] == "VALID"
    assert res["readiness_score"] >= 0.85
    assert res["non_signal"] is True
    assert res["dry_run"] is True
