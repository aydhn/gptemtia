from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


FX_NEWS_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "fxnews_eur_usd_central_bank",
        "fx_pair": "EUR/USD",
        "news_tag": "CENTRAL_BANK",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Merkez bankası haber başlığı konusu; tam metin indirilmez, sentiment trade sinyali olamaz.",
    },
    {
        "alignment_id": "fxnews_eur_usd_inflation",
        "fx_pair": "EUR/USD",
        "news_tag": "INFLATION",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Enflasyon haber metadata etiketi eşlemesi.",
    },
    {
        "alignment_id": "fxnews_usd_try_turkey",
        "fx_pair": "USD/TRY",
        "news_tag": "TURKEY_ECONOMY",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Türkiye ekonomisi haber metadata konusu bağlantısı.",
    },
    {
        "alignment_id": "fxnews_global_risk",
        "fx_pair": "EUR/USD",
        "news_tag": "RISK_SENTIMENT",
        "metadata_only": True,
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Küresel risk iştahı başlık etiketi; telifli içerik kopyalanmaz.",
    },
]


def build_fx_news_metadata_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(FX_NEWS_ITEMS)
    summary = summarize_fx_news_metadata_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_fx_news_metadata_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_metadata_only = bool(df["metadata_only"].all()) if "metadata_only" in df.columns else False
    all_no_full_text = bool((~df["full_text_collected"]).all()) if "full_text_collected" in df.columns else False
    return {
        "total_alignments": len(df),
        "fx_pairs": list(df["fx_pair"].unique()) if "fx_pair" in df.columns else [],
        "news_tags": list(df["news_tag"].unique()) if "news_tag" in df.columns else [],
        "all_metadata_only": all_metadata_only,
        "all_no_full_text": all_no_full_text,
        "all_non_signal": True,
        "non_signal": True,
        "status": "READY" if (all_metadata_only and all_no_full_text) else "SAFETY_VIOLATION",
    }

