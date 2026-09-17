# -*- coding: utf-8 -*-
"""Unit tests for Advanced ML Acceptance Pipeline."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_pipeline import (
    AdvancedMlAcceptancePipeline,
)


def test_pipeline_dry_run():
    pipeline = AdvancedMlAcceptancePipeline()

    # Test all stages with save=False (dry run without touching disk)
    dfs_prof, s_prof = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in dfs_prof
    assert s_prof["non_signal"] is True

    dfs_cmp, s_cmp = pipeline.build_components_checkpoints(save=False)
    assert "components" in dfs_cmp
    assert s_cmp["non_signal"] is True

    dfs_phase, s_phase = pipeline.build_phase_acceptance(save=False)
    assert "phase_136" in dfs_phase
    assert s_phase["non_signal"] is True

    dfs_dep, s_dep = pipeline.build_dependency_evidence(save=False)
    assert "dependencies" in dfs_dep

    dfs_bnd, s_bnd = pipeline.build_boundaries_gates(save=False)
    assert "non_production_boundaries" in dfs_bnd

    dfs_blk, s_blk = pipeline.build_blockers_gaps_warnings_findings(save=False)
    assert "findings" in dfs_blk

    dfs_scr, s_scr = pipeline.build_scoring_manifest(save=False)
    assert "scoring" in dfs_scr
    assert "manifest" in dfs_scr

    dfs_hlt, s_hlt = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in dfs_hlt
    assert "handoff" in dfs_hlt

    df_stat, s_stat = pipeline.build_advanced_ml_acceptance_status(save=False)
    assert not df_stat.empty
    assert s_stat["status"] == "ACCEPTED"
    assert s_stat["non_signal"] is True
