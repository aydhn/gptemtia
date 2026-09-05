from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


COMMODITY_NEWS_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "comnews_wti_crude_tag",
        "commodity_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "news_tag": "CRUDE_OIL",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Ham petrol haber başlığı ve konu metadata etiketi eşlemesi.",
    },
    {
        "alignment_id": "comnews_wti_energy_tag",
        "commodity_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "news_tag": "ENERGY",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Enerji sektörü haber etiketi; makale metni toplanmaz.",
    },
    {
        "alignment_id": "comnews_gold_precious_metals",
        "commodity_symbol": "XAU/USD",
        "news_tag": "PRECIOUS_METALS",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Kıymetli madenler haber etiketi eşlemesi.",
    },
    {
        "alignment_id": "comnews_ng_energy_tag",
        "commodity_symbol": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
        "news_tag": "NATURAL_GAS",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Doğal gaz depolama/arz haber etiketi eşlemesi.",
    },
]


def build_commodity_news_metadata_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(COMMODITY_NEWS_ITEMS)
    summary = summarize_commodity_news_metadata_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_commodity_news_metadata_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_metadata_only = bool(df["metadata_only"].all()) if "metadata_only" in df.columns else False
    all_no_full_text = bool((~df["full_text_collected"]).all()) if "full_text_collected" in df.columns else False
    return {
        "total_alignments": len(df),
        "commodities": list(df["commodity_symbol"].unique()) if "commodity_symbol" in df.columns else [],
        "news_tags": list(df["news_tag"].unique()) if "news_tag" in df.columns else [],
        "all_metadata_only": all_metadata_only,
        "all_no_full_text": all_no_full_text,
        "all_non_signal": True,
        "non_signal": True,
        "status": "READY" if (all_metadata_only and all_no_full_text) else "SAFETY_VIOLATION",
    }

