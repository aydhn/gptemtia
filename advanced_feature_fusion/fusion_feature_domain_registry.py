from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_fusion.fusion_feature_config import (
    FusionFeatureProfile,
    get_default_fusion_feature_profile,
)
from advanced_feature_fusion.fusion_feature_models import (
    FusionFeatureDomain,
    build_fusion_feature_domain_id,
)


DOMAIN_SPECS: List[Dict[str, Any]] = [
    {
        "label": "fusion_feature_profile_domain",
        "name": "Fusion Feature Profile Registry",
        "description": "Profil yönetimi, faz parametreleri ve güvenlik sınırları.",
        "required_outputs": ["profile_id", "profile_name", "status_label"],
    },
    {
        "label": "macro_fusion_contract_domain",
        "name": "Macro Feature Fusion Contracts",
        "description": "Makro zaman serisi, release lag ve revizyon sözleşmeleri.",
        "required_outputs": ["contract_id", "contract_name", "fusion_family"],
    },
    {
        "label": "calendar_event_fusion_contract_domain",
        "name": "Calendar Event Fusion Contracts",
        "description": "Ekonomik takvim olay penceresi ve önem derecesi sözleşmeleri.",
        "required_outputs": ["contract_id", "contract_name", "fusion_family"],
    },
    {
        "label": "release_event_fusion_contract_domain",
        "name": "Release Event Fusion Contracts",
        "description": "Actual, forecast, previous, delay ve surprise sözleşmeleri.",
        "required_outputs": ["contract_id", "contract_name", "fusion_family"],
    },
    {
        "label": "news_metadata_fusion_contract_domain",
        "name": "News Metadata Fusion Contracts",
        "description": "Haber konu, etiket, kaynak ve takvim bağıntı sözleşmeleri (metadata-only).",
        "required_outputs": ["contract_id", "contract_name", "fusion_family"],
    },
    {
        "label": "macro_release_lag_policy_domain",
        "name": "Macro Release Lag Policy",
        "description": "Makro verisinin sadece release zamanı sonrasında kullanımını denetleyen politika.",
        "required_outputs": ["policy_id", "policy_name", "future_data_allowed"],
    },
    {
        "label": "calendar_event_window_policy_domain",
        "name": "Calendar Event Window Policy",
        "description": "Olay öncesi ve sonrası bayrak pencereleri politikası.",
        "required_outputs": ["policy_id", "policy_name", "non_signal"],
    },
    {
        "label": "news_metadata_only_policy_domain",
        "name": "News Metadata-Only Policy",
        "description": "Haber tam metni, scraping ve telifli veri kullanımını kesin yasaklayan politika.",
        "required_outputs": ["policy_id", "policy_name", "full_text_allowed"],
    },
    {
        "label": "fusion_timestamp_alignment_domain",
        "name": "Fusion Timestamp Alignment Policy",
        "description": "Evrensel UTC ve zaman sırası doğrulama politikası.",
        "required_outputs": ["policy_id", "policy_name", "future_data_allowed"],
    },
    {
        "label": "fusion_asof_join_domain",
        "name": "Fusion Asof Join Policy",
        "description": "Sadece geriye dönük (backward-only) deterministik asof birleştirme motoru.",
        "required_outputs": ["policy_id", "policy_name", "future_data_allowed"],
    },
    {
        "label": "no_lookahead_fusion_guard_domain",
        "name": "No-Lookahead Fusion Guard",
        "description": "Gelecek verisi, negatif shift ve yasaklı kolon denetim muhafızı.",
        "required_outputs": ["guard_id", "guard_name", "status_label"],
    },
    {
        "label": "macro_feature_fusion_domain",
        "name": "Macro Feature Fusion Engine",
        "description": "Makro seviye, değişim ve frekans özellikleri.",
        "required_outputs": ["macro_feature_name", "output_field"],
    },
    {
        "label": "macro_surprise_placeholder_domain",
        "name": "Macro Surprise Feature Placeholder",
        "description": "Actual - forecast sürpriz temsilcisi.",
        "required_outputs": ["surprise_field", "status_label"],
    },
    {
        "label": "macro_revision_placeholder_domain",
        "name": "Macro Revision Feature Placeholder",
        "description": "Revizyon durumu temsilcisi.",
        "required_outputs": ["revision_field", "status_label"],
    },
    {
        "label": "calendar_event_window_feature_domain",
        "name": "Calendar Event Window Features",
        "description": "Pre-event ve post-event zaman pencereleri bayrakları.",
        "required_outputs": ["window_field", "status_label"],
    },
    {
        "label": "release_event_feature_domain",
        "name": "Release Event Features",
        "description": "Gecikme süresi, actual varlığı ve revize önceki değer bayrakları.",
        "required_outputs": ["feature_name", "output_field"],
    },
    {
        "label": "event_importance_placeholder_domain",
        "name": "Event Importance Placeholder",
        "description": "Olay önem ağırlığı temsilcisi.",
        "required_outputs": ["importance_field", "status_label"],
    },
    {
        "label": "news_topic_fusion_domain",
        "name": "News Topic Feature Fusion",
        "description": "Haber konu bayrakları ve konu sayıları.",
        "required_outputs": ["topic_field", "status_label"],
    },
    {
        "label": "news_asset_tag_fusion_domain",
        "name": "News Asset Tag Feature Fusion",
        "description": "Varlık ve makro etiket sayıları.",
        "required_outputs": ["tag_field", "status_label"],
    },
    {
        "label": "news_event_linkage_domain",
        "name": "News Event Linkage Features",
        "description": "Haber ile takvim olayı arasındaki referans bağıntısı.",
        "required_outputs": ["linkage_field", "status_label"],
    },
    {
        "label": "news_freshness_placeholder_domain",
        "name": "News Freshness Feature Placeholder",
        "description": "Haber tazelik ve yaş göstergesi.",
        "required_outputs": ["freshness_field", "status_label"],
    },
    {
        "label": "macro_calendar_fusion_domain",
        "name": "Macro-Calendar Cross Fusion",
        "description": "Makro gösterge ile ekonomik takvim release eşlemesi.",
        "required_outputs": ["fusion_pair", "status_label"],
    },
    {
        "label": "macro_news_fusion_domain",
        "name": "Macro-News Cross Fusion",
        "description": "Makro gösterge ile haber makro etiketleri eşlemesi.",
        "required_outputs": ["fusion_pair", "status_label"],
    },
    {
        "label": "calendar_news_fusion_domain",
        "name": "Calendar-News Cross Fusion",
        "description": "Takvim olayı ile haber referansı eşlemesi.",
        "required_outputs": ["fusion_pair", "status_label"],
    },
    {
        "label": "cross_domain_context_fusion_domain",
        "name": "Cross-Domain Context Fusion",
        "description": "FX ve Emtia varlıklarına makro/takvim/haber bağlamı ekleme.",
        "required_outputs": ["context_name", "status_label"],
    },
    {
        "label": "fusion_feature_matrix_contract_domain",
        "name": "Fusion Feature Matrix Contracts",
        "description": "Çok alanlı füzyon özellik matrisi sözleşmeleri.",
        "required_outputs": ["contract_name", "status_label"],
    },
    {
        "label": "fusion_feature_matrix_domain",
        "name": "Fusion Feature Matrix Engine",
        "description": "Birleştirilmiş bağlamsal özellik matrisi ve manifest.",
        "required_outputs": ["matrix_name", "row_count", "feature_count"],
    },
    {
        "label": "fusion_feature_metadata_domain",
        "name": "Fusion Feature Metadata Registry",
        "description": "Özellik metadata, zaman politikası ve birleştirme türü kaydı.",
        "required_outputs": ["metadata_id", "feature_name", "fusion_family"],
    },
    {
        "label": "fusion_feature_dependency_domain",
        "name": "Fusion Feature Dependency Registry",
        "description": "Özelliklerin girdi alanı bağımlılıkları haritası.",
        "required_outputs": ["feature_name", "dependencies"],
    },
    {
        "label": "fusion_feature_validation_domain",
        "name": "Fusion Feature Validation Engine",
        "description": "Sıfır gelecek sızıntısı ve yasaklı kolon denetim kuralları.",
        "required_outputs": ["rule_id", "rule_name", "status_label"],
    },
    {
        "label": "fusion_quality_handoff_domain",
        "name": "Fusion Quality Handoff Assessment",
        "description": "Füzyon kalitesi ve eksik alan inceleme kuyruğu.",
        "required_outputs": ["handoff_id", "status_label"],
    },
    {
        "label": "fusion_feature_health_domain",
        "name": "Fusion Feature Health Check",
        "description": "Sistem sağlığı ve modül bağımlılık kontrolleri.",
        "required_outputs": ["component", "status_label"],
    },
    {
        "label": "fusion_feature_safety_domain",
        "name": "Fusion Feature Safety Boundary",
        "description": "NO-GO ve SAFE-GO prensipleri.",
        "required_outputs": ["rule_id", "rule_type", "enforced"],
    },
    {
        "label": "fusion_feature_report_domain",
        "name": "Fusion Feature Report Generation",
        "description": "Füzyon özellik matrisi ve kalite metrikleri raporlama motoru.",
        "required_outputs": ["report_id", "status_label"],
    },
    {
        "label": "phase_121_handoff_domain",
        "name": "Phase 121 Feature Validation Handoff",
        "description": "Phase 121 No-Lookahead ve Validasyon katmanına resmi devir maddeleri.",
        "required_outputs": ["item_id", "topic", "status"],
    },
]


def build_fusion_feature_domain_registry(
    profile: FusionFeatureProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_fusion_feature_profile()
    rows = []
    for spec in DOMAIN_SPECS:
        domain = FusionFeatureDomain(
            domain_id=build_fusion_feature_domain_id(spec["label"]),
            domain_label=spec["label"],
            domain_name=spec["name"],
            description=spec["description"],
            required_outputs=spec["required_outputs"],
            warnings=[],
        )
        rows.append(domain.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_fusion_feature_domains(df)
    summary["active_profile"] = active_profile.name
    summary["status"] = "READY"
    return df, summary


def summarize_fusion_feature_domains(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_domains": 0, "status": "EMPTY"}
    return {
        "total_domains": len(df),
        "total_required_outputs": sum(len(x) for x in df["required_outputs"]),
        "status": "READY",
    }


def get_fusion_feature_domains_registry() -> pd.DataFrame:
    """Return DataFrame of domain registry."""
    df, _ = build_fusion_feature_domain_registry()
    return df


def get_fusion_feature_domains_summary() -> Dict[str, Any]:
    """Return summary dictionary of domain registry."""
    _, summary = build_fusion_feature_domain_registry()
    return summary
