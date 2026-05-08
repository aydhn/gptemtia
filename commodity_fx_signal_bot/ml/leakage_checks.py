import pandas as pd

def detect_target_columns_in_features(feature_columns: list[str]) -> dict:
    leaky_cols = [c for c in feature_columns if c.startswith("target_")]
    return {
        "passed": len(leaky_cols) == 0,
        "leaky_columns": leaky_cols
    }

def detect_future_named_columns(feature_columns: list[str]) -> dict:
    patterns = ["future_", "forward_", "next_", "result_", "net_pnl", "gross_pnl", "exit_"]
    leaky_cols = []
    for col in feature_columns:
        col_lower = col.lower()
        if any(p in col_lower for p in patterns):
             leaky_cols.append(col)

    return {
        "passed": len(leaky_cols) == 0,
        "leaky_columns": leaky_cols
    }

def detect_leaky_id_columns(feature_columns: list[str]) -> dict:
    leaky_cols = [c for c in feature_columns if c.endswith("_id") or "source_" in c.lower()]
    return {
        "passed": len(leaky_cols) == 0,
        "leaky_columns": leaky_cols
    }

def check_feature_target_timestamp_alignment(X: pd.DataFrame, y: pd.DataFrame) -> dict:
    if X.empty or y.empty:
         return {"passed": True, "details": "Empty frames"}

    # Check if indices match exactly
    match = X.index.equals(y.index)
    return {
         "passed": match,
         "details": "Indices match exactly" if match else "Indices differ"
    }

def check_target_horizon_overlap_with_split(dataset: pd.DataFrame, target_col: str, split_manifest: pd.DataFrame | None = None) -> dict:
    # A placeholder for future deeper checks if splits are provided as DataFrame
    return {"passed": True, "details": "Not fully implemented"}

def build_leakage_audit_report(X: pd.DataFrame, y: pd.DataFrame, metadata: dict | None = None) -> dict:
    feature_cols = list(X.columns)

    t_check = detect_target_columns_in_features(feature_cols)
    f_check = detect_future_named_columns(feature_cols)
    id_check = detect_leaky_id_columns(feature_cols)
    align_check = check_feature_target_timestamp_alignment(X, y)

    passed = t_check["passed"] and f_check["passed"] and id_check["passed"] and align_check["passed"]

    risk_score = 0
    if not t_check["passed"]: risk_score += 50
    if not f_check["passed"]: risk_score += 30
    if not id_check["passed"]: risk_score += 10
    if not align_check["passed"]: risk_score += 10

    warnings = []
    if risk_score > 0:
        warnings.append(f"Leakage risk detected! Score: {risk_score}")

    return {
        "passed": passed,
        "leakage_risk_score": risk_score,
        "target_columns_in_features": t_check["leaky_columns"],
        "future_named_columns": f_check["leaky_columns"],
        "leaky_id_columns": id_check["leaky_columns"],
        "timestamp_alignment_issues": not align_check["passed"],
        "warnings": warnings
    }
