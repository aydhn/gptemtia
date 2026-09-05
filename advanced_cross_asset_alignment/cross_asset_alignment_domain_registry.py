from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    CrossAssetAlignmentDomain,
    build_cross_asset_alignment_domain_id,
)
from advanced_cross_asset_alignment.cross_asset_alignment_labels import list_cross_asset_alignment_domain_labels


DOMAIN_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "label": "cross_asset_alignment_profile_domain",
        "name": "Cross-Asset Alignment Profile Domain",
        "description": "Profil yönetimi, non-signal araştırma parametreleri ve güvenlik sınırları.",
        "outputs": ["profile_registry", "profile_summary"],
    },
    {
        "label": "cross_asset_alignment_domain",
        "name": "Cross-Asset Alignment Core Domain",
        "description": "Cross-asset feature alignment ana çalışma alanı ve koordinasyon katmanı.",
        "outputs": ["alignment_status", "alignment_summary"],
    },
    {
        "label": "asset_universe_domain",
        "name": "Asset Universe Alignment Domain",
        "description": "FX, emtia, makro, takvim ve haber metadata evrenlerinin eşlenmesi.",
        "outputs": ["asset_universe_registry", "universe_summary"],
    },
    {
        "label": "symbol_mapping_domain",
        "name": "Symbol Mapping Domain",
        "description": "Varlık ve gösterge sembollerinin kanonik slug standardına dönüştürülmesi.",
        "outputs": ["symbol_mapping_registry", "normalized_symbols"],
    },
    {
        "label": "feature_namespace_domain",
        "name": "Feature Namespace Domain",
        "description": "Multi-domain feature kolonları için tekil, deterministik snake_case isimlendirme standardı.",
        "outputs": ["namespace_registry", "namespaced_feature_list"],
    },
    {
        "label": "timestamp_alignment_domain",
        "name": "Timestamp Alignment Contract Domain",
        "description": "UTC zaman damgaları üzerinde lookahead sızıntısız zaman hizalama sözleşmeleri.",
        "outputs": ["timestamp_alignment_contracts", "timestamp_validation_report"],
    },
    {
        "label": "session_calendar_alignment_domain",
        "name": "Session Calendar Alignment Domain",
        "description": "Farklı piyasa seansları (FX 24/5, emtia, makro veri yayını) için kova (bucket) hizalaması.",
        "outputs": ["session_calendar_registry", "session_buckets"],
    },
    {
        "label": "feature_matrix_contract_domain",
        "name": "Feature Matrix Contract Domain",
        "description": "Çoklu domain feature matrislerinin non-signal join ve birleşim sözleşmeleri.",
        "outputs": ["feature_matrix_contracts", "contract_summary"],
    },
    {
        "label": "join_policy_domain",
        "name": "Join Policy Domain",
        "description": "Farklı frekans ve zaman aralıklarındaki verilerin birleşim kuralları.",
        "outputs": ["join_policy_registry", "join_policy_definitions"],
    },
    {
        "label": "asof_join_policy_domain",
        "name": "Asof Join Policy Domain",
        "description": "Yalnızca geriye dönük (backward-only) asof join protokolleri ve tolerans kuralları.",
        "outputs": ["asof_join_policy_registry", "asof_join_specs"],
    },
    {
        "label": "no_lookahead_alignment_guard_domain",
        "name": "No-Lookahead Alignment Guard Domain",
        "description": "Geleceğe ait veri sızıntısını ve geleceğe kaydırma (shift(-1)) kullanımını kesin engelleyen guard.",
        "outputs": ["no_lookahead_guard_registry", "lookahead_audit_report"],
    },
    {
        "label": "cross_asset_metadata_domain",
        "name": "Cross-Asset Feature Metadata Domain",
        "description": "Hizalanmış tüm kolonların kaynak, domain, kanonik sembol ve politika metadataları.",
        "outputs": ["cross_asset_metadata_registry", "metadata_summary"],
    },
    {
        "label": "fx_commodity_alignment_domain",
        "name": "FX - Commodity Alignment Domain",
        "description": "FX kurları ile emtia sürekli sözleşmeleri ve spot kurları arasındaki bağlam hizalaması.",
        "outputs": ["fx_commodity_alignment_registry"],
    },
    {
        "label": "fx_macro_alignment_domain",
        "name": "FX - Macro Alignment Domain",
        "description": "FX kurları ile faiz, enflasyon ve makro göstergeler arasındaki bağlam hizalaması.",
        "outputs": ["fx_macro_alignment_registry"],
    },
    {
        "label": "fx_calendar_alignment_domain",
        "name": "FX - Calendar Alignment Domain",
        "description": "FX kurları ile ekonomik takvim olayları ve duyuruları arasındaki zaman penceresi hizalaması.",
        "outputs": ["fx_calendar_alignment_registry"],
    },
    {
        "label": "fx_news_alignment_domain",
        "name": "FX - News Metadata Alignment Domain",
        "description": "FX kurları ile haber konusu/etiketi (metadata-only) arasındaki konu ve zaman hizalaması.",
        "outputs": ["fx_news_metadata_alignment_registry"],
    },
    {
        "label": "commodity_macro_alignment_domain",
        "name": "Commodity - Macro Alignment Domain",
        "description": "Emtia fiyat serileri ile makroekonomik değişkenler (getiri, enflasyon, DXY) arasındaki bağlam.",
        "outputs": ["commodity_macro_alignment_registry"],
    },
    {
        "label": "commodity_calendar_alignment_domain",
        "name": "Commodity - Calendar Alignment Domain",
        "description": "Emtia varlıkları ile stok ve depolama raporlama takvimi arasındaki olay penceresi hizalaması.",
        "outputs": ["commodity_calendar_alignment_registry"],
    },
    {
        "label": "commodity_news_alignment_domain",
        "name": "Commodity - News Metadata Alignment Domain",
        "description": "Emtia varlıkları ile enerji, metal ve tarım haber metadata etiketleri arasındaki bağlam.",
        "outputs": ["commodity_news_metadata_alignment_registry"],
    },
    {
        "label": "macro_calendar_alignment_domain",
        "name": "Macro - Calendar Alignment Domain",
        "description": "Makro zaman serisi ile ekonomik takvim duyuru anı ve revizyonları arasındaki senkronizasyon.",
        "outputs": ["macro_calendar_alignment_registry"],
    },
    {
        "label": "calendar_news_alignment_domain",
        "name": "Calendar - News Metadata Alignment Domain",
        "description": "Ekonomik takvim olayları ile haber konu başlıkları arasındaki metadata bağlantısı.",
        "outputs": ["calendar_news_metadata_alignment_registry"],
    },
    {
        "label": "cross_domain_feature_matrix_domain",
        "name": "Cross-Domain Feature Matrix Domain",
        "description": "Farklı domainlerin bir araya getirildiği non-signal araştırma matrisi şablonu.",
        "outputs": ["cross_domain_feature_matrix_placeholder", "matrix_summary"],
    },
    {
        "label": "aligned_feature_matrix_manifest_domain",
        "name": "Aligned Feature Matrix Manifest Domain",
        "description": "Hizalanmış matrislerin kaynak koruma, satır/sütun sayısı ve non-signal manifest kaydı.",
        "outputs": ["aligned_feature_matrix_manifest"],
    },
    {
        "label": "alignment_validation_domain",
        "name": "Alignment Validation Domain",
        "description": "Yasaklı kelime, sütun, geleceğe ait veri ve sözleşme uyum denetimleri.",
        "outputs": ["validation_rule_registry", "validation_report"],
    },
    {
        "label": "alignment_quality_handoff_domain",
        "name": "Alignment Quality Handoff Domain",
        "description": "Manuel inceleme kuyruğu, eksik veri ve drift izleme devir raporu.",
        "outputs": ["quality_handoff_report"],
    },
    {
        "label": "cross_asset_health_domain",
        "name": "Cross-Asset Health Domain",
        "description": "Öncül faz bağımlılıkları ve modül import edilebilirlik sağlık kontrolü.",
        "outputs": ["health_check_report"],
    },
    {
        "label": "cross_asset_safety_domain",
        "name": "Cross-Asset Safety Domain",
        "description": "Kesin No-Go ve Safe-Go güvenlik sınırları yönetimi.",
        "outputs": ["safety_boundary_report"],
    },
    {
        "label": "phase_120_handoff_domain",
        "name": "Phase 120 Fusion Handoff Domain",
        "description": "Phase 120 Macro/Calendar/News Feature Fusion fazına aktarılan sözleşme ve veriler.",
        "outputs": ["phase_120_handoff_report"],
    },
]


def build_cross_asset_alignment_domain_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    rows = []
    for d in DOMAIN_DEFINITIONS:
        item = CrossAssetAlignmentDomain(
            domain_id=build_cross_asset_alignment_domain_id(d["label"]),
            domain_label=d["label"],
            domain_name=d["name"],
            description=d["description"],
            required_outputs=d["outputs"],
            warnings=[],
        )
        rows.append(item.to_dict())

    df = pd.DataFrame(rows)
    df["non_signal"] = True
    summary = {
        "profile": active_profile.name,
        "total_domains": len(df),
        "non_signal": True,
        "status": "READY",
    }
    return df, summary
