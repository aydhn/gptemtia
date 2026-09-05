from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationRule,
    build_normalization_rule_id,
)

DEFAULT_RULES_SPEC = [
    {
        "name": "canonical_schema_enforcement",
        "domain": "canonical_schema",
        "dataset_types": ["all"],
        "action_label": "action_canonicalize_schema_version",
        "description": "Veri setinin kanonik şema yapısına uygunluğunu denetler.",
        "source_field": "schema_id",
        "target_field": "canonical_schema_id",
        "manual_review_required": False,
    },
    {
        "name": "canonical_field_mapping",
        "domain": "canonical_field",
        "dataset_types": ["all"],
        "action_label": "action_create_normalized_view",
        "description": "Kaynak alan adlarını kanonik alan kataloğuyla eşler.",
        "source_field": "field_name",
        "target_field": "canonical_field_name",
        "manual_review_required": False,
    },
    {
        "name": "schema_version_standardization",
        "domain": "schema_version",
        "dataset_types": ["all"],
        "action_label": "action_canonicalize_schema_version",
        "description": "Şema sürümlerini 'vX.Y' standart etiketine dönüştürür.",
        "source_field": "version",
        "target_field": "normalized_schema_version",
        "manual_review_required": False,
    },
    {
        "name": "provider_name_canonicalization",
        "domain": "provider_name",
        "dataset_types": ["dataset_provider_metadata", "all"],
        "action_label": "action_canonicalize_provider",
        "description": "Sağlayıcı isimlerini standart küçük harf slug formatına dönüştürür.",
        "source_field": "provider_name",
        "target_field": "normalized_provider_name",
        "manual_review_required": False,
    },
    {
        "name": "fx_symbol_slashed_standard",
        "domain": "fx_symbol",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_fx_quote"],
        "action_label": "action_canonicalize_symbol",
        "description": "FX sembollerini standart ISO 'BASE/QUOTE' (örn. EUR/USD) formatına dönüştürür.",
        "source_field": "pair",
        "target_field": "normalized_pair",
        "manual_review_required": False,
    },
    {
        "name": "commodity_symbol_root_standard",
        "domain": "commodity_symbol",
        "dataset_types": ["dataset_commodity_spot", "dataset_commodity_ohlcv"],
        "action_label": "action_canonicalize_symbol",
        "description": "Emtia sembollerini kanonik kodlara ve sürekli vadeli yer tutucularına dönüştürür.",
        "source_field": "symbol",
        "target_field": "normalized_symbol",
        "manual_review_required": False,
    },
    {
        "name": "macro_indicator_code_standard",
        "domain": "macro_indicator",
        "dataset_types": ["dataset_macro_timeseries"],
        "action_label": "action_canonicalize_symbol",
        "description": "Makroekonomik gösterge adlarını merkezi taksonomi kodlarına dönüştürür.",
        "source_field": "indicator",
        "target_field": "normalized_indicator",
        "manual_review_required": False,
    },
    {
        "name": "calendar_event_name_standard",
        "domain": "calendar_event",
        "dataset_types": ["dataset_calendar_event", "dataset_release_event"],
        "action_label": "action_canonicalize_tag",
        "description": "Ekonomik takvim olay isimlerini kanonik olay kimliklerine dönüştürür.",
        "source_field": "canonical_event",
        "target_field": "normalized_event",
        "manual_review_required": False,
    },
    {
        "name": "news_topic_tag_standard",
        "domain": "news_topic_tag",
        "dataset_types": ["dataset_news_metadata"],
        "action_label": "action_canonicalize_tag",
        "description": "Haber konu ve etiketlerini büyük harf ve standart kategori kodlarına dönüştürür.",
        "source_field": "tags",
        "target_field": "normalized_tags",
        "manual_review_required": False,
    },
    {
        "name": "region_iso_standard",
        "domain": "region_currency",
        "dataset_types": ["all"],
        "action_label": "action_canonicalize_region",
        "description": "Ülke ve bölge adlarını ISO alpha-2 veya kanonik bölge koduna çevirir.",
        "source_field": "region",
        "target_field": "normalized_region",
        "manual_review_required": False,
    },
    {
        "name": "currency_iso_standard",
        "domain": "region_currency",
        "dataset_types": ["all"],
        "action_label": "action_canonicalize_region",
        "description": "Para birimi adlarını standart 3 harfli ISO kodlarına çevirir.",
        "source_field": "currency",
        "target_field": "normalized_currency",
        "manual_review_required": False,
    },
    {
        "name": "timestamp_utc_iso_standard",
        "domain": "timestamp_timezone",
        "dataset_types": ["all"],
        "action_label": "action_canonicalize_timestamp",
        "description": "Zaman damgalarını ISO 8601 UTC formatına standartlaştırır, orijinali korur.",
        "source_field": "timestamp",
        "target_field": "normalized_timestamp",
        "manual_review_required": False,
    },
    {
        "name": "session_alignment_policy",
        "domain": "session_alignment",
        "dataset_types": ["dataset_fx_ohlcv", "dataset_commodity_ohlcv", "dataset_calendar_event"],
        "action_label": "action_manual_review_only",
        "description": "Piyasa seans saatleri ve açıklanma gecikmelerini hizalama gereksinimlerini belirler.",
        "source_field": "session_meta",
        "target_field": "session_alignment_status",
        "manual_review_required": True,
    },
    {
        "name": "frequency_canonical_standard",
        "domain": "frequency",
        "dataset_types": ["dataset_macro_timeseries", "dataset_fx_ohlcv", "dataset_commodity_ohlcv"],
        "action_label": "action_canonicalize_frequency",
        "description": "Periyot ifadelerini standart kanonik frekanslara ('1d', '1w', '1mo', vb.) çevirir.",
        "source_field": "frequency",
        "target_field": "normalized_frequency",
        "manual_review_required": False,
    },
    {
        "name": "unit_vocabulary_standard",
        "domain": "unit",
        "dataset_types": ["dataset_macro_timeseries", "dataset_commodity_spot"],
        "action_label": "action_canonicalize_unit",
        "description": "Ölçü birimi ifadelerini standart kanonik sözlüğe uyarlar (değer dönüştürmeden).",
        "source_field": "unit",
        "target_field": "normalized_unit",
        "manual_review_required": False,
    },
    {
        "name": "numeric_type_safe_cast",
        "domain": "numeric_type",
        "dataset_types": ["all"],
        "action_label": "action_create_normalized_view",
        "description": "Sayısal değerleri güvenli float'a çevirir, geçersizleri koruyup izole eder.",
        "source_field": "value",
        "target_field": "normalized_value",
        "manual_review_required": False,
    },
    {
        "name": "string_case_slug_standard",
        "domain": "string_case_slug",
        "dataset_types": ["all"],
        "action_label": "action_create_normalized_view",
        "description": "Metin alanlarını slug veya büyük harf token formatına dönüştürür.",
        "source_field": "name",
        "target_field": "normalized_name",
        "manual_review_required": False,
    },
    {
        "name": "duplicate_key_generation",
        "domain": "duplicate_key",
        "dataset_types": ["all"],
        "action_label": "action_create_normalized_view",
        "description": "Mükerrerlik tespiti için birleşik kanonik anahtar üretir (kayıt silmeden).",
        "source_field": "primary_keys",
        "target_field": "canonical_duplicate_key",
        "manual_review_required": False,
    },
    {
        "name": "normalized_view_generation",
        "domain": "normalized_view",
        "dataset_types": ["all"],
        "action_label": "action_create_normalized_view",
        "description": "Orijinal tabloyu koruyarak ayrı kanonik görünüm tablosu oluşturur.",
        "source_field": "raw_dataframe",
        "target_field": "normalized_dataframe",
        "manual_review_required": False,
    },
    {
        "name": "phase_114_lineage_handoff_prep",
        "domain": "phase_114_handoff",
        "dataset_types": ["all"],
        "action_label": "action_manual_review_only",
        "description": "Tüm alan eşlemeleri ve dönüşüm kararlarını Phase 114 köken izleme için kaydeder.",
        "source_field": "transformation_rule",
        "target_field": "lineage_record",
        "manual_review_required": True,
    },
]


def build_default_normalization_rules(
    profile: DataNormalizationProfile,
) -> List[NormalizationRule]:
    rules = []
    for spec in DEFAULT_RULES_SPEC:
        rule = NormalizationRule(
            rule_id=build_normalization_rule_id(spec["name"], spec["domain"]),
            rule_name=spec["name"],
            rule_domain=spec["domain"],
            dataset_types=spec["dataset_types"],
            action_label=spec["action_label"],
            description=spec["description"],
            source_field=spec["source_field"],
            target_field=spec["target_field"],
            non_destructive=True,
            future_phase_owner="Phase 114",
            manual_review_required=spec.get("manual_review_required", False),
            warnings=[],
        )
        rules.append(rule)
    return rules


def build_normalization_rule_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = build_default_normalization_rules(profile)
    records = [r.to_dict() for r in rules]
    df = pd.DataFrame.from_records(records)
    summary = summarize_normalization_rule_registry(df)
    return df, summary


def summarize_normalization_rule_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "rule_names": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domains": df["rule_domain"].unique().tolist() if "rule_domain" in df.columns else [],
        "all_non_destructive": bool(df["non_destructive"].all()) if "non_destructive" in df.columns else True,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 113,
        "target_final_phase": 160,
    }
