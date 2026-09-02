from pathlib import Path
from local_simplification.simplification_pipeline import LocalSimplificationPipeline

class MockDataLake:
    pass

class MockSettings:
    pass

def test_pipeline():
    pipeline = LocalSimplificationPipeline(MockDataLake(), MockSettings(), Path("."))
    res, status = pipeline.build_simplification_domain_registry(save=False)
    assert status["status"] == "ok"
