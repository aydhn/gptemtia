import pytest
import pandas as pd
from ml.training_config import get_default_ml_training_profile
from ml.model_trainer import MLModelTrainer

def test_prepare_training_data():
    profile = get_default_ml_training_profile()
    trainer = MLModelTrainer(profile)

    df = pd.DataFrame({
        "feat1": [1, 2, 3],
        "target": [0, 1, 0]
    })

    X, y, prep_res = trainer.prepare_training_data(df, "target")
    assert not prep_res["warnings"]
    assert len(X.columns) == 1
    assert y.name == "target"

    # Missing target
    X, y, prep_res = trainer.prepare_training_data(df, "unknown")
    assert len(prep_res["warnings"]) > 0

def test_train_from_dataset():
    profile = get_default_ml_training_profile()
    trainer = MLModelTrainer(profile)

    # Create tiny dataset
    df = pd.DataFrame({
        "feat1": list(range(100)),
        "target_direction_class_5": [0, 1] * 50
    })

    # min_train_rows is 300 by default, so this should fail with insufficient_data
    model, preprocessor, result, prep_res = trainer.train_from_dataset("TEST", "1d", df)

    assert model is None
    assert result.status == "insufficient_data"
