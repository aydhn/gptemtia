
from local_review_governance.manual_approval_ledger import build_manual_approval_ledger_rehearsal, build_manual_approval_ledger_registry
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_ledger():
    p = get_default_local_review_governance_profile()
    t, s = build_manual_approval_ledger_rehearsal(p)
    assert len(t) > 0
    df, s2 = build_manual_approval_ledger_registry(p)
    assert not df.empty
