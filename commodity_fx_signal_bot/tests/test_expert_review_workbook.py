
from local_review_governance.expert_review_workbook import build_expert_review_workbook
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_workbook():
    p = get_default_local_review_governance_profile()
    df, s = build_expert_review_workbook(p)
    assert not df.empty
