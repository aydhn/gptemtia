import pytest
import pandas as pd
from evidence_governance.evidence_config import get_default_evidence_governance_profile
from evidence_governance.evidence_validation import (
    validate_evidence_artifacts,
    validate_policy_control_mapping,
    validate_traceability_matrix,
    validate_no_official_compliance_claims
)

def test_evidence_validation():
    profile = get_default_evidence_governance_profile()

    art_df = pd.DataFrame([{"artifact_id": "a1", "relative_path": "path"}])
    res = validate_evidence_artifacts(art_df, profile)
    assert res["passed"] is True

    res = validate_policy_control_mapping(pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), profile)
    assert res["passed"] is True

    res = validate_no_official_compliance_claims(text="official compliance certified")
    assert res["passed"] is False
    assert "Forbidden term" in res["warnings"][0]
