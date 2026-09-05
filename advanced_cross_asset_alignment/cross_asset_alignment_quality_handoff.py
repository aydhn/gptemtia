from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


QUALITY_HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "handoff_topic": "symbol_mapping_manual_review",
        "description": "Farklı sağlayıcılardan gelen yeni sembollerin ve ticker kodlarının manuel inceleme prosedürü.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "asset_symbol_mapping",
    },
    {
        "handoff_topic": "timestamp_alignment_manual_review",
        "description": "Ayrıştırılamayan veya zaman dilimi bilgisi eksik olan seriler için inceleme süreci.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "timestamp_alignment_contracts",
    },
    {
        "handoff_topic": "session_mismatch_policy",
        "description": "24/5 FX seansı ile emtia işlem pencereleri arasındaki seans uyuşmazlığı politikası.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "session_calendar_alignment",
    },
    {
        "handoff_topic": "future_leakage_risk_mitigation",
        "description": "Backward-only asof join ve negatif shift yasaklarının operasyonel denetimi.",
        "target_phase": 121,
        "status": "READY",
        "dependency": "no_lookahead_alignment_guard",
    },
    {
        "handoff_topic": "duplicate_feature_namespace_resolution",
        "description": "Cross-domain birleşiminde aynı ada sahip feature çakışmalarının engellenmesi.",
        "target_phase": 119,
        "status": "READY",
        "dependency": "cross_domain_feature_namespace",
    },
    {
        "handoff_topic": "macro_release_lag_policy",
        "description": "Makro duyurularının gerçekleşme zamanı ve veri revizyon politikası aktarımı.",
        "target_phase": 120,
        "status": "READY",
        "dependency": "macro_calendar_alignment",
    },
    {
        "handoff_topic": "event_window_policy",
        "description": "Ekonomik takvim olay öncesi ve sonrası pencere etiketleme kuralı.",
        "target_phase": 120,
        "status": "READY",
        "dependency": "fx_calendar_alignment",
    },
    {
        "handoff_topic": "news_metadata_only_boundary",
        "description": "Haber tarafında yalnızca etiket/sayı kullanılması ve sıfır tam metin kuralının devri.",
        "target_phase": 120,
        "status": "READY",
        "dependency": "news_metadata_alignment",
    },
    {
        "handoff_topic": "phase_120_fusion_dependency",
        "description": "Phase 120 Macro/Calendar/News Feature Fusion için ortak veri matrisi devir arayüzü.",
        "target_phase": 120,
        "status": "READY",
        "dependency": "cross_domain_feature_matrix",
    },
    {
        "handoff_topic": "phase_121_no_lookahead_dependency",
        "description": "Phase 121 Sıkı No-Lookahead ve Feature Validasyon denetimine girdi sözleşmesi.",
        "target_phase": 121,
        "status": "FORWARD_CONTRACT",
        "dependency": "no_lookahead_alignment_guard",
    },
    {
        "handoff_topic": "phase_124_feature_store_integration_dependency",
        "description": "Hizalanmış matrislerin FeatureStore kayıt şemasına uyumlu aktarım sözleşmesi.",
        "target_phase": 124,
        "status": "FORWARD_CONTRACT",
        "dependency": "aligned_feature_matrix_manifest",
    },
]


def build_cross_asset_alignment_quality_handoff_report(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(QUALITY_HANDOFF_ITEMS)
    summary = summarize_cross_asset_alignment_quality_handoff(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_cross_asset_alignment_quality_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_handoff_items": 0, "status": "EMPTY"}

    ready_count = int((df["status"] == "READY").sum()) if "status" in df.columns else 0
    forward_count = int((df["status"] == "FORWARD_CONTRACT").sum()) if "status" in df.columns else 0

    return {
        "total_handoff_items": len(df),
        "ready_items_count": ready_count,
        "forward_contract_count": forward_count,
        "target_phases": list(df["target_phase"].unique()) if "target_phase" in df.columns else [],
        "non_signal": True,
        "status": "READY",
    }
