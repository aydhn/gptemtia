
from pathlib import Path
from local_review_governance.review_governance_binder import build_terminal_review_governance_binder
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_binder():
    p = get_default_local_review_governance_profile()
    t, s = build_terminal_review_governance_binder(Path("."), p)
    assert len(t) > 0
