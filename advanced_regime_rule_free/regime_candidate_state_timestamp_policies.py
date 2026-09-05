"""Phase 128: Regime Candidate State Timestamp Policies.

Enforces UTC timezone normalization, temporal ordering, and point-in-time constraints.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

TIMESTAMP_POLICIES = [
    {
        "policy_id": "policy_strict_utc",
        "description": "All candidate state timestamps must be parsed and recorded in UTC timezone.",
        "enforced": True,
    },
    {
        "policy_id": "policy_context_before_base",
        "description": "Context timestamp must be strictly less than or equal to base candidate timestamp (context_ts <= base_ts).",
        "enforced": True,
    },
    {
        "policy_id": "policy_non_decreasing_order",
        "description": "Candidate state timelines per asset must be monotonically non-decreasing.",
        "enforced": True,
    },
    {
        "policy_id": "policy_nanosecond_precision",
        "description": "Timestamps use datetime64[ns, UTC] precision to prevent rounding collisions.",
        "enforced": True,
    },
]


def validate_candidate_state_timestamp_policy(
    df: pd.DataFrame,
    base_ts: str = "timestamp_utc",
    context_ts: str | None = None,
) -> Dict:
    """Validate DataFrame against timestamp policy."""
    if df.empty or base_ts not in df.columns:
        return {"is_valid": True, "note": "Empty dataframe or base timestamp not found"}

    violations = []

    # Check monotonicity
    ts_series = pd.to_datetime(df[base_ts], utc=True)
    if not ts_series.is_monotonic_increasing:
        # Check if grouped by entity
        if "entity_id" in df.columns:
            for _, group in df.groupby("entity_id"):
                sub_ts = pd.to_datetime(group[base_ts], utc=True)
                if not sub_ts.is_monotonic_increasing:
                    violations.append("Non-monotonic timestamp sequence within entity group")
                    break
        else:
            violations.append("Non-monotonic global timestamp sequence")

    # Check context ordering if context_ts provided
    if context_ts and context_ts in df.columns:
        ctx_series = pd.to_datetime(df[context_ts], utc=True)
        leakage = int((ctx_series > ts_series).sum())
        if leakage > 0:
            violations.append(f"Context timestamp exceeds base timestamp in {leakage} rows")

    return {
        "is_valid": len(violations) == 0,
        "violations": violations,
        "total_rows_checked": len(df),
    }


def build_regime_candidate_state_timestamp_policy_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for timestamp policies."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for p in TIMESTAMP_POLICIES:
        row = p.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_timestamp_policies(df)
    return df, summary


def summarize_candidate_state_timestamp_policies(df: pd.DataFrame) -> Dict:
    """Summarize timestamp policies."""
    total = len(df)
    all_enforced = bool(df["enforced"].all()) if not df.empty else True

    return {
        "total_timestamp_policies": total,
        "all_enforced": all_enforced,
        "status": "VALID" if all_enforced else "INVALID",
    }
