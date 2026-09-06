"""Phase 132 -> Phase 133 Handoff Report.

Hands off macro/event/news regime context outputs to Phase 133:
Regime Validation and No-Lookahead Acceptance.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

HANDOFF_ITEMS = [
    {
        "item_id": "handoff_01_regime_val_prereq",
        "topic": "regime validation acceptance prerequisites",
        "requirement": "All Phase 126-132 regime and context datasets must be verifiable without execution errors.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_02_no_lookahead_prereq",
        "topic": "no-lookahead acceptance prerequisites",
        "requirement": "Zero negative shift operations and zero forward-looking timestamp alignments allowed.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_03_macro_release_ts",
        "topic": "macro release timestamp validation prerequisites",
        "requirement": "Historical release timestamps must be proven to reflect actual public availability date.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_04_event_window_val",
        "topic": "event window validation prerequisites",
        "requirement": "Pre-event and post-event window boundaries must not consume future price discovery bars.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_05_release_alignment_val",
        "topic": "scheduled/actual release alignment validation prerequisites",
        "requirement": "Actual release timestamp latency verification must confirm zero premature disclosure leaks.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_06_metadata_only_news",
        "topic": "metadata-only news validation prerequisites",
        "requirement": "News feeds must strictly consist of tags, topics, timestamps, and source IDs.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_07_forbidden_news_content",
        "topic": "forbidden news content validation prerequisites",
        "requirement": "Complete absence of full article body, scraped HTML, sentiment scores, and embeddings.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_08_cross_asset_macro_sens",
        "topic": "cross-asset macro sensitivity validation prerequisites",
        "requirement": "FX and Commodity macro sensitivity matrices must adhere to common asset key schemas.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_09_transition_context_val",
        "topic": "transition context validation prerequisites",
        "requirement": "State transition alignment around macro events must not trigger speculative jumps.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_10_quality_dep_reqs",
        "topic": "quality dependency requirements",
        "requirement": "Feature quality, drift, and stationarity metrics from Phase 123 must meet thresholds.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_11_source_preservation",
        "topic": "source preservation requirements",
        "requirement": "Raw datasets, lake records, and feature stores must be 100% immutable and un-dropped.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_12_manual_review_blockers",
        "topic": "manual review blockers before Phase 133",
        "requirement": "Zero unresolved manual review blockers permissible for Phase 133 acceptance sign-off.",
        "status": "READY",
        "target_phase": 133,
    },
    {
        "item_id": "handoff_13_clear_boundary_non_signal",
        "topic": "clear boundary: Phase 133 validates regime context, not trade signals",
        "requirement": "Phase 133 is strictly an acceptance and validation gate; zero trading signals generated.",
        "status": "READY",
        "target_phase": 133,
    },
]


def build_phase_133_regime_validation_no_lookahead_acceptance_handoff_report(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary dictionary for Phase 133 handoff."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in HANDOFF_ITEMS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["current_phase"] = 132
        row["target_final_phase"] = 160
        row["next_phase"] = 133
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)

    all_ready = bool((df["status"] == "READY").all())
    summary = {
        "handoff_status": "READY" if all_ready else "BLOCKED",
        "current_phase": 132,
        "next_phase": 133,
        "target_final_phase": 160,
        "total_items": len(df),
        "all_ready": all_ready,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_phase_133_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for handoff DataFrame."""
    ready_cnt = int((df["status"] == "READY").sum()) if "status" in df.columns else 0
    return {
        "total_items": len(df),
        "ready_items": ready_cnt,
        "all_ready": bool(ready_cnt == len(df) and len(df) > 0),
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
