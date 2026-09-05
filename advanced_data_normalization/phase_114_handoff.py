from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

HANDOFF_ITEMS = [
    {
        "lineage_area": "Source-to-normalized field lineage",
        "normalized_dataset_type": "all",
        "transformation_rule": "field_level_canonicalization",
        "source_field": "raw_columns",
        "target_field": "canonical_fields",
        "mapping_source": "canonical_field_registry",
        "provenance_need": "Her kanonik alanın hangi ham sütundan türetildiğinin grafiği.",
        "audit_note": "Phase 113 kanonik alan kataloğu Phase 114 soy kütüğüne hazırlandı.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "Symbol mapping provenance",
        "normalized_dataset_type": "dataset_fx_quote",
        "transformation_rule": "symbol_slashing_and_root_mapping",
        "source_field": "pair, symbol",
        "target_field": "normalized_pair, normalized_symbol",
        "mapping_source": "fx_symbol_normalization_enforcement",
        "provenance_need": "Sembol dönüşüm tablosu kaynak ve hedef ilişki kaydı.",
        "audit_note": "FX ve emtia sembol eşlemeleri Phase 114'e devredildi.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "Timestamp timezone provenance",
        "normalized_dataset_type": "all",
        "transformation_rule": "iso8601_utc_normalization",
        "source_field": "timestamp",
        "target_field": "normalized_timestamp",
        "mapping_source": "timestamp_timezone_normalization",
        "provenance_need": "Orijinal saat dilimi ve UTC çevrim dönüşüm kanıtı.",
        "audit_note": "UTC kanonik standardı Phase 114 için hazırlandı.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "Unit/frequency mapping provenance",
        "normalized_dataset_type": "dataset_macro_timeseries",
        "transformation_rule": "vocabulary_standardization",
        "source_field": "unit, frequency",
        "target_field": "normalized_unit, normalized_frequency",
        "mapping_source": "unit_normalization, frequency_normalization",
        "provenance_need": "Birim ve periyot sözlük dönüşüm haritası.",
        "audit_note": "Dönüşüm değer çarpanı uygulanmadı; sözlük standardı kaydedildi.",
        "manual_review_required": True,
    },
    {
        "lineage_area": "Provider name canonicalization provenance",
        "normalized_dataset_type": "dataset_provider_metadata",
        "transformation_rule": "provider_slugification",
        "source_field": "provider_name",
        "target_field": "normalized_provider_name",
        "mapping_source": "provider_name_normalization",
        "provenance_need": "Sağlayıcı takma adları ile kanonik sağlayıcı kimliği bağlantısı.",
        "audit_note": "Credential içermeyen sağlayıcı isimleri bağlandı.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "News metadata-only provenance",
        "normalized_dataset_type": "dataset_news_metadata",
        "transformation_rule": "metadata_only_boundary_preservation",
        "source_field": "tags, headline",
        "target_field": "normalized_tags",
        "mapping_source": "news_topic_tag_normalization_enforcement",
        "provenance_need": "Haber metin gövdesi indirilmediğinin ve telif hakkı güvenliğinin kanıtı.",
        "audit_note": "Sıfır tam metin kuralı teyit edildi.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "Calendar release event provenance",
        "normalized_dataset_type": "dataset_calendar_event",
        "transformation_rule": "event_naming_and_time_split",
        "source_field": "canonical_event, scheduled_time",
        "target_field": "normalized_event, scheduled_time",
        "mapping_source": "calendar_event_normalization_enforcement",
        "provenance_need": "Planlanan ve gerçekleşen saat ayrımının soy kütüğü.",
        "audit_note": "Gecikme süresi verisi ayrık olarak tutuluyor.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "Macro revision/frequency provenance",
        "normalized_dataset_type": "dataset_macro_timeseries",
        "transformation_rule": "timeseries_frequency_revision_policy",
        "source_field": "value, timestamp",
        "target_field": "normalized_value, normalized_timestamp",
        "mapping_source": "macro_indicator_normalization_enforcement",
        "provenance_need": "Revizyon serilerinin ve frekans uyumunun soy kütüğü izi.",
        "audit_note": "Revizyon geçmişi Phase 114 soy kütüğüne hazırlandı.",
        "manual_review_required": True,
    },
    {
        "lineage_area": "Commodity futures metadata provenance",
        "normalized_dataset_type": "dataset_commodity_spot",
        "transformation_rule": "futures_contract_root_derivation",
        "source_field": "symbol",
        "target_field": "normalized_symbol",
        "mapping_source": "commodity_symbol_normalization_enforcement",
        "provenance_need": "Vadeli kontrat kodundan sürekli kontrat köküne dönüşüm kanıtı.",
        "audit_note": "Sürekli kontrat kök eşleştirmesi tamamlandı.",
        "manual_review_required": True,
    },
    {
        "lineage_area": "Duplicate key derivation provenance",
        "normalized_dataset_type": "all",
        "transformation_rule": "canonical_duplicate_key_composite",
        "source_field": "primary_key_fields",
        "target_field": "canonical_duplicate_key",
        "mapping_source": "duplicate_key_normalization",
        "provenance_need": "Bileşik anahtar üretiminde kullanılan alanların tam listesi.",
        "audit_note": "Kayıt silinmediği ve yalnızca anahtar üretildiği doğrulandı.",
        "manual_review_required": False,
    },
    {
        "lineage_area": "Normalized view manifest provenance",
        "normalized_dataset_type": "all",
        "transformation_rule": "view_manifest_record",
        "source_field": "original_ref",
        "target_field": "normalized_ref",
        "mapping_source": "normalized_view_models",
        "provenance_need": "Kaynak dosya URI ile hedef normalize görünüm URI arasındaki birebir bağ.",
        "audit_note": "Non-destructive görünüm referansları bağlandı.",
        "manual_review_required": False,
    },
]


def build_phase_114_lineage_provenance_handoff_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(HANDOFF_ITEMS)
    summary = summarize_phase_114_handoff(df)
    return df, summary


def summarize_phase_114_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_handoff_items": len(df),
        "target_phase": 114,
        "target_phase_name": "Data Lineage and Provenance",
        "lineage_areas": df["lineage_area"].tolist() if "lineage_area" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "destructive_actions": False,
        "current_phase": 113,
        "target_final_phase": 160,
    }
