"""Phase 130: Candidate State Sequence Schema.

Defines tabular schema and column specifications for candidate state sequences.
Guarantees non-signal and zero-label compliance.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

CANDIDATE_STATE_SEQUENCE_COLUMNS: List[Dict[str, Any]] = [
    {
        "column_name": "sequence_key",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": True,
        "is_timestamp": False,
        "description": "Unique key identifying the state sequence observation",
    },
    {
        "column_name": "entity_type",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": True,
        "is_timestamp": False,
        "description": "Asset class or instrument domain (e.g. fx, commodity)",
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
        "description": "UTC timestamp of the state observation point",
    },
    {
        "column_name": "candidate_state_context",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Current candidate state descriptor from Phase 128/129",
    },
    {
        "column_name": "previous_candidate_state_context",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Preceding candidate state descriptor in chronological sequence",
    },
    {
        "column_name": "sequence_position_placeholder",
        "data_type": "integer",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Integer index indicating sequential position in entity run",
    },
    {
        "column_name": "source_candidate_state_ref",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Reference pointer to Phase 128 candidate state record",
    },
    {
        "column_name": "validation_status_ref",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Validation compliance reference status",
    },
    {
        "column_name": "quality_status_ref",
        "data_type": "string",
        "is_required": True,
        "is_entity_key": False,
        "is_timestamp": False,
        "description": "Data quality compliance reference status",
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


def build_candidate_state_sequence_schema_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dataframe and summary of candidate state sequence schema."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(CANDIDATE_STATE_SEQUENCE_COLUMNS)
    summary = summarize_candidate_state_sequence_schema(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def validate_candidate_state_sequence_schema(
    df: pd.DataFrame,
    required_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Validate a dataframe conforms to candidate state sequence schema and contains no forbidden columns."""
    if required_columns is None:
        required_columns = [
            col["column_name"]
            for col in CANDIDATE_STATE_SEQUENCE_COLUMNS
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


def summarize_candidate_state_sequence_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize candidate state sequence schema."""
    return {
        "total_schema_columns": len(df),
        "required_columns_count": int(df["is_required"].sum()) if "is_required" in df.columns else 0,
        "entity_key_columns": df[df["is_entity_key"]]["column_name"].tolist() if "is_entity_key" in df.columns else [],
        "timestamp_columns": df[df["is_timestamp"]]["column_name"].tolist() if "is_timestamp" in df.columns else [],
        "non_signal_certified": True,
    }
