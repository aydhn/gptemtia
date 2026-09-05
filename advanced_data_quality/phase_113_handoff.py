from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile

HANDOFF_ITEMS = [
    {
        "normalization_area": "FX symbol normalization enforcement",
        "source_phase": "Phase 107",
        "affected_dataset_type": "dataset_fx_ohlcv",
        "issue_detected_by_quality_rule": "fx_quote_integrity",
        "normalization_need": "Slash vs unslashed pair canonicalization (e.g. USD/TRY vs USDTRY).",
        "suggested_phase_113_module": "normalization_fx_symbols",
        "manual_review_required": False,
    },
    {
        "normalization_area": "Commodity symbol normalization enforcement",
        "source_phase": "Phase 108",
        "affected_dataset_type": "dataset_commodity_spot",
        "issue_detected_by_quality_rule": "commodity_spot_sanity",
        "normalization_need": "Kanonik emtia sembolleri ve kontrat kök eşleştirmesi.",
        "suggested_phase_113_module": "normalization_commodity_symbols",
        "manual_review_required": False,
    },
    {
        "normalization_area": "Macro indicator/frequency/unit normalization",
        "source_phase": "Phase 109",
        "affected_dataset_type": "dataset_macro_timeseries",
        "issue_detected_by_quality_rule": "macro_timeseries_sanity",
        "normalization_need": "Yıllık/aylık frekans ve birim (yüzde, endeks) format uyumu.",
        "suggested_phase_113_module": "normalization_macro_indicators",
        "manual_review_required": True,
    },
    {
        "normalization_area": "Calendar timezone/session normalization",
        "source_phase": "Phase 110",
        "affected_dataset_type": "dataset_calendar_event",
        "issue_detected_by_quality_rule": "calendar_event_sanity",
        "normalization_need": "Yerel saat dilimlerini UTC formatına standartlaştırma.",
        "suggested_phase_113_module": "normalization_calendar_timezone",
        "manual_review_required": False,
    },
    {
        "normalization_area": "Calendar release timestamp alignment",
        "source_phase": "Phase 110",
        "affected_dataset_type": "dataset_release_event",
        "issue_detected_by_quality_rule": "calendar_release_values_sanity",
        "normalization_need": "Açıklanma saati ile planlanan saat arasındaki gecikme hizalaması.",
        "suggested_phase_113_module": "normalization_release_timestamps",
        "manual_review_required": True,
    },
    {
        "normalization_area": "News topic/tag normalization",
        "source_phase": "Phase 111",
        "affected_dataset_type": "dataset_news_metadata",
        "issue_detected_by_quality_rule": "news_metadata_integrity",
        "normalization_need": "Haber etiketlerinin küçük harf ve standart liste tipine dönüştürülmesi.",
        "suggested_phase_113_module": "normalization_news_taxonomy",
        "manual_review_required": False,
    },
    {
        "normalization_area": "Provider metadata canonicalization",
        "source_phase": "Phase 106",
        "affected_dataset_type": "dataset_provider_metadata",
        "issue_detected_by_quality_rule": "provider_policy_presence",
        "normalization_need": "Sağlayıcı isim ve tip tanımlarının standartlaştırılması.",
        "suggested_phase_113_module": "normalization_provider_metadata",
        "manual_review_required": False,
    },
    {
        "normalization_area": "Duplicate key normalization",
        "source_phase": "Phase 112",
        "affected_dataset_type": "all",
        "issue_detected_by_quality_rule": "duplicate_record_keys",
        "normalization_need": "Mükerrer anahtarların tekilleştirme stratejisi (son kaydı koruma vb.).",
        "suggested_phase_113_module": "normalization_deduplication",
        "manual_review_required": True,
    },
    {
        "normalization_area": "Timestamp canonical timezone",
        "source_phase": "Phase 112",
        "affected_dataset_type": "all",
        "issue_detected_by_quality_rule": "timestamp_parseability",
        "normalization_need": "Tüm zaman serilerinin ISO8601 UTC formatına çevrilmesi.",
        "suggested_phase_113_module": "normalization_timestamps",
        "manual_review_required": False,
    },
    {
        "normalization_area": "Unit conversion policy placeholder",
        "source_phase": "Phase 112",
        "affected_dataset_type": "dataset_commodity_spot",
        "issue_detected_by_quality_rule": "unit_vocabulary_check",
        "normalization_need": "Ons, varil, bushel birim çevrim politikası taslağı.",
        "suggested_phase_113_module": "normalization_unit_conversion",
        "manual_review_required": True,
    },
    {
        "normalization_area": "Schema version alignment",
        "source_phase": "Phase 112",
        "affected_dataset_type": "all",
        "issue_detected_by_quality_rule": "schema_mandatory_fields",
        "normalization_need": "Şema sürümlerinin v1.0 sözleşmesine uygunluğunun garantilenmesi.",
        "suggested_phase_113_module": "normalization_schema_alignment",
        "manual_review_required": False,
    },
]


def build_phase_113_normalization_handoff_report(
    profile: DataQualityProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(HANDOFF_ITEMS)
    summary = summarize_phase_113_handoff(df)
    return df, summary


def summarize_phase_113_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_areas": len(df),
        "target_phase": 113,
        "target_phase_name": "Data Normalization Layer",
        "areas": df["normalization_area"].tolist() if "normalization_area" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 112,
        "target_final_phase": 160,
    }
