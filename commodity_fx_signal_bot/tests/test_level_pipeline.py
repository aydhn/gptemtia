import pytest
from levels.level_pipeline import LevelPipeline
from levels.level_config import get_default_level_profile
from config.settings import Settings
from data.storage.data_lake import DataLake


class DummyDataLake(DataLake):
    def has_features(self, spec, timeframe, feature_set):
        return False


def test_pipeline_no_data():
    settings = Settings()
    prof = get_default_level_profile()
    from config.symbols import get_symbol_spec

    spec = get_symbol_spec("GC=F")

    from pathlib import Path

    lake = DummyDataLake(Path("/tmp/lake"))
    pipeline = LevelPipeline(lake, settings, prof)

    df, sumry = pipeline.build_for_symbol_timeframe(spec, "1d", save=False)
    assert df.empty
    assert "warnings" in sumry
