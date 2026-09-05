"""Phase 128: Regime Candidate State Validation Dependencies.

Defines validation gating rules linked to Phase 121 feature validation and Phase 127 matrix contracts.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

VALIDATION_DEPENDENCIES = [
    {
        "validation_id": "val_phase_121_no_lookahead",
        "category": "temporal_validation",
        "description": "Requires zero lookahead bias certification from Phase 121 validation suite.",
        "enforced": True,
        "is_blocker": True,
    },
    {
        "validation_id": "val_forbidden_columns",
        "category": "schema_validation",
        "description": "Requires zero occurrence of target, label, prediction, buy, sell, or signal column names.",
        "enforced": True,
        "is_blocker": True,
    },
    {
        "validation_id": "val_timestamp_order",
        "category": "temporal_validation",
        "description": "Requires monotonically increasing UTC timestamps and context_ts <= base_ts.",
        "enforced": True,
        "is_blocker": True,
    },
    {
        "validation_id": "val_news_metadata_only",
        "category": "compliance_validation",
        "description": "Requires zero raw article body, html scraping, or full-text fields in news-derived candidate states.",
        "enforced": True,
        "is_blocker": True,
    },
    {
        "validation_id": "val_source_preservation",
        "category": "data_integrity",
        "description": "Requires zero source overwriting, deletion, or in-place modification during prep.",
        "enforced": True,
        "is_blocker": True,
    },
    {
        "validation_id": "val_non_signal_compliance",
        "category": "governance_validation",
        "description": "Requires that all candidate and pseudo-state outputs carry explicit non-signal metadata.",
        "enforced": True,
        "is_blocker": True,
    },
]


def build_regime_candidate_state_validation_dependency_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for validation dependencies."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for v in VALIDATION_DEPENDENCIES:
        row = v.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_validation_dependencies(df)
    return df, summary


def summarize_candidate_state_validation_dependencies(df: pd.DataFrame) -> Dict:
    """Summarize validation dependencies."""
    total = len(df)
    blockers = int(df["is_blocker"].sum()) if not df.empty else 0
    all_enforced = bool(df["enforced"].all()) if not df.empty else True

    return {
        "total_validation_dependencies": total,
        "blocking_validation_count": blockers,
        "all_enforced": all_enforced,
        "status": "VALID" if all_enforced and blockers == total else "INVALID",
    }
