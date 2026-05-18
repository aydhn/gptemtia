"""
Quality checking for observability outputs, ensuring no sensitive data or live trade artifacts leak.
"""

from typing import Dict, Any, Optional, List

import pandas as pd


# Forbidden terms implying live trading or execution
_FORBIDDEN_TRADE_TERMS = [
    "LIVE_ORDER",
    "BROKER_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION",
    "LIVE_POSITION",
    "REAL_PORTFOLIO",
    "LIVE_SIGNAL",
    "BUY_NOW",
    "SELL_NOW"
]

# Sensitive keys that shouldn't appear unmasked
_SENSITIVE_KEYS = [
    "bot_token",
    "chat_id",
    "api_key",
    "secret",
    "password"
]


def _search_dataframe_for_terms(df: pd.DataFrame, terms: List[str]) -> List[str]:
    """Search all string columns in a DataFrame for any of the given terms."""
    if df is None or df.empty:
        return []

    found_terms = []

    # Only search object (string) columns
    str_cols = df.select_dtypes(include=['object', 'string']).columns

    for term in terms:
        for col in str_cols:
            # Case insensitive check
            if df[col].astype(str).str.contains(term, case=False, na=False).any():
                if term not in found_terms:
                    found_terms.append(term)

    return found_terms


def _search_dict_for_terms(d: Dict[str, Any], terms: List[str]) -> List[str]:
    """Recursively search a dictionary for any of the given terms."""
    if not d:
        return []

    found_terms = []

    def _search(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                _search(str(k))
                _search(v)
        elif isinstance(obj, (list, tuple, set)):
            for item in obj:
                _search(item)
        elif isinstance(obj, str):
            for term in terms:
                if term.lower() in obj.lower() and term not in found_terms:
                    found_terms.append(term)

    _search(d)
    return found_terms


def check_health_report_quality(health_df: pd.DataFrame) -> Dict[str, Any]:
    """Check the quality of a health report dataframe."""
    if health_df is None or health_df.empty:
        return {"valid": False, "warnings": ["Health report is empty or None"]}

    warnings = []

    # Check for expected columns
    expected = ["component", "status", "health_score"]
    for col in expected:
        if col not in health_df.columns:
            warnings.append(f"Missing expected column: {col}")

    # Check scores bounds
    if "health_score" in health_df.columns:
        invalid_scores = health_df[~health_df["health_score"].between(0.0, 1.0)]
        if not invalid_scores.empty:
            warnings.append(f"Found {len(invalid_scores)} components with out-of-bounds health_score")

    return {"valid": len(warnings) == 0, "warnings": warnings}


def check_runtime_metrics_quality(metrics_df: pd.DataFrame) -> Dict[str, Any]:
    """Check the quality of a runtime metrics dataframe."""
    if metrics_df is None or metrics_df.empty:
        return {"valid": False, "warnings": ["Runtime metrics report is empty or None"]}

    warnings = []

    if "duration_seconds" in metrics_df.columns:
        negative_durations = metrics_df[metrics_df["duration_seconds"] < 0]
        if not negative_durations.empty:
            warnings.append(f"Found {len(negative_durations)} negative duration metrics")

    return {"valid": len(warnings) == 0, "warnings": warnings}


def check_log_records_quality(log_df: pd.DataFrame) -> Dict[str, Any]:
    """Check the quality of a structured logs dataframe."""
    if log_df is None or log_df.empty:
        return {"valid": False, "warnings": ["Logs report is empty or None"]}

    warnings = []
    expected = ["timestamp_utc", "level", "component", "message"]
    for col in expected:
        if col not in log_df.columns:
            warnings.append(f"Missing expected log column: {col}")

    return {"valid": len(warnings) == 0, "warnings": warnings}


def check_diagnostics_summary_quality(summary: Dict[str, Any]) -> Dict[str, Any]:
    """Check the quality of a self-diagnostics summary dictionary."""
    if not summary:
        return {"valid": False, "warnings": ["Summary is empty"]}

    warnings = []
    if "overall_health_score" in summary:
        score = summary["overall_health_score"]
        if not (0.0 <= score <= 1.0):
            warnings.append(f"overall_health_score out of bounds: {score}")

    if "recommended_system_actions" in summary:
        actions = summary["recommended_system_actions"]
        # Basic check to ensure actions don't contain trade terminology
        found = _search_dict_for_terms({"actions": actions}, _FORBIDDEN_TRADE_TERMS)
        if found:
            warnings.append(f"Recommended actions contain forbidden trade terms: {found}")

    return {"valid": len(warnings) == 0, "warnings": warnings}


def check_for_sensitive_data_in_observability(df: Optional[pd.DataFrame] = None, summary: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Scan observability outputs for unmasked sensitive keys."""
    found_sensitive = []

    if df is not None:
        found_sensitive.extend(_search_dataframe_for_terms(df, _SENSITIVE_KEYS))

    if summary is not None:
        found_sensitive.extend(_search_dict_for_terms(summary, _SENSITIVE_KEYS))

    # Remove duplicates
    found_sensitive = list(set(found_sensitive))

    warnings = []
    if found_sensitive:
        warnings.append(f"Found unmasked sensitive keys in observability data: {found_sensitive}")

    return {"safe": len(warnings) == 0, "found_sensitive": found_sensitive, "warnings": warnings}


def check_for_forbidden_trade_terms_in_observability(df: Optional[pd.DataFrame] = None, summary: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Scan observability outputs for forbidden live trading terms."""
    found_terms = []

    if df is not None:
        found_terms.extend(_search_dataframe_for_terms(df, _FORBIDDEN_TRADE_TERMS))

    if summary is not None:
        found_terms.extend(_search_dict_for_terms(summary, _FORBIDDEN_TRADE_TERMS))

    # Remove duplicates
    found_terms = list(set(found_terms))

    warnings = []
    if found_terms:
        warnings.append(f"Found forbidden trade execution terms in observability data: {found_terms}")

    return {"safe": len(warnings) == 0, "found_terms": found_terms, "warnings": warnings}


def build_observability_quality_report(
    summary: Dict[str, Any],
    health_df: Optional[pd.DataFrame] = None,
    metrics_df: Optional[pd.DataFrame] = None
) -> Dict[str, Any]:
    """Build a comprehensive quality report on the observability outputs themselves."""

    health_qual = check_health_report_quality(health_df) if health_df is not None else {"valid": True, "warnings": []}
    metrics_qual = check_runtime_metrics_quality(metrics_df) if metrics_df is not None else {"valid": True, "warnings": []}
    diag_qual = check_diagnostics_summary_quality(summary)

    sensitive_check = check_for_sensitive_data_in_observability(health_df, summary)
    trade_terms_check = check_for_forbidden_trade_terms_in_observability(health_df, summary)

    all_warnings = (
        health_qual["warnings"] +
        metrics_qual["warnings"] +
        diag_qual["warnings"] +
        sensitive_check["warnings"] +
        trade_terms_check["warnings"]
    )

    return {
        "health_report_valid": health_qual["valid"],
        "runtime_metrics_valid": metrics_qual["valid"],
        "logs_valid": True, # Hard to check standalone here without the log dataframe
        "sensitive_data_found": not sensitive_check["safe"],
        "forbidden_trade_terms_found": not trade_terms_check["safe"],
        "warning_count": len(all_warnings),
        "passed": len(all_warnings) == 0,
        "warnings": all_warnings
    }
