from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline
from config import settings
from data.storage.data_lake import DataLake

def test_pipeline():
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_advanced_config_status(save=False)
    assert df is not None

from unittest.mock import MagicMock

def test_pipeline_save_errors():
    dl = MagicMock()
    dl.save_advanced_config_profile_registry.side_effect = Exception("Mocked error")
    dl.save_research_mode_preset_registry.side_effect = Exception("Mocked error")
    dl.save_composed_research_profile_registry.side_effect = Exception("Mocked error")
    dl.save_profile_compatibility_matrix.side_effect = Exception("Mocked error")
    dl.save_profile_validation_report.side_effect = Exception("Mocked error")
    dl.save_advanced_config_report.side_effect = Exception("Mocked error")

    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")

    registries, summaries = pipeline.build_profile_registries(save=True)
    assert registries is not None

    preset_df, preset_summary = pipeline.build_research_mode_presets(save=True)
    assert preset_df is not None

    composed_df, composed_summary = pipeline.build_composed_research_profiles(save=True)
    assert composed_df is not None

    compatibility_df, comp_summary = pipeline.build_profile_compatibility_matrix(save=True)
    assert compatibility_df is not None

    quality, score_summary = pipeline.build_profile_quality_report(save=True)
    assert quality is not None

    status_df, status_summary = pipeline.build_advanced_config_status(save=True)
    assert status_df is not None
