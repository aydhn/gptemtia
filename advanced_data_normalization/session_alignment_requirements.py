from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

SESSION_REQUIREMENTS = [
    {
        "session_type": "fx_market_hours",
        "description": "FX 24/5 işlem seansı (Pazar 22:00 UTC - Cuma 22:00 UTC) hizalaması.",
        "canonical_behavior": "Hafta sonu boşlukları işaretlenir; suni bar doldurma yapılmaz.",
        "manual_review_required": False,
    },
    {
        "session_type": "commodity_futures_session",
        "description": "Emtia vadeli kontrat seans saatleri ve takas kesintisi uyumu.",
        "canonical_behavior": "Borsa işlem saatlerine göre seans dışı veriler manuel incelemeye alınır.",
        "manual_review_required": True,
    },
    {
        "session_type": "macro_release_alignment",
        "description": "Makro veri açıklanma saati ile dönem sonu zaman damgasının ayrıştırılması.",
        "canonical_behavior": "Dönem damgası timestamp'e, açıklanma zamanı release_time'a konur.",
        "manual_review_required": False,
    },
    {
        "session_type": "calendar_release_session",
        "description": "Ekonomik takvim planlanan vs gerçekleşen saat eşleştirmesi.",
        "canonical_behavior": "Planlanan saat ve gerçekleşen saat ayrı alanlarda tutulur.",
        "manual_review_required": False,
    },
    {
        "session_type": "news_freshness_alignment",
        "description": "Haber yayın saatinin piyasa fiyat barlarıyla zaman hizalaması.",
        "canonical_behavior": "Yayın saati UTC olarak etiketlenir; geleceğe yönelik veri sızıntısı önlenir.",
        "manual_review_required": True,
    },
]


def build_session_alignment_requirement_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(SESSION_REQUIREMENTS)
    summary = summarize_session_alignment_requirements(df)
    return df, summary


def summarize_session_alignment_requirements(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_requirements": len(df),
        "session_types": df["session_type"].tolist() if "session_type" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 113,
        "target_final_phase": 160,
    }
