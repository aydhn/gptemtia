from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import (
    DataQualityDomain,
    build_data_quality_domain_id,
)


def build_default_data_quality_domains(profile: DataQualityProfile) -> List[DataQualityDomain]:
    domain_specs = [
        ("data_quality_profile_domain", "Profile Registry", "Data quality profile yönetimi", ["profile_registry"]),
        ("quality_rule_domain", "Quality Rules", "Tüm kalite kural tanımları ve kayıtları", ["rule_registry"]),
        ("quality_severity_domain", "Severity Hierarchy", "Kural ihlal ciddiyet seviyeleri", ["severity_registry"]),
        ("schema_compliance_domain", "Schema Compliance", "Alan varlığı ve şema uyum kontrolleri", ["schema_compliance_rule_set"]),
        ("missing_data_domain", "Missing Data", "Eksik alan ve eksik veri kontrolleri", ["missing_data_rule_set"]),
        ("stale_data_domain", "Stale Data", "Bayat veri ve tazelik kontrolleri", ["stale_data_rule_set"]),
        ("duplicate_data_domain", "Duplicate Records", "Tekrarlanan kayıt kontrolleri", ["duplicate_data_rule_set"]),
        ("outlier_placeholder_domain", "Outlier Placeholder", "Uç değer tespit placeholder kuralları", ["outlier_placeholder_rule_set"]),
        ("timestamp_integrity_domain", "Timestamp Integrity", "Zaman damgası bütünlük ve sıralama kontrolleri", ["timestamp_integrity_rule_set"]),
        ("frequency_unit_domain", "Frequency & Unit", "Frekans ve birim tutarlılık kontrolleri", ["frequency_unit_rule_set"]),
        ("fx_quality_domain", "FX Quality", "Döviz veri seti kalite kuralları", ["fx_quality_rule_set"]),
        ("commodity_quality_domain", "Commodity Quality", "Emtia spot, vadeli ve ohlcv kuralları", ["commodity_quality_rule_set"]),
        ("macro_quality_domain", "Macro Quality", "Makro zaman serisi ve revizyon kuralları", ["macro_quality_rule_set"]),
        ("calendar_quality_domain", "Calendar Quality", "Ekonomik takvim olay ve sürpriz kuralları", ["calendar_quality_rule_set"]),
        ("news_metadata_quality_domain", "News Metadata Quality", "Haber metadata ve etiketleme kuralları", ["news_metadata_quality_rule_set"]),
        ("provider_metadata_quality_domain", "Provider Metadata Quality", "Sağlayıcı metadata ve lisans/credential kuralları", ["provider_metadata_quality_rule_set"]),
        ("ohlc_consistency_domain", "OHLC Consistency", "OHLC fiyat tutarlılık kontratı", ["ohlc_consistency_contract"]),
        ("quote_consistency_domain", "Quote Consistency", "Bid-ask ve spread tutarlılık kontratı", ["quote_consistency_contract"]),
        ("event_release_consistency_domain", "Event Release Consistency", "Yayın takvimi tutarlılık kontratı", ["event_release_consistency_contract"]),
        ("news_copyright_quality_domain", "News Copyright Boundary", "Telif ve no-scraping sınır kontrolleri", ["news_copyright_rule_set"]),
        ("quality_finding_domain", "Quality Findings", "Kalite bulguları merkezi kaydı", ["quality_finding_registry"]),
        ("manual_review_domain", "Manual Review Queue", "Manuel inceleme kuyruğu (non-destructive)", ["manual_review_queue"]),
        ("provider_quality_score_domain", "Provider Quality Score", "Sağlayıcı kalite puanlama modeli", ["provider_quality_score_report"]),
        ("dataset_quality_score_domain", "Dataset Quality Score", "Veri seti kalite puanlama modeli", ["dataset_quality_score_report"]),
        ("cross_provider_quality_domain", "Cross-Provider Quality", "Sağlayıcılar arası kalite karşılaştırma placeholder", ["cross_provider_quality_placeholder"]),
        ("data_quality_health_domain", "Health Check", "Data quality altyapı sağlık kontrolü", ["data_quality_health_check"]),
        ("data_quality_validation_domain", "Validation", "Kalite kuralları doğrulama raporu", ["data_quality_validation_report"]),
        ("data_quality_safety_domain", "Safety Boundary", "Güvenlik ve no-go sınırları", ["data_quality_safety_boundary"]),
        ("phase_113_handoff_domain", "Phase 113 Handoff", "Phase 113 Data Normalization handoff raporu", ["phase_113_handoff_report"]),
    ]

    domains = []
    for label, name, desc, outputs in domain_specs:
        dom = DataQualityDomain(
            domain_id=build_data_quality_domain_id(label),
            domain_label=label,
            domain_name=name,
            description=desc,
            required_outputs=outputs,
            warnings=[]
        )
        domains.append(dom)
    return domains


def build_data_quality_domain_registry(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    domains = build_default_data_quality_domains(profile)
    records = [d.to_dict() for d in domains]
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_quality_domains(df)
    return df, summary


def summarize_data_quality_domains(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_domains": len(df),
        "domain_labels": df["domain_label"].tolist() if "domain_label" in df.columns else [],
        "current_phase": 112,
        "target_final_phase": 160,
    }
