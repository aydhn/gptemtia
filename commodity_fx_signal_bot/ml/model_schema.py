import pandas as pd
from dataclasses import dataclass, asdict
from .model_labels import is_classification_task

@dataclass
class FeatureSchema:
    feature_columns: list[str]
    numeric_columns: list[str]
    categorical_columns: list[str]
    dropped_columns: list[str]
    feature_count: int
    warnings: list[str]

@dataclass
class TargetSchema:
    target_column: str
    target_type: str
    class_labels: list[str]
    target_distribution: dict
    missing_ratio: float
    warnings: list[str]

def infer_feature_schema(X: pd.DataFrame) -> FeatureSchema:
    warnings = []
    numeric_columns = list(X.select_dtypes(include=['number']).columns)
    categorical_columns = list(X.select_dtypes(include=['object', 'category']).columns)

    # Check for high cardinality
    for col in categorical_columns:
        if X[col].nunique() > 100:
            warnings.append(f"High cardinality feature: {col} ({X[col].nunique()} unique values)")

    return FeatureSchema(
        feature_columns=list(X.columns),
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
        dropped_columns=[],
        feature_count=len(X.columns),
        warnings=warnings
    )

def infer_target_schema(y: pd.Series, task_type: str, target_column: str) -> TargetSchema:
    warnings = []
    missing_ratio = float(y.isna().mean()) if len(y) > 0 else 1.0

    if len(y) == 0:
        warnings.append("Empty target series")
        return TargetSchema(target_column, task_type, [], {}, 1.0, warnings)

    class_labels = []
    target_distribution = {}

    if is_classification_task(task_type):
        class_labels = [str(x) for x in y.dropna().unique()]
        target_distribution = y.value_counts(normalize=True).to_dict()
        if len(class_labels) < 2:
            warnings.append(f"Target has less than 2 classes: {class_labels}")
    else:
        desc = y.describe()
        target_distribution = {
            "mean": float(desc.get("mean", 0)),
            "std": float(desc.get("std", 0)),
            "min": float(desc.get("min", 0)),
            "max": float(desc.get("max", 0))
        }

    return TargetSchema(
        target_column=target_column,
        target_type=task_type,
        class_labels=class_labels,
        target_distribution=target_distribution,
        missing_ratio=missing_ratio,
        warnings=warnings
    )

def feature_schema_to_dict(schema: FeatureSchema) -> dict:
    return asdict(schema)

def target_schema_to_dict(schema: TargetSchema) -> dict:
    return asdict(schema)

def validate_feature_target_schema(X: pd.DataFrame, y: pd.Series, task_type: str) -> dict:
    warnings = []
    passed = True

    if y.name in X.columns:
        warnings.append(f"Target column '{y.name}' found in feature matrix X")
        passed = False

    if len(X) != len(y):
        warnings.append(f"Length mismatch: X has {len(X)} rows, y has {len(y)} rows")
        passed = False

    if len(y.dropna()) == 0:
        warnings.append("Target series contains only NaN values")
        passed = False

    return {"passed": passed, "warnings": warnings}
