"""Phase 127: Regime Matrix Namespace Standards and Key Generation.

Enforces lowercase snake_case standards with mandatory 'regime_matrix_' prefixes,
strict avoidance of forbidden terms, and dedicated 'regime_state_' prefixes for state schemas.
"""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

FORBIDDEN_TERMS = [
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
    "future_return",
    "forward_return",
    "next_return",
]

NAMESPACE_CONVENTIONS: List[Dict[str, Any]] = [
    {
        "namespace_type": "feature_matrix_key",
        "pattern": "^regime_matrix__[a-z0-9_]+__[a-z0-9_]+__[a-z0-9_]+$",
        "example": "regime_matrix__fx__eur_usd__trend_context",
        "description": "Standard identifier for a regime feature matrix column.",
        "status": "matrix_ready",
        "non_signal": True,
    },
    {
        "namespace_type": "factor_matrix_key",
        "pattern": "^regime_matrix__factor__[a-z0-9_]+__[a-z0-9_]+$",
        "example": "regime_matrix__factor__volatility__compression_ratio",
        "description": "Standard identifier for an aligned factor in the regime matrix.",
        "status": "matrix_ready",
        "non_signal": True,
    },
    {
        "namespace_type": "context_matrix_key",
        "pattern": "^regime_matrix__context__[a-z0-9_]+__[a-z0-9_]+$",
        "example": "regime_matrix__context__macro__inflation_trend",
        "description": "Standard identifier for an environmental context indicator.",
        "status": "matrix_ready",
        "non_signal": True,
    },
    {
        "namespace_type": "state_dataset_key",
        "pattern": "^regime_state__[a-z0-9_]+__[a-z0-9_]+$",
        "example": "regime_state__candidate_context__volatility_high",
        "description": "Standard identifier for a candidate state dataset row or field.",
        "status": "matrix_ready",
        "non_signal": True,
    },
]


def build_regime_matrix_key(entity_type: str, symbol_or_entity: str, feature_name: str) -> str:
    """Construct a canonical regime feature matrix key."""
    clean_entity = re.sub(r"[^a-zA-Z0-9_]", "_", entity_type).strip("_").lower()
    clean_sym = re.sub(r"[^a-zA-Z0-9_]", "_", symbol_or_entity).strip("_").lower()
    clean_feat = re.sub(r"[^a-zA-Z0-9_]", "_", feature_name).strip("_").lower()
    return f"regime_matrix__{clean_entity}__{clean_sym}__{clean_feat}"


def validate_regime_matrix_key(key: str) -> Dict[str, Any]:
    """Validate a regime matrix key against namespace and non-signal standards."""
    key_clean = key.strip().lower()

    starts_correctly = key_clean.startswith("regime_matrix_") or key_clean.startswith("regime_state_")

    is_snake_case = bool(re.match(r"^[a-z0-9_]+$", key_clean))

    forbidden_hits = [term for term in FORBIDDEN_TERMS if term in key_clean]

    is_valid = starts_correctly and is_snake_case and len(forbidden_hits) == 0

    return {
        "key": key,
        "is_valid": is_valid,
        "starts_correctly": starts_correctly,
        "is_snake_case": is_snake_case,
        "forbidden_hits": forbidden_hits,
        "non_signal": True,
    }


def build_regime_matrix_namespace_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the regime matrix namespace convention registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for conv in NAMESPACE_CONVENTIONS:
        c_copy = conv.copy()
        c_copy["current_phase"] = p.current_phase
        c_copy["target_final_phase"] = p.target_final_phase
        c_copy["next_phase"] = p.next_phase
        c_copy["source_preserved"] = True
        rows.append(c_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_namespace(df)
    return df, summary


def summarize_regime_matrix_namespace(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime matrix namespace registry."""
    return {
        "total_conventions": len(df),
        "namespace_types": df["namespace_type"].tolist() if not df.empty else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "mandatory_prefix": "regime_matrix_",
        "state_prefix": "regime_state_",
        "forbidden_terms_count": len(FORBIDDEN_TERMS),
        "status": "matrix_ready",
    }
