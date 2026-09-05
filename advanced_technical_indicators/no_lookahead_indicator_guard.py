from typing import Tuple, Dict, Any, List
import re
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

FORBIDDEN_COLUMNS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return"
]


def validate_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    # Look for shift(-...) in source text
    pattern = re.compile(r'\.shift\s*\(\s*-\s*\d+\s*\)')
    matches = pattern.findall(source_text)
    return {
        "valid": len(matches) == 0,
        "forbidden_matches": matches,
        "violation_count": len(matches),
    }


def validate_no_forward_return_columns(df: pd.DataFrame) -> Dict[str, Any]:
    violations = []
    for col in df.columns:
        cl = str(col).lower()
        if "forward" in cl or "future" in cl or "next_ret" in cl or "fwd_" in cl:
            violations.append(col)
    return {
        "valid": len(violations) == 0,
        "forward_columns": violations,
    }


def validate_no_target_label_prediction_columns(df: pd.DataFrame) -> Dict[str, Any]:
    violations = []
    for col in df.columns:
        cl = str(col).lower()
        for forbidden in FORBIDDEN_COLUMNS:
            if forbidden == cl or cl.startswith(f"{forbidden}_") or cl.endswith(f"_{forbidden}"):
                violations.append(col)
                break
    return {
        "valid": len(violations) == 0,
        "target_columns": violations,
    }


def build_no_lookahead_indicator_guard_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rows = [
        {"rule_name": "no_negative_shift", "description": "shift(-1) or negative lookahead shifts are strictly forbidden."},
        {"rule_name": "no_forward_returns", "description": "Future or forward-looking returns cannot be added to feature engine."},
        {"rule_name": "no_target_label_columns", "description": "Target, label, prediction, buy/sell signal columns are barred."},
        {"rule_name": "immutable_input_guard", "description": "All transformations must operate on df.copy() without in-place mutation."},
    ]
    df = pd.DataFrame(rows)
    df["status"] = "ACTIVE"
    summary = {
        "total_rules": len(df),
        "status": "READY",
        "current_phase": profile.current_phase,
    }
    return df, summary


def summarize_no_lookahead_guard(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "guard_active": True,
    }
