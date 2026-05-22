from factor_research.factor_pipeline import FactorResearchPipeline
from data.storage.data_lake import DataLake
from config.paths import ProjectPaths
from config.settings import Settings

def test_factor_pipeline():
    paths = ProjectPaths()
    dl = DataLake(paths)
    s = Settings()
    pipe = FactorResearchPipeline(dl, s)
    assert pipe is not None
