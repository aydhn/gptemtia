
from local_closure.closure_models import ClosureDomain, build_closure_domain_id, closure_domain_to_dict

def test_models():
    id1 = build_closure_domain_id("test")
    id2 = build_closure_domain_id("test")
    assert id1 == id2
    
    domain = ClosureDomain(id1, "test_label", "Test", "Desc", ["req"], [])
    d = closure_domain_to_dict(domain)
    assert d["domain_id"] == id1
    assert d["domain_label"] == "test_label"
