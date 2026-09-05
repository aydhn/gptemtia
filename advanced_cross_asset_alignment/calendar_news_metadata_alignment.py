from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


CALENDAR_NEWS_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "calnews_fomc_central_bank",
        "calendar_event": "FOMC_RATE_DECISION",
        "news_topic": "CENTRAL_BANK",
        "linkage_type": "event_topic_link",
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "FOMC kararı ve merkez bankası haber konusu bağlantısı; makale metni toplanmaz.",
    },
    {
        "alignment_id": "calnews_cpi_inflation",
        "calendar_event": "US_CPI_RELEASE",
        "news_topic": "INFLATION",
        "linkage_type": "event_topic_link",
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Enflasyon takvimi ve enflasyon haber konu başlığı eşlemesi.",
    },
    {
        "alignment_id": "calnews_eia_energy",
        "calendar_event": "EIA_CRUDE_INVENTORY_RELEASE",
        "news_topic": "CRUDE_OIL",
        "linkage_type": "event_topic_link",
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "EIA ham petrol stok duyurusu ve ham petrol haber etiketleri eşlemesi.",
    },
    {
        "alignment_id": "calnews_nfp_labor",
        "calendar_event": "US_NONFARM_PAYROLLS_RELEASE",
        "news_topic": "LABOR_MARKET",
        "linkage_type": "event_topic_link",
        "full_text_collected": False,
        "sentiment_signal_allowed": False,
        "non_signal": True,
        "notes": "Tarım dışı istihdam verisi ve istihdam piyasası haber etiketleri eşlemesi.",
    },
]


def build_calendar_news_metadata_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(CALENDAR_NEWS_ITEMS)
    summary = summarize_calendar_news_metadata_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_calendar_news_metadata_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_no_full_text = bool((~df["full_text_collected"]).all()) if "full_text_collected" in df.columns else False
    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    return {
        "total_alignments": len(df),
        "calendar_events": list(df["calendar_event"].unique()) if "calendar_event" in df.columns else [],
        "news_topics": list(df["news_topic"].unique()) if "news_topic" in df.columns else [],
        "all_no_full_text": all_no_full_text,
        "all_non_signal": all_non_signal,
        "status": "READY" if (all_no_full_text and all_non_signal) else "SAFETY_VIOLATION",
    }
