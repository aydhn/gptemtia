
from pathlib import Path
from local_review_governance.review_governance_evidence import build_review_governance_evidence_index
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_evidence():
    p = get_default_local_review_governance_profile()
    df, s = build_review_governance_evidence_index(Path("."), p)
    assert not df.empty
