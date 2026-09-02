from local_performance.performance_pipeline import LocalPerformancePipeline
from local_performance.performance_config import get_default_local_performance_profile
from pathlib import Path
from config.settings import Settings

class MockDataLake:
    pass

def test_performance_pipeline():
    p = get_default_local_performance_profile()
    dl = MockDataLake()
    s = Settings()
    pipe = LocalPerformancePipeline(dl, s, Path("."), p)
    res, summ = pipe.build_performance_domain_registry(save=False)
    assert "performance_domain_registry" in res
