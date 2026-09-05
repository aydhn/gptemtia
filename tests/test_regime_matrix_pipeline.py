from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_matrix_pipeline import RegimeMatrixPipeline
from data.storage.data_lake import DataLake


def test_regime_matrix_pipeline_run():
    lake = DataLake()
    prof = get_default_regime_matrix_profile()
    pipeline = RegimeMatrixPipeline(data_lake=lake, profile=prof)

    result = pipeline.run_all(save=True)
    assert result["pipeline_status"] == "SUCCESS"
    assert result["current_phase"] == 127
    assert result["next_phase"] == 128
    assert result["target_final_phase"] == 160
    assert result["non_signal"] is True
    assert result["source_preserved"] is True
    assert result["model_training_executed"] is False


def test_regime_matrix_pipeline_status():
    lake = DataLake()
    prof = get_default_regime_matrix_profile()
    pipeline = RegimeMatrixPipeline(data_lake=lake, profile=prof)

    df_stat, s_stat = pipeline.build_regime_matrix_status(save=True)
    assert len(df_stat) == 1
    assert df_stat.iloc[0]["phase"] == 127
    assert df_stat.iloc[0]["next_phase"] == 128
    assert df_stat.iloc[0]["status"] == "READY"
