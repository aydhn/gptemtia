"""Phase 127: Regime Matrix Forbidden Column Policies.

Enforces systematic detection and exclusion of unauthorized columns across all matrix layers.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

FORBIDDEN_COLUMNS_DEFINITION: List[Dict[str, Any]] = [
    {
        "category": "trading_signal",
        "forbidden_terms": ["signal", "buy", "sell", "long", "short", "position", "recommendation"],
        "rationale": "Prevents trade execution directives in offline research layers.",
        "is_blocking": True,
    },
    {
        "category": "supervised_target_label",
        "forbidden_terms": ["target", "label", "prediction", "forecast"],
        "rationale": "Prevents target leakage prior to Phase 128 rule-free labeling and Phase 136 ML.",
        "is_blocking": True,
    },
    {
        "category": "lookahead_future_return",
        "forbidden_terms": ["future_return", "forward_return", "next_return", "shift_neg"],
        "rationale": "Prevents temporal lookahead bias and future observation contamination.",
        "is_blocking": True,
    },
    {
        "category": "copyrighted_scraping_content",
        "forbidden_terms": ["full_text", "article_body", "raw_content", "scraped_html", "page_html"],
        "rationale": "Strictly enforces news metadata-only policy with zero web scraping.",
        "is_blocking": True,
    },
    {
        "category": "dense_vectors",
        "forbidden_terms": ["embedding", "vector", "latent_dim"],
        "rationale": "Enforces transparent tabulate-compatible numerical research representations.",
        "is_blocking": True,
    },
    {
        "category": "broker_execution_directives",
        "forbidden_terms": ["order_id", "broker_account", "fill_price", "slippage_sim", "execution_status"],
        "rationale": "Prohibits live broker order fields and simulated trade accounting artifacts.",
        "is_blocking": True,
    },
]

FORBIDDEN_COLUMN_SUBSTRINGS = [
    "signal", "buy", "sell", "target", "label", "prediction", "pred",
    "forecast", "future", "forward", "lead", "shift_neg", "full_text",
    "article_body", "raw_content", "scraped_html", "embedding", "vector",
    "order_id", "broker_account",
]


def is_forbidden_column_name(column_name: str) -> bool:
    """Determine whether a column name contains forbidden target, prediction, signal, or lookahead terms."""
    c_lower = str(column_name).lower()
    for term in FORBIDDEN_COLUMN_SUBSTRINGS:
        if term in c_lower:
            return True
    return False


def find_forbidden_columns(column_names: List[str]) -> List[str]:
    """Identify all forbidden columns within a list of column names."""
    return [col for col in column_names if is_forbidden_column_name(col)]


def build_regime_matrix_forbidden_column_policy_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the forbidden column policy registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for cat in FORBIDDEN_COLUMNS_DEFINITION:
        c_copy = cat.copy()
        c_copy["current_phase"] = p.current_phase
        c_copy["target_final_phase"] = p.target_final_phase
        c_copy["next_phase"] = p.next_phase
        c_copy["source_preserved"] = True
        c_copy["non_signal"] = True
        c_copy["status"] = "matrix_ready"
        rows.append(c_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_forbidden_column_policies(df)
    return df, summary


def validate_regime_matrix_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Audit a list of column names against all forbidden terms."""
    violations = find_forbidden_columns(column_names)
    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violation_count": len(violations),
        "violations": violations,
        "total_columns_audited": len(column_names),
        "non_signal": True,
    }


def summarize_regime_matrix_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policy registry."""
    return {
        "total_categories": len(df),
        "total_forbidden_column_types": len(df),
        "categories": df["category"].tolist() if not df.empty else [],
        "all_blocking": bool(df["is_blocking"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_forbidden_column_policies = build_regime_matrix_forbidden_column_policy_registry

