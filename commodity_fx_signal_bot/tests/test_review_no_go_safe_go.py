
from local_review_governance.review_no_go_safe_go import build_review_governance_no_go_safe_go_summary
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_no_go_safe_go():
    p = get_default_local_review_governance_profile()
    df, s = build_review_governance_no_go_safe_go_summary(p)
    assert not df.empty
