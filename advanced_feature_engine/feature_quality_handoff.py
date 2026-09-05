from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile

QUALITY_HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "handoff_area": "Missing Feature Value Handling",
        "source_phase": "Phase 112 Data Quality",
        "target_phase": "Phase 117 Technical Indicator Expansion",
        "description": "Isınma periyodundaki eksik değerler maskelenir; veri uydurma veya sentetik dolgu yapılmaz.",
        "enforcement_status": "ACTIVE",
    },
    {
        "handoff_area": "Stale Input Feature Masking",
        "source_phase": "Phase 112 Data Quality",
        "target_phase": "Phase 116/117 Feature Engine",
        "description": "Bayat veri bayrağı taşıyan seriler feature hesaplamasında filtrelenir veya uyarılır.",
        "enforcement_status": "ACTIVE",
    },
    {
        "handoff_area": "Duplicate Key Feature Isolation",
        "source_phase": "Phase 113 Normalization",
        "target_phase": "Phase 116 Feature Engine",
        "description": "Kanonik tekil anahtarlar kullanılarak mükerrer kayıtların zaman serisi hesabını bozması engellenir.",
        "enforcement_status": "ACTIVE",
    },
    {
        "handoff_area": "Normalization Layer Dependency",
        "source_phase": "Phase 113 Normalization",
        "target_phase": "Phase 116 Feature Engine",
        "description": "Semboller, saat dilimleri (UTC) ve birimler normalize edilmiş girdi kontratlarına dayanır.",
        "enforcement_status": "ACTIVE",
    },
    {
        "handoff_area": "Lineage Audit Dependency",
        "source_phase": "Phase 114 Lineage",
        "target_phase": "Phase 116 Feature Engine",
        "description": "Ham veriden türetilen her feature kolonunun girdi kaynağı ve dönüşüm adımı izlenebilir.",
        "enforcement_status": "ACTIVE",
    },
    {
        "handoff_area": "Rolling Warmup NaN Policy",
        "source_phase": "Phase 116 Feature Engine",
        "target_phase": "Phase 117/118 Feature Packs",
        "description": "Window - 1 kadar ilk satır için NaN korunur; erken sinyal veya sahte dolgu üretilmez.",
        "enforcement_status": "ACTIVE",
    },
    {
        "handoff_area": "Feature Outlier Clipping Placeholder",
        "source_phase": "Phase 116 Feature Engine",
        "target_phase": "Phase 118 Volatility Feature Pack",
        "description": "Aşırı aykırı değerlerin z-score ve IQR bazlı kırpılması placeholder'ı.",
        "enforcement_status": "PLANNED",
    },
    {
        "handoff_area": "Feature Drift Diagnostics Placeholder",
        "source_phase": "Phase 116 Feature Engine",
        "target_phase": "Phase 123 Feature Drift Diagnostics",
        "description": "Zaman içindeki feature dağılım kaymalarını izleme placeholder'ı.",
        "enforcement_status": "PLANNED",
    },
]


def build_feature_quality_handoff_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(QUALITY_HANDOFF_ITEMS)
    summary = summarize_feature_quality_handoff(df)
    return df, summary


def summarize_feature_quality_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_handoff_areas": len(df),
        "active_enforcements": int((df["enforcement_status"] == "ACTIVE").sum()) if not df.empty and "enforcement_status" in df.columns else 0,
        "planned_enforcements": int((df["enforcement_status"] == "PLANNED").sum()) if not df.empty and "enforcement_status" in df.columns else 0,
        "all_handoff_defined": len(df) >= 8,
        "non_signal": True,
    }
