"""Phase 128: Candidate State Assignment Policies.

Defines contextual assignment policy placeholders without model execution, cluster execution, or trade signals.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import CandidateStateAssignmentPolicy

CANDIDATE_STATE_ASSIGNMENT_POLICIES = [
    CandidateStateAssignmentPolicy(
        policy_name="threshold_free_context_assignment_placeholder",
        policy_type="context_heuristics",
        description="Placeholder defining qualitative context assignment without rigid hardcoded trading thresholds.",
        candidate_state_family="general_context",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="percentile_context_assignment_placeholder",
        policy_type="percentile_boundary",
        description="Placeholder for rolling percentile ranking assignment in future research phases.",
        candidate_state_family="volatility_trend",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="rank_context_assignment_placeholder",
        policy_type="relative_rank",
        description="Placeholder for cross-sectional relative rank assignment across assets.",
        candidate_state_family="cross_asset",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="distance_to_centroid_placeholder",
        policy_type="distance_metric",
        description="Placeholder for distance-to-centroid assignment specification (no centroids calculated in Phase 128).",
        candidate_state_family="cluster_prep",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="cluster_membership_placeholder",
        policy_type="cluster_membership",
        description="Placeholder for future unsupervised cluster membership mapping (no clustering executed).",
        candidate_state_family="cluster_prep",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="transition_context_placeholder",
        policy_type="transition_dynamics",
        description="Placeholder for state change and transition dynamics assignment.",
        candidate_state_family="transition",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="uncertainty_context_placeholder",
        policy_type="uncertainty_filter",
        description="Placeholder for assigning uncertain context when data quality or drift violates thresholds.",
        candidate_state_family="uncertain",
    ),
    CandidateStateAssignmentPolicy(
        policy_name="manual_review_assignment_placeholder",
        policy_type="manual_override",
        description="Placeholder routing ambiguous state candidates to human researcher review queue.",
        candidate_state_family="manual_review",
    ),
]


def build_candidate_state_assignment_policy_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate state assignment policies."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for p in CANDIDATE_STATE_ASSIGNMENT_POLICIES:
        row = p.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_assignment_policies(df)
    return df, summary


def validate_candidate_state_assignment_policy(policy: dict) -> dict:
    """Validate that an assignment policy strictly enforces non-execution and non-signal boundaries."""
    violations = []
    name = policy.get("policy_name", "unknown")

    if policy.get("execution_allowed", True):
        violations.append("execution_allowed must be False")
    if policy.get("generates_trade_signal", True):
        violations.append("generates_trade_signal must be False")
    if not policy.get("non_signal", False):
        violations.append("non_signal must be True")

    for word in ["buy", "sell", "long", "short", "position", "signal", "target"]:
        if word in name.lower() and word != "signal":
            violations.append(f"Forbidden word '{word}' in assignment policy name")

    return {
        "policy_name": name,
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_candidate_state_assignment_policies(df: pd.DataFrame) -> Dict:
    """Summarize candidate state assignment policies."""
    total_policies = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_non_executable = bool((~df["execution_allowed"]).all()) if not df.empty else True
    all_non_trade_signal = bool((~df["generates_trade_signal"]).all()) if not df.empty else True

    return {
        "total_policies": total_policies,
        "all_non_signal": all_non_signal,
        "all_non_executable": all_non_executable,
        "all_non_trade_signal": all_non_trade_signal,
        "policies_status": "VALID" if all_non_signal and all_non_executable else "INVALID",
    }
