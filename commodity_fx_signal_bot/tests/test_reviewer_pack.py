from local_acceptance.reviewer_pack import build_independent_reviewer_pack
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_independent_reviewer_pack():
    p = get_default_local_acceptance_profile()
    text, s = build_independent_reviewer_pack(None, None, None, p)
    assert "Independent Reviewer Pack" in text
