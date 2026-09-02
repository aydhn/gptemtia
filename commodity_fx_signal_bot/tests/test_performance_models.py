from local_performance.performance_models import build_performance_domain_id, build_resource_estimate_id, build_runtime_estimate_id, build_efficiency_candidate_id, PerformanceDomain, performance_domain_to_dict

def test_builders():
    assert build_performance_domain_id("test") == build_performance_domain_id("test")
    assert build_resource_estimate_id("a", "b") == build_resource_estimate_id("a", "b")
    assert build_runtime_estimate_id("a", "b") == build_runtime_estimate_id("a", "b")
    assert build_efficiency_candidate_id("a", "b") == build_efficiency_candidate_id("a", "b")

def test_dataclasses():
    d = PerformanceDomain("1", "lbl", "name", "desc", [], [])
    dct = performance_domain_to_dict(d)
    assert "domain_id" in dct
