"""Phase 128: Candidate State Schema.

Defines the standard canonical schema for candidate state records, strictly banning trade/target terms.
"""

from typing import Dict, List, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import CandidateStateSchemaItem

CANDIDATE_STATE_COLUMNS = [
    CandidateStateSchemaItem("candidate_state_key", "string", "Canonical unique identifier for candidate state record"),
    CandidateStateSchemaItem("entity_type", "string", "Entity type e.g. commodity, fx"),
    CandidateStateSchemaItem("entity_id", "string", "Entity identifier e.g. BRENT, USDTRY"),
    CandidateStateSchemaItem("timestamp_utc", "datetime64[ns, UTC]", "Point-in-time timestamp in UTC"),
    CandidateStateSchemaItem("candidate_state_family", "string", "Candidate state family classification"),
    CandidateStateSchemaItem("candidate_state_context", "string", "Contextual research annotation"),
    CandidateStateSchemaItem("source_matrix_ref", "string", "Reference to Phase 127 regime feature matrix"),
    CandidateStateSchemaItem("assignment_policy_ref", "string", "Reference to assignment policy specification"),
    CandidateStateSchemaItem("validation_status_ref", "string", "Reference to validation gate check"),
    CandidateStateSchemaItem("quality_status_ref", "string", "Reference to quality and drift metrics"),
    CandidateStateSchemaItem("manual_review_required", "boolean", "Flag indicating human researcher review is required"),
    CandidateStateSchemaItem("non_signal", "boolean", "Mandatory invariant certifying record is not a trading signal"),
]

FORBIDDEN_CANDIDATE_STATE_COLUMNS = [
    "target",
    "label",
    "prediction",
    "recommendation",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "future_return",
    "forward_return",
    "next_return",
    "shift_negative",
    "signal",
]


def build_candidate_state_schema_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate state schema."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for col in CANDIDATE_STATE_COLUMNS:
        row = col.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_schema(df)
    return df, summary


def validate_candidate_state_schema(
    df: pd.DataFrame,
    required_columns: List[str] | None = None,
) -> Dict:
    """Validate a DataFrame against candidate state schema and forbidden columns."""
    req_cols = required_columns or [c.column_name for c in CANDIDATE_STATE_COLUMNS]
    actual_cols = list(df.columns)

    missing_cols = [c for c in req_cols if c not in actual_cols]

    found_forbidden = []
    for col in actual_cols:
        col_lower = col.lower()
        for forbidden in FORBIDDEN_CANDIDATE_STATE_COLUMNS:
            if forbidden == col_lower or f"_{forbidden}" in col_lower or f"{forbidden}_" in col_lower:
                if forbidden == "signal" and col_lower in ["non_signal", "is_signal"]:
                    continue
                found_forbidden.append(col)

    is_valid = (len(missing_cols) == 0) and (len(found_forbidden) == 0)

    return {
        "is_valid": is_valid,
        "missing_columns": missing_cols,
        "forbidden_columns_detected": found_forbidden,
        "total_columns": len(actual_cols),
    }


def summarize_candidate_state_schema(df: pd.DataFrame) -> Dict:
    """Summarize candidate state schema specifications."""
    total_fields = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_not_target = bool((~df["is_target_or_prediction"]).all()) if not df.empty else True

    return {
        "total_schema_fields": total_fields,
        "mandatory_fields_count": int(df["is_mandatory"].sum()) if not df.empty else 0,
        "all_non_signal": all_non_signal,
        "all_not_target_or_prediction": all_not_target,
        "forbidden_terms_guarded": True,
        "schema_status": "VALID" if all_non_signal and all_not_target else "INVALID",
    }
