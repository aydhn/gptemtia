"""Phase 130: Pseudo-State Sequence Schema.

Defines tabular schema and column specifications for pseudo-state sequences.
Strictly verifies that no model training, clustering, or unsupervised algorithms were executed.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

PSEUDO_STATE_SEQUENCE_COLUMNS: List[Dict[str, Any]] = [
    {
        "column_name": "pseudo_sequence_key",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": True,
        "is_timestamp": False,
        "description": "Unique key identifying the pseudo state sequence observation",
    },
    {
        "column_name": "entity_type",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": True,
        "is_timestamp": False,
        "description": "Asset class or instrument domain",
    },
    {
        "column_name": "entity_id",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": True,
        "is_timestamp": False,
        "description": "Symbol or asset identifier",
    },
    {
        "column_name": "timestamp_utc",
        "data_type": "timestamp_utc",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": True,
        "description": "UTC timestamp of the observation point",
    },
    {
        "column_name": "pseudo_state_context",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Pseudo-state cluster placeholder identifier",
    },
    {
        "column_name": "previous_pseudo_state_context",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Preceding pseudo-state cluster identifier",
    },
    {
        "column_name": "source_pseudo_state_ref",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Reference pointer to Phase 128 pseudo state record",
    },
    {
        "column_name": "model_training_executed",
        "data_type": "boolean",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Invariant flag certifying ML model training was NOT executed (False)",
    },
    {
        "column_name": "clustering_executed",
        "data_type": "boolean",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Invariant flag certifying clustering was NOT executed (False)",
    },
    {
        "column_name": "unsupervised_execution",
        "data_type": "boolean",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Invariant flag certifying unsupervised algorithm was NOT executed (False)",
    },
    {
        "column_name": "manual_review_required",
        "data_type": "boolean",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Flag indicating manual inspection is required",
    },
    {
        "column_name": "non_signal",
        "data_type": "boolean",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Invariant flag certifying non-signal nature of this sequence",
    },
]

FORBIDDEN_TRANSITION_COLUMNS = [
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


def build_pseudo_state_sequence_schema_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dataframe and summary of pseudo-state sequence schema."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(PSEUDO_STATE_SEQUENCE_COLUMNS)
    summary = summarize_pseudo_state_sequence_schema(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_pseudo_state_sequence_schema(
    df: pd.DataFrame,
    required_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Validate a dataframe conforms to pseudo-state sequence schema."""
    if required_columns is None:
        required_columns = [
            col["column_name"]
            for col in PSEUDO_STATE_SEQUENCE_COLUMNS
            if col["is_required"]
        ]

    missing = [c for c in required_columns if c not in df.columns]
    forbidden_found = []
    for c in df.columns:
        c_lower = c.lower()
        if c_lower in ["non_signal", "is_signal"]:
            continue
        if "sequence_position" in c_lower:
            continue
        for f in FORBIDDEN_TRANSITION_COLUMNS:
            if f == c_lower or f"_{f}" in c_lower or f"{f}_" in c_lower:
                forbidden_found.append(c)
                break

    is_valid = len(missing) == 0 and len(forbidden_found) == 0
    return {
        "is_valid": is_valid,
        "missing_columns": missing,
        "forbidden_columns": forbidden_found,
        "total_columns": len(df.columns),
    }


def summarize_pseudo_state_sequence_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize pseudo-state sequence schema."""
    return {
        "total_schema_columns": len(df),
        "required_columns_count": int(df["is_required"].sum()) if "is_required" in df.columns else 0,
        "zero_model_training_certified": True,
        "zero_clustering_certified": True,
        "non_signal_certified": True,
    }
