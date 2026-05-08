import pandas as pd
from .dataset_config import MLDatasetProfile

def check_dataset_min_rows(dataset: pd.DataFrame, min_rows: int = 200) -> dict:
    passed = len(dataset) >= min_rows
    return {
        "passed": passed,
        "details": f"Row count {len(dataset)} vs min {min_rows}"
    }

def check_feature_nan_ratio(X: pd.DataFrame, max_nan_ratio: float = 0.35) -> dict:
    if X.empty:
        return {"passed": False, "ratio": 1.0}
    ratio = float(X.isna().mean().mean())
    return {
        "passed": ratio <= max_nan_ratio,
        "ratio": ratio
    }

def check_target_nan_ratio(y: pd.DataFrame, max_nan_ratio: float = 0.20) -> dict:
    if y.empty:
        return {"passed": False, "ratio": 1.0}
    # y might be a DataFrame of targets
    ratio = float(y.isna().mean().mean())
    return {
        "passed": ratio <= max_nan_ratio,
        "ratio": ratio
    }

def check_target_class_balance(y: pd.Series) -> dict:
    if y.empty or pd.api.types.is_numeric_dtype(y):
        return {"balance": {}, "note": "Not categorical or empty"}

    counts = y.value_counts(normalize=True).to_dict()
    return {"balance": counts}

def check_feature_variance(X: pd.DataFrame) -> dict:
    if X.empty:
        return {"low_variance_count": 0}

    numeric_X = X.select_dtypes(include='number')
    variances = numeric_X.var()
    low_var = variances[variances == 0].index.tolist()

    return {"low_variance_count": len(low_var), "low_variance_columns": low_var}

def check_duplicate_rows(dataset: pd.DataFrame) -> dict:
    dups = dataset.duplicated().sum()
    return {"passed": dups == 0, "duplicate_count": int(dups)}

def check_index_integrity(dataset: pd.DataFrame) -> dict:
    is_dt = pd.api.types.is_datetime64_any_dtype(dataset.index)
    dups = dataset.index.duplicated().sum()
    return {
        "is_datetime": is_dt,
        "duplicate_index_count": int(dups),
        "passed": is_dt and dups == 0
    }

def build_dataset_quality_report(X: pd.DataFrame, y: pd.DataFrame, dataset: pd.DataFrame, profile: MLDatasetProfile) -> dict:
    min_rows_chk = check_dataset_min_rows(dataset, profile.min_rows)
    f_nan_chk = check_feature_nan_ratio(X, profile.max_feature_nan_ratio)
    t_nan_chk = check_target_nan_ratio(y, profile.max_target_nan_ratio)
    var_chk = check_feature_variance(X)
    dup_row_chk = check_duplicate_rows(dataset)
    idx_chk = check_index_integrity(dataset)

    passed = (
        min_rows_chk["passed"] and
        f_nan_chk["passed"] and
        t_nan_chk["passed"] and
        dup_row_chk["passed"] and
        idx_chk["passed"]
    )

    warnings = []
    if not min_rows_chk["passed"]: warnings.append("Failed min rows check")
    if not f_nan_chk["passed"]: warnings.append(f"Failed feature NaN ratio check ({f_nan_chk['ratio']:.2f})")
    if not t_nan_chk["passed"]: warnings.append(f"Failed target NaN ratio check ({t_nan_chk['ratio']:.2f})")

    # Class balance for the first categorical target if any
    cat_targets = y.select_dtypes(exclude='number')
    balance = {}
    if not cat_targets.empty:
         balance = check_target_class_balance(cat_targets.iloc[:, 0]).get("balance", {})

    return {
        "row_count": len(dataset),
        "feature_count": len(X.columns),
        "target_count": len(y.columns),
        "min_rows_passed": min_rows_chk["passed"],
        "feature_nan_ratio": f_nan_chk["ratio"],
        "target_nan_ratio": t_nan_chk["ratio"],
        "low_variance_feature_count": var_chk["low_variance_count"],
        "duplicate_row_count": dup_row_chk["duplicate_count"],
        "target_class_balance": balance,
        "index_is_datetime": idx_chk["is_datetime"],
        "duplicate_index_count": idx_chk["duplicate_index_count"],
        "passed": passed,
        "warnings": warnings
    }
