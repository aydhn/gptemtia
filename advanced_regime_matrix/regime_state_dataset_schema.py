"""Phase 127: Regime State Dataset Schema Definition and Validation.

Defines canonical fields and validation logic for state dataset rows, strictly prohibiting
target, label, prediction, or position terminology.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

MINIMUM_STATE_DATASET_COLUMNS: List[str] = [
    "dataset_key",
    "entity_type",
    "entity_id",
    "timestamp_utc",
    "regime_family",
    "regime_state_candidate_context",
    "source_matrix_ref",
    "validation_status_ref",
    "quality_status_ref",
    "manual_review_required",
    "non_signal",
]

FORBIDDEN_STATE_DATASET_FIELDS: List[str] = [
    "target",
    "label",
    "prediction",
    "recommendation",
    "buy",
    "sell",
    "long",
    "short",
    "position",
]

STATE_SCHEMA_FIELDS: List[Dict[str, Any]] = [
    {"field_name": "dataset_key", "data_type": "string", "description": "Canonical state dataset row identifier."},
    {"field_name": "entity_type", "data_type": "string", "description": "Type of entity (fx_pair, commodity_symbol, etc.)."},
    {"field_name": "entity_id", "data_type": "string", "description": "Normalized identifier of the entity."},
    {"field_name": "timestamp_utc", "data_type": "datetime64[ns, UTC]", "description": "UTC timestamp of the state context."},
    {"field_name": "regime_family", "data_type": "string", "description": "Associated regime family from Phase 126."},
    {"field_name": "regime_state_candidate_context", "data_type": "string", "description": "Descriptive candidate context flag (NOT a label or target)."},
    {"field_name": "source_matrix_ref", "data_type": "string", "description": "Lineage reference to source feature matrix key."},
    {"field_name": "validation_status_ref", "data_type": "string", "description": "Audit validation status code."},
    {"field_name": "quality_status_ref", "data_type": "string", "description": "Quality assurance audit status code."},
    {"field_name": "manual_review_required", "data_type": "bool", "description": "Manual review queue requirement flag."},
    {"field_name": "non_signal", "data_type": "bool", "description": "System invariant indicating non-signal status."},
]


def build_regime_state_dataset_schema_registry(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build state dataset schema registry."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for f in STATE_SCHEMA_FIELDS:
        f_copy = f.copy()
        f_copy["current_phase"] = p.current_phase
        f_copy["target_final_phase"] = p.target_final_phase
        f_copy["next_phase"] = p.next_phase
        f_copy["non_signal"] = True
        f_copy["source_preserved"] = True
        rows.append(f_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_state_dataset_schema(df)
    return df, summary


def validate_regime_state_dataset_schema(
    df: pd.DataFrame,
    required_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Audit a DataFrame representing a regime state dataset against schema and forbidden terms."""
    cols_to_check = required_columns or MINIMUM_STATE_DATASET_COLUMNS
    missing = [c for c in cols_to_check if c not in df.columns]

    forbidden_found = [
        c for c in df.columns if any(fb in c.lower() for fb in FORBIDDEN_STATE_DATASET_FIELDS)
    ]

    is_valid = len(missing) == 0 and len(forbidden_found) == 0
    return {
        "is_valid": is_valid,
        "missing_columns": missing,
        "forbidden_fields_found": forbidden_found,
        "row_count": len(df),
        "non_signal": True,
    }


def summarize_regime_state_dataset_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime state dataset schema."""
    return {
        "total_schema_fields": len(df),
        "field_count": len(df),
        "minimum_columns": MINIMUM_STATE_DATASET_COLUMNS,
        "forbidden_fields_prohibited": FORBIDDEN_STATE_DATASET_FIELDS,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "status": "matrix_ready",
    }


build_regime_state_dataset_schema = build_regime_state_dataset_schema_registry
REGIME_STATE_STANDARD_FIELDS = MINIMUM_STATE_DATASET_COLUMNS

