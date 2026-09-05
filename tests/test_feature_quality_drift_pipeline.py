"""Tests for advanced_feature_quality_drift.feature_quality_drift_pipeline."""

import pytest
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_pipeline import (
    FeatureQualityDriftPipeline,
)
from advanced_feature_quality_drift.feature_quality_drift_config import (
    get_default_feature_quality_drift_profile,
)


def test_feature_quality_drift_pipeline_init():
    pipe = FeatureQualityDriftPipeline()
    assert pipe.profile.name == "balanced_local_feature_quality_drift"
    assert pipe.profile.current_phase == 123
    assert pipe.profile.target_final_phase == 160
    assert pipe.profile.next_phase == 124


def test_pipeline_build_profiles_domains_metrics_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_profiles_domains_metrics(save=False)
    assert "profiles" in tables
    assert "domains" in tables
    assert "quality_metrics" in tables
    assert "drift_metrics" in tables
    assert "quality_thresholds" in tables
    assert "drift_thresholds" in tables
    assert "quality_contracts" in tables
    assert "drift_contracts" in tables
    assert summaries["profiles"]["total_profiles"] == 3


def test_pipeline_build_quality_diagnostics_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_quality_diagnostics(save=False)
    assert "missingness" in tables
    assert "infinite_values" in tables
    assert "all_nan" in tables
    assert "zero_variance" in tables
    assert "duplicates" in tables
    assert "distribution_summary" in tables
    assert "staleness" in tables
    assert "namespace" in tables


def test_pipeline_build_drift_diagnostics_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_drift_diagnostics(save=False)
    assert "distribution_drift" in tables
    assert "rolling_stability" in tables


def test_pipeline_build_factor_quality_drift_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_factor_quality_drift(save=False)
    assert "factor_family_quality" in tables
    assert "factor_family_drift" in tables
    assert "factor_availability" in tables
    assert "factor_dependency_quality" in tables


def test_pipeline_build_macro_cross_asset_quality_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_macro_cross_asset_quality(save=False)
    assert "macro_calendar_news_quality" in tables
    assert "cross_asset_feature_quality" in tables


def test_pipeline_build_findings_scoring_manifest_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_findings_scoring_manifest(save=False)
    assert "quality_findings" in tables
    assert "drift_findings" in tables
    assert "quality_manual_review" in tables
    assert "drift_manual_review" in tables
    assert "quality_score" in tables
    assert "drift_score" in tables
    assert "manifest" in tables


def test_pipeline_build_health_validation_safety_handoff_no_save():
    pipe = FeatureQualityDriftPipeline()
    tables, summaries = pipe.build_health_validation_safety_handoff(save=False)
    assert "health_check" in tables
    assert "validation_report" in tables
    assert "safety_boundary" in tables
    assert "phase_124_handoff" in tables


def test_pipeline_build_feature_quality_drift_status_no_save():
    pipe = FeatureQualityDriftPipeline()
    df, summary = pipe.build_feature_quality_drift_status(save=False)
    assert not df.empty
    assert summary["total_subsystems"] == 35
    assert summary["passed_subsystems"] == 35
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
