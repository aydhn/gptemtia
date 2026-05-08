import pandas as pd
import numpy as np
from .preprocessing import BasicPreprocessor
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score

def evaluate_classification_model(model, preprocessor: BasicPreprocessor, X: pd.DataFrame, y: pd.Series) -> dict:
    if len(y) == 0:
        return {"warnings": ["Empty target series"]}

    y_pred = model.predict(X)

    unique_classes = np.unique(y)

    metrics = {
        "accuracy": float(accuracy_score(y, y_pred)),
        "class_distribution": y.value_counts(normalize=True).to_dict(),
        "warnings": []
    }

    if len(unique_classes) > 1:
        metrics["balanced_accuracy"] = float(balanced_accuracy_score(y, y_pred))
        metrics["f1_macro"] = float(f1_score(y, y_pred, average='macro', zero_division=0))
        metrics["precision_macro"] = float(precision_score(y, y_pred, average='macro', zero_division=0))
        metrics["recall_macro"] = float(recall_score(y, y_pred, average='macro', zero_division=0))
        metrics["classification_report"] = classification_report(y, y_pred, output_dict=True, zero_division=0)
        metrics["confusion_matrix"] = build_confusion_matrix_table(y, pd.Series(y_pred, index=y.index)).to_dict()
    else:
        metrics["warnings"].append("Only one class present in target, limited metrics calculated")

    return metrics

def evaluate_regression_model(model, preprocessor: BasicPreprocessor, X: pd.DataFrame, y: pd.Series) -> dict:
    if len(y) == 0:
        return {"warnings": ["Empty target series"]}

    y_pred = model.predict(X)

    metrics = {
        "rmse": float(np.sqrt(mean_squared_error(y, y_pred))),
        "mae": float(mean_absolute_error(y, y_pred)),
        "prediction_mean": float(np.mean(y_pred)),
        "target_mean": float(np.mean(y)),
        "warnings": []
    }

    if len(y) > 1 and np.std(y) > 0:
        metrics["r2"] = float(r2_score(y, y_pred))
        metrics["explained_variance"] = float(explained_variance_score(y, y_pred))
    else:
        metrics["warnings"].append("Variance is 0 or less than 2 samples, R2 not calculated")

    return metrics

def build_confusion_matrix_table(y_true: pd.Series, y_pred: pd.Series) -> pd.DataFrame:
    labels = sorted(list(set(y_true.unique()) | set(y_pred.unique())))
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    df = pd.DataFrame(cm, index=[f"True_{l}" for l in labels], columns=[f"Pred_{l}" for l in labels])
    return df

def build_classification_report_table(y_true: pd.Series, y_pred: pd.Series) -> pd.DataFrame:
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    df = pd.DataFrame(report).transpose()
    return df

def evaluate_model_by_split(model, preprocessor: BasicPreprocessor, dataset: pd.DataFrame, target_column: str, split_manifest: dict, task_type: str) -> tuple[dict, dict]:
    train_indices = split_manifest.get("train_indices", [])
    test_indices = split_manifest.get("test_indices", [])

    if not test_indices:
        return {}, {"warnings": ["No test indices in split manifest"]}

    X_test = dataset.iloc[test_indices].drop(columns=[target_column])
    y_test = dataset.iloc[test_indices][target_column]

    try:
        X_test_trans = preprocessor.transform(X_test)
    except Exception as e:
        return {}, {"warnings": [f"Transform error: {str(e)}"]}

    if task_type == "classification":
        metrics = evaluate_classification_model(model, preprocessor, X_test_trans, y_test)
    else:
        metrics = evaluate_regression_model(model, preprocessor, X_test_trans, y_test)

    return metrics, {"passed": True, "warnings": metrics.get("warnings", [])}

def build_model_evaluation_report(model, preprocessor: BasicPreprocessor, dataset: pd.DataFrame, target_column: str, task_type: str, split_manifest: dict | None = None) -> tuple[dict, dict]:
    if split_manifest:
        return evaluate_model_by_split(model, preprocessor, dataset, target_column, split_manifest, task_type)

    # Evaluate on full dataset if no split provided
    X = dataset.drop(columns=[target_column])
    y = dataset[target_column]

    try:
        X_trans = preprocessor.transform(X)
    except Exception as e:
        return {}, {"warnings": [f"Transform error: {str(e)}"]}

    if task_type == "classification":
        metrics = evaluate_classification_model(model, preprocessor, X_trans, y)
    else:
        metrics = evaluate_regression_model(model, preprocessor, X_trans, y)

    return metrics, {"passed": True, "warnings": metrics.get("warnings", [])}
