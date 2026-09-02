import pytest
from pathlib import Path
from local_training.training_pipeline import LocalTrainingPipeline
from local_training.training_config import get_default_local_training_profile

class MockDataLake:
    def __getattr__(self, item):
        def _mock(*args, **kwargs):
            import pandas as pd
            if "load" in item:
                return pd.DataFrame()
            return Path("mock")
        return _mock

class MockSettings:
    pass

def test_pipeline():
    p = LocalTrainingPipeline(MockDataLake(), MockSettings(), Path("."), get_default_local_training_profile())
    d1, s1 = p.build_training_domain_registry()
    assert isinstance(d1, dict)
    d2, s2 = p.build_onboarding_curriculum()
    assert isinstance(d2, dict)
    d3, s3 = p.build_guided_walkthroughs()
    assert isinstance(d3, dict)
    d4, s4 = p.build_training_packs()
    assert isinstance(d4, dict)
    t, s5 = p.build_handover_education_binder()
    assert isinstance(t, str)
