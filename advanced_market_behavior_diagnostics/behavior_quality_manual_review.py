"""Phase 129: Behavior Quality Manual Review Queue.

Manages non-destructive analyst inspection queue items without allowing auto-deletion,
auto-imputation, clustering execution, model training, or trading signal generation.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

CORE_MANUAL_REVIEW_ITEMS = [
    {
        "item_id": "review_p129_001",
        "domain": "candidate_state_ambiguity_domain",
        "target_entity": "candidate_state_range_breakout_transition",
        "severity": "behavior_low",
        "reason": "Verify boundary separation between range breakout and trend continuation states.",
        "suggested_action": "inspect candidate state ambiguity",
        "blocking_for_phase_130": False,
    },
    {
        "item_id": "review_p129_002",
        "domain": "news_metadata_behavior_domain",
        "target_entity": "news_metadata_context",
        "severity": "behavior_info",
        "reason": "Confirm metadata-only news ingestion boundaries remain intact across all providers.",
        "suggested_action": "inspect news metadata-only boundary",
        "blocking_for_phase_130": False,
    },
    {
        "item_id": "review_p129_003",
        "domain": "transition_readiness_domain",
        "target_entity": "phase_130_transition_handoff",
        "severity": "behavior_info",
        "reason": "Confirm readiness for Phase 130 Regime Transition and Stability Analysis initialization.",
        "suggested_action": "inspect transition readiness",
        "blocking_for_phase_130": False,
    },
]

FORBIDDEN_REVIEW_ACTIONS = [
    "auto-delete",
    "auto-overwrite",
    "auto-impute",
    "enable scraping",
    "generate signal",
    "run clustering",
    "train model",
    "run dimensionality reduction",
    "approve production",
    "approve broker readiness",
]


def build_behavior_quality_manual_review_queue(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and metadata summary of manual review queue."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_MANUAL_REVIEW_ITEMS:
        # verify no forbidden action is suggested
        action_lower = item["suggested_action"].lower()
        for forbidden in FORBIDDEN_REVIEW_ACTIONS:
            if forbidden in action_lower:
                raise ValueError(f"Forbidden manual review action detected: {forbidden}")

        row = dict(item)
        row["review_id"] = item.get("item_id", "")
        row["destructive_action_allowed"] = False
        row["non_signal"] = True
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_behavior_quality_manual_review_queue(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_behavior_quality_manual_review_queue(df: pd.DataFrame) -> dict:
    """Summarize manual review queue."""
    if df.empty:
        return {
            "total_items": 0,
            "blocking_items_count": 0,
            "destructive_action_allowed": False,
            "non_signal": True,
        }
    return {
        "total_items": len(df),
        "blocking_items_count": int(df["blocking_for_phase_130"].sum()) if "blocking_for_phase_130" in df.columns else 0,
        "destructive_action_allowed": False,
        "non_signal": True,
        "actions": df["suggested_action"].tolist() if "suggested_action" in df.columns else [],
    }
