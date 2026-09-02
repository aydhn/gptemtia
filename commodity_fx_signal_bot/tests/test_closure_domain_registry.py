
from local_closure.closure_domain_registry import build_closure_domain_registry, build_default_closure_domains
from local_closure.closure_config import get_default_local_closure_profile

def test_closure_domain_registry():
    p = get_default_local_closure_profile()
    df, summary = build_closure_domain_registry(p)
    assert not df.empty
    assert summary["total_domains"] > 0
    
    domains = build_default_closure_domains(p)
    assert len(domains) > 0
    for d in domains:
        for r in d.required_outputs:
            assert "secret" not in r.lower()
