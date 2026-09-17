# -*- coding: utf-8 -*-
"""Unit tests for Phase 144 Model Governance Config, Labels, Models, Profiles, and Domains."""

import pytest
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
    list_model_governance_profiles,
    validate_model_governance_profiles,
)
from advanced_model_governance.model_governance_labels import (
    MODEL_GOVERNANCE_DOMAIN_LABELS,
    MODEL_GOVERNANCE_STATUS_LABELS,
    MODEL_GOVERNANCE_APPROVAL_LABELS,
    list_model_governance_domain_labels,
    list_model_governance_status_labels,
    list_model_governance_approval_labels,
    validate_model_governance_domain_label,
    validate_model_governance_status_label,
    validate_model_governance_approval_label,
)
from advanced_model_governance.model_governance_models import (
    ModelGovernanceProfileItem,
    ModelGovernanceContract,
    ModelCardContract,
    ModelCardTemplate,
    GovernanceBoundary,
)
from advanced_model_governance.model_governance_profile_registry import (
    build_model_governance_profile_registry,
)
from advanced_model_governance.model_governance_domain_registry import (
    build_model_governance_domain_registry,
)


def test_model_governance_config_defaults():
    profile = get_model_governance_profile()
    assert profile.profile_name == "balanced_local_model_governance_contracts"
    assert profile.allow_model_registry_write is False
    assert profile.allow_artifact_persistence is False
    assert profile.allow_model_deployment is False
    assert profile.allow_production_approval is False
    assert profile.allow_broker_ready_claim is False
    assert profile.allow_live_trading is False
    assert profile.allow_model_predict is False
    assert profile.allow_model_training is False
    assert profile.allow_signal_generation is False
    assert profile.allow_real_audit_log is False
    assert profile.non_production is True


def test_list_available_profiles():
    profiles = list_model_governance_profiles()
    assert "balanced_local_model_governance_contracts" in profiles
    assert "strict_non_production_governance_safety" in profiles
    assert "dry_run_model_cards_audit_focus" in profiles
    assert validate_model_governance_profiles() is True


def test_model_governance_labels():
    domains = list_model_governance_domain_labels()
    assert "model_card_contract_domain" in domains
    assert validate_model_governance_domain_label("governance_approval_boundary_domain") is True
    assert validate_model_governance_domain_label("invalid_domain") is False

    statuses = list_model_governance_status_labels()
    assert "governance_contract_ready" in statuses
    assert validate_model_governance_status_label("governance_contract_ready") is True

    approvals = list_model_governance_approval_labels()
    assert "approval_blocked_non_production" in approvals
    assert validate_model_governance_approval_label("approval_blocked_non_production") is True


def test_model_governance_models():
    prof_rec = ModelGovernanceProfileItem(
        profile_name="test_prof",
        display_name="Test Profile",
        description="test",
    )
    assert prof_rec.profile_name == "test_prof"

    boundary = GovernanceBoundary(
        boundary_name="test_boundary",
        boundary_type="non_production",
        enforcement_rule="blocked",
    )
    assert boundary.boundary_name == "test_boundary"


def test_model_governance_profile_registry():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_profile_registry(prof)
    assert len(df) >= 3
    assert summary["total_profiles"] >= 3
    assert "balanced_local_model_governance_contracts" in df["profile_name"].values
    assert "profile_name" in df.columns


def test_model_governance_domain_registry():
    prof = get_model_governance_profile()
    df, summary = build_model_governance_domain_registry(prof)
    assert len(df) >= 7
    assert summary["total_domains"] >= 7
    assert "model_governance_profile_domain" in df["domain_name"].values
    assert "model_card_contract_domain" in df["domain_name"].values

