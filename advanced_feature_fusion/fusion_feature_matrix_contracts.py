"""Fusion Feature Matrix Contracts.

Defines structural and behavioral contracts for multi-domain fusion matrices.
Strictly non-signal, research use only.
"""

from typing import Any, Dict, List
import pandas as pd
from advanced_feature_fusion.no_lookahead_fusion_guard import (
    validate_no_forbidden_fusion_columns,
    validate_no_full_article_columns,
)


FUSION_MATRIX_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "FMC-001-TIMESTAMP",
        "name": "Timestamp Monotonicity and UTC Contract",
        "requirement": "Matrix must have a monotonically increasing, UTC-aware timestamp index or column.",
        "severity": "CRITICAL",
    },
    {
        "contract_id": "FMC-002-NON-SIGNAL",
        "name": "Zero Signal/Target Invariant",
        "requirement": "Matrix must contain zero buy/sell signals, predictions, targets, or labels.",
        "severity": "CRITICAL",
    },
    {
        "contract_id": "FMC-003-NO-ARTICLE-TEXT",
        "name": "Metadata-Only News Invariant",
        "requirement": "Matrix must contain zero full article text, body, html, or embeddings.",
        "severity": "CRITICAL",
    },
    {
        "contract_id": "FMC-004-BACKWARD-JOIN",
        "name": "Backward-Only AsOf Join Alignment",
        "requirement": "All fused macro/calendar/news features must have release/publication timestamp <= base timestamp.",
        "severity": "CRITICAL",
    },
    {
        "contract_id": "FMC-005-IMMUTABILITY",
        "name": "Source Input Immutability",
        "requirement": "Source DataFrames must not be modified in-place during matrix construction.",
        "severity": "HIGH",
    },
]


def get_fusion_feature_matrix_contracts() -> List[Dict[str, Any]]:
    """Return list of fusion feature matrix contracts."""
    return [dict(c) for c in FUSION_MATRIX_CONTRACTS]


def get_fusion_feature_matrix_contracts_summary() -> Dict[str, Any]:
    """Summary of matrix contracts."""
    contracts = get_fusion_feature_matrix_contracts()
    return {
        "contract_count": len(contracts),
        "contract_ids": [c["contract_id"] for c in contracts],
        "zero_signal_mandate": True,
        "metadata_only_mandate": True,
    }


def validate_fusion_feature_matrix_contract(df: pd.DataFrame, timestamp_col: str = "timestamp") -> List[str]:
    """Validate DataFrame against matrix contracts and return list of violations."""
    violations = []
    if df.empty:
        return ["Matrix is empty."]

    # Check timestamp
    if timestamp_col in df.columns:
        ts = pd.to_datetime(df[timestamp_col], utc=True)
        if not ts.is_monotonic_increasing:
            violations.append("Timestamp column is not monotonically increasing.")
    elif isinstance(df.index, pd.DatetimeIndex):
        if not df.index.is_monotonic_increasing:
            violations.append("DatetimeIndex is not monotonically increasing.")
    else:
        violations.append(f"Missing required timestamp column '{timestamp_col}' or DatetimeIndex.")

    # Check forbidden columns
    try:
        res_forbidden = validate_no_forbidden_fusion_columns(df)
        if isinstance(res_forbidden, dict) and not res_forbidden.get("valid", True):
            violations.append(res_forbidden.get("message", "Forbidden columns detected."))
    except ValueError as e:
        violations.append(str(e))

    # Check full article columns
    try:
        res_article = validate_no_full_article_columns(df)
        if isinstance(res_article, dict) and not res_article.get("valid", True):
            violations.append(res_article.get("message", "Full article columns detected."))
    except ValueError as e:
        violations.append(str(e))

    return violations
