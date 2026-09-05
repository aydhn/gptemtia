
from local_review_governance.review_governance_non_goals import build_review_governance_non_goals_registry
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_non_goals():
    p = get_default_local_review_governance_profile()
    df, s = build_review_governance_non_goals_registry(p)
    assert not df.empty
