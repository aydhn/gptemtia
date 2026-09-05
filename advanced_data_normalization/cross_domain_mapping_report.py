from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

CROSS_DOMAIN_MAPPINGS = [
    {
        "mapping_domain": "fx_to_news_tag",
        "source_phase": "Phase 107",
        "source_entity": "EUR/USD, USD/TRY",
        "canonical_entity": "FX_CURRENCY, CENTRAL_BANK",
        "normalized_field": "normalized_tags",
        "related_dataset_types": ["dataset_fx_quote", "dataset_news_metadata"],
        "phase_114_lineage_need": "FX parite haber bağlantı soy kütüğü.",
        "manual_review_required": False,
    },
    {
        "mapping_domain": "commodity_to_news_tag",
        "source_phase": "Phase 108",
        "source_entity": "XAU/USD, BRENT, WTI",
        "canonical_entity": "PRECIOUS_METALS, CRUDE_OIL",
        "normalized_field": "normalized_tags",
        "related_dataset_types": ["dataset_commodity_spot", "dataset_news_metadata"],
        "phase_114_lineage_need": "Emtia haber teması dönüşüm izi.",
        "manual_review_required": False,
    },
    {
        "mapping_domain": "macro_to_calendar_event",
        "source_phase": "Phase 109 & 110",
        "source_entity": "FED_POLICY_RATE, US_CPI_YOY",
        "canonical_entity": "FOMC_RATE_DECISION, US_CPI_RELEASE",
        "normalized_field": "canonical_event",
        "related_dataset_types": ["dataset_macro_timeseries", "dataset_calendar_event"],
        "phase_114_lineage_need": "Makro seri ve takvim olayı ortak kanonik kimlik eşleştirmesi.",
        "manual_review_required": False,
    },
    {
        "mapping_domain": "calendar_to_news_linkage",
        "source_phase": "Phase 110 & 111",
        "source_entity": "FOMC_RATE_DECISION, CBRT_RATE_DECISION",
        "canonical_entity": "CENTRAL_BANK, INTEREST_RATE",
        "normalized_field": "event_linkage_id",
        "related_dataset_types": ["dataset_calendar_event", "dataset_news_metadata"],
        "phase_114_lineage_need": "Takvim olayı ve haber metadata referans bağlantısı.",
        "manual_review_required": True,
    },
    {
        "mapping_domain": "region_currency_to_macro_calendar",
        "source_phase": "Phase 109 & 110",
        "source_entity": "US/USD, TR/TRY, EU/EUR",
        "canonical_entity": "ISO_REGION_ALPHA2, ISO_CURRENCY_CODE",
        "normalized_field": "normalized_region, normalized_currency",
        "related_dataset_types": ["dataset_macro_timeseries", "dataset_calendar_event"],
        "phase_114_lineage_need": "Bölge ve para birimi standartlaşma soy kütüğü.",
        "manual_review_required": False,
    },
    {
        "mapping_domain": "provider_name_to_metadata",
        "source_phase": "Phase 106",
        "source_entity": "Provider Display Name",
        "canonical_entity": "normalized_provider_name (slug)",
        "normalized_field": "provider",
        "related_dataset_types": ["dataset_provider_metadata", "all"],
        "phase_114_lineage_need": "Sağlayıcı takma adından kanonik kimliğe dönüşüm kaydı.",
        "manual_review_required": False,
    },
]


def build_cross_domain_normalized_mapping_report(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(CROSS_DOMAIN_MAPPINGS)
    summary = summarize_cross_domain_normalized_mapping(df)
    return df, summary


def summarize_cross_domain_normalized_mapping(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_mappings": len(df),
        "mapping_domains": df["mapping_domain"].tolist() if "mapping_domain" in df.columns else [],
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 113,
        "target_final_phase": 160,
    }
