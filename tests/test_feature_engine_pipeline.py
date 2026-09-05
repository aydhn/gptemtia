from pathlib import Path
from config.settings import Settings
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_pipeline import FeatureEnginePipeline


def test_feature_engine_pipeline():
    settings = Settings()
    profile = get_default_feature_engine_profile()
    project_root = Path(__file__).resolve().parent.parent

    pipeline = FeatureEnginePipeline(
        data_lake=None,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    status_df, overall_sum = pipeline.build_feature_engine_status(save=False)

    assert not status_df.empty
    assert len(status_df) >= 20
    assert overall_sum["all_subsystems_ready"] is True
    assert overall_sum["current_phase"] == 116
    assert overall_sum["target_final_phase"] == 160
    assert overall_sum["next_phase"] == 117
    assert overall_sum["non_signal"] is True
