
from local_review_governance.human_review_maps import build_human_review_cockpit_route_map
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_maps():
    p = get_default_local_review_governance_profile()
    df, s = build_human_review_cockpit_route_map(p)
    assert not df.empty
