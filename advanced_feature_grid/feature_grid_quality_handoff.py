from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


QUALITY_HANDOFF_ITEMS = [
    {
        "category": "row_count_sufficiency",
        "item_name": "insufficient_rows_for_large_windows",
        "description": "200+ gibi büyük pencereler için en az 250+ satır geçmiş veri zorunluluğu uyarısı.",
        "status": "MONITORED",
        "target_phase": 119,
    },
    {
        "category": "warmup_policy",
        "item_name": "warmup_nan_policy",
        "description": "Başlangıç NaN değerlerinin otomatik silinmeyip Phase 121'e kadar korunması politikası.",
        "status": "ENFORCED",
        "target_phase": 121,
    },
    {
        "category": "duplicate_check",
        "item_name": "duplicate_feature_names",
        "description": "Mükerrer feature isimlerinin tespit edilip Phase 121/124 çözümüne bayraklanması.",
        "status": "FLAGGED",
        "target_phase": 121,
    },
    {
        "category": "performance",
        "item_name": "high_feature_count_warning",
        "description": "Çoklu window matrisinin bellek ve işlem maliyetini sınırlamak için kademeli provizyon.",
        "status": "OPTIMIZED",
        "target_phase": 124,
    },
    {
        "category": "input_integrity",
        "item_name": "missing_input_fields_guard",
        "description": "OHLCV ve quote girdi alanlarının eksikliği durumunda erken validasyon hatası üretimi.",
        "status": "ENFORCED",
        "target_phase": 119,
    },
    {
        "category": "input_integrity",
        "item_name": "non_numeric_input_guard",
        "description": "Sayısal olmayan girdilerin reddedilmesi ve float64 tip dönüşümünün güvenceye alınması.",
        "status": "ENFORCED",
        "target_phase": 119,
    },
    {
        "category": "lookahead_guard",
        "item_name": "no_lookahead_dependency",
        "description": "Geleceğe bakan hiçbir getiri veya negatif shift içermeyen geriye dönük hesaplama garantisi.",
        "status": "VERIFIED",
        "target_phase": 121,
    },
    {
        "category": "alignment_readiness",
        "item_name": "phase_119_cross_asset_alignment_readiness",
        "description": "Varlıklar arası zaman ve sembol hizalaması için feature grid şemalarının hazır olması.",
        "status": "READY",
        "target_phase": 119,
    },
    {
        "category": "validation_dependency",
        "item_name": "phase_121_validation_dependency",
        "description": "Feature doğrulama ve drift tespit katmanı için gerekli sözleşmelerin aktarılması.",
        "status": "READY",
        "target_phase": 121,
    },
    {
        "category": "storage_dependency",
        "item_name": "phase_124_feature_store_integration_dependency",
        "description": "Offline FeatureStore entegrasyonu ve partition tasarımı için hazır bulunuşluk.",
        "status": "READY",
        "target_phase": 124,
    },
]


def build_feature_grid_quality_handoff_report(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(QUALITY_HANDOFF_ITEMS)
    summary = summarize_feature_grid_quality_handoff(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_quality_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_handoff_items": 0, "status": "EMPTY"}

    return {
        "total_handoff_items": len(df),
        "phase_119_items": int((df["target_phase"] == 119).sum()) if "target_phase" in df.columns else 0,
        "phase_121_items": int((df["target_phase"] == 121).sum()) if "target_phase" in df.columns else 0,
        "phase_124_items": int((df["target_phase"] == 124).sum()) if "target_phase" in df.columns else 0,
        "non_signal": True,
        "status": "READY",
    }
