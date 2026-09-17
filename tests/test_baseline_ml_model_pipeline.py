# -*- coding: utf-8 -*-
"""Unit tests for baseline ML model pipeline."""

import pytest
import pandas as pd
from advanced_baseline_ml_models.baseline_ml_model_pipeline import (
    BaselineMlModelPipeline,
    run_baseline_ml_model_pipeline,
)


def test_baseline_ml_model_pipeline_steps():
    pipeline = BaselineMlModelPipeline()

    # Step 1: Profiles, domains, families
    t1, s1 = pipeline.build_profiles_domains_families(save=False)
    assert len(t1["profiles"]) == 3
    assert len(t1["domains"]) == 37
    assert len(t1["model_families"]) == 10

    # Step 2: Model contracts
    t2, s2 = pipeline.build_model_contracts(save=False)
    assert len(t2["model_contracts"]) == 10
    assert len(t2["input_contracts"]) == 3
    assert len(t2["output_contracts"]) == 10

    # Step 3: Dry run harness
    t3, s3 = pipeline.build_dry_run_harness(save=False)
    assert len(t3["training_plans"]) == 10
    assert len(t3["harness_contracts"]) == 5
    assert len(t3["harness_interfaces"]) == 15
    assert len(t3["trainer_stubs"]) == 10
    assert len(t3["dry_run_policies"]) == 6

    # Step 4: Disabled execution reports
    t4, s4 = pipeline.build_disabled_execution_reports(save=False)
    assert len(t4) == 5

    # Step 5: Placeholders and dependencies
    t5, s5 = pipeline.build_placeholders_dependencies_inputs(save=False)
    assert len(t5["metric_placeholders"]) == 8
    assert len(t5["evaluation_placeholders"]) == 7
    assert len(t5["validation_dependencies"]) == 6
    assert len(t5["quality_dependencies"]) == 5
    assert len(t5["lineage"]) == 5
    assert len(t5["forbidden_columns"]) == 23

    # Step 6: Findings, scoring, manifest
    t6, s6 = pipeline.build_findings_scoring_manifest(save=False)
    assert len(t6["findings"]) == 0
    assert len(t6["manual_review"]) == 5
    assert len(t6["scoring"]) == 1
    assert len(t6["manifest"]) == 1

    # Step 7: Health, validation, safety, handoff
    t7, s7 = pipeline.build_health_validation_safety_handoff(save=False)
    assert s7["validation"]["all_passed"] is True
    assert s7["handoff"]["all_satisfied"] is True


def test_baseline_ml_model_pipeline_status():
    pipeline = BaselineMlModelPipeline()
    status_df, summary = pipeline.build_baseline_ml_model_status(save=False)

    assert isinstance(status_df, pd.DataFrame)
    assert len(status_df) == 18
    assert summary["current_phase"] == 138
    assert summary["next_phase"] == 139
    assert summary["target_final_phase"] == 160
    assert summary["all_components_ready"] is True
    assert summary["real_training_executed"] is False
    assert summary["model_fit_executed"] is False
    assert summary["model_predict_executed"] is False
    assert summary["target_label_generated"] is False
    assert summary["artifact_persisted"] is False
    assert summary["model_registry_written"] is False
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False


def test_run_baseline_ml_model_pipeline():
    result = run_baseline_ml_model_pipeline(save=False)
    assert result["pipeline_status"] == "READY"
    assert result["current_phase"] == 138
    assert result["next_phase"] == 139
    assert result["target_final_phase"] == 160
    assert result["real_training_executed"] is False
    assert result["predictions_executed"] is False
    assert result["phase_139_handoff_ready"] is True
