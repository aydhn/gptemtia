import pytest
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.control_registry import (
    build_default_control_registry,
    control_registry_to_dataframe,
    validate_control_registry
)

def test_build_default_control_registry():
    profile = get_default_evidence_governance_profile()
    controls = build_default_control_registry(profile)
    assert len(controls) > 0
    assert controls[0].status == "control_unknown"

def test_control_registry_to_dataframe():
    profile = get_default_evidence_governance_profile()
    controls = build_default_control_registry(profile)
    df = control_registry_to_dataframe(controls)
    assert "control_id" in df.columns
    assert "required_evidence_labels" in df.columns

def test_validate_control_registry():
    profile = get_default_evidence_governance_profile()
    controls = build_default_control_registry(profile)
    df = control_registry_to_dataframe(controls)
    res = validate_control_registry(df, profile)
    assert res["passed"] is True
