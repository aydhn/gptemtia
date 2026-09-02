from local_acceptance.acceptance_validation import build_acceptance_validation_report
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_validation_report():
    p = get_default_local_acceptance_profile()
    res, s = build_acceptance_validation_report({}, p)
    assert not res.empty
