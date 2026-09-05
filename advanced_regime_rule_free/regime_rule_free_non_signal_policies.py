"""Phase 128: Regime Rule-Free Non-Signal Policies.

Enforces zero-tolerance policies prohibiting the use of candidate or pseudo-states as trading signals.
"""

from typing import Dict, Tuple
import re
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

NON_SIGNAL_POLICIES = [
    {
        "policy_id": "nsp_candidate_not_signal",
        "description": "Candidate states represent descriptive research taxonomy and must NEVER be presented as trading signals.",
        "enforced": True,
    },
    {
        "policy_id": "nsp_pseudo_state_not_signal",
        "description": "Pseudo-states are exploratory schema placeholders and carry zero trade recommendation capability.",
        "enforced": True,
    },
    {
        "policy_id": "nsp_no_directional_bias",
        "description": "Neither candidate state nor pseudo-state provides directional certainty (long/short).",
        "enforced": True,
    },
    {
        "policy_id": "nsp_no_execution_routing",
        "description": "System contains zero order routing, broker connection, or automated execution mechanisms.",
        "enforced": True,
    },
    {
        "policy_id": "nsp_mandatory_disclaimer",
        "description": "All reports, outputs, and dataset exports must include the mandatory non-signal research disclaimer.",
        "enforced": True,
    },
]

FORBIDDEN_TEXT_TERMS = [
    r"\bal\s+sinyali\b",
    r"\bsat\s+sinyali\b",
    r"\bbuy\s+signal\b",
    r"\bsell\s+signal\b",
    r"\blong\s+aç\b",
    r"\bshort\s+aç\b",
    r"\bkesin\s+al\b",
    r"\bkesin\s+sat\b",
    r"\byatırım\s+tavsiyesi\b",
    r"\btrading\s+recommendation\b",
]


def validate_regime_rule_free_non_signal_text(text: str) -> Dict:
    """Validate that given text contains no trading signals or recommendations."""
    text_lower = text.lower()
    detected = []
    for pattern in FORBIDDEN_TEXT_TERMS:
        if re.search(pattern, text_lower):
            detected.append(pattern)

    return {
        "is_valid": len(detected) == 0,
        "detected_signal_terms": detected,
    }


def build_regime_rule_free_non_signal_policy_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for non-signal policies."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for p in NON_SIGNAL_POLICIES:
        row = p.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_rule_free_non_signal_policies(df)
    return df, summary


def summarize_regime_rule_free_non_signal_policies(df: pd.DataFrame) -> Dict:
    """Summarize non-signal policies."""
    total = len(df)
    all_enforced = bool(df["enforced"].all()) if not df.empty else True

    return {
        "total_non_signal_policies": total,
        "all_enforced": all_enforced,
        "policy_status": "ACTIVE_SECURE" if all_enforced else "UNSAFE",
    }
