from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline
from config import settings
from data.storage.data_lake import DataLake

def test_pipeline():
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_advanced_config_status(save=False)
    assert df is not None
