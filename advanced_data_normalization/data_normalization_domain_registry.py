from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_labels import NORMALIZATION_DOMAINS
from advanced_data_normalization.data_normalization_models import (
    DataNormalizationDomain,
    build_data_normalization_domain_id,
)

DOMAIN_METADATA: Dict[str, Dict[str, Any]] = {
    "data_normalization_profile_domain": {
        "name": "Data Normalization Profiles",
        "description": "Normalizasyon profilleri ve çalışma modu yapılandırması.",
        "outputs": ["profile_registry"],
    },
    "data_normalization_domain": {
        "name": "Normalization Domains",
        "description": "Normalizasyon kapsamındaki veri ve operasyon alanları.",
        "outputs": ["domain_registry"],
    },
    "normalization_rule_domain": {
        "name": "Normalization Rules",
        "description": "Dönüşüm ve kanonikleştirme kuralları kataloğu.",
        "outputs": ["rule_registry"],
    },
    "normalization_status_domain": {
        "name": "Normalization Statuses",
        "description": "Normalizasyon sonuç ve audit durum tanımları.",
        "outputs": ["status_registry"],
    },
    "canonical_schema_domain": {
        "name": "Canonical Schemas",
        "description": "Tüm varlıklar için merkezi kanonik şema sözleşmeleri.",
        "outputs": ["canonical_schema_registry"],
    },
    "canonical_field_domain": {
        "name": "Canonical Fields",
        "description": "Şemalara ait zorunlu, opsiyonel ve birim politikası alanları.",
        "outputs": ["canonical_field_registry"],
    },
    "schema_version_normalization_domain": {
        "name": "Schema Version Normalization",
        "description": "Şema sürümlerinin kanonik vX.Y formatına uyarlanması.",
        "outputs": ["schema_version_registry"],
    },
    "provider_name_normalization_domain": {
        "name": "Provider Name Normalization",
        "description": "Sağlayıcı adlarının standart slug formatına çevrilmesi.",
        "outputs": ["provider_name_registry"],
    },
    "fx_symbol_normalization_domain": {
        "name": "FX Symbol Normalization",
        "description": "Döviz parite sembollerinin standart ISO slash formatına çevrilmesi.",
        "outputs": ["fx_symbol_enforcement_report"],
    },
    "commodity_symbol_normalization_domain": {
        "name": "Commodity Symbol Normalization",
        "description": "Emtia sembollerinin ve vadeli kontrat köklerinin kanonikleştirilmesi.",
        "outputs": ["commodity_symbol_enforcement_report"],
    },
    "macro_indicator_normalization_domain": {
        "name": "Macro Indicator Normalization",
        "description": "Makroekonomik gösterge kodlarının merkezi ontolojiye uyarlanması.",
        "outputs": ["macro_indicator_enforcement_report"],
    },
    "calendar_event_normalization_domain": {
        "name": "Calendar Event Normalization",
        "description": "Ekonomik takvim olay isimlerinin ve açıklamalarının kanonikleştirilmesi.",
        "outputs": ["calendar_event_enforcement_report"],
    },
    "news_topic_tag_normalization_domain": {
        "name": "News Topic/Tag Normalization",
        "description": "Haber konu ve etiketlerinin büyük harf slug taksonomisine dönüştürülmesi.",
        "outputs": ["news_topic_tag_enforcement_report"],
    },
    "region_currency_normalization_domain": {
        "name": "Region and Currency Normalization",
        "description": "Ülke, bölge ve para birimi kodlarının ISO standardına getirilmesi.",
        "outputs": ["region_currency_registry"],
    },
    "timestamp_timezone_normalization_domain": {
        "name": "Timestamp and Timezone Normalization",
        "description": "Tüm zaman damgalarının ISO8601 UTC formatına standartlaştırılması.",
        "outputs": ["timestamp_timezone_registry"],
    },
    "session_alignment_domain": {
        "name": "Session Alignment Requirements",
        "description": "Piyasa seansları ve açıklanma saatleri hizalama gereksinimleri.",
        "outputs": ["session_alignment_registry"],
    },
    "frequency_normalization_domain": {
        "name": "Frequency Normalization",
        "description": "Veri periyotlarının kanonik frekans kodlarına dönüştürülmesi.",
        "outputs": ["frequency_registry"],
    },
    "unit_normalization_domain": {
        "name": "Unit Normalization",
        "description": "Ölçü birimlerinin standart kanonik sözlüğe uyarlanması.",
        "outputs": ["unit_registry"],
    },
    "numeric_type_normalization_domain": {
        "name": "Numeric Type Normalization",
        "description": "Sayısal alanların güvenli float dönüşümü ve geçersiz değer izolasyonu.",
        "outputs": ["numeric_type_registry"],
    },
    "string_case_slug_normalization_domain": {
        "name": "String Case and Slug Normalization",
        "description": "Metin ve etiket alanlarının büyük/küçük harf ve slug standartlaştırması.",
        "outputs": ["string_slug_registry"],
    },
    "duplicate_key_normalization_domain": {
        "name": "Duplicate Key Normalization",
        "description": "Mükerrer anahtarların tekilleştirme anahtarının oluşturulması (silme yapmadan).",
        "outputs": ["duplicate_key_registry"],
    },
    "normalized_view_domain": {
        "name": "Normalized Views",
        "description": "Orijinal veriyi bozmadan sunulan kanonik görünüm modelleri.",
        "outputs": ["normalized_view_registry"],
    },
    "normalization_finding_domain": {
        "name": "Normalization Findings",
        "description": "Normalizasyon kural kontrolünde tespit edilen uyumsuzluklar.",
        "outputs": ["normalization_finding_registry"],
    },
    "normalization_decision_domain": {
        "name": "Normalization Decisions",
        "description": "Her bulgu için uygulanan veya incelenen karar kaydı.",
        "outputs": ["normalization_decision_registry"],
    },
    "manual_review_normalization_domain": {
        "name": "Manual Review Normalization Queue",
        "description": "Otomatik çözülemeyen veya belirsiz kayıtların inceleme kuyruğu.",
        "outputs": ["manual_review_queue"],
    },
    "normalization_scoring_domain": {
        "name": "Normalization Scoring",
        "description": "Veri seti ve sağlayıcı bazlı kanonikleşme oran skoru.",
        "outputs": ["normalization_score_report"],
    },
    "cross_domain_mapping_domain": {
        "name": "Cross-Domain Normalized Mapping",
        "description": "FX, emtia, makro, takvim ve haber arasındaki çapraz ilişki haritası.",
        "outputs": ["cross_domain_mapping_report"],
    },
    "data_normalization_health_domain": {
        "name": "Data Normalization Health",
        "description": "Normalizasyon katmanının sistem bileşen sağlık durumu.",
        "outputs": ["data_normalization_health_check"],
    },
    "data_normalization_validation_domain": {
        "name": "Data Normalization Validation",
        "description": "Sözleşme, güvenlik ve alan bütünlüğü doğrulama raporu.",
        "outputs": ["data_normalization_validation_report"],
    },
    "data_normalization_safety_boundary_domain": {
        "name": "Data Normalization Safety Boundary",
        "description": "No-Go ve Safe-Go güvenlik sınırlarının denetimi.",
        "outputs": ["data_normalization_safety_boundary"],
    },
    "phase_114_handoff_domain": {
        "name": "Phase 114 Lineage & Provenance Handoff",
        "description": "Phase 114 veri kökeni ve soy kütüğü için devir raporu.",
        "outputs": ["phase_114_handoff_report"],
    },
    "unknown_normalization_domain": {
        "name": "Unknown Normalization Domain",
        "description": "Sınıflandırılamayan normalizasyon istekleri için yedek alan.",
        "outputs": [],
    },
}


def build_default_data_normalization_domains(
    profile: DataNormalizationProfile,
) -> List[DataNormalizationDomain]:
    domains = []
    for d_label in NORMALIZATION_DOMAINS:
        meta = DOMAIN_METADATA.get(
            d_label,
            {"name": d_label.replace("_", " ").title(), "description": "", "outputs": []},
        )
        domain = DataNormalizationDomain(
            domain_id=build_data_normalization_domain_id(d_label),
            domain_label=d_label,
            domain_name=meta["name"],
            description=meta["description"],
            required_outputs=meta["outputs"],
            warnings=[],
        )
        domains.append(domain)
    return domains


def build_data_normalization_domain_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = build_default_data_normalization_domains(profile)
    records = [d.to_dict() for d in items]
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_normalization_domains(df)
    return df, summary


def summarize_data_normalization_domains(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_domains": len(df),
        "domain_labels": df["domain_label"].tolist() if "domain_label" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
