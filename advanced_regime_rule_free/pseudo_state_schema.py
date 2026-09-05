"""Phase 128: Pseudo-State Schema.

Defines non-signal pseudo-state schema contracts for research purposes.
"""

from typing import Dict, List, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import PseudoStateSchemaItem

PSEUDO_STATE_DEFINITIONS = [
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_volatility_high",
        pseudo_state_family="volatility",
        pseudo_state_context="High volatility regime candidate placeholder",
        source_candidate_state_ref="candidate_state_volatility_context",
        future_phase_usage_note="For Phase 129 market behavior diagnostics only. Zero signal generation.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_volatility_normal",
        pseudo_state_family="volatility",
        pseudo_state_context="Normal volatility regime candidate placeholder",
        source_candidate_state_ref="candidate_state_volatility_context",
        future_phase_usage_note="Baseline volatility reference without trading direction.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_volatility_compressed",
        pseudo_state_family="volatility",
        pseudo_state_context="Compressed volatility regime candidate placeholder",
        source_candidate_state_ref="candidate_state_volatility_context",
        future_phase_usage_note="Bandwidth compression diagnostic context.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_trend_persistent",
        pseudo_state_family="trend",
        pseudo_state_context="Directional persistence candidate placeholder (non-directional trade claim)",
        source_candidate_state_ref="candidate_state_trend_context",
        future_phase_usage_note="Measures directional persistence without buy/sell advice.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_range_mean_reverting",
        pseudo_state_family="range",
        pseudo_state_context="Mean reverting range candidate placeholder",
        source_candidate_state_ref="candidate_state_range_context",
        future_phase_usage_note="Oscillator boundary assessment without execution.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_macro_shock_context",
        pseudo_state_family="macro_event",
        pseudo_state_context="Elevated macro surprise candidate placeholder",
        source_candidate_state_ref="candidate_state_macro_event_context",
        future_phase_usage_note="Event impact window analysis in Phase 129.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_transition_pending",
        pseudo_state_family="transition",
        pseudo_state_context="Inter-state transition candidate placeholder",
        source_candidate_state_ref="candidate_state_transition_context",
        future_phase_usage_note="State transition probability research in Phase 130.",
    ),
    PseudoStateSchemaItem(
        pseudo_state_key="pseudo_state_uncertain_unassigned",
        pseudo_state_family="uncertain",
        pseudo_state_context="Uncertain or low-quality data candidate placeholder",
        source_candidate_state_ref="candidate_state_uncertain_context",
        future_phase_usage_note="Safety fallback context when data quality or drift fails gates.",
    ),
]

PSEUDO_STATE_SCHEMA_COLUMNS = [
    "pseudo_state_key",
    "pseudo_state_family",
    "pseudo_state_context",
    "source_candidate_state_ref",
    "future_phase_usage_note",
    "model_training_executed",
    "clustering_executed",
    "unsupervised_execution",
    "manual_review_required",
    "non_signal",
]


def build_pseudo_state_schema_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for pseudo-state schema."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for item in PSEUDO_STATE_DEFINITIONS:
        row = item.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_pseudo_state_schema(df)
    return df, summary


def validate_pseudo_state_schema(
    df: pd.DataFrame,
    required_columns: List[str] | None = None,
) -> Dict:
    """Validate DataFrame against pseudo-state schema and zero-execution invariants."""
    req_cols = required_columns or PSEUDO_STATE_SCHEMA_COLUMNS
    actual_cols = list(df.columns)

    missing_cols = [c for c in req_cols if c not in actual_cols]

    # Verify invariants if columns present
    training_executed = bool(df["model_training_executed"].any()) if "model_training_executed" in df.columns else False
    clustering_executed = bool(df["clustering_executed"].any()) if "clustering_executed" in df.columns else False
    unsupervised_executed = bool(df["unsupervised_execution"].any()) if "unsupervised_execution" in df.columns else False
    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False

    is_valid = (
        len(missing_cols) == 0
        and not training_executed
        and not clustering_executed
        and not unsupervised_executed
        and all_non_signal
    )

    return {
        "is_valid": is_valid,
        "missing_columns": missing_cols,
        "training_executed": training_executed,
        "clustering_executed": clustering_executed,
        "unsupervised_executed": unsupervised_executed,
        "all_non_signal": all_non_signal,
    }


def summarize_pseudo_state_schema(df: pd.DataFrame) -> Dict:
    """Summarize pseudo-state schema specifications."""
    total_states = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_no_training = bool((~df["model_training_executed"]).all()) if not df.empty else True
    all_no_clustering = bool((~df["clustering_executed"]).all()) if not df.empty else True

    return {
        "total_pseudo_states": total_states,
        "all_non_signal": all_non_signal,
        "all_no_training": all_no_training,
        "all_no_clustering": all_no_clustering,
        "schema_status": "VALID" if all_non_signal and all_no_training and all_no_clustering else "INVALID",
    }
