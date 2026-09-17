# -*- coding: utf-8 -*-
"""Phase 143: Feature Store Explainability Linkage."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_featurestore_explainability_linkage_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of feature store explainability linkage contracts."""
    prof = profile or get_explainability_profile()

    linkages = [
        ("fs_linkage_brent_returns", "brent_crude_returns", "phase_137_feature_store", "Brent returns feature attribution linkage"),
        ("fs_linkage_gold_volatility", "gold_realized_volatility", "phase_137_feature_store", "Gold realized volatility feature attribution linkage"),
        ("fs_linkage_usd_try_spread", "usd_try_bid_ask_spread", "phase_137_feature_store", "USD/TRY bid-ask spread feature attribution linkage"),
        ("fs_linkage_macro_cpi_rate", "macro_cpi_inflation_rate", "phase_137_feature_store", "Macro CPI inflation rate attribution linkage"),
        ("fs_linkage_metadata_news_counts", "news_metadata_headline_count", "phase_137_feature_store", "Metadata-only news headline count attribution linkage"),
    ]

    rows: List[Dict[str, Any]] = []
    for lid, fname, sourceref, desc in linkages:
        rows.append({
            "linkage_id": lid,
            "feature_name": fname,
            "feature_store_ref": sourceref,
            "description": desc,
            "no_lookahead_enforced": True,
            "metadata_only_enforced": True,
            "source_preserved": True,
            "is_linkage_contract": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_featurestore_explainability_linkage(df)
    return df, summary


def summarize_featurestore_explainability_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature store explainability linkage contracts."""
    return {
        "total_featurestore_linkages": len(df),
        "all_linkage_contract": bool(df["is_linkage_contract"].all()) if not df.empty else True,
        "all_no_lookahead_enforced": bool(df["no_lookahead_enforced"].all()) if not df.empty else True,
        "all_metadata_only_enforced": bool(df["metadata_only_enforced"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
