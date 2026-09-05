import re
from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import FORBIDDEN_OUTPUT_WORDS


GUARD_RULES = [
    {
        "rule_id": "guard_no_negative_shift",
        "name": "No Negative Shift Guard",
        "description": "Kaynak kodda shift(-k) veya negatif shift çağrısının kullanımını yasaklar.",
        "severity": "CRITICAL",
    },
    {
        "rule_id": "guard_no_forward_returns",
        "name": "No Forward Return Columns Guard",
        "description": "DataFrame kolonlarında future_return, forward_return, next_return tespit eder.",
        "severity": "CRITICAL",
    },
    {
        "rule_id": "guard_no_target_label_prediction",
        "name": "No Target/Label/Prediction Columns Guard",
        "description": "DataFrame kolonlarında target, label, prediction, signal vb. tespit eder.",
        "severity": "CRITICAL",
    },
]


def validate_feature_grid_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    findings = []
    # Pattern to catch .shift(-1) or .shift(-n) or shift( -
    matches = re.findall(r"\.shift\s*\(\s*-[0-9]+\s*\)", source_text)
    if matches:
        findings.append(f"Negatif shift (lookahead) tespit edildi: {matches}")

    return {
        "valid": len(findings) == 0,
        "negative_shift_detected": len(findings) > 0,
        "findings": findings,
    }


def validate_feature_grid_no_forward_return_columns(df: pd.DataFrame) -> Dict[str, Any]:
    findings = []
    forbidden_terms = ["future_return", "forward_return", "next_return", "fwd_ret", "future_ret"]

    for col in df.columns:
        col_lower = str(col).lower()
        for term in forbidden_terms:
            if term in col_lower:
                findings.append(f"Gelecek getiri kolonu tespit edildi: '{col}' (eşleşen: '{term}')")

    return {
        "valid": len(findings) == 0,
        "forward_returns_detected": len(findings) > 0,
        "findings": findings,
    }


def validate_feature_grid_no_target_label_prediction_columns(df: pd.DataFrame) -> Dict[str, Any]:
    findings = []

    for col in df.columns:
        col_lower = str(col).lower()
        for forbidden in FORBIDDEN_OUTPUT_WORDS:
            tokens = col_lower.split("_")
            if forbidden in tokens or forbidden in col_lower:
                findings.append(f"Yasaklı hedef/tahmin/sinyal kolonu tespit edildi: '{col}' (eşleşen: '{forbidden}')")

    return {
        "valid": len(findings) == 0,
        "forbidden_columns_detected": len(findings) > 0,
        "findings": findings,
    }


def build_feature_grid_no_lookahead_guard_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(GUARD_RULES)
    summary = summarize_feature_grid_no_lookahead_guard(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_no_lookahead_guard(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_guard_rules": 0, "status": "EMPTY"}

    return {
        "total_guard_rules": len(df),
        "strictly_backward_looking": True,
        "lookahead_forbidden": True,
        "status": "ACTIVE",
    }
