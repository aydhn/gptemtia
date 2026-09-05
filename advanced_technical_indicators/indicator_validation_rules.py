from typing import Tuple, Dict, Any, List
import numpy as np
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

FORBIDDEN_COLUMNS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return"
]


def validate_indicator_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    if not isinstance(df, pd.DataFrame):
        return {"valid": False, "error": "Input is not a pandas DataFrame"}
    if df.empty:
        return {"valid": False, "error": "DataFrame is empty"}
    return {"valid": True, "rows": len(df), "columns": list(df.columns)}


def validate_indicator_output_no_forbidden_columns(df: pd.DataFrame) -> Dict[str, Any]:
    forbidden_detected = []
    for col in df.columns:
        cl = str(col).lower()
        for forbidden in FORBIDDEN_COLUMNS:
            if forbidden == cl or cl.startswith(f"{forbidden}_") or cl.endswith(f"_{forbidden}"):
                forbidden_detected.append(col)
                break
    return {
        "valid": len(forbidden_detected) == 0,
        "violations": forbidden_detected,
    }


def validate_indicator_output_numeric_sanity(
    df: pd.DataFrame,
    output_fields: List[str],
) -> Dict[str, Any]:
    issues = []
    for f in output_fields:
        if f not in df.columns:
            continue
        s = df[f]
        inf_count = int(np.isinf(s).sum())
        if inf_count > 0:
            issues.append(f"Field '{f}' contains {inf_count} infinite values.")
    return {
        "valid": len(issues) == 0,
        "issues": issues,
    }


def build_indicator_validation_rule_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"rule_name": "no_forbidden_column_names", "description": "Output columns must never match signal/target/prediction keywords."},
        {"rule_name": "numeric_sanity_check", "description": "Feature outputs must not contain unhandled infinite values."},
        {"rule_name": "non_mutation_check", "description": "Functions must not alter original input DataFrame."},
        {"rule_name": "warmup_nan_tolerance", "description": "Initial window NaNs are valid and expected; not errors."},
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_rules": len(df),
        "status": "READY",
        "current_phase": profile.current_phase,
    }
    return df, summary


def summarize_indicator_validation_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "active": True,
    }
