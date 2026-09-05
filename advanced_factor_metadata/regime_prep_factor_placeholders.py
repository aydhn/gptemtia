"""Phase 122 Regime Prep Factor Placeholders Registry.

Defines candidate feature aggregations structured as inputs for Phase 126+
Regime Classification. Does not perform regime classification or switching.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_PLACEHOLDER_ONLY

REGIME_PREP_FACTOR_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_regime_volatility_prep_placeholder",
        "factor_family": "regime_prep",
        "input_features": ["volatility__realized_vol_20", "volatility__atr_14"],
        "downstream_phase_target": "Phase 127 Volatility Regime Classifier",
        "non_signal_usage": "Candidate volatility feature bundle for future regime detection.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_regime_trend_prep_placeholder",
        "factor_family": "regime_prep",
        "input_features": ["trend__sma_slope_50", "trend__donchian_high_20"],
        "downstream_phase_target": "Phase 128 Trend Regime Classifier",
        "non_signal_usage": "Candidate trend persistence bundle for future regime models.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_regime_macro_context_prep_placeholder",
        "factor_family": "regime_prep",
        "input_features": ["fusion__macro_cpi_rate", "fusion__macro_policy_rate"],
        "downstream_phase_target": "Phase 130 Macro Regime Classifier",
        "non_signal_usage": "Candidate macro cycle state bundle for future regime classifiers.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_regime_event_context_prep_placeholder",
        "factor_family": "regime_prep",
        "input_features": ["fusion__event_pre_release_window", "fusion__event_importance_weight"],
        "downstream_phase_target": "Phase 132 Regime Transition Detection",
        "non_signal_usage": "Candidate high-impact event window bundle for transition monitoring.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_regime_prep_factor_placeholder_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Regime Prep Factor Placeholder Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in REGIME_PREP_FACTOR_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "placeholder_factors": len(records),
        "target_regime_phases": ["Phase 127", "Phase 128", "Phase 130", "Phase 132"],
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_PLACEHOLDER_ONLY,
    }
    return df, summary


def summarize_regime_prep_factor_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime prep factor placeholders DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
        "non_signal": True,
    }
