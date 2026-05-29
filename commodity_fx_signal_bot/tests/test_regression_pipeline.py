import pytest
from pathlib import Path
from config.settings import settings
from scenario_regression.regression_config import get_default_scenario_regression_profile
from scenario_regression.regression_pipeline import ScenarioRegressionPipeline

class MockDataLake:
    def __getattr__(self, name):
        if name.startswith("save_"):
            return lambda *args, **kwargs: Path("/")
        if name.startswith("load_"):
            return lambda *args, **kwargs: None
        return super().__getattr__(name)

def test_regression_pipeline():
    prof = get_default_scenario_regression_profile()
    dl = MockDataLake()
    pipe = ScenarioRegressionPipeline(dl, settings, Path("/"), prof)

    df, summ = pipe.build_scenario_regression_status(save=False)
    assert not df.empty
