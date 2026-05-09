import pytest
import pandas as pd
from unittest.mock import MagicMock
from commodity_fx_signal_bot.ml.artifact_loader import ModelArtifactLoader
from commodity_fx_signal_bot.ml.prediction_config import MLPredictionProfile

def test_select_candidate_models():
    mock_lake = MagicMock()
    loader = ModelArtifactLoader(mock_lake)

    df = pd.DataFrame({
        "model_id": ["m1", "m2", "m3"],
        "model_family": ["random_forest", "dummy", "random_forest"],
        "model_quality_score": [0.8, 0.2, 0.9],
        "dataset_quality_score": [0.8, 0.8, 0.8],
        "leakage_risk_score": [0.1, 0.1, 0.5],
        "model_status": ["ready", "ready", "warning"]
    })

    profile = MLPredictionProfile(
        name="test", description="test", dataset_profile="test", training_profile="test",
        allowed_model_families=("random_forest",),
        min_model_quality_score=0.5,
        min_dataset_quality_score=0.5,
        max_leakage_risk_score=0.2,
        allow_warning_models=False
    )

    res_df, status = loader.select_candidate_models(df, profile)

    assert len(res_df) == 1
    assert res_df.iloc[0]["model_id"] == "m1"
