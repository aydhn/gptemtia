
from local_review_governance.reviewer_console_maps import build_reviewer_console_command_map
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_console_maps():
    p = get_default_local_review_governance_profile()
    df, s = build_reviewer_console_command_map(p)
    assert not df.empty
