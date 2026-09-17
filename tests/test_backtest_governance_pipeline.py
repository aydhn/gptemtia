# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Governance Pipeline."""

from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_pipeline import (
    BacktestGovernancePipeline,
)


def test_backtest_governance_pipeline_run():
    profile = get_default_backtest_governance_profile()
    pipeline = BacktestGovernancePipeline(profile=profile)

    # Test discrete steps with save=False
    dfs_prof, sums_prof = pipeline.build_profiles_and_scopes(save=False)
    assert "profiles" in dfs_prof
    assert "domains" in dfs_prof
    assert "scopes" in dfs_prof

    dfs_cntr, sums_cntr = pipeline.build_governance_contracts(save=False)
    assert "governance_contracts" in dfs_cntr

    dfs_bias, sums_bias = pipeline.build_bias_controls(save=False)
    assert "bias_contracts" in dfs_bias

    dfs_rep, sums_rep = pipeline.build_result_and_claim_boundaries(save=False)
    assert "result_reporting" in dfs_rep
    assert "metric_claim_boundaries" in dfs_rep

    dfs_real, sums_real = pipeline.build_realism_governance(save=False)
    assert "transaction_cost" in dfs_real
    assert "slippage" in dfs_real

    dfs_spl, sums_spl = pipeline.build_split_and_walk_forward_governance(save=False)
    assert "split" in dfs_spl

    dfs_str, sums_str = pipeline.build_stress_and_monte_carlo_governance(save=False)
    assert "stress_testing" in dfs_str

    dfs_aud, sums_aud = pipeline.build_audit_and_evidence_policies(save=False)
    assert "audit_policies" in dfs_aud

    dfs_gate, sums_gate = pipeline.build_manual_review_and_go_no_go(save=False)
    assert "manual_review_gates" in dfs_gate

    dfs_grd, sums_grd = pipeline.build_guards_and_disabled_reports(save=False)
    assert "exec_disabled" in dfs_grd

    dfs_find, sums_find = pipeline.build_findings_scoring_manifest(save=False)
    assert "scoring" in dfs_find
    assert "manifest" in dfs_find

    dfs_hlth, sums_hlth = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in dfs_hlth
    assert "validation" in dfs_hlth
    assert "safety" in dfs_hlth
    assert "handoff" in dfs_hlth

    # Test master run_pipeline with save=False
    result = pipeline.run_pipeline(save=False)
    assert result["current_phase"] == 150
    assert result["next_phase"] == 151
    assert result["target_final_phase"] == 160
    assert result["non_signal"] is True
    assert result["local_only"] is True
    assert result["all_negative_invariants_satisfied"] is True
    assert result["phase_151_handoff_ready"] is True
    assert result["status"] == "PHASE_150_COMPLETED_READY_FOR_PHASE_151"
