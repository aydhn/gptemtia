import pytest
import pandas as pd
from pathlib import Path
from advanced_backtest_acceptance.backtest_acceptance_pipeline import BacktestAcceptancePipeline
from advanced_backtest_acceptance.backtest_acceptance_config import get_backtest_acceptance_profile

def test_backtest_acceptance_pipeline_dry_run():
    pipeline = BacktestAcceptancePipeline(project_root=Path("."))
    assert pipeline.profile is not None

    # Step 1: Profiles, domains, scope
    dfs_pds, s_pds = pipeline.build_profiles_domains_scope(save=False)
    assert "profiles" in dfs_pds
    assert "domains" in dfs_pds
    assert "scope" in dfs_pds
    assert s_pds["non_signal"] is True

    # Step 2: Components & checkpoints
    dfs_cmp, s_cmp = pipeline.build_components_checkpoints(save=False)
    assert "components" in dfs_cmp
    assert "checkpoints" in dfs_cmp
    assert s_cmp["non_signal"] is True

    # Step 3: Phase acceptance
    dfs_pha, s_pha = pipeline.build_phase_acceptance(save=False)
    assert len(dfs_pha) == 6
    assert s_pha["non_signal"] is True

    # Step 4: Dependency & evidence
    dfs_dep, s_dep = pipeline.build_dependency_evidence(save=False)
    assert "dependencies" in dfs_dep
    assert "evidence" in dfs_dep
    assert "safety_registry" in dfs_dep
    assert s_dep["non_signal"] is True

    # Step 5: Boundaries & gates
    dfs_bnd, s_bnd = pipeline.build_boundaries_gates(save=False)
    assert "non_production_boundaries" in dfs_bnd
    assert "manual_review_gates" in dfs_bnd
    assert "go_no_go" in dfs_bnd
    assert s_bnd["non_signal"] is True

    # Step 6: Blockers, gaps, warnings, findings
    dfs_bgwf, s_bgwf = pipeline.build_blockers_gaps_warnings_findings(save=False)
    assert "blockers" in dfs_bgwf
    assert "gaps" in dfs_bgwf
    assert "warnings" in dfs_bgwf
    assert "findings" in dfs_bgwf
    assert s_bgwf["non_signal"] is True

    # Step 7: Scoring & manifest
    dfs_scm, s_scm = pipeline.build_scoring_manifest(save=False)
    assert "scoring" in dfs_scm
    assert "manifest" in dfs_scm
    assert s_scm["non_signal"] is True

    # Step 8: Health, validation, safety, handoff
    dfs_hvsh, s_hvsh = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in dfs_hvsh
    assert "validation" in dfs_hvsh
    assert "safety" in dfs_hvsh
    assert "handoff" in dfs_hvsh
    assert s_hvsh["non_signal"] is True

    # Step 9: Consolidated status
    df_stat, s_stat = pipeline.build_backtest_acceptance_status(save=False)
    assert isinstance(df_stat, pd.DataFrame)
    assert s_stat["status"] == "ACCEPTED"
    assert s_stat["non_signal"] is True
    assert (df_stat["production_ready"] == False).all()
    assert (df_stat["broker_ready"] == False).all()
    assert (df_stat["live_trading_ready"] == False).all()
