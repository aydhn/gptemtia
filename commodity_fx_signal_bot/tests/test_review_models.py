
from local_review_governance.review_models import build_review_domain_id, ReviewDomain

def test_models():
    id1 = build_review_domain_id("test")
    id2 = build_review_domain_id("test")
    assert id1 == id2
