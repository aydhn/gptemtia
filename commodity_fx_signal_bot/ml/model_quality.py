import pandas as pd
from .training_config import MLTrainingProfile

def check_training_data_sufficiency(X_train: pd.DataFrame, y_train: pd.Series, profile: MLTrainingProfile) -> dict:
    warnings = []
    passed = True

    if len(X_train) < profile.min_train_rows:
        warnings.append(f"Training data ({len(X_train)} rows) is less than minimum ({profile.min_train_rows})")
        passed = False

    return {"passed": passed, "warnings": warnings}

def check_target_validity(y: pd.Series, task_type: str) -> dict:
    warnings = []
    passed = True

    if len(y.dropna()) == 0:
        warnings.append("Target series contains only NaN values")
        passed = False

    if task_type == "classification":
        n_classes = y.dropna().nunique()
        if n_classes < 2:
            warnings.append(f"Classification target has {n_classes} classes, minimum 2 required")
            passed = False

    return {"passed": passed, "warnings": warnings}

def check_model_metric_sanity(metrics: dict, task_type: str) -> dict:
    warnings = []
    passed = True

    if task_type == "classification":
        if "balanced_accuracy" in metrics and metrics["balanced_accuracy"] < 0.5:
            warnings.append("Balanced accuracy is below 0.5 (worse than random)")
    else:
        if "r2" in metrics and metrics["r2"] < 0:
            warnings.append("R2 score is negative (worse than mean prediction)")

    return {"passed": passed, "warnings": warnings}

def check_cv_consistency(cv_df: pd.DataFrame) -> dict:
    warnings = []
    passed = True

    if cv_df.empty or "metric_primary" not in cv_df:
        return {"passed": True, "warnings": ["No CV data for consistency check"]}

    std = cv_df["metric_primary"].std()
    mean = cv_df["metric_primary"].mean()

    if std > 0.2:
        warnings.append(f"CV metrics show high variance (std: {std:.4f})")

    if mean < 0:
        warnings.append(f"CV mean metric is negative ({mean:.4f})")

    return {"passed": passed, "warnings": warnings}

def check_model_vs_dummy(metrics: dict, dummy_metrics: dict | None = None) -> dict:
    warnings = []
    passed = True

    if not dummy_metrics:
        return {"passed": True, "warnings": []}

    if "balanced_accuracy" in metrics and "balanced_accuracy" in dummy_metrics:
        if metrics["balanced_accuracy"] < dummy_metrics["balanced_accuracy"]:
            warnings.append(f"Model balanced accuracy ({metrics['balanced_accuracy']:.4f}) is worse than dummy ({dummy_metrics['balanced_accuracy']:.4f})")

    if "r2" in metrics and "r2" in dummy_metrics:
        if metrics["r2"] < dummy_metrics["r2"]:
            warnings.append(f"Model R2 ({metrics['r2']:.4f}) is worse than dummy ({dummy_metrics['r2']:.4f})")

    return {"passed": passed, "warnings": warnings}

def check_for_forbidden_live_terms_in_model_metadata(metadata: dict) -> dict:
    warnings = []
    passed = True

    forbidden_terms = [
        "LIVE_ORDER", "BROKER_ORDER", "SEND_ORDER", "EXECUTE_TRADE",
        "REAL_POSITION", "LIVE_POSITION", "MARKET_ORDER", "LIMIT_ORDER",
        "LIVE_SIGNAL", "DEPLOYED_LIVE_MODEL"
    ]

    metadata_str = str(metadata).upper()

    for term in forbidden_terms:
        if term in metadata_str:
            warnings.append(f"Forbidden live term found in metadata: {term}")
            passed = False

    return {"passed": passed, "warnings": warnings}

def build_model_quality_report(
    training_result: dict,
    evaluation_report: dict,
    cv_summary: dict,
    leakage_audit: dict | None = None,
    dataset_quality: dict | None = None,
) -> dict:
    warnings = []
    passed = True

    # Just basic checks
    cv_consistency = cv_summary.get("warnings", [])
    if cv_consistency:
        warnings.extend(cv_consistency)

    metrics_sanity = check_model_metric_sanity(evaluation_report, training_result.get("task_type", "classification"))
    if not metrics_sanity["passed"]:
        passed = False
    if metrics_sanity["warnings"]:
        warnings.extend(metrics_sanity["warnings"])

    live_terms = check_for_forbidden_live_terms_in_model_metadata(training_result)
    if not live_terms["passed"]:
        passed = False
    if live_terms["warnings"]:
        warnings.extend(live_terms["warnings"])

    leakage_passed = leakage_audit.get("passed", True) if leakage_audit else True
    dataset_quality_passed = dataset_quality.get("passed", True) if dataset_quality else True

    return {
        "training_data_sufficient": True, # checked before
        "target_valid": True, # checked before
        "metric_sanity_passed": metrics_sanity["passed"],
        "cv_consistency_passed": len(cv_consistency) == 0,
        "leakage_audit_passed": leakage_passed,
        "dataset_quality_passed": dataset_quality_passed,
        "forbidden_live_terms_found": not live_terms["passed"],
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }
