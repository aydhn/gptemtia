# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Forbidden Column Policies."""

from typing import Any, Dict, List


FORBIDDEN_PATTERNS = [
    "target",
    "label",
    "forward_return",
    "future_price",
    "signal",
    "trade_recommendation",
    "order_size",
    "broker_",
    "article_body",
    "full_text",
    "raw_html",
    "embedding",
    "vector",
]


def get_ensemble_forbidden_column_patterns() -> List[str]:
    """Get list of forbidden substring patterns for column names in ensemble contracts.
    
    Returns:
        List[str]: List of forbidden patterns.
    """
    return list(FORBIDDEN_PATTERNS)


def check_columns_against_ensemble_policy(columns: List[str]) -> Dict[str, Any]:
    """Check a list of columns against the ensemble forbidden column policy.
    
    Args:
        columns: List of column names to check.
        
    Returns:
        Dict[str, Any]: Check result including violations and pass flag.
    """
    violations: List[str] = []
    for col in columns:
        col_lower = col.lower()
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in col_lower:
                violations.append(f"Column '{col}' violates forbidden pattern '{pattern}'")
                break
    
    return {
        "columns_checked": len(columns),
        "violations_count": len(violations),
        "violations": violations,
        "policy_passed": len(violations) == 0,
        "non_signal": True,
    }


def summarize_ensemble_forbidden_column_policy() -> Dict[str, Any]:
    """Summarize forbidden column policy.
    
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "policy_name": "ensemble_forbidden_column_policy_v140",
        "forbidden_patterns_count": len(FORBIDDEN_PATTERNS),
        "patterns": list(FORBIDDEN_PATTERNS),
        "enforced": True,
        "non_signal": True,
    }
