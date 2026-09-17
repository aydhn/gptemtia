# -*- coding: utf-8 -*-
"""Tests for Phase 157: Portfolio Acceptance Validation."""

import pytest
import pandas as pd

from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_labels import (
    VALIDATION_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)
from advanced_portfolio_acceptance.portfolio_acceptance_validation import (
    FORBIDDEN_CLAIM_PHRASES,
    validate_no_forbidden_portfolio_acceptance_claims,
    validate_portfolio_acceptance_profile_registry,
    validate_portfolio_acceptance_manifest,
    build_portfolio_acceptance_validation_report,
)
from advanced_portfolio_acceptance.portfolio_acceptance_profile_registry import (
    build_portfolio_acceptance_profile_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_manifest import (
    build_portfolio_acceptance_manifest,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_checkpoints import (
    build_portfolio_acceptance_component_checkpoint_registry,
)
from advanced_portfolio_acceptance.phase_153_portfolio_construction_acceptance import (
    build_phase_153_portfolio_construction_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_154_portfolio_optimization_acceptance import (
    build_phase_154_portfolio_optimization_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_155_risk_reporting_acceptance import (
    build_phase_155_risk_reporting_acceptance_registry,
)
from advanced_portfolio_acceptance.phase_156_portfolio_scenario_control_acceptance import (
    build_phase_156_portfolio_scenario_control_acceptance_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_go_no_go_boundaries import (
    build_portfolio_acceptance_go_no_go_boundary_registry,
)


def test_validate_no_forbidden_claims_clean():
    """Verify clean text passes validation without issues."""
    text = "Phase 157 offline dry run contract acceptance report. Strictly non-production."
    res = validate_no_forbidden_portfolio_acceptance_claims(text=text)
    assert res["is_clean"] is True
    assert len(res["violations"]) == 0


def test_validate_no_forbidden_claims_dirty():
    """Verify forbidden claim words are detected."""
    bad_text = "This system is production ready and generates a buy signal with guaranteed profit."
    res = validate_no_forbidden_portfolio_acceptance_claims(text=bad_text)
    assert res["is_clean"] is False
    assert len(res["violations"]) >= 3


def test_validate_profile_registry():
    """Verify profile registry passes validation."""
    df, _ = build_portfolio_acceptance_profile_registry()
    res = validate_portfolio_acceptance_profile_registry(df)
    assert res["passed"] is True
    assert len(res["issues"]) == 0


def test_validate_manifest():
    """Verify manifest passes validation."""
    df, _ = build_portfolio_acceptance_manifest()
    res = validate_portfolio_acceptance_manifest(df)
    assert res["passed"] is True
    assert len(res["issues"]) == 0


def test_build_validation_report():
    """Verify comprehensive validation report passes all checks."""
    df_prof, _ = build_portfolio_acceptance_profile_registry()
    df_chk, _ = build_portfolio_acceptance_component_checkpoint_registry()
    df_153, _ = build_phase_153_portfolio_construction_acceptance_registry()
    df_154, _ = build_phase_154_portfolio_optimization_acceptance_registry()
    df_155, _ = build_phase_155_risk_reporting_acceptance_registry()
    df_156, _ = build_phase_156_portfolio_scenario_control_acceptance_registry()
    df_gng, _ = build_portfolio_acceptance_go_no_go_boundary_registry()
    df_mnf, _ = build_portfolio_acceptance_manifest()

    tables = {
        "profiles": df_prof,
        "checkpoints": df_chk,
        "phase_153": df_153,
        "phase_154": df_154,
        "phase_155": df_155,
        "phase_156": df_156,
        "go_no_go": df_gng,
        "manifest": df_mnf,
    }

    df, summary = build_portfolio_acceptance_validation_report(tables)

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert all(df["passed"])
    assert all(df["status"] == "PASS")

    assert isinstance(summary, dict)
    assert summary["domain"] == VALIDATION_DOMAIN
    assert summary["all_passed"] is True
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["status"] == PORTFOLIO_ACCEPTANCE_READY
