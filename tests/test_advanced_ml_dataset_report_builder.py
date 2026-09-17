"""Test suite for Phase 137 Advanced ML Dataset Report Builder."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_report_builder import (
    build_advanced_ml_dataset_profile_markdown_report,
    build_ml_dataset_contract_markdown_report,
    build_ml_dataset_schema_markdown_report,
    build_ml_dataset_split_policy_markdown_report,
    build_ml_dataset_guard_markdown_report,
    build_feature_snapshot_contract_markdown_report,
    build_ml_experiment_registry_markdown_report,
    build_ml_dataset_findings_markdown_report,
    build_ml_dataset_readiness_score_markdown_report,
    build_advanced_ml_dataset_manifest_markdown_report,
    build_advanced_ml_dataset_validation_markdown_report,
    build_advanced_ml_dataset_safety_markdown_report,
    build_phase_138_handoff_markdown_report,
    build_advanced_ml_dataset_disclaimer,
)


def test_reports_contain_mandatory_disclaimer():
    disclaimer = build_advanced_ml_dataset_disclaimer()
    assert "Phase 137 Advanced ML Dataset Contracts and Experiment Registry" in disclaimer
    assert "Canlı emir" in disclaimer

    r1 = build_advanced_ml_dataset_profile_markdown_report({"total_profiles": 3})
    assert disclaimer in r1

    r2 = build_ml_dataset_contract_markdown_report({"total_contracts": 8})
    assert disclaimer in r2

    r3 = build_advanced_ml_dataset_manifest_markdown_report({"current_phase": 137})
    assert disclaimer in r3

    r4 = build_phase_138_handoff_markdown_report({"handoff_status": "READY_FOR_PHASE_138"})
    assert disclaimer in r4
