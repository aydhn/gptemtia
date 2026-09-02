
from pathlib import Path
from config.settings import Settings
from local_closure.closure_pipeline import LocalClosurePipeline

class MockDataLake:
    def __init__(self):
        pass
    def __getattr__(self, name):
        def method(*args, **kwargs):
            return None
        return method

def test_pipeline():
    settings = Settings()
    dl = MockDataLake()
    pipeline = LocalClosurePipeline(dl, settings, Path.cwd()) # type: ignore
    
    df, sum = pipeline.build_closure_domain_registry(save=True)
    assert sum is not None
