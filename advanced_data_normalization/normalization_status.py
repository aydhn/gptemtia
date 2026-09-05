from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_labels import NORMALIZATION_STATUSES

STATUS_DESCRIPTIONS: Dict[str, str] = {
    "normalization_applied": "Kanonikleştirme veya dönüşüm kuralı başarıyla uygulandı.",
    "normalization_not_applicable": "Kayıt veya alan bu normalizasyon kuralı kapsamına girmiyor.",
    "normalization_manual_review_required": "Değer belirsiz veya harici sözlükte yok; manuel inceleme gerekli.",
    "normalization_blocked_by_safety": "Güvenlik veya non-destructive sınırları nedeniyle işlem engellendi.",
    "normalization_placeholder_only": "Alan henüz aktif kurala sahip değil; yer tutucu uygulandı.",
    "normalization_failed": "Normalizasyon kuralı işletilirken hata oluştu.",
    "normalization_unknown": "Durum tespit edilemedi.",
}


def build_normalization_status_registry(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for s in NORMALIZATION_STATUSES:
        records.append({
            "status_label": s,
            "description": STATUS_DESCRIPTIONS.get(s, ""),
            "non_destructive": True,
            "audit_required": s in ["normalization_manual_review_required", "normalization_blocked_by_safety"],
            "current_phase": 113,
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_normalization_status(df)
    return df, summary


def summarize_normalization_status(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_statuses": len(df),
        "statuses": df["status_label"].tolist() if "status_label" in df.columns else [],
        "current_phase": 113,
        "target_final_phase": 160,
    }
