"""Test suite for Phase 135 Report Builder."""

import pandas as pd
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_acceptance_disclaimer,
    build_regime_acceptance_profile_markdown_report,
    build_regime_block_inventory_markdown_report,
    build_regime_block_dependency_markdown_report,
    build_regime_acceptance_gate_markdown_report,
    build_regime_acceptance_score_markdown_report,
    build_regime_manual_review_markdown_report,
    build_regime_compliance_markdown_report,
    build_regime_component_acceptance_markdown_report,
    build_regime_contract_markdown_report,
    build_regime_acceptance_manifest_markdown_report,
    build_regime_health_markdown_report,
    build_regime_validation_markdown_report,
    build_phase_136_handoff_markdown_report,
)


def test_disclaimer_present():
    disclaimer = build_regime_acceptance_disclaimer()
    assert "Phase 135" in disclaimer
    assert "Canlı emir" in disclaimer
    assert "kesin AL/SAT" in disclaimer


def test_all_markdown_reports():
    summary = {"active_profile": "test", "total_profiles": 3, "status": "READY"}
    df = pd.DataFrame([{"col": "val"}])

    r1 = build_regime_acceptance_profile_markdown_report(summary, df)
    assert "Phase 135" in r1
    assert "test" in r1

    r2 = build_regime_block_inventory_markdown_report({"total_modules": 10}, df)
    assert "Inventory" in r2

    r3 = build_regime_block_dependency_markdown_report({"total_dependency_steps": 10}, df)
    assert "Dependency" in r3

    r4 = build_regime_acceptance_gate_markdown_report({"total_gates": 17}, df)
    assert "Acceptance Gate" in r4

    r5 = build_regime_acceptance_score_markdown_report({"acceptance_score": 1.0}, df)
    assert "Acceptance Score" in r5

    r6 = build_regime_manual_review_markdown_report({"total_review_items": 1}, df)
    assert "Manual Review" in r6

    r7 = build_regime_compliance_markdown_report({"total_checks": 3}, df)
    assert "Compliance" in r7

    r8 = build_regime_component_acceptance_markdown_report({"total_components": 10}, df)
    assert "Component Acceptance" in r8

    r9 = build_regime_contract_markdown_report({"status": "READY"}, df)
    assert "Contract Audit" in r9

    r10 = build_regime_acceptance_manifest_markdown_report({"block_name": "Regime Block"}, df)
    assert "Manifest" in r10

    r11 = build_regime_health_markdown_report({"all_healthy": True}, df)
    assert "Health" in r11

    r12 = build_regime_validation_markdown_report({"all_passed": True}, df)
    assert "Validation" in r12

    r13 = build_phase_136_handoff_markdown_report({"source_phase": 135, "next_phase": 136}, df)
    assert "Phase 136" in r13
