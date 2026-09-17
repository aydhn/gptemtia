# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Health Check, Validation Report, and Safety Boundary."""

from pathlib import Path
import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.model_governance_health import (
    build_model_governance_health_check,
)
from advanced_model_governance.model_governance_validation import (
    build_model_governance_validation_report,
)
from advanced_model_governance.model_governance_safety_boundary import (
    build_model_governance_safety_boundary,
)


def test_model_governance_health_check():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_health_check(Path("."), prof)
    assert len(df) >= 7
    assert summary["all_components_healthy"] is True
    assert summary["status"] == "ALL_SYSTEMS_OPERATIONAL"
    assert (df["status"] == "HEALTHY").all()


def test_model_governance_validation_report():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_validation_report({}, prof)
    assert len(df) >= 1
    assert summary["status"] == "PASS"
    assert summary["all_passed"] is True
    assert summary["clean_claims"] is True


def test_model_governance_safety_boundary():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_safety_boundary(prof)
    assert len(df) >= 20
    assert summary["all_no_go_enforced"] is True
    assert summary["status"] == "SECURE"
    assert (df["is_strictly_enforced"] == True).all()
