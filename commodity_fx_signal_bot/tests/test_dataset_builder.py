import pytest
import pandas as pd
from ml.dataset_builder import SupervisedDatasetBuilder
from ml.dataset_config import get_default_ml_dataset_profile

def test_align_features_and_targets():
    builder = SupervisedDatasetBuilder(get_default_ml_dataset_profile())

    X = pd.DataFrame({"f1": [1, 2, 3]}, index=[0, 1, 2])
    y = pd.DataFrame({"t1": [10, 20]}, index=[1, 2])

    Xa, ya, _ = builder.align_features_and_targets(X, y)

    assert len(Xa) == 2
    assert len(ya) == 2
    assert list(Xa.index) == [1, 2]

def test_build_supervised_dataset():
    builder = SupervisedDatasetBuilder(get_default_ml_dataset_profile())

    X = pd.DataFrame({"f1": [1, 2]}, index=[1, 2])
    y = pd.DataFrame({"t1": [10, 20]}, index=[1, 2])

    ds, summary = builder.build_supervised_dataset(X, y)

    assert "f1" in ds.columns
    assert "target_t1" in ds.columns

def test_select_target():
    builder = SupervisedDatasetBuilder(get_default_ml_dataset_profile())
    ds = pd.DataFrame({"f1": [1, 2, 3], "target_t1": [10, None, 30]})

    X, y, summary = builder.select_target(ds, "target_t1")

    assert len(X) == 2
    assert "target_t1" not in X.columns
    assert len(y) == 2
