# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Robustness Master Pipeline."""

from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_pipeline import MonteCarloRobustnessPipeline


def test_pipeline_dry_run_no_save():
    profile = get_default_monte_carlo_profile()
    pipeline = MonteCarloRobustnessPipeline(profile=profile)

    res = pipeline.run_pipeline(save=False)
    assert res["status"] == "PHASE_149_COMPLETED_READY_FOR_PHASE_150"
    assert res["current_phase"] == 149
    assert res["next_phase"] == 150
    assert res["all_negative_invariants_satisfied"] is True
    assert res["validation_status"] == "PASS"
    assert res["phase_150_handoff_ready"] is True


def test_pipeline_individual_steps():
    profile = get_default_monte_carlo_profile()
    pipeline = MonteCarloRobustnessPipeline(profile=profile)

    _, s1 = pipeline.build_profiles_and_scopes(save=False)
    assert s1["profiles"]["status"] == "monte_carlo_contract_ready"

    _, s2 = pipeline.build_robustness_and_bootstrap_contracts(save=False)
    assert s2["core"]["all_contracts_valid"] is True

    _, s3 = pipeline.build_resampling_and_perturbations(save=False)
    assert s3["residuals"]["all_unexecuted"] is True

    _, s4 = pipeline.build_parameter_stability_and_sensitivity(save=False)
    assert s4["stability"]["all_valid"] is True

    _, s5 = pipeline.build_envelopes_and_distributions(save=False)
    assert s5["envelope"]["all_uncalculated"] is True

    _, s6 = pipeline.build_dependencies_and_linkages(save=False)
    assert s6["stress"]["all_satisfied"] is True

    _, s7 = pipeline.build_io_contracts_and_metrics(save=False)
    assert s7["inputs"]["all_valid"] is True

    _, s8 = pipeline.build_guards_and_disabled_reports(save=False)
    assert s8["guards"]["all_active"] is True

    _, s9 = pipeline.build_findings_scoring_manifest(save=False)
    assert s9["scoring"]["meets_threshold"] is True

    _, s10 = pipeline.build_health_validation_safety_handoff(save=False)
    assert s10["validation"]["all_passed"] is True
    assert s10["handoff"]["phase_150_handoff_ready"] is True

    df_stat, s_stat = pipeline.build_monte_carlo_status(save=False)
    assert not df_stat.empty
    assert s_stat["all_components_ready"] is True
