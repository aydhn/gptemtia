import pandas as pd
import numpy as np
from dataclasses import dataclass, asdict
from .training_config import MLTrainingProfile
from .preprocessing import BasicPreprocessor
from .baseline_models import create_baseline_model
from .model_evaluator import evaluate_classification_model, evaluate_regression_model
from .model_labels import is_classification_task

@dataclass
class CVFold:
    fold_id: str
    train_start: str
    train_end: str
    test_start: str
    test_end: str
    train_indices: list[int]
    test_indices: list[int]
    embargo_bars: int
    warnings: list[str]

def create_chronological_cv_folds(index: pd.DatetimeIndex, n_splits: int = 5, embargo_bars: int = 5, min_train_rows: int = 100, min_test_rows: int = 20) -> list[CVFold]:
    n_samples = len(index)
    folds = []

    if n_samples < min_train_rows + min_test_rows:
        return folds

    fold_size = (n_samples - min_train_rows) // n_splits

    if fold_size < min_test_rows:
        return folds

    for i in range(n_splits):
        train_end_idx = min_train_rows + i * fold_size
        test_start_idx = train_end_idx + embargo_bars
        test_end_idx = test_start_idx + fold_size

        if i == n_splits - 1:
            test_end_idx = n_samples

        if test_start_idx >= n_samples or test_end_idx - test_start_idx < min_test_rows:
            continue

        train_indices = list(range(0, train_end_idx))
        test_indices = list(range(test_start_idx, test_end_idx))

        fold = CVFold(
            fold_id=f"fold_{i+1}",
            train_start=str(index[train_indices[0]]),
            train_end=str(index[train_indices[-1]]),
            test_start=str(index[test_indices[0]]),
            test_end=str(index[test_indices[-1]]),
            train_indices=train_indices,
            test_indices=test_indices,
            embargo_bars=embargo_bars,
            warnings=[]
        )
        folds.append(fold)

    return folds

def cv_fold_to_dict(fold: CVFold) -> dict:
    return {
        "fold_id": fold.fold_id,
        "train_start": fold.train_start,
        "train_end": fold.train_end,
        "test_start": fold.test_start,
        "test_end": fold.test_end,
        "train_rows": len(fold.train_indices),
        "test_rows": len(fold.test_indices),
        "embargo_bars": fold.embargo_bars,
        "warnings": fold.warnings
    }

def validate_cv_folds(folds: list[CVFold]) -> dict:
    warnings = []
    passed = True

    if not folds:
        return {"passed": False, "warnings": ["No folds generated"]}

    for fold in folds:
        if not fold.train_indices or not fold.test_indices:
            warnings.append(f"Fold {fold.fold_id} has empty train/test indices")
            passed = False

        if fold.train_indices[-1] >= fold.test_indices[0]:
            warnings.append(f"Fold {fold.fold_id} has overlapping or out-of-order train/test indices")
            passed = False

    return {"passed": passed, "warnings": warnings}

def run_cross_validation(
    X: pd.DataFrame,
    y: pd.Series,
    model_family: str,
    task_type: str,
    profile: MLTrainingProfile,
) -> tuple[pd.DataFrame, dict]:
    folds = create_chronological_cv_folds(
        X.index,
        n_splits=profile.cv_n_splits,
        embargo_bars=profile.cv_embargo_bars,
        min_train_rows=profile.min_train_rows,
        min_test_rows=profile.min_test_rows
    )

    val_res = validate_cv_folds(folds)
    if not val_res["passed"]:
        return pd.DataFrame(), {"passed": False, "warnings": val_res["warnings"]}

    results = []

    for fold in folds:
        X_train, y_train = X.iloc[fold.train_indices], y.iloc[fold.train_indices]
        X_test, y_test = X.iloc[fold.test_indices], y.iloc[fold.test_indices]

        preprocessor = BasicPreprocessor(
            drop_high_nan_features=profile.drop_high_nan_features,
            max_nan_ratio=profile.max_feature_nan_ratio,
            enable_imputation=profile.enable_basic_imputation,
            enable_scaling=profile.enable_basic_scaling
        )

        try:
            X_train_trans = preprocessor.fit_transform(X_train, y_train)
            X_test_trans = preprocessor.transform(X_test)

            # Align columns if dummies added features that don't match
            missing_cols = set(X_train_trans.columns) - set(X_test_trans.columns)
            for c in missing_cols:
                X_test_trans[c] = 0
            X_test_trans = X_test_trans[X_train_trans.columns]

            model = create_baseline_model(model_family, task_type)
            model.fit(X_train_trans, y_train)

            if is_classification_task(task_type):
                metrics = evaluate_classification_model(model, preprocessor, X_test_trans, y_test)
                metric_primary = metrics.get('balanced_accuracy', 0.0)
            else:
                metrics = evaluate_regression_model(model, preprocessor, X_test_trans, y_test)
                metric_primary = metrics.get('r2', 0.0)

            res = {
                "fold_id": fold.fold_id,
                "train_rows": len(X_train),
                "test_rows": len(X_test),
                "metric_primary": metric_primary,
                "warnings": []
            }
            res.update(metrics)
            results.append(res)

        except Exception as e:
            results.append({
                "fold_id": fold.fold_id,
                "train_rows": len(X_train),
                "test_rows": len(X_test),
                "metric_primary": 0.0,
                "warnings": [f"CV error: {str(e)}"]
            })

    df = pd.DataFrame(results)

    summary = {
        "n_folds": len(folds),
        "mean_primary_metric": df["metric_primary"].mean() if "metric_primary" in df else 0.0,
        "std_primary_metric": df["metric_primary"].std() if "metric_primary" in df else 0.0,
        "passed": True,
        "warnings": []
    }

    return df, summary
