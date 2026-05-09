import pytest
import pandas as pd
from commodity_fx_signal_bot.ml.ensemble import ModelEnsembleBuilder
from commodity_fx_signal_bot.ml.prediction_config import MLPredictionProfile

def test_ensemble_classification():
    profile = MLPredictionProfile(
        name="test", description="", dataset_profile="", training_profile="",
        allowed_model_families=("test",), uncertainty_warning_threshold=0.6,
        min_confidence_score=0.4
    )

    df1 = pd.DataFrame({"predicted_label": ["predicted_up"], "confidence_score": [0.8], "class_probability_up": [0.8], "class_probability_down": [0.2], "task_type": ["classification"]})
    df2 = pd.DataFrame({"predicted_label": ["predicted_up"], "confidence_score": [0.6], "class_probability_up": [0.6], "class_probability_down": [0.4], "task_type": ["classification"]})

    builder = ModelEnsembleBuilder(profile)
    res, sum_dict = builder.build_ensemble_prediction({"m1": df1, "m2": df2})

    assert not res.empty
    assert res.iloc[0]["ensemble_model_count"] == 2
    assert res.iloc[0]["ensemble_predicted_direction"] == "predicted_up"
    assert res.iloc[0]["ensemble_confidence_score"] == 0.7
    assert res.iloc[0]["ensemble_disagreement_score"] == 0.3
