
from pathlib import Path
from local_review_governance.reviewer_console import build_offline_reviewer_console_packet
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_console():
    p = get_default_local_review_governance_profile()
    t, s = build_offline_reviewer_console_packet(Path("."), p)
    assert len(t) > 0
