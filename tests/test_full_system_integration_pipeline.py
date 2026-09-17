# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Full System Integration Pipeline."""

import pytest
import pandas as pd
from unittest.mock import MagicMock
from advanced_full_system_integration.full_system_integration_pipeline import (
    FullSystemIntegrationPipeline,
)


def test_pipeline_methods_no_save():
    mock_dl = MagicMock()
    pipeline = FullSystemIntegrationPipeline(data_lake=mock_dl)

    # 1. Profiles, domains, scope
    dfs_pds, s_pds = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in dfs_pds
    assert "domains" in dfs_pds
    assert "scope" in dfs_pds
    assert s_pds["non_signal"] is True

    # 2. Components, dependencies, checkpoints
    dfs_cdc, s_cdc = pipeline.build_components_dependencies_checkpoints(save=False)
    assert "components" in dfs_cdc
    assert "dependencies" in dfs_cdc
    assert "checkpoints" in dfs_cdc
    assert s_cdc["non_signal"] is True

    # 3. Contracts, manifests, evidence
    dfs_cmv, s_cmv = pipeline.build_contract_manifest_validation_integration(save=False)
    assert "contracts" in dfs_cmv
    assert "manifests" in dfs_cmv
    assert "evidence" in dfs_cmv
    assert s_cmv["non_signal"] is True

    # 4. Boundaries, manual review
    dfs_bmr, s_bmr = pipeline.build_boundaries_manual_review(save=False)
    assert "safety" in dfs_bmr
    assert "non_production" in dfs_bmr
    assert "dry_run" in dfs_bmr
    assert "manual_review_gates" in dfs_bmr
    assert s_bmr["non_signal"] is True

    # 5. Acceptance rehearsal
    dfs_aar, s_aar = pipeline.build_advanced_acceptance_rehearsal(save=False)
    assert "rehearsal" in dfs_aar
    assert "checkpoints" in dfs_aar
    assert s_aar["non_signal"] is True

    # 6. Subsystem integrations
    dfs_sub, s_sub = pipeline.build_subsystem_integrations(save=False)
    assert len(dfs_sub) >= 10
    assert s_sub["non_signal"] is True

    # 7. Disabled execution reports
    dfs_dis, s_dis = pipeline.build_disabled_execution_reports(save=False)
    assert len(dfs_dis) == 13
    assert s_dis["non_signal"] is True

    # 8. Findings, scoring, manifest
    dfs_fsm, s_fsm = pipeline.build_findings_scoring_manifest(save=False)
    assert "blockers" in dfs_fsm
    assert "gaps" in dfs_fsm
    assert "warnings" in dfs_fsm
    assert "findings" in dfs_fsm
    assert "scoring" in dfs_fsm
    assert "manifest" in dfs_fsm
    assert s_fsm["non_signal"] is True


def test_pipeline_status():
    mock_dl = MagicMock()
    pipeline = FullSystemIntegrationPipeline(data_lake=mock_dl)
    status_df, summary = pipeline.build_full_system_integration_status(save=False)

    assert isinstance(status_df, pd.DataFrame)
    assert len(status_df) >= 8
    assert summary["readiness_score"] >= 0.50
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True
