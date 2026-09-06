"""Phase 132: Macro/Event/News Transition Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_TRANSITION_CONTEXTS = [
    {
        "transition_context_id": "trans_macro_release",
        "context_name": "macro_release_transition_context",
        "transition_type": "event_driven_transition",
        "triggers_reclassification": False,
        "description": "Macro data release point transition tracking without predicting new states.",
    },
    {
        "transition_context_id": "trans_pre_event",
        "context_name": "pre_event_transition_context",
        "transition_type": "anticipatory_window_transition",
        "triggers_reclassification": False,
        "description": "Pre-event calm/compression regime state alignment.",
    },
    {
        "transition_context_id": "trans_post_event",
        "context_name": "post_event_transition_context",
        "transition_type": "digestion_window_transition",
        "triggers_reclassification": False,
        "description": "Post-event volatility expansion regime state alignment.",
    },
    {
        "transition_context_id": "trans_news_event",
        "context_name": "news_event_transition_context",
        "transition_type": "news_attention_transition",
        "triggers_reclassification": False,
        "description": "Shifts in news metadata attention cluster regimes.",
    },
    {
        "transition_context_id": "trans_release_lag",
        "context_name": "release_lag_transition_context",
        "transition_type": "lag_boundary_transition",
        "triggers_reclassification": False,
        "description": "Transition tracking at the expiry of historical reporting lags.",
    },
    {
        "transition_context_id": "trans_state_sequence",
        "context_name": "macro_event_state_sequence_context",
        "transition_type": "sequence_continuity_transition",
        "triggers_reclassification": False,
        "description": "State transition sequence continuity verification across event windows.",
    },
]


def build_macro_event_news_transition_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro/event/news transition contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_TRANSITION_CONTEXTS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_transition_contexts": len(df),
        "transition_types": df["transition_type"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_transition_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for transition context registry."""
    return {
        "total_contexts": len(df),
        "transition_types": df["transition_type"].nunique() if "transition_type" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
