"""Phase 122 Factor Family Registry.

Defines the non-signal factor family taxonomy covering trend, momentum,
volatility, mean-reversion, returns, quote microstructure, macro context,
calendar events, news attention, cross-asset context, regime-prep, and composites.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import (
    FACTOR_FAMILY_CALENDAR_EVENT,
    FACTOR_FAMILY_COMPOSITE,
    FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
    FACTOR_FAMILY_MACRO_CONTEXT,
    FACTOR_FAMILY_MEAN_REVERSION,
    FACTOR_FAMILY_MOMENTUM,
    FACTOR_FAMILY_NEWS_ATTENTION,
    FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
    FACTOR_FAMILY_REGIME_PREP,
    FACTOR_FAMILY_RETURN,
    FACTOR_FAMILY_TREND,
    FACTOR_FAMILY_VOLATILITY,
    FACTOR_PLACEHOLDER_ONLY,
    FACTOR_READY,
)
from advanced_factor_metadata.factor_metadata_models import (
    FactorFamily,
    build_factor_family_id,
)

FACTOR_FAMILY_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "family_label": FACTOR_FAMILY_TREND,
        "family_name": "Trend Factor Family",
        "description": "Directional persistence and slope metrics derived from moving averages and channel breakouts.",
        "source_feature_families": ["moving_average_grid", "donchian_grid", "macd_features"],
        "expected_inputs": ["sma_grid", "ema_grid", "donchian_high", "donchian_low"],
        "non_signal_usage_note": "Research grouping for trend slope and channel context. Strictly non-signal.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_MOMENTUM,
        "family_name": "Momentum Factor Family",
        "description": "Velocity and rate of price changes derived from oscillators and multi-window ROC.",
        "source_feature_families": ["rsi_grid", "roc_grid", "stochastic_grid"],
        "expected_inputs": ["rsi_14", "roc_10", "roc_20", "stoch_k"],
        "non_signal_usage_note": "Research grouping for momentum magnitude. Not an overbought/oversold signal.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_VOLATILITY,
        "family_name": "Volatility Factor Family",
        "description": "Dispersion, range, and realized variance metrics across parameterized observation windows.",
        "source_feature_families": ["atr_grid", "realized_vol_grid", "bollinger_bandwidth"],
        "expected_inputs": ["atr_14", "rolling_std_20", "realized_vol_20", "bb_width_20"],
        "non_signal_usage_note": "Risk and dispersion context. Zero directional claim or position sizing.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_MEAN_REVERSION,
        "family_name": "Mean Reversion Factor Family",
        "description": "Distance-to-mean, standard score (z-score), and oscillation boundary metrics.",
        "source_feature_families": ["zscore_grid", "distance_to_ma_grid", "percentile_rank"],
        "expected_inputs": ["zscore_20", "dist_sma_50", "percentile_100"],
        "non_signal_usage_note": "Distributional distance context. Not an entry or counter-trend signal.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_RETURN,
        "family_name": "Return Factor Family",
        "description": "Multi-horizon trailing returns and cumulative log return representations.",
        "source_feature_families": ["return_grid", "log_return_grid"],
        "expected_inputs": ["ret_1d", "ret_5d", "ret_20d", "log_ret_1d"],
        "non_signal_usage_note": "Trailing historical return observations. Zero forward or lookahead returns.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_QUOTE_MICROSTRUCTURE,
        "family_name": "Quote Microstructure Factor Placeholder",
        "description": "Bid-ask spread widths, mid-quote changes, and order staleness contextual indicators.",
        "source_feature_families": ["quote_spread_grid", "bid_ask_ratio_grid"],
        "expected_inputs": ["spread_bps", "mid_change_1m", "staleness_sec"],
        "non_signal_usage_note": "Execution liquidity hygiene context. Placeholder only.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "family_label": FACTOR_FAMILY_MACRO_CONTEXT,
        "family_name": "Macro Context Factor Family",
        "description": "Point-in-time macroeconomic levels, surprise metrics, and revision indicators.",
        "source_feature_families": ["macro_fusion", "macro_revision_flags"],
        "expected_inputs": ["inflation_rate", "policy_rate", "gdp_growth", "macro_surprise"],
        "non_signal_usage_note": "Macroeconomic backdrop classification. No directional economic bets.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_CALENDAR_EVENT,
        "family_name": "Calendar Event Factor Family",
        "description": "Scheduled economic releases, window proximity indicators, and release delay flags.",
        "source_feature_families": ["calendar_event_windows", "release_delay_features"],
        "expected_inputs": ["event_pre_window", "event_post_window", "event_importance_weight"],
        "non_signal_usage_note": "Event risk awareness and blackout intervals. Not an event-trading strategy.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_NEWS_ATTENTION,
        "family_name": "News Attention Factor Family",
        "description": "Headline entity counts, topic frequency, and metadata attention intensity.",
        "source_feature_families": ["news_topic_fusion", "news_asset_tag_fusion"],
        "expected_inputs": ["topic_attention_count", "asset_tag_count", "macro_tag_count"],
        "non_signal_usage_note": "Metadata-only count aggregation. Zero article text, NLP sentiment, or scraping.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_CROSS_ASSET_CONTEXT,
        "family_name": "Cross-Asset Context Factor Family",
        "description": "Aligned multi-domain feature context across FX, commodities, and macro variables.",
        "source_feature_families": ["cross_domain_fusion", "aligned_cross_asset_matrix"],
        "expected_inputs": ["fx_commodity_corr", "gold_rate_spread", "oil_usd_context"],
        "non_signal_usage_note": "Cross-domain aligned observation matrix. No multi-asset arbitrage trading.",
        "status_label": FACTOR_READY,
        "manual_review_required": False,
    },
    {
        "family_label": FACTOR_FAMILY_REGIME_PREP,
        "family_name": "Regime Prep Factor Placeholder",
        "description": "Candidate feature aggregates structured as inputs for Phase 126+ Regime Classification.",
        "source_feature_families": ["volatility_grid", "macro_fusion", "trend_grid"],
        "expected_inputs": ["regime_vol_input", "regime_trend_input"],
        "non_signal_usage_note": "Preparation contracts for Phase 126+. Does not perform regime classification.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
    {
        "family_label": FACTOR_FAMILY_COMPOSITE,
        "family_name": "Composite Factor Placeholder",
        "description": "Multi-family feature aggregation containers for cross-disciplinary research grouping.",
        "source_feature_families": ["trend_grid", "macro_fusion", "cross_domain_matrix"],
        "expected_inputs": ["comp_tech_input", "comp_macro_input"],
        "non_signal_usage_note": "Multi-feature grouping placeholder. Not an execution strategy or rule engine.",
        "status_label": FACTOR_PLACEHOLDER_ONLY,
        "manual_review_required": True,
    },
]


def build_factor_family_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Family Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    items: List[Dict[str, Any]] = []
    for d in FACTOR_FAMILY_DEFINITIONS:
        family = FactorFamily(
            family_id=build_factor_family_id(d["family_label"]),
            family_label=d["family_label"],
            family_name=d["family_name"],
            description=d["description"],
            source_feature_families=d["source_feature_families"],
            expected_inputs=d["expected_inputs"],
            non_signal_usage_note=d["non_signal_usage_note"],
            status_label=d["status_label"],
            manual_review_required=d["manual_review_required"],
        )
        items.append(family.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_families": len(items),
        "ready_families": sum(1 for i in items if i["status_label"] == FACTOR_READY),
        "placeholder_families": sum(1 for i in items if i["status_label"] == FACTOR_PLACEHOLDER_ONLY),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_READY,
    }
    return df, summary
