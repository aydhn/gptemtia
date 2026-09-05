
from local_review_governance.review_validation import build_review_validation_report
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_validation():
    p = get_default_local_review_governance_profile()
    df, s = build_review_validation_report({}, p)
    assert not df.empty
