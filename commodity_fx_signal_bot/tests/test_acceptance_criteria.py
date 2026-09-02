from local_acceptance.acceptance_criteria import build_acceptance_criteria_registry
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_criteria_registry():
    p = get_default_local_acceptance_profile()
    df, s = build_acceptance_criteria_registry(p)
    assert not df.empty
