from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline
from config import settings
from data.storage.data_lake import DataLake

def test_pipeline():
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_advanced_config_status(save=False)
    assert df is not None

from unittest.mock import patch

def test_build_profile_quality_report_exception_handled():
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")

    with patch.object(dl, 'save_profile_validation_report', side_effect=Exception("Test Exception")):
        quality, score_summary = pipeline.build_profile_quality_report(save=True)

        # Exception should be caught and not bubbled up
        assert score_summary is not None
