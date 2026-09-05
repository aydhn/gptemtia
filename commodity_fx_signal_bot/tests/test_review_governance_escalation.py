
from local_review_governance.review_governance_escalation import build_review_governance_escalation_rehearsal
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_escalation():
    p = get_default_local_review_governance_profile()
    t, s = build_review_governance_escalation_rehearsal(p)
    assert len(t) > 0
