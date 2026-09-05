
from local_review_governance.expert_review_maps import build_expert_review_checklist_registry
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_expert_maps():
    p = get_default_local_review_governance_profile()
    df, s = build_expert_review_checklist_registry(p)
    assert not df.empty
