import pytest
from evidence_governance.evidence_config import (
    EvidenceGovernanceProfile,
    get_evidence_governance_profile,
    list_evidence_governance_profiles,
    validate_evidence_governance_profiles,
    get_default_evidence_governance_profile
)

def test_validate_evidence_governance_profiles():
    # Should run without error
    validate_evidence_governance_profiles()

def test_get_default_evidence_governance_profile():
    prof = get_default_evidence_governance_profile()
    assert prof is not None
    assert prof.name == "balanced_local_evidence"

def test_profile_constraints():
    profiles = list_evidence_governance_profiles(enabled_only=False)
    for p in profiles:
        assert p.language != ""
        assert p.max_artifacts > 0
        assert p.max_artifact_mb > 0
        assert p.freshness_days_warning > 0
        assert p.dry_run_default is True
        assert p.allow_official_compliance_claims is False
        assert p.allow_legal_opinion is False
        assert p.allow_cloud_export is False
        assert p.allow_external_auditor_upload is False
        assert p.allow_file_modification is False
        assert p.allow_file_deletion is False

def test_unknown_profile():
    with pytest.raises(ValueError):
        get_evidence_governance_profile("non_existent_profile")
