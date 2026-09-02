from local_performance.performance_domain_registry import build_performance_domain_registry, build_default_performance_domains
from local_performance.performance_config import get_default_local_performance_profile

def test_domain_registry():
    p = get_default_local_performance_profile()
    df, s = build_performance_domain_registry(p)
    assert not df.empty
    domains = build_default_performance_domains(p)
    assert len(domains) > 0
