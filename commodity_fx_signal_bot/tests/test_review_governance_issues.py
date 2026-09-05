
from local_review_governance.review_governance_issues import build_review_governance_issue_register
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_issues():
    p = get_default_local_review_governance_profile()
    df, s = build_review_governance_issue_register(p)
    assert not df.empty
