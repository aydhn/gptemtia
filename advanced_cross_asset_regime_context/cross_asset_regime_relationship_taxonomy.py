"""Phase 131: Cross-Asset Regime Relationship Taxonomy.

Defines canonical taxonomy and conceptual semantics for cross-asset linkages,
ensuring all relationship categories remain non-signal and non-predictive.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

TAXONOMY_ITEMS: List[Dict[str, Any]] = [
    {
        "taxonomy_id": "tax_co_movement",
        "taxonomy_name": "Cross-Asset Co-Movement Context",
        "relationship_type": "co_movement_context",
        "description": "Descriptive directional or state concurrence across asset classes without trade signaling.",
        "diagnostic_role": "state_concurrence_monitoring",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_divergence",
        "taxonomy_name": "Cross-Asset Divergence Context",
        "relationship_type": "divergence_context",
        "description": "Observation of decoupling between historical or baseline linked assets; strictly NOT trade entry.",
        "diagnostic_role": "decoupling_diagnostics",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_convergence",
        "taxonomy_name": "Cross-Asset Convergence Context",
        "relationship_type": "convergence_context",
        "description": "Observation of narrowing gap across correlated regimes; strictly NOT mean-reversion trading rule.",
        "diagnostic_role": "re-coupling_diagnostics",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_volatility_linkage",
        "taxonomy_name": "Cross-Asset Volatility Linkage Context",
        "relationship_type": "volatility_linkage_context",
        "description": "Assessment of contemporaneous volatility level, compression, and expansion alignment across domains.",
        "diagnostic_role": "volatility_spillover_context",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_trend_linkage",
        "taxonomy_name": "Cross-Asset Trend Linkage Context",
        "relationship_type": "trend_linkage_context",
        "description": "Analysis of multi-asset trend persistence and joint momentum state alignment without directional trade claims.",
        "diagnostic_role": "trend_congruence_context",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_range_linkage",
        "taxonomy_name": "Cross-Asset Range Linkage Context",
        "relationship_type": "range_linkage_context",
        "description": "Examination of joint rangebound consolidation and breakout test regimes across correlated assets.",
        "diagnostic_role": "consolidation_structure_context",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_macro_sensitivity",
        "taxonomy_name": "Macro Sensitivity Regime Context",
        "relationship_type": "macro_sensitivity_context",
        "description": "Contextual mapping of rate, inflation, and growth release states to asset regime behaviors.",
        "diagnostic_role": "macro_environment_mapping",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_event_sensitivity",
        "taxonomy_name": "Event Sensitivity Regime Context",
        "relationship_type": "event_sensitivity_context",
        "description": "Scheduled economic event window positioning and release boundary context.",
        "diagnostic_role": "calendar_window_profiling",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_news_metadata_linkage",
        "taxonomy_name": "News Metadata Linkage Context",
        "relationship_type": "news_metadata_linkage_context",
        "description": "Topic tag clustering and freshness metadata linkages without article text, scraping, or NLP models.",
        "diagnostic_role": "metadata_attention_context",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_transition_alignment",
        "taxonomy_name": "Transition Alignment Context",
        "relationship_type": "transition_alignment_context",
        "description": "Temporal alignment of Phase 130 state transitions between FX and commodity series.",
        "diagnostic_role": "multi_asset_transition_synchronization",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_lead_lag_placeholder",
        "taxonomy_name": "Lead-Lag Placeholder Context",
        "relationship_type": "lead_lag_placeholder_context",
        "description": "Descriptive temporal precedence metadata placeholder without causality estimation or future forecasting.",
        "diagnostic_role": "structural_lead_lag_specification",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_correlation_placeholder",
        "taxonomy_name": "Correlation Placeholder Context",
        "relationship_type": "correlation_placeholder_context",
        "description": "Tabular statistical placeholder schema for correlation coefficients without predictive modeling.",
        "diagnostic_role": "empirical_co_dependence_structure",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
    {
        "taxonomy_id": "tax_uncertainty",
        "taxonomy_name": "Cross-Asset Uncertainty Context",
        "relationship_type": "uncertainty_context",
        "description": "Ambiguity and dispersion quantification across discordant cross-asset regime states.",
        "diagnostic_role": "regime_discordance_measurement",
        "allows_trading_signal": False,
        "allows_prediction": False,
        "requires_no_lookahead": True,
    },
]


def build_cross_asset_regime_relationship_taxonomy_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build taxonomy registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in TAXONOMY_ITEMS:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_relationship_taxonomy(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_relationship_taxonomy(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize relationship taxonomy definitions and safety invariants."""
    return {
        "total_taxonomy_items": len(df),
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals_allowed": bool((~df["allows_trading_signal"]).all()) if not df.empty else True,
        "zero_predictions_allowed": bool((~df["allows_prediction"]).all()) if not df.empty else True,
        "all_require_no_lookahead": bool(df["requires_no_lookahead"].all()) if not df.empty else True,
    }
