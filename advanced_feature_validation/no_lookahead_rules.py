"""No-Lookahead Guard and Leakage Detection Rules.

Detects negative shift operations, forward returns, and future timestamp relationships.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import re
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

LOOKAHEAD_PATTERNS = [
    r"\.shift\(\s*-\s*\d+\s*\)",
    r"\.pct_change\(\s*-\s*\d+\s*\)",
    r"\blead\(",
    r"\.rolling\(.*\)\.mean\(\)\.shift\(-",
]

FORWARD_RETURN_COLUMNS = [
    "future_return",
    "forward_return",
    "next_return",
    "fwd_return",
    "return_next",
    "fwd_ret",
    "target_return",
    "future",
    "lead",
]


def build_no_lookahead_rule_registry(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of no-lookahead rules."""
    active_profile = profile or get_default_feature_validation_profile()

    records = [
        {
            "rule_name": "no_negative_shift",
            "target_type": "source_code_and_expressions",
            "severity": "validation_critical",
            "description": "Scans computation logic for negative shift index lookahead.",
            "patterns": LOOKAHEAD_PATTERNS,
            "action": "flag_finding_block_downstream",
        },
        {
            "rule_name": "no_forward_return_columns",
            "target_type": "dataframe_columns",
            "severity": "validation_critical",
            "description": "Scans DataFrame columns for forward-looking return series.",
            "patterns": FORWARD_RETURN_COLUMNS,
            "action": "flag_finding_block_downstream",
        },
        {
            "rule_name": "no_future_timestamp_relation",
            "target_type": "timestamp_series_comparison",
            "severity": "validation_critical",
            "description": "Ensures context timestamps do not exceed base event timestamps (context_ts <= base_ts).",
            "patterns": ["context_ts > base_ts"],
            "action": "flag_finding_block_downstream",
        },
        {
            "rule_name": "no_lead_window_functions",
            "target_type": "window_aggregation",
            "severity": "validation_critical",
            "description": "Prohibits forward lead window operations and future rolling slices.",
            "patterns": ["lead()", "future_window"],
            "action": "flag_finding_block_downstream",
        },
        {
            "rule_name": "no_future_event_leakage",
            "target_type": "event_timestamp_ordering",
            "severity": "validation_critical",
            "description": "Prohibits future scheduled events leaking into historical bars prior to publication.",
            "patterns": ["future_event_date"],
            "action": "flag_finding_block_downstream",
        },
    ]


    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "total_rules": len(records),
        "leakage_tolerance": "zero",
        "current_phase": active_profile.current_phase,
        "non_signal": True,
    }
    return df, summary


def validate_no_negative_shift_usage(source_text: str) -> Dict[str, Any]:
    """Scan source code text for negative shift or lead operations."""
    violations = []
    for pat in LOOKAHEAD_PATTERNS:
        matches = list(re.finditer(pat, source_text, re.IGNORECASE))
        for m in matches:
            violations.append({
                "pattern": pat,
                "matched_text": m.group(0),
                "position": m.start(),
                "severity": "validation_critical",
            })

    passed = len(violations) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "violations": violations,
        "violation_count": len(violations),
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_no_forward_return_columns(df: pd.DataFrame) -> Dict[str, Any]:
    """Scan DataFrame columns for forward return names."""
    found = []
    for col in df.columns:
        c_lower = str(col).lower()
        for fwd in FORWARD_RETURN_COLUMNS:
            if fwd in c_lower:
                found.append({
                    "column": col,
                    "matched_pattern": fwd,
                    "severity": "validation_critical",
                })

    passed = len(found) == 0
    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "violations": found,
        "violation_count": len(found),
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def validate_no_future_timestamp_relation(
    base_ts: pd.Series, context_ts: pd.Series
) -> Dict[str, Any]:
    """Verify that context timestamp is strictly less than or equal to base timestamp."""
    b_series = pd.to_datetime(base_ts)
    c_series = pd.to_datetime(context_ts)

    # Valid comparisons where both are non-null
    valid_mask = b_series.notna() & c_series.notna()
    leakage_mask = valid_mask & (c_series > b_series)

    leakage_count = int(leakage_mask.sum())
    passed = leakage_count == 0

    return {
        "passed": passed,
        "status_label": "validation_pass" if passed else "validation_fail",
        "total_compared": int(valid_mask.sum()),
        "leakage_count": leakage_count,
        "leakage_detected": not passed,
        "message": "All context timestamps are on or before base timestamps."
        if passed
        else f"Detected {leakage_count} occurrences where context_ts > base_ts (future leakage).",
        "manual_review_required": not passed,
        "destructive_action_allowed": False,
    }


def summarize_no_lookahead_rules(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize lookahead compliance for a feature DataFrame."""
    res_fwd = validate_no_forward_return_columns(df)
    return {
        "passed": res_fwd["passed"],
        "status": res_fwd["status_label"],
        "forward_return_columns_found": res_fwd["violation_count"],
        "manual_review_required": res_fwd["manual_review_required"],
    }


def get_no_lookahead_rules() -> List[Dict[str, Any]]:
    df, _ = build_no_lookahead_rule_registry()
    return df.to_dict("records")


def check_no_lookahead_rules(df: pd.DataFrame) -> Dict[str, Any]:
    res = validate_no_forward_return_columns(df)
    return {
        "is_valid": res["passed"],
        "passed": res["passed"],
        "violations": res["violations"],
    }

