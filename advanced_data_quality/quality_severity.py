from typing import Tuple, Dict, Any
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile

SEVERITY_DEFINITIONS = [
    {
        "severity_label": "quality_critical",
        "severity_level": 5,
        "name": "Critical",
        "description": "Güvenlik, telif hakkı, credential sızıntısı, destructive action teşebbüsü veya kritik şema kırılması.",
        "score_penalty": 0.40,
        "requires_immediate_action": True,
        "blocks_pipeline": True,
    },
    {
        "severity_label": "quality_high",
        "severity_level": 4,
        "name": "High",
        "description": "Eksik birincil kritik alan, timestamp bozulması, ters spread, bid>ask veya provider metadata sorunu.",
        "score_penalty": 0.20,
        "requires_immediate_action": True,
        "blocks_pipeline": False,
    },
    {
        "severity_label": "quality_medium",
        "severity_level": 3,
        "name": "Medium",
        "description": "Stale veri, mükerrer kayıt, frekans/birim uyumsuzluğu veya outlier placeholder uyarısı.",
        "score_penalty": 0.10,
        "requires_immediate_action": False,
        "blocks_pipeline": False,
    },
    {
        "severity_label": "quality_low",
        "severity_level": 2,
        "name": "Low",
        "description": "Opsiyonel metadata eksikliği, eksik hacim/open interest veya ikincil alan uyarıları.",
        "score_penalty": 0.03,
        "requires_immediate_action": False,
        "blocks_pipeline": False,
    },
    {
        "severity_label": "quality_info",
        "severity_level": 1,
        "name": "Info",
        "description": "Bilgilendirme notu, kanonik format tavsiyesi veya manuel inceleme notu.",
        "score_penalty": 0.00,
        "requires_immediate_action": False,
        "blocks_pipeline": False,
    },
]


def build_quality_severity_registry(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    df = pd.DataFrame.from_records(SEVERITY_DEFINITIONS)
    summary = summarize_quality_severity(df)
    return df, summary


def summarize_quality_severity(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_severities": len(df),
        "severity_labels": df["severity_label"].tolist() if "severity_label" in df.columns else [],
        "max_penalty": float(df["score_penalty"].max()) if "score_penalty" in df.columns and len(df) > 0 else 0.0,
        "current_phase": 112,
        "target_final_phase": 160,
    }
