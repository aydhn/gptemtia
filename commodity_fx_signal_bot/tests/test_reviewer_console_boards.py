
from local_review_governance.reviewer_console_boards import build_reviewer_console_status_board
from local_review_governance.review_config import get_default_local_review_governance_profile

def test_boards():
    p = get_default_local_review_governance_profile()
    df, s = build_reviewer_console_status_board(p)
    assert not df.empty
