from local_performance.performance_quality import check_for_forbidden_terms_in_performance
from local_performance.performance_config import get_default_local_performance_profile

def test_performance_quality():
    res = check_for_forbidden_terms_in_performance("benchmark completed")
    assert not res["valid"]
    res2 = check_for_forbidden_terms_in_performance("gercek benchmark degildir")
    assert res2["valid"]
