"""Phase 122 Quote Microstructure Factor Placeholders Registry.

Defines placeholders for bid-ask spreads, mid-quote shifts, and quote staleness.
Strictly non-signal and research-only placeholders.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_PLACEHOLDER_ONLY

QUOTE_MICROSTRUCTURE_METADATA: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_quote_spread_context_placeholder",
        "factor_family": "quote_microstructure",
        "input_features": ["quote__spread_bps"],
        "calculation_type": "normalized_spread_basis_points",
        "non_signal_usage": "Liquidity cost and spread width placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_quote_mid_change_context_placeholder",
        "factor_family": "quote_microstructure",
        "input_features": ["quote__mid_change_1m"],
        "calculation_type": "high_frequency_midpoint_delta",
        "non_signal_usage": "Short-horizon quote revision rate placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "factor_name": "factor_quote_staleness_context_placeholder",
        "factor_family": "quote_microstructure",
        "input_features": ["quote__staleness_seconds"],
        "calculation_type": "quote_update_latency_seconds",
        "non_signal_usage": "Data freshness and tick latency assessment placeholder.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_quote_microstructure_factor_placeholder_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Quote Microstructure Factor Placeholder Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    records = [dict(item) for item in QUOTE_MICROSTRUCTURE_METADATA]
    df = pd.DataFrame(records)

    summary = {
        "active_profile": active_profile.name,
        "total_factors": len(records),
        "placeholder_factors": len(records),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_PLACEHOLDER_ONLY,
    }
    return df, summary


def summarize_quote_microstructure_factor_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize quote microstructure factor placeholders DataFrame."""
    return {
        "total_factors": len(df),
        "status": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
        "non_signal": True,
    }
