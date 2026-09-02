from pathlib import Path
from config.settings import Settings
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from data.storage.data_lake import DataLake

def test_local_acceptance_pipeline():
    s = Settings()
    dl = DataLake(str(Path('.')))
    pipeline = LocalAcceptancePipeline(dl, s, Path("."))
    dfs, sm = pipeline.build_acceptance_domain_registry(save=False)
    assert not dfs["domain"].empty
