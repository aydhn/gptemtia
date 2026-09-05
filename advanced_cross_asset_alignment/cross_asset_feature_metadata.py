from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


FEATURE_METADATA_ENTRIES: List[Dict[str, Any]] = [
    {
        "feature_name": "fx_eur_usd_sma_w20",
        "source_domain": "fx",
        "aligned_domain": "fx",
        "canonical_symbol": "EUR/USD",
        "namespace": "fx_eur_usd",
        "timestamp_policy": "canonical_utc",
        "join_policy": "join_policy_exact_timestamp",
        "no_lookahead_checked": True,
        "non_signal": True,
        "phase_120_fusion_ready": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "fx_eur_usd_rsi_w14",
        "source_domain": "fx",
        "aligned_domain": "fx",
        "canonical_symbol": "EUR/USD",
        "namespace": "fx_eur_usd",
        "timestamp_policy": "canonical_utc",
        "join_policy": "join_policy_exact_timestamp",
        "no_lookahead_checked": True,
        "non_signal": True,
        "phase_120_fusion_ready": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "commodity_xau_usd_close",
        "source_domain": "commodity",
        "aligned_domain": "fx",
        "canonical_symbol": "XAU/USD",
        "namespace": "commodity_xau_usd",
        "timestamp_policy": "canonical_utc",
        "join_policy": "join_policy_asof_backward",
        "no_lookahead_checked": True,
        "non_signal": True,
        "phase_120_fusion_ready": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "macro_us_10y_yield_yield_diff_1d",
        "source_domain": "macro",
        "aligned_domain": "fx",
        "canonical_symbol": "US_10Y_YIELD",
        "namespace": "macro_us_10y_yield",
        "timestamp_policy": "canonical_utc",
        "join_policy": "join_policy_asof_backward",
        "no_lookahead_checked": True,
        "non_signal": True,
        "phase_120_fusion_ready": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "calendar_fomc_event_active_window",
        "source_domain": "calendar",
        "aligned_domain": "fx",
        "canonical_symbol": "FOMC_RATE_DECISION",
        "namespace": "calendar_fomc_rate_decision",
        "timestamp_policy": "canonical_utc",
        "join_policy": "join_policy_event_window_placeholder",
        "no_lookahead_checked": True,
        "non_signal": True,
        "phase_120_fusion_ready": True,
        "manual_review_required": False,
    },
    {
        "feature_name": "news_central_bank_mention_count_1d",
        "source_domain": "news",
        "aligned_domain": "fx",
        "canonical_symbol": "CENTRAL_BANK",
        "namespace": "news_central_bank",
        "timestamp_policy": "canonical_utc",
        "join_policy": "join_policy_metadata_tag_link",
        "no_lookahead_checked": True,
        "non_signal": True,
        "phase_120_fusion_ready": True,
        "manual_review_required": False,
    },
]


def build_cross_asset_feature_metadata_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(FEATURE_METADATA_ENTRIES)
    summary = summarize_cross_asset_feature_metadata(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_cross_asset_feature_metadata(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_metadata_entries": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    all_lookahead_checked = bool(df["no_lookahead_checked"].all()) if "no_lookahead_checked" in df.columns else False
    ready_count = int((df["phase_120_fusion_ready"]).sum()) if "phase_120_fusion_ready" in df.columns else 0

    return {
        "total_metadata_entries": len(df),
        "total_features": len(df),
        "domains": list(df["source_domain"].unique()) if "source_domain" in df.columns else [],
        "source_domains": list(df["source_domain"].unique()) if "source_domain" in df.columns else [],
        "aligned_domains": list(df["aligned_domain"].unique()) if "aligned_domain" in df.columns else [],
        "all_non_signal": all_non_signal,
        "all_lookahead_checked": all_lookahead_checked,
        "phase_120_fusion_ready_count": ready_count,
        "status": "READY" if (all_non_signal and all_lookahead_checked) else "SAFETY_VIOLATION",
    }

