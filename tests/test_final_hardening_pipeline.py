# -*- coding: utf-8 -*-
"""Unit tests for Phase 159 Final Hardening Pipeline."""

from advanced_final_hardening.final_hardening_pipeline import FinalHardeningPipeline
from advanced_final_hardening.final_hardening_labels import (
    FINAL_HARDENING_CONTRACT_READY,
    RELEASE_CANDIDATE_CONTRACT_READY,
)


def test_pipeline_methods():
    pipeline = FinalHardeningPipeline()

    tables, summary = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in tables
    assert summary["status"] == FINAL_HARDENING_CONTRACT_READY

    tables, summary = pipeline.build_final_hardening_contracts(save=False)
    assert "contracts" in tables
    assert summary["status"] == FINAL_HARDENING_CONTRACT_READY

    tables, summary = pipeline.build_freeze_audits(save=False)
    assert "config_freeze" in tables

    tables, summary = pipeline.build_inventory_reports(save=False)
    assert "scripts" in tables

    tables, summary = pipeline.build_release_candidate_checkpoints(save=False)
    assert "checklist" in tables

    tables, summary = pipeline.build_release_candidate_boundaries(save=False)
    assert "no_go" in tables

    tables, summary = pipeline.build_findings_scoring_manifest(save=False)
    assert "manifest" in tables
    assert summary["status"] == RELEASE_CANDIDATE_CONTRACT_READY

    tables, summary = pipeline.build_health_validation_safety_handoff(save=False)
    assert "validation" in tables
    assert summary["status"] == FINAL_HARDENING_CONTRACT_READY

    df_status, summary_status = pipeline.build_release_candidate_status(save=False)
    assert not df_status.empty
    assert summary_status["status"] == RELEASE_CANDIDATE_CONTRACT_READY
    assert summary_status["phase_160_handoff_ready"] is True
