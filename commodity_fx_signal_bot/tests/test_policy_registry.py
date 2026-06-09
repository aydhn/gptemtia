import pytest
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.policy_registry import (
    build_default_policy_registry,
    policy_registry_to_dataframe,
    validate_policy_registry
)

def test_build_default_policy_registry():
    profile = get_default_evidence_governance_profile()
    policies = build_default_policy_registry(profile)
    assert len(policies) > 0
    assert not policies[0].official_compliance_claim

def test_policy_registry_to_dataframe():
    profile = get_default_evidence_governance_profile()
    policies = build_default_policy_registry(profile)
    df = policy_registry_to_dataframe(policies)
    assert "policy_id" in df.columns

def test_validate_policy_registry():
    profile = get_default_evidence_governance_profile()
    policies = build_default_policy_registry(profile)
    df = policy_registry_to_dataframe(policies)
    res = validate_policy_registry(df, profile)
    assert res["passed"] is True
