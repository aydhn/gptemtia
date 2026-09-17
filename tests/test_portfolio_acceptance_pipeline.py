# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Pipeline."""

import pytest
import pandas as pd
from unittest.mock import MagicMock

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_pipeline import (
    PortfolioAcceptancePipeline,
)


def test_pipeline_methods_no_save():
    """Verify all pipeline sub-methods execute cleanly with save=False."""
    mock_dl = MagicMock()
    pipeline = PortfolioAcceptancePipeline(data_lake=mock_dl)

    # 1. build_profiles_domains_scope
    dfs, summary = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in dfs
    assert "domains" in dfs
    assert "scope" in dfs
    assert summary["non_signal"] is True

    # 2. build_components_checkpoints
    dfs_cmp, summary_cmp = pipeline.build_components_checkpoints(save=False)
    assert "components" in dfs_cmp
    assert "checkpoints" in dfs_cmp
    assert summary_cmp["non_signal"] is True

    # 3. build_phase_acceptance
    dfs_ph, summary_ph = pipeline.build_phase_acceptance(save=False)
    assert "phase_153" in dfs_ph
    assert "phase_154" in dfs_ph
    assert "phase_155" in dfs_ph
    assert "phase_156" in dfs_ph
    assert summary_ph["non_signal"] is True

    # 4. build_dependency_evidence
    dfs_dep, summary_dep = pipeline.build_dependency_evidence(save=False)
    assert "dependencies" in dfs_dep
    assert "evidence" in dfs_dep
    assert "safety_registry" in dfs_dep

    # 5. build_boundaries_gates
    dfs_bnd, summary_bnd = pipeline.build_boundaries_gates(save=False)
    assert "non_production_boundaries" in dfs_bnd
    assert "manual_review_gates" in dfs_bnd
    assert "go_no_go" in dfs_bnd

    # 6. build_blockers_gaps_warnings_findings
    dfs_fnd, summary_fnd = pipeline.build_blockers_gaps_warnings_findings(save=False)
    assert "blockers" in dfs_fnd
    assert "gaps" in dfs_fnd
    assert "warnings" in dfs_fnd
    assert "findings" in dfs_fnd

    # 7. build_scoring_manifest
    dfs_scr, summary_scr = pipeline.build_scoring_manifest(save=False)
    assert "scoring" in dfs_scr
    assert "manifest" in dfs_scr

    # 8. build_health_validation_safety_handoff
    dfs_hvs, summary_hvs = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in dfs_hvs
    assert "validation" in dfs_hvs
    assert "safety" in dfs_hvs
    assert "handoff" in dfs_hvs

    # Verify no save methods were called on mock DataLake
    mock_dl.save_portfolio_acceptance_profile_registry.assert_not_called()
    mock_dl.save_portfolio_acceptance_manifest.assert_not_called()


def test_pipeline_build_status_no_save():
    """Verify full end-to-end acceptance status pipeline with save=False."""
    mock_dl = MagicMock()
    pipeline = PortfolioAcceptancePipeline(data_lake=mock_dl)

    status_df, full_summary = pipeline.build_portfolio_acceptance_status(save=False)

    assert isinstance(status_df, pd.DataFrame)
    assert len(status_df) == 8
    assert (status_df["status"] == "READY").all()

    assert isinstance(full_summary, dict)
    assert full_summary["status"] == "ACCEPTED"
    assert full_summary["meets_threshold"] is True
    assert full_summary["handoff_ready"] is True
    assert full_summary["non_signal"] is True

    # No files should have been persisted through DataLake
    mock_dl.save_portfolio_acceptance_report.assert_not_called()
