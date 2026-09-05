from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_grid.feature_grid_config import get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_pipeline import FeatureGridPipeline


def test_feature_grid_pipeline_save_false(tmp_path):
    settings = Settings()
    data_lake = DataLake(base_dir=tmp_path)
    profile = get_default_feature_grid_profile()

    pipeline = FeatureGridPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=tmp_path,
        profile=profile,
    )

    tables_p, sum_p = pipeline.build_profiles_domains_contracts(save=False)
    assert "profiles" in tables_p
    assert "window_contracts" in tables_p

    tables_c, sum_c = pipeline.build_parameter_naming_schema_policies(save=False)
    assert "parameter_grids" in tables_c
    assert "naming" in tables_c

    tables_w, sum_w = pipeline.build_window_grid_registries(save=False)
    assert "moving_average" in tables_w
    assert "momentum" in tables_w

    tables_r, sum_r = pipeline.run_feature_grid_computation_rehearsal(save=False)
    assert "rehearsal" in tables_r
    assert sum_r["rehearsal"]["all_passed"] is True

    tables_m, sum_m = pipeline.build_metadata_dependency_quality(save=False)
    assert "metadata" in tables_m

    tables_h, sum_h = pipeline.build_health_validation_safety_handoff(save=False)
    assert "validation" in tables_h

    df_status, sum_status = pipeline.build_feature_grid_status(save=False)
    assert not df_status.empty
    assert sum_status["current_phase"] == 118
    assert sum_status["target_final_phase"] == 160
    assert sum_status["next_phase"] == 119
