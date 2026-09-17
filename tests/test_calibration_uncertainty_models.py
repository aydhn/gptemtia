# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Models."""

from advanced_calibration_uncertainty.calibration_uncertainty_models import (
    ProbabilityCalibrationContract,
    UncertaintyEstimationContract,
    CalibrationMethodPlaceholder,
    UncertaintyMethodPlaceholder,
    CalibrationUncertaintyManifest,
    CalibrationUncertaintyFinding,
    CalibrationUncertaintyReadinessScore,
)


def test_contract_models_defaults():
    cal = ProbabilityCalibrationContract(
        contract_name="test_cal",
        calibration_method_family="test_family",
        candidate_model_contract_ref="cand_ref",
        ensemble_contract_ref="ens_ref",
        dataset_contract_ref="ds_ref",
        experiment_registry_ref="exp_ref",
        required_no_lookahead_guard_ref="nl_ref",
        required_metadata_only_news_guard_ref="mn_ref",
        required_source_preservation_guard_ref="sp_ref",
        required_validation_dependency_ref="val_ref",
        required_quality_dependency_ref="qual_ref",
    )
    assert cal.contract_name == "test_cal"
    assert cal.probability_prediction_allowed is False
    assert cal.calibration_fit_allowed is False
    assert cal.calibration_transform_allowed is False
    assert cal.non_signal_required is True

    unc = UncertaintyEstimationContract(
        contract_name="test_unc",
        uncertainty_method_family="test_family",
        candidate_model_contract_ref="cand_ref",
        ensemble_contract_ref="ens_ref",
        calibration_contract_ref="cal_ref",
        dataset_contract_ref="ds_ref",
        required_no_lookahead_guard_ref="nl_ref",
        required_metadata_only_news_guard_ref="mn_ref",
        required_source_preservation_guard_ref="sp_ref",
    )
    assert unc.contract_name == "test_unc"
    assert unc.uncertainty_estimation_allowed is False
    assert unc.prediction_interval_allowed is False
    assert unc.non_signal_required is True


def test_manifest_model():
    man = CalibrationUncertaintyManifest(manifest_name="test_manifest")
    assert man.current_phase == 141
    assert man.next_phase == 142
    assert man.probability_prediction_executed is False
    assert man.uncertainty_estimation_executed is False
    assert man.real_training_executed is False
    assert man.non_signal is True
