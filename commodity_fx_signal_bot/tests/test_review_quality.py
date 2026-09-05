
from local_review_governance.review_quality import check_for_forbidden_terms_in_review
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_quality():
    res = check_for_forbidden_terms_in_review(text="live order")
    assert "live order" in res["found"]
