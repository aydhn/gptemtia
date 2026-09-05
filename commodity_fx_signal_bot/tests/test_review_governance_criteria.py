
from local_review_governance.review_governance_criteria import build_review_governance_criteria_matrix
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_criteria():
    p = get_default_local_review_governance_profile()
    df, s = build_review_governance_criteria_matrix(p)
    assert not df.empty
