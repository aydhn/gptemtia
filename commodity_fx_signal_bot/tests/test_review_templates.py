from local_acceptance.review_templates import build_independent_review_notes_template, build_acceptance_response_template
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_review_templates():
    p = get_default_local_acceptance_profile()
    nt, _ = build_independent_review_notes_template(p)
    rt, _ = build_acceptance_response_template(p)
    assert "Independent Review Notes" in nt
    assert "Acceptance Response" in rt
