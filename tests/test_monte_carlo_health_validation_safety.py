# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Health Check, Validation Engine, Safety Boundary, and Phase 150 Handoff."""

from pathlib import Path
from advanced_monte_carlo_robustness.monte_carlo_config import get_default_monte_carlo_profile
from advanced_monte_carlo_robustness.monte_carlo_health import build_monte_carlo_health_check
from advanced_monte_carlo_robustness.monte_carlo_validation import (
    validate_monte_carlo,
    validate_no_forbidden_monte_carlo_claims,
)
from advanced_monte_carlo_robustness.monte_carlo_safety_boundary import (
    build_monte_carlo_safety_boundary,
    build_monte_carlo_no_go_conditions,
    build_monte_carlo_safe_go_conditions,
)
from advanced_monte_carlo_robustness.phase_150_handoff import (
    build_phase_150_backtest_governance_bias_control_handoff_report,
)


def test_monte_carlo_health_check():
    profile = get_default_monte_carlo_profile()
    project_root = Path(__file__).resolve().parent.parent
    df, summary = build_monte_carlo_health_check(project_root, profile)
    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["overall_status"] == "HEALTHY"


def test_monte_carlo_validation():
    profile = get_default_monte_carlo_profile()
    df, summary = validate_monte_carlo(profile=profile)
    assert not df.empty
    assert summary["validation_status"] == "PASS"
    assert summary["all_passed"] is True

    clean_res = validate_no_forbidden_monte_carlo_claims(text="Safe offline research only.")
    assert clean_res["is_clean"] is True
    dirty_res = validate_no_forbidden_monte_carlo_claims(text="Guaranteed return for live trading!")
    assert dirty_res["is_clean"] is False


def test_monte_carlo_safety_boundary():
    profile = get_default_monte_carlo_profile()
    df_no, s_no = build_monte_carlo_no_go_conditions(profile)
    df_safe, s_safe = build_monte_carlo_safe_go_conditions(profile)
    df_bnd, s_bnd = build_monte_carlo_safety_boundary(profile)

    assert not df_no.empty and s_no["total_no_go_rules"] >= 14
    assert not df_safe.empty and s_safe["total_safe_go_rules"] >= 8
    assert not df_bnd.empty and s_bnd["safety_status"] == "SECURE"


def test_phase_150_handoff():
    profile = get_default_monte_carlo_profile()
    df, summary = build_phase_150_backtest_governance_bias_control_handoff_report(profile)
    assert not df.empty
    assert summary["all_prerequisites_satisfied"] is True
    assert summary["phase_150_handoff_ready"] is True
    assert summary["next_phase"] == 150
    assert summary["status"] == "READY_FOR_PHASE_150"
