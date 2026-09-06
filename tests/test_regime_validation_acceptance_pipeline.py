"""Tests for Regime Validation Acceptance Pipeline."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)


def test_regime_validation_acceptance_pipeline():
    pipeline = RegimeValidationAcceptancePipeline()

    # Step 1: Profiles, domains, gates
    t_pg, s_pg = pipeline.build_profiles_domains_gates(save=False)
    assert "profiles" in t_pg
    assert "domains" in t_pg
    assert "gates" in t_pg
    assert s_pg["gates"]["all_passed"] is True

    # Step 2: Core acceptance reports
    t_core, s_core = pipeline.build_core_acceptance_reports(save=False)
    assert s_core["no_lookahead"]["lookahead_clean"] is True
    assert s_core["metadata_only_news"]["metadata_only_pure"] is True

    # Step 3: Absence reports
    t_abs, s_abs = pipeline.build_absence_acceptance_reports(save=False)
    assert s_abs["target_label_absence"]["all_absent"] is True
    assert s_abs["model_execution_absence"]["all_zero_execution"] is True

    # Step 4: Component acceptance reports
    t_comp, s_comp = pipeline.build_component_acceptance_reports(save=False)
    assert s_comp["matrix"]["all_passed"] is True
    assert s_comp["candidate_state"]["all_passed"] is True

    # Step 5: Dependency acceptance reports
    t_dep, s_dep = pipeline.build_dependency_acceptance_reports(save=False)
    assert s_dep["validation_dependencies"]["all_satisfied"] is True
    assert s_dep["quality_dependencies"]["all_satisfied"] is True

    # Step 6: Findings, scoring, manifest
    t_fsm, s_fsm = pipeline.build_findings_scoring_manifest(save=False)
    assert s_fsm["score"]["overall_score"] == 1.0
    assert s_fsm["manifest"]["manifest_valid"] is True

    # Step 7: Health, validation, safety, handoff
    t_hvs, s_hvs = pipeline.build_health_validation_safety_handoff(save=False)
    assert s_hvs["validation"]["status"] == "VALIDATION_PASS"
    assert s_hvs["handoff"]["handoff_status"] == "READY"

    # Step 8: Status summary
    df_status, s_status = pipeline.build_regime_validation_acceptance_status(save=False)
    assert not df_status.empty
    assert s_status["overall_status"] == "ACCEPTANCE_PASS"

    # Full pipeline dry run
    full_res = pipeline.run_full_pipeline(save=False)
    assert full_res["status"] == "ACCEPTANCE_PASS"
    assert full_res["current_phase"] == 133
    assert full_res["next_phase"] == 134
    assert full_res["non_signal"] is True
