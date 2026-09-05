
from local_review_governance.review_domain_registry import build_review_governance_domain_registry
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_domain_registry():
    p = get_default_local_review_governance_profile()
    df, s = build_review_governance_domain_registry(p)
    assert not df.empty
