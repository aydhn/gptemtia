from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile

FORBIDDEN_SIGNAL_COLUMNS = {
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
}

FORBIDDEN_LOOKAHEAD_PATTERNS = ["_future_", "_lead_", "_next_"]


def validate_no_signal_columns(df: pd.DataFrame) -> Dict[str, Any]:
    cols = [c.lower() for c in df.columns]
    violating = [c for c in cols if c in FORBIDDEN_SIGNAL_COLUMNS]
    return {
        "valid": len(violating) == 0,
        "violating_columns": violating,
        "total_columns_checked": len(cols),
        "rule": "no_signal_columns",
    }


def validate_no_lookahead_columns(df: pd.DataFrame) -> Dict[str, Any]:
    violating = []
    for c in df.columns:
        c_lower = c.lower()
        if any(pat in c_lower for pat in FORBIDDEN_LOOKAHEAD_PATTERNS):
            violating.append(c)
    return {
        "valid": len(violating) == 0,
        "violating_columns": violating,
        "total_columns_checked": len(df.columns),
        "rule": "no_lookahead_columns",
    }


def validate_feature_dataframe(
    df: pd.DataFrame,
    feature_columns: List[str],
) -> Dict[str, Any]:
    sig_check = validate_no_signal_columns(df)
    look_check = validate_no_lookahead_columns(df)

    missing = [f for f in feature_columns if f not in df.columns]

    all_valid = sig_check["valid"] and look_check["valid"] and len(missing) == 0
    return {
        "valid": all_valid,
        "signal_columns_valid": sig_check["valid"],
        "lookahead_valid": look_check["valid"],
        "missing_features": missing,
        "violating_signal_columns": sig_check["violating_columns"],
        "violating_lookahead_columns": look_check["violating_columns"],
        "total_rows": len(df),
        "total_columns": len(df.columns),
    }


def build_feature_validation_rule_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_id": "fvr_01_no_signal_columns",
            "rule_name": "No Signal Column Names Enforcement",
            "severity": "CRITICAL",
            "description": "signal, buy, sell, long, short, position, target, label isimli kolonlar kesinlikle yasaktır.",
            "enforced": True,
        },
        {
            "rule_id": "fvr_02_no_lookahead_shifts",
            "rule_name": "No Forward Lookahead Shift Enforcement",
            "severity": "CRITICAL",
            "description": "shift(-1) ve geleceğe dönük veri sızıntısı kesinlikle engellenir.",
            "enforced": True,
        },
        {
            "rule_id": "fvr_03_non_destructive_transform",
            "rule_name": "Non-destructive Copy Transform Enforcement",
            "severity": "HIGH",
            "description": "Girdi veri çerçevesi in-place değiştirilemez; df.copy() ile yeni dataframe döner.",
            "enforced": True,
        },
        {
            "rule_id": "fvr_04_window_warmup_policy",
            "rule_name": "Warmup NaN Preservation Policy",
            "severity": "MEDIUM",
            "description": "Pencere ısınma periyodundaki NaN değerler sessizce sentetik veriyle doldurulamaz.",
            "enforced": True,
        },
        {
            "rule_id": "fvr_05_input_contract_field_check",
            "rule_name": "Input Contract Schema Compliance",
            "severity": "HIGH",
            "description": "Feature hesaplaması öncesi zorunlu girdi alanlarının varlığı kontrol edilir.",
            "enforced": True,
        },
    ]

    df = pd.DataFrame.from_records(rules)
    summary = summarize_feature_validation_rules(df)
    return df, summary


def summarize_feature_validation_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty and "enforced" in df.columns else True,
        "critical_rules_count": int((df["severity"] == "CRITICAL").sum()) if not df.empty and "severity" in df.columns else 0,
        "non_signal": True,
    }
