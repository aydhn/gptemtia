"""Phase 130: Regime Transition Thresholds.

Defines operational thresholds and warning triggers for transition ambiguity,
sequence continuity, stability degradation, and manual review requirements.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

TRANSITION_THRESHOLDS: List[Dict[str, Any]] = [
    {
        "threshold_key": "sequence_missingness_warning_above",
        "threshold_value": 0.25,
        "comparator": ">",
        "severity": "transition_medium",
        "description": "Trigger warning if candidate sequence missingness exceeds 25%",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "sequence_missingness_critical_above",
        "threshold_value": 0.50,
        "comparator": ">",
        "severity": "transition_critical",
        "description": "Trigger critical alert if candidate sequence missingness exceeds 50%",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "transition_ambiguity_warning_above",
        "threshold_value": 0.50,
        "comparator": ">",
        "severity": "transition_high",
        "description": "Trigger alert if transition ambiguity between candidate states exceeds 0.50",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "continuity_warning_below",
        "threshold_value": 0.50,
        "comparator": "<",
        "severity": "transition_high",
        "description": "Trigger warning if timestamp continuity falls below 0.50",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "stability_warning_below",
        "threshold_value": 0.45,
        "comparator": "<",
        "severity": "transition_high",
        "description": "Trigger review if aggregate transition stability falls below 0.45",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "manual_review_if_insufficient_sequence",
        "threshold_value": True,
        "comparator": "==",
        "severity": "transition_critical",
        "description": "Require manual review if sequence history is shorter than minimum window",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "manual_review_if_timestamp_gap",
        "threshold_value": True,
        "comparator": "==",
        "severity": "transition_medium",
        "description": "Require manual review if irregular timestamp gap is identified",
        "manual_review_triggered": True,
    },
    {
        "threshold_key": "manual_review_if_future_timestamp_risk",
        "threshold_value": True,
        "comparator": "==",
        "severity": "transition_critical",
        "description": "Block transition analysis if context timestamp exceeds observation timestamp",
        "manual_review_triggered": True,
    },
]


def build_regime_transition_threshold_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition threshold registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    rows = []
    for t in TRANSITION_THRESHOLDS:
        item = dict(t)
        item["non_signal"] = True
        rows.append(item)
    df = pd.DataFrame(rows)
    summary = summarize_regime_transition_thresholds(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_transition_thresholds(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize transition thresholds."""
    return {
        "total_thresholds": len(df),
        "threshold_keys": df["threshold_key"].tolist() if not df.empty else [],
        "manual_review_enforced": bool(df["manual_review_triggered"].all()) if not df.empty else True,
        "non_signal": True,
        "all_non_signal": True,
    }

