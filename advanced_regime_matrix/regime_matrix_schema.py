"""Phase 127: Regime Matrix Schema Definition and Validation.

Defines standard column schemas and schema validator for regime feature matrices.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

MINIMUM_REGIME_MATRIX_COLUMNS: List[str] = [
    "matrix_key",
    "entity_type",
    "entity_id",
    "timestamp_utc",
    "symbol",
    "feature_name",
    "feature_family",
    "factor_family",
    "regime_family",
    "source_phase",
    "validation_status",
    "quality_score_ref",
    "drift_score_ref",
    "lineage_ref",
    "manual_review_required",
    "non_signal",
]

CANONICAL_SCHEMA_FIELDS: List[Dict[str, Any]] = [
    {"column_name": "matrix_key", "data_type": "string", "description": "Canonical regime matrix column or row identifier."},
    {"column_name": "entity_type", "data_type": "string", "description": "Type of entity (fx_pair, commodity_symbol, etc.)."},
    {"column_name": "entity_id", "data_type": "string", "description": "Specific entity identifier (e.g. EUR/USD, XAU/USD)."},
    {"column_name": "timestamp_utc", "data_type": "datetime64[ns, UTC]", "description": "UTC timestamp of the observation point."},
    {"column_name": "symbol", "data_type": "string", "description": "Normalized asset or cross symbol."},
    {"column_name": "feature_name", "data_type": "string", "description": "Name of the aligned feature or metric."},
    {"column_name": "feature_family", "data_type": "string", "description": "Underlying feature family (trend, vol, etc.)."},
    {"column_name": "factor_family", "data_type": "string", "description": "Corresponding factor family from Phase 122."},
    {"column_name": "regime_family", "data_type": "string", "description": "Associated regime family from Phase 126."},
    {"column_name": "source_phase", "data_type": "int64", "description": "Upstream source phase providing this feature."},
    {"column_name": "validation_status", "data_type": "string", "description": "Audit status (VALIDATION_PASS, VALIDATION_WARN, etc.)."},
    {"column_name": "quality_score_ref", "data_type": "string", "description": "Reference key to quality score record."},
    {"column_name": "drift_score_ref", "data_type": "string", "description": "Reference key to drift score record."},
    {"column_name": "lineage_ref", "data_type": "string", "description": "Lineage provenance reference."},
    {"column_name": "manual_review_required", "data_type": "bool", "description": "Flag indicating manual audit is mandatory."},
    {"column_name": "non_signal", "data_type": "bool", "description": "System invariant indicating non-signal status."},
]


def build_regime_matrix_schema_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the schema registry for regime feature matrices."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for f in CANONICAL_SCHEMA_FIELDS:
        f_copy = f.copy()
        f_copy["current_phase"] = p.current_phase
        f_copy["target_final_phase"] = p.target_final_phase
        f_copy["next_phase"] = p.next_phase
        f_copy["non_signal"] = True
        f_copy["source_preserved"] = True
        rows.append(f_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_schema(df)
    return df, summary


def validate_regime_matrix_schema(
    df: pd.DataFrame,
    required_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Audit a DataFrame against the minimum required regime matrix columns."""
    cols_to_check = required_columns or MINIMUM_REGIME_MATRIX_COLUMNS
    missing = [c for c in cols_to_check if c not in df.columns]

    forbidden_cols = ["buy", "sell", "target", "label", "prediction", "future_return", "forward_return"]
    forbidden_found = []
    for c in df.columns:
        c_lower = str(c).lower()
        if c_lower == "non_signal" or "non_signal" in c_lower:
            continue
        if any(fb in c_lower for fb in forbidden_cols):
            forbidden_found.append(c)
        elif "signal" in c_lower:
            forbidden_found.append(c)

    is_valid = len(missing) == 0 and len(forbidden_found) == 0
    return {
        "is_valid": is_valid,
        "missing_columns": missing,
        "forbidden_columns_found": forbidden_found,
        "total_columns": len(df.columns),
        "row_count": len(df),
        "non_signal": True,
    }


def summarize_regime_matrix_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the regime matrix schema fields."""
    return {
        "total_schema_fields": len(df),
        "column_count": len(df),
        "minimum_columns": MINIMUM_REGIME_MATRIX_COLUMNS,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_matrix_schema = build_regime_matrix_schema_registry
REGIME_MATRIX_MINIMUM_COLUMNS = MINIMUM_REGIME_MATRIX_COLUMNS

