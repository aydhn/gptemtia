"""Test suite for Phase 139 GPU Training Governance Report Builder."""

import pandas as pd
from advanced_gpu_training_governance.gpu_training_governance_report_builder import (
    DISCLAIMER_TEXT,
    build_gpu_training_governance_disclaimer,
    build_gpu_training_governance_profile_markdown_report,
    build_gpu_training_resource_policy_markdown_report,
    build_gpu_training_harness_markdown_report,
    build_gpu_training_dry_run_guard_markdown_report,
    build_gpu_training_disabled_execution_markdown_report,
    build_gpu_training_dependency_markdown_report,
    build_gpu_training_audit_placeholder_markdown_report,
    build_gpu_training_findings_markdown_report,
    build_gpu_training_readiness_score_markdown_report,
    build_gpu_training_governance_manifest_markdown_report,
    build_gpu_training_governance_validation_markdown_report,
    build_gpu_training_governance_safety_markdown_report,
    build_phase_140_handoff_markdown_report,
)


def test_disclaimer_content():
    disc = build_gpu_training_governance_disclaimer()
    assert disc == DISCLAIMER_TEXT
    assert "YASAL UYARI VE GÜVENLİK SINIRI" in disc
    assert "Phase 139" in disc
    assert "Canlı emir, broker talimatı" in disc


def test_all_report_builders_contain_disclaimer():
    summary = {"active_profile": "balanced_local_gpu_governance", "non_signal": True}
    sample_df = pd.DataFrame([{"col1": "val1"}])

    builders = [
        build_gpu_training_governance_profile_markdown_report,
        build_gpu_training_resource_policy_markdown_report,
        build_gpu_training_harness_markdown_report,
        build_gpu_training_dry_run_guard_markdown_report,
        build_gpu_training_disabled_execution_markdown_report,
        build_gpu_training_dependency_markdown_report,
        build_gpu_training_audit_placeholder_markdown_report,
        build_gpu_training_findings_markdown_report,
        build_gpu_training_readiness_score_markdown_report,
        build_gpu_training_governance_manifest_markdown_report,
        build_gpu_training_governance_validation_markdown_report,
        build_gpu_training_governance_safety_markdown_report,
        build_phase_140_handoff_markdown_report,
    ]

    for builder in builders:
        report = builder(summary, sample_df)
        assert "YASAL UYARI VE GÜVENLİK SINIRI" in report
        assert "Phase 139" in report or "Phase 140" in report
