# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Governance Approval, Release, and Non-Production Boundaries."""

import pytest
from advanced_model_governance.model_governance_config import get_model_governance_profile
from advanced_model_governance.governance_approval_boundaries import (
    build_governance_approval_boundary_registry,
    validate_governance_approval_request,
)
from advanced_model_governance.governance_release_boundaries import (
    build_governance_release_boundary_registry,
    validate_governance_release_request,
)
from advanced_model_governance.governance_non_production_boundaries import (
    build_governance_non_production_boundary_registry,
)
from advanced_model_governance.governance_manual_review_gates import (
    build_governance_manual_review_gate_registry,
)


def test_governance_approval_boundaries():
    prof = get_model_governance_profile()
    df, summary = build_governance_approval_boundary_registry(prof)
    assert len(df) >= 4
    assert summary["total_boundaries"] >= 4
    assert summary["all_actions_blocked"] is True
    assert (df["action_permitted"] == False).all()
    assert (df["status"] == "ENFORCED").all()

    req = validate_governance_approval_request("production_approval")
    assert req["is_blocked"] is True
    assert req["approval_status"] == "BLOCKED_BY_POLICY"


def test_governance_release_boundaries():
    prof = get_model_governance_profile()
    df, summary = build_governance_release_boundary_registry(prof)
    assert len(df) >= 3
    assert summary["total_release_boundaries"] >= 3
    assert summary["all_releases_blocked"] is True
    assert (df["release_allowed"] == False).all()
    assert (df["status"] == "BLOCKED_BY_POLICY").all()

    rel = validate_governance_release_request("test_release")
    assert rel["release_granted"] is False
    assert rel["status"] == "BLOCKED_BY_POLICY"


def test_governance_non_production_boundaries():
    prof = get_model_governance_profile()
    df, summary = build_governance_non_production_boundary_registry(prof)
    assert len(df) >= 4
    assert summary["total_rules"] >= 4
    assert (df["is_enforced"] == True).all()
    assert summary["all_enforced"] is True


def test_governance_manual_review_gates():
    prof = get_model_governance_profile()
    df, summary = build_governance_manual_review_gate_registry(prof)
    assert len(df) >= 4
    assert summary["total_gates"] >= 4
    assert "gate_name" in df.columns
