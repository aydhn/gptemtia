"""Phase 128: Regime Candidate Feature Sets.

Defines canonical candidate feature sets referencing Phase 127 matrix inputs, Phase 122 factors, and Phase 123 quality.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)

CANDIDATE_FEATURE_SETS = [
    {
        "feature_set_id": "cfs_technical_volatility",
        "feature_set_name": "Technical Volatility Feature Set",
        "source_phase_refs": ["phase_117", "phase_118", "phase_122", "phase_127"],
        "feature_count": 6,
        "features": ["rolling_std", "atr", "realized_volatility", "parkinson_volatility", "garman_klass", "range_pct"],
        "factor_family_ref": "volatility_factor_family",
        "non_signal": True,
    },
    {
        "feature_set_id": "cfs_technical_trend",
        "feature_set_name": "Technical Trend & Momentum Feature Set",
        "source_phase_refs": ["phase_117", "phase_118", "phase_122", "phase_127"],
        "feature_count": 6,
        "features": ["ma_distance", "adx_dmi", "aroon", "rsi", "momentum", "roc"],
        "factor_family_ref": "trend_momentum_factor_family",
        "non_signal": True,
    },
    {
        "feature_set_id": "cfs_range_mean_reversion",
        "feature_set_name": "Range and Mean Reversion Feature Set",
        "source_phase_refs": ["phase_117", "phase_118", "phase_122", "phase_127"],
        "feature_count": 5,
        "features": ["bollinger_bandwidth", "bollinger_percent_b", "range_zscore", "donchian_position", "distance_to_sma"],
        "factor_family_ref": "range_mean_reversion_factor_family",
        "non_signal": True,
    },
    {
        "feature_set_id": "cfs_cross_asset_alignment",
        "feature_set_name": "Cross-Asset Alignment Feature Set",
        "source_phase_refs": ["phase_119", "phase_122", "phase_127"],
        "feature_count": 4,
        "features": ["rolling_correlation_30d", "rolling_correlation_90d", "cross_asset_spread", "beta_to_benchmark"],
        "factor_family_ref": "cross_asset_factor_family",
        "non_signal": True,
    },
    {
        "feature_set_id": "cfs_macro_event_context",
        "feature_set_name": "Macro and Calendar Event Feature Set",
        "source_phase_refs": ["phase_109", "phase_110", "phase_120", "phase_127"],
        "feature_count": 4,
        "features": ["macro_surprise_index", "event_impact_weight", "release_staleness_hours", "pre_release_window_flag"],
        "factor_family_ref": "macro_calendar_factor_family",
        "non_signal": True,
    },
    {
        "feature_set_id": "cfs_news_metadata_attention",
        "feature_set_name": "News Metadata Attention Feature Set",
        "source_phase_refs": ["phase_111", "phase_120", "phase_127"],
        "feature_count": 4,
        "features": ["headline_volume_24h", "urgency_flag_ratio", "source_count", "topic_diversity_score"],
        "factor_family_ref": "news_metadata_factor_family",
        "non_signal": True,
    },
    {
        "feature_set_id": "cfs_quality_drift_diagnostics",
        "feature_set_name": "Data Quality and Drift Diagnostics Set",
        "source_phase_refs": ["phase_112", "phase_123", "phase_124", "phase_127"],
        "feature_count": 4,
        "features": ["feature_quality_score", "feature_drift_psi", "missing_rate_window", "staleness_minutes"],
        "factor_family_ref": "quality_drift_factor_family",
        "non_signal": True,
    },
]


def build_regime_candidate_feature_set_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for candidate feature sets."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for cfs in CANDIDATE_FEATURE_SETS:
        row = cfs.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_regime_candidate_feature_sets(df)
    return df, summary


def summarize_regime_candidate_feature_sets(df: pd.DataFrame) -> Dict:
    """Summarize candidate feature sets."""
    total = len(df)
    total_features = int(df["feature_count"].sum()) if not df.empty else 0
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True

    return {
        "total_feature_sets": total,
        "total_candidate_features": total_features,
        "all_non_signal": all_non_signal,
        "feature_sets_status": "VALID" if all_non_signal and total > 0 else "INVALID",
    }
