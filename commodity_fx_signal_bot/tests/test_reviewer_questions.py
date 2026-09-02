from local_acceptance.reviewer_questions import build_reviewer_question_bank
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_reviewer_question_bank():
    p = get_default_local_acceptance_profile()
    df, s = build_reviewer_question_bank(p)
    assert not df.empty
