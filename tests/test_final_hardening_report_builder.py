# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Report Builder."""

import pandas as pd
from advanced_final_hardening.final_hardening_report_builder import (
    build_final_hardening_disclaimer,
    build_final_hardening_profile_markdown_report,
    build_final_hardening_contract_markdown_report,
    build_operator_runbook_markdown_report,
    build_release_candidate_contract_markdown_report,
    build_final_freeze_markdown_report,
    build_final_inventory_markdown_report,
    build_operator_protocol_markdown_report,
    build_release_candidate_checkpoint_markdown_report,
    build_release_candidate_boundary_markdown_report,
    build_release_candidate_findings_markdown_report,
    build_release_candidate_readiness_score_markdown_report,
    build_release_candidate_manifest_markdown_report,
    build_final_hardening_validation_markdown_report,
    build_final_hardening_safety_markdown_report,
    build_phase_160_handoff_markdown_report,
    build_final_hardening_full_markdown_report,
)


def test_build_markdown_reports():
    df = pd.DataFrame([{"key": "val", "status": "OK"}])
    summary = {"total": 1, "status": "OK"}

    disc = build_final_hardening_disclaimer()
    assert "PHASE 159" in disc

    r1 = build_final_hardening_profile_markdown_report(summary, df)
    assert "Profile Registry Report" in r1

    r2 = build_final_hardening_contract_markdown_report(summary, df)
    assert "Contracts Report" in r2

    r3 = build_operator_runbook_markdown_report(summary, df)
    assert "Operator Runbook Contracts Report" in r3

    r4 = build_release_candidate_contract_markdown_report(summary, df)
    assert "Release Candidate Contracts Report" in r4

    r5 = build_final_freeze_markdown_report(summary, df)
    assert "Freeze Contracts Report" in r5

    r6 = build_final_inventory_markdown_report(summary, df)
    assert "Inventory Report" in r6

    r7 = build_operator_protocol_markdown_report(summary, df)
    assert "Operator Protocols Report" in r7

    r8 = build_release_candidate_checkpoint_markdown_report(summary, df)
    assert "Release Candidate Checkpoints Report" in r8

    r9 = build_release_candidate_boundary_markdown_report(summary, df)
    assert "Release Candidate Boundaries Report" in r9

    r10 = build_release_candidate_findings_markdown_report(summary, df)
    assert "Release Candidate Findings Report" in r10

    r11 = build_release_candidate_readiness_score_markdown_report(summary, df)
    assert "Release Candidate Readiness Score Report" in r11

    r12 = build_release_candidate_manifest_markdown_report(summary, df)
    assert "Release Candidate Manifest Report" in r12

    r13 = build_final_hardening_validation_markdown_report(summary, df)
    assert "Final Hardening Validation Report" in r13

    r14 = build_final_hardening_safety_markdown_report(summary, df)
    assert "Safety Boundary Report" in r14

    r15 = build_phase_160_handoff_markdown_report(summary, df)
    assert "Handoff Report" in r15

    r16 = build_final_hardening_full_markdown_report({"profiles": df}, summary)
    assert "Master Final Hardening" in r16
