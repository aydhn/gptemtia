
from pathlib import Path
from local_review_governance.human_review_cockpit import build_final_local_human_review_cockpit, build_human_review_cockpit_index
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_cockpit():
    p = get_default_local_review_governance_profile()
    t, s = build_final_local_human_review_cockpit(Path("."), p)
    assert len(t) > 0
    df, s2 = build_human_review_cockpit_index(p)
    assert not df.empty
