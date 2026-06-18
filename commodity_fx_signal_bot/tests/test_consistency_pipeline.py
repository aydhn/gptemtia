import pytest
from pathlib import Path
from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from local_consistency.consistency_config import get_default_local_consistency_profile
from local_consistency.consistency_pipeline import LocalConsistencyPipeline

def test_pipeline_methods():
    settings = Settings()
    paths = ProjectPaths()
    data_lake = DataLake(paths.lake_dir)
    profile = get_default_local_consistency_profile()
    pipeline = LocalConsistencyPipeline(data_lake, settings, Path("."), profile)

    # test without saving to not create files randomly in the test suite
    df, summary = pipeline.build_consistency_check_registry(save=False)
    assert df is not None
