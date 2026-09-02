from local_acceptance.acceptance_domain_registry import build_acceptance_domain_registry
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_domain_registry():
    p = get_default_local_acceptance_profile()
    df, s = build_acceptance_domain_registry(p)
    assert not df.empty
    assert s["total_domains"] > 0
