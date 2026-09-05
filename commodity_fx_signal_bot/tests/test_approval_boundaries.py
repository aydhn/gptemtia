
from local_review_governance.approval_boundaries import build_manual_approval_boundary_registry
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_boundaries():
    p = get_default_local_review_governance_profile()
    df, s = build_manual_approval_boundary_registry(p)
    assert not df.empty
