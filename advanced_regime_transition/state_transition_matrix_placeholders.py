"""Phase 130: State Transition Matrix Placeholders.

Provides structural matrix placeholders for candidate regime transitions.
Explicitly non-executable: no Markov chain fitting, no forward probability generation,
no trading suggestions.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

TRANSITION_MATRIX_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "matrix_identifier": "volatility_regime_transition_matrix_placeholder",
        "matrix_family": "volatility",
        "row_states": "vol_compression, vol_normal, vol_expansion",
        "column_states": "vol_compression, vol_normal, vol_expansion",
        "is_placeholder_only": True,
        "is_fitted_markov_model": False,
        "produces_trade_probabilities": False,
        "non_signal": True,
        "description": "3x3 structural transition placeholder for volatility regimes",
    },
    {
        "matrix_identifier": "trend_range_transition_matrix_placeholder",
        "matrix_family": "trend_range",
        "row_states": "bullish_trend, bearish_trend, range_bound",
        "column_states": "bullish_trend, bearish_trend, range_bound",
        "is_placeholder_only": True,
        "is_fitted_markov_model": False,
        "produces_trade_probabilities": False,
        "non_signal": True,
        "description": "3x3 structural transition placeholder for directional and consolidation states",
    },
    {
        "matrix_identifier": "macro_reaction_transition_matrix_placeholder",
        "matrix_family": "macro_event",
        "row_states": "pre_release_dormant, release_active, post_release_absorbed",
        "column_states": "pre_release_dormant, release_active, post_release_absorbed",
        "is_placeholder_only": True,
        "is_fitted_markov_model": False,
        "produces_trade_probabilities": False,
        "non_signal": True,
        "description": "3x3 structural placeholder for event window regime transitions",
    },
]


def build_state_transition_matrix_placeholder_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition matrix placeholder registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    rows = []
    for item in TRANSITION_MATRIX_PLACEHOLDERS:
        row = dict(item)
        row["matrix_id"] = item["matrix_identifier"]
        row["is_placeholder"] = item["is_placeholder_only"]
        row["markov_chain_fitted"] = item["is_fitted_markov_model"]
        row["forward_probability_generated"] = item["produces_trade_probabilities"]
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_state_transition_matrix_placeholders(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_state_transition_matrix_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state transition matrix placeholders."""
    is_ph = bool(df["is_placeholder_only"].all()) if not df.empty and "is_placeholder_only" in df.columns else True
    zero_markov = bool(not df["is_fitted_markov_model"].any()) if not df.empty and "is_fitted_markov_model" in df.columns else True
    return {
        "total_matrix_placeholders": len(df),
        "total_matrix_entries": len(df),
        "all_placeholder_only": is_ph,
        "all_placeholders": is_ph,
        "zero_markov_models_fitted": zero_markov,
        "zero_markov_fitted": zero_markov,
        "zero_trade_probabilities": True,
        "non_signal_guaranteed": True,
    }

