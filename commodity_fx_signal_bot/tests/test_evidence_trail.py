from pathlib import Path
from local_acceptance.evidence_trail import build_audit_style_local_evidence_trail
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_audit_style_local_evidence_trail():
    p = get_default_local_acceptance_profile()
    df, s = build_audit_style_local_evidence_trail(Path("."), p)
    assert not df.empty
