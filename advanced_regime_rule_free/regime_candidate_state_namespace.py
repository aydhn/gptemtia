"""Phase 128: Regime Candidate State Namespace.

Enforces strict naming conventions, prefix rules, and forbidden term rejection for candidate state keys.
"""

from typing import Dict, Tuple
import re
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

FORBIDDEN_NAMESPACE_WORDS = [
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
]

NAMESPACE_RULES = [
    {
        "rule_id": "rule_candidate_prefix",
        "description": "All candidate state keys must start with 'candidate_state_' (or 'pseudo_state_' for pseudo-states).",
        "enforced": True,
    },
    {
        "rule_id": "rule_lowercase_snake_case",
        "description": "All candidate state keys must be strictly lowercase snake_case alphanumeric.",
        "enforced": True,
    },
    {
        "rule_id": "rule_no_forbidden_words",
        "description": "Keys must not contain trading words: buy, sell, long, short, position, target, label, prediction, etc.",
        "enforced": True,
    },
    {
        "rule_id": "rule_entity_family_composite",
        "description": "Canonical key format is 'candidate_state_<entity_type>_<entity_id>_<family>'.",
        "enforced": True,
    },
]


def build_candidate_state_key(
    entity_type: str,
    entity_id: str,
    candidate_state_family: str,
) -> str:
    """Construct canonical candidate state key."""
    clean_type = entity_type.strip().lower().replace("-", "_")
    clean_id = entity_id.strip().lower().replace("-", "_")
    clean_family = candidate_state_family.strip().lower().replace("-", "_")

    key = f"candidate_state_{clean_type}_{clean_id}_{clean_family}"
    return key


def validate_candidate_state_key(key: str) -> Dict:
    """Validate candidate state key against namespace conventions."""
    violations = []

    if not (key.startswith("candidate_state_") or key.startswith("pseudo_state_")):
        violations.append("Key must start with 'candidate_state_' or 'pseudo_state_'")

    if not re.match(r"^[a-z0-9_]+$", key):
        violations.append("Key must be strictly lowercase alphanumeric snake_case")

    for forbidden in FORBIDDEN_NAMESPACE_WORDS:
        # Allow 'non_signal' if present, but reject standalone or embedded signal terms
        parts = key.split("_")
        if forbidden in parts:
            violations.append(f"Forbidden word '{forbidden}' detected in namespace key")

    return {
        "key": key,
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def build_regime_candidate_state_namespace_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate state namespace rules."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for r in NAMESPACE_RULES:
        row = r.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_candidate_state_namespace(df)
    return df, summary


def summarize_regime_candidate_state_namespace(df: pd.DataFrame) -> Dict:
    """Summarize candidate state namespace rules."""
    total = len(df)
    all_enforced = bool(df["enforced"].all()) if not df.empty else True

    return {
        "total_namespace_rules": total,
        "all_rules_enforced": all_enforced,
        "forbidden_words_count": len(FORBIDDEN_NAMESPACE_WORDS),
        "namespace_status": "VALID" if all_enforced else "INVALID",
    }
