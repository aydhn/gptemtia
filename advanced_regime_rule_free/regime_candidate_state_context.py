"""Phase 128: Regime Candidate State Context.

Defines candidate state contextual environments strictly for non-signal research annotation.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

CANDIDATE_STATE_CONTEXTS = [
    {
        "context_id": "volatility_candidate_context",
        "family": "volatility",
        "description": "Contextual research annotation reflecting high/normal/compressed dispersion conditions.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "trend_candidate_context",
        "family": "trend",
        "description": "Contextual research annotation reflecting directional persistence or exhaustion without trade bias.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "range_candidate_context",
        "family": "range",
        "description": "Contextual research annotation reflecting mean reversion and boundary oscillation.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "macro_event_candidate_context",
        "family": "macro_event",
        "description": "Contextual research annotation tracking scheduled economic releases and central bank shocks.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "news_attention_candidate_context",
        "family": "news_attention",
        "description": "Contextual research annotation tracking headline metadata volume and attention spikes.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "cross_asset_candidate_context",
        "family": "cross_asset",
        "description": "Contextual research annotation evaluating co-movement, decoupling, and flight-to-safety dynamics.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "transition_candidate_context",
        "family": "transition",
        "description": "Contextual research annotation evaluating market behavior shifts between baseline states.",
        "is_signal": False,
        "non_signal": True,
    },
    {
        "context_id": "uncertainty_candidate_context",
        "family": "uncertain",
        "description": "Contextual research annotation capturing degraded data, elevated drift, or high noise regimes.",
        "is_signal": False,
        "non_signal": True,
    },
]


def build_regime_candidate_state_context_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate state contexts."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for c in CANDIDATE_STATE_CONTEXTS:
        row = c.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_candidate_state_context(df)
    return df, summary


def summarize_regime_candidate_state_context(df: pd.DataFrame) -> Dict:
    """Summarize candidate state context items."""
    total = len(df)
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True
    all_not_signal = bool((~df["is_signal"]).all()) if not df.empty else True

    return {
        "total_candidate_contexts": total,
        "all_non_signal": all_non_signal,
        "all_not_signal": all_not_signal,
        "status": "VALID" if all_non_signal and all_not_signal else "INVALID",
    }
