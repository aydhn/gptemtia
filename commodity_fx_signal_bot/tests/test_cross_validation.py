import pytest
import pandas as pd
from ml.cross_validation import create_chronological_cv_folds, validate_cv_folds

def test_create_chronological_cv_folds():
    dates = pd.date_range("2023-01-01", periods=100)

    folds = create_chronological_cv_folds(dates, n_splits=3, embargo_bars=5, min_train_rows=30, min_test_rows=10)

    assert len(folds) == 3
    for fold in folds:
        assert len(fold.train_indices) >= 30
        assert len(fold.test_indices) >= 10
        # Check chronological order and embargo
        assert fold.train_indices[-1] + 5 < fold.test_indices[0]

def test_validate_cv_folds():
    dates = pd.date_range("2023-01-01", periods=100)
    folds = create_chronological_cv_folds(dates, n_splits=3, embargo_bars=5, min_train_rows=30, min_test_rows=10)

    res = validate_cv_folds(folds)
    assert res["passed"]
