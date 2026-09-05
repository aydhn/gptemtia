from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityRule, build_quality_rule_id


def build_default_quality_rules(profile: DataQualityProfile) -> List[QualityRule]:
    rule_specs = [
        # Schema compliance
        ("schema_mandatory_fields", "schema_compliance", ["all"], "quality_critical",
         "Zorunlu şema alanlarının DataFrame içinde eksiksiz bulunması kontrolü.", "check_schema_compliance", "Phase 113", True),
        
        # Missing data
        ("missing_field_presence", "missing_data", ["all"], "quality_high",
         "Birincil anahtar veya kritik alanların yokluğu kontrolü.", "check_missing_required_fields", "Phase 113", True),
        ("missing_values_threshold", "missing_data", ["all"], "quality_medium",
         "Kritik alanlarda NaN / null değer oranının kontrolü.", "check_missing_values", "Phase 113", True),
        
        # Stale data
        ("stale_timestamp_check", "stale_data", ["all"], "quality_medium",
         "Veri yaşının belirlenen maksimum eşikten büyük olmaması kontrolü.", "check_stale_timestamp", "Phase 113", True),
         
        # Duplicate data
        ("duplicate_record_keys", "duplicate_data", ["all"], "quality_medium",
         "Birincil anahtar alanları üzerinde mükerrer kayıt kontrolü.", "check_duplicate_records", "Phase 113", True),
         
        # Outlier placeholder
        ("outlier_placeholder_detection", "outlier_placeholder", ["dataset_fx_ohlcv", "dataset_commodity_ohlcv", "dataset_macro_timeseries"], "quality_medium",
         "Sayısal alanlarda aşırı sapma (outlier) placeholder kontrolü (tahribatsız).", "build_outlier_placeholder_findings", "Phase 113", True),
         
        # Timestamp integrity
        ("timestamp_parseability", "timestamp_integrity", ["all"], "quality_high",
         "Zaman damgalarının ISO8601 veya geçerli formata parse edilebilirlik kontrolü.", "check_timestamp_parseability", "Phase 113", True),
        ("timestamp_ordering", "timestamp_integrity", ["all"], "quality_medium",
         "Zaman damgalarının monoton artan sırada olması kontrolü.", "check_timestamp_ordering", "Phase 113", True),
         
        # Frequency / Unit
        ("frequency_vocabulary_check", "frequency_unit", ["dataset_macro_timeseries", "dataset_calendar_event"], "quality_medium",
         "Kanonik frekans değerlerinin sözlük uyumu kontrolü.", "check_frequency_values", "Phase 113", True),
        ("unit_vocabulary_check", "frequency_unit", ["dataset_commodity_spot", "dataset_macro_timeseries"], "quality_medium",
         "Kanonik birim değerlerinin sözlük uyumu kontrolü.", "check_unit_values", "Phase 113", True),
         
        # FX quality
        ("fx_quote_sanity", "fx_quality", ["dataset_fx_quote"], "quality_high",
         "FX quote bid <= ask, spread >= 0 ve mid yaklaşık ortalama kontrolü.", "check_fx_quote_quality", "Phase 113", True),
        ("fx_ohlcv_sanity", "fx_quality", ["dataset_fx_ohlcv"], "quality_high",
         "FX OHLCV alan varlığı ve kanonik çift formatı kontrolü.", "check_fx_ohlcv_quality", "Phase 113", True),
         
        # Commodity quality
        ("commodity_spot_sanity", "commodity_quality", ["dataset_commodity_spot"], "quality_high",
         "Emtia spot fiyat, birim ve para birimi alan kontrolü.", "check_commodity_spot_quality", "Phase 113", True),
        ("commodity_ohlcv_sanity", "commodity_quality", ["dataset_commodity_ohlcv"], "quality_high",
         "Emtia OHLCV alan ve bar tutarlılık kontrolü.", "check_commodity_ohlcv_quality", "Phase 113", True),
        ("commodity_futures_metadata_sanity", "commodity_quality", ["dataset_commodity_ohlcv"], "quality_medium",
         "Vadeli işlem kontrat metadata (vade, kök sembol) alan kontrolü.", "check_futures_metadata_quality", "Phase 113", True),
         
        # Macro quality
        ("macro_timeseries_sanity", "macro_quality", ["dataset_macro_timeseries"], "quality_high",
         "Makro zaman serisi indikatör, değer, bölge ve frekans kontrolü.", "check_macro_timeseries_quality", "Phase 113", True),
        ("macro_release_metadata_sanity", "macro_quality", ["dataset_macro_timeseries", "dataset_release_event"], "quality_medium",
         "Makro revizyon durumu ve yayın referansı kontrolü.", "check_macro_release_metadata_quality", "Phase 113", True),
         
        # Calendar quality
        ("calendar_event_sanity", "calendar_quality", ["dataset_calendar_event"], "quality_high",
         "Ekonomik takvim olay zamanı, bölge, etki ve kategori kontrolü.", "check_calendar_event_quality", "Phase 113", True),
        ("calendar_release_values_sanity", "calendar_quality", ["dataset_release_event"], "quality_medium",
         "Açıklanan, beklenen, önceki değer tutarlılık kontrolü.", "check_release_event_quality", "Phase 113", True),
         
        # News metadata quality
        ("news_metadata_integrity", "news_metadata_quality", ["dataset_news_metadata"], "quality_high",
         "Haber metadata başlık/özet referansı, kaynak ve etiket kontrolü.", "check_news_metadata_quality", "Phase 113", True),
        ("news_item_reference_integrity", "news_metadata_quality", ["dataset_news_metadata"], "quality_medium",
         "Haber öğesi referansı ve no-sentiment-as-signal kontrolü.", "check_news_item_reference_quality", "Phase 113", True),
         
        # Provider metadata quality
        ("provider_metadata_credential_leak", "provider_metadata_quality", ["dataset_provider_metadata"], "quality_critical",
         "Sağlayıcı metadatasında API key/secret/token sızıntısı olmaması kontrolü.", "check_provider_metadata_quality", "Phase 113", True),
        ("provider_no_scraping_policy", "provider_metadata_quality", ["dataset_provider_metadata"], "quality_high",
         "Sağlayıcı no-scraping politikasının varlığı kontrolü.", "check_provider_metadata_quality", "Phase 113", True),
         
        # OHLC consistency
        ("ohlc_bar_geometry", "ohlc_consistency", ["dataset_fx_ohlcv", "dataset_commodity_ohlcv"], "quality_high",
         "High >= Low, High >= Open/Close, Low <= Open/Close kontrolleri.", "check_ohlc_consistency", "Phase 113", True),
         
        # Quote consistency
        ("quote_spread_geometry", "quote_consistency", ["dataset_fx_quote"], "quality_high",
         "Bid <= Ask ve Spread >= 0 tutarlılık kontratı.", "check_quote_consistency", "Phase 113", True),
         
        # Event release consistency
        ("event_release_timing", "event_release_consistency", ["dataset_calendar_event", "dataset_release_event"], "quality_medium",
         "Zamanlama ve revizyon durumu tutarlılık kontratı.", "check_event_release_consistency", "Phase 113", True),
         
        # News copyright quality
        ("news_copyright_no_scraping_boundary", "news_copyright_quality", ["dataset_news_metadata"], "quality_critical",
         "Tam metin, ham makale gövdesi veya scraping içeriğinin kesinlikle engellenmesi.", "check_news_copyright_boundary", "Phase 113", True),
    ]

    rules = []
    for name, domain, ds_types, sev, desc, func_ref, owner, manual in rule_specs:
        rule = QualityRule(
            rule_id=build_quality_rule_id(name, domain),
            rule_name=name,
            rule_domain=domain,
            dataset_types=ds_types,
            severity_label=sev,
            description=desc,
            check_function_ref=func_ref,
            future_phase_owner=owner,
            manual_review_required=manual,
            warnings=[]
        )
        rules.append(rule)
    return rules


def build_quality_rule_registry(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = build_default_quality_rules(profile)
    records = [r.to_dict() for r in rules]
    df = pd.DataFrame.from_records(records)
    summary = summarize_quality_rule_registry(df)
    return df, summary


def summarize_quality_rule_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "rule_names": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domains": sorted(list(df["rule_domain"].unique())) if "rule_domain" in df.columns else [],
        "severities": df["severity_label"].value_counts().to_dict() if "severity_label" in df.columns else {},
        "current_phase": 112,
        "target_final_phase": 160,
    }
