# -*- coding: utf-8 -*-
"""Unit tests for Phase 147: Health Check, Validation, Safety Boundary, Handoff."""

from pathlib import Path
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_health import (
    build_walk_forward_health_check,
)
from advanced_walk_forward_validation.walk_forward_profile_registry import (
    build_walk_forward_profile_registry,
)
from advanced_walk_forward_validation.walk_forward_validation_contracts import (
    build_walk_forward_validation_contract_registry,
)
from advanced_walk_forward_validation.oos_benchmark_contracts import (
    build_oos_benchmark_contract_registry,
)
from advanced_walk_forward_validation.validation_no_lookahead_guards import (
    build_validation_no_lookahead_guard_registry,
)
from advanced_walk_forward_validation.walk_forward_manifest import (
    build_walk_forward_manifest,
)
from advanced_walk_forward_validation.walk_forward_validation import (
    build_walk_forward_validation_report,
    validate_no_forbidden_walk_forward_claims,
)
from advanced_walk_forward_validation.walk_forward_safety_boundary import (
    build_walk_forward_safety_boundary,
)
from advanced_walk_forward_validation.phase_148_handoff import (
    build_phase_148_stress_testing_scenario_simulation_handoff_report,
)


def test_health_check():
    prof = get_default_walk_forward_profile()
    project_root = Path(__file__).resolve().parent.parent
    df, summary = build_walk_forward_health_check(project_root, prof)
    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["status"] == "HEALTHY"


def test_validation_report():
    prof = get_default_walk_forward_profile()
    df_prof, _ = build_walk_forward_profile_registry(prof)
    df_wf, _ = build_walk_forward_validation_contract_registry(prof)
    df_bnch, _ = build_oos_benchmark_contract_registry(prof)
    df_grd, _ = build_validation_no_lookahead_guard_registry(prof)
    df_man, _ = build_walk_forward_manifest(prof)

    val_tables = {
        "profiles": df_prof,
        "walk_forward_contracts": df_wf,
        "oos_benchmark_contracts": df_bnch,
        "no_lookahead_guards": df_grd,
        "manifest": df_man,
    }

    df_val, s_val = build_walk_forward_validation_report(val_tables, prof)
    assert not df_val.empty
    assert s_val["all_passed"] is True
    assert s_val["validation_status"] == "PASS"

    claim_res = validate_no_forbidden_walk_forward_claims(text="This has a guaranteed_return")
    assert claim_res["is_valid"] is False


def test_safety_boundary():
    prof = get_default_walk_forward_profile()
    df, summary = build_walk_forward_safety_boundary(prof)
    assert not df.empty
    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] >= 10
    assert summary["safe_go_count"] >= 5


def test_phase_148_handoff():
    prof = get_default_walk_forward_profile()
    df, summary = build_phase_148_stress_testing_scenario_simulation_handoff_report(prof)
    assert not df.empty
    assert summary["status"] == "READY_FOR_PHASE_148"
    assert summary["source_phase"] == 147
    assert summary["next_phase"] == 148
    assert summary["all_prerequisites_satisfied"] is True
