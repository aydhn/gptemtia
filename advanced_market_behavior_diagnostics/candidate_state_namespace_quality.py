"""Phase 129: Candidate State Namespace Quality Report.

Verifies candidate state naming conventions (`candidate_state_*`), snake_case standards,
and catches forbidden trading signal, directional, and prediction terms.
"""

import re
from typing import List, Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import CORE_CANDIDATE_STATES

FORBIDDEN_NAMESPACE_TERMS = [
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
    "order",
    "trade",
    "bullish",
    "bearish",
]


def validate_candidate_state_namespace_quality(names: List[str]) -> dict:
    """Validate a list of candidate state names against naming conventions and forbidden terms."""
    valid_names = []
    invalid_prefix = []
    forbidden_matches = []

    for name in names:
        if not name.startswith("candidate_state_"):
            invalid_prefix.append(name)
            continue
        # check forbidden words
        lowered = name.lower()
        found_forbidden = [term for term in FORBIDDEN_NAMESPACE_TERMS if term in lowered]
        if found_forbidden:
            forbidden_matches.append((name, found_forbidden))
        else:
            valid_names.append(name)

    return {
        "total_names": len(names),
        "valid_count": len(valid_names),
        "invalid_prefix_count": len(invalid_prefix),
        "forbidden_matches_count": len(forbidden_matches),
        "is_all_clean": len(invalid_prefix) == 0 and len(forbidden_matches) == 0,
        "invalid_prefix_names": invalid_prefix,
        "forbidden_matches": forbidden_matches,
    }


def build_candidate_state_namespace_quality_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build candidate state namespace quality report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    names = [item["candidate_state_name"] for item in CORE_CANDIDATE_STATES]
    validation_res = validate_candidate_state_namespace_quality(names)

    rows = []
    for item in CORE_CANDIDATE_STATES:
        name = item["candidate_state_name"]
        has_correct_prefix = name.startswith("candidate_state_")
        lowered = name.lower()
        found_forbidden = [term for term in FORBIDDEN_NAMESPACE_TERMS if term in lowered]

        rows.append(
            {
                "candidate_state_name": name,
                "has_correct_prefix": has_correct_prefix,
                "is_snake_case": bool(re.match(r"^[a-z0-9_]+$", name)),
                "has_forbidden_terms": len(found_forbidden) > 0,
                "forbidden_terms": ",".join(found_forbidden) if found_forbidden else "none",
                "namespace_status": "behavior_quality_ready" if has_correct_prefix and not found_forbidden else "behavior_quality_manual_review_required",
                "namespace_valid": has_correct_prefix and len(found_forbidden) == 0,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_namespace_quality(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_candidate_state_namespace_quality(df: pd.DataFrame) -> dict:
    """Summarize candidate state namespace quality."""
    if df.empty:
        return {
            "total_names": 0,
            "all_valid": False,
            "all_namespaces_valid": False,
            "forbidden_count": 0,
            "forbidden_keywords_found": False,
            "non_signal": True,
        }
    all_valid = bool((df["namespace_status"] == "behavior_quality_ready").all()) if "namespace_status" in df.columns else False
    forbidden_count = int(df["has_forbidden_terms"].sum()) if "has_forbidden_terms" in df.columns else 0
    return {
        "total_names": len(df),
        "all_valid": all_valid,
        "all_namespaces_valid": all_valid,
        "forbidden_count": forbidden_count,
        "forbidden_keywords_found": forbidden_count > 0,
        "non_signal": True,
    }

