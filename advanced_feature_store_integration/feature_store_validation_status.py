"""Phase 124 Feature Store Validation Status Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

VALIDATION_STATUS_ENTRIES = [
    {
        "status_id": "VAL_STAT_001",
        "entity_id": "eurusd",
        "feature_name": "sma_20",
        "status_label": "validation_pass",
        "severity": "info",
        "issues_detected": 0,
        "description": "Tüm no-lookahead ve veri tipi validasyonlarından başarıyla geçti.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "status_id": "VAL_STAT_002",
        "entity_id": "brent",
        "feature_name": "atr_14",
        "status_label": "validation_pass",
        "severity": "info",
        "issues_detected": 0,
        "description": "Zaman damgası sıralaması ve aykırı değer kontrolleri tam uyumlu.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "status_id": "VAL_STAT_003",
        "entity_id": "cross_asset",
        "feature_name": "brent_eurusd_corr_30",
        "status_label": "validation_pass_with_warnings",
        "severity": "warning",
        "issues_detected": 1,
        "description": "Asof join backward tolerans sınırında uyarı; no-lookahead korundu.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "status_id": "VAL_STAT_004",
        "entity_id": "macro_news",
        "feature_name": "energy_event_attention_score",
        "status_label": "validation_manual_review_required",
        "severity": "high",
        "issues_detected": 1,
        "description": "Haber metaveri etiket dağılımı insan incelemesi gerektiriyor; silme yapılmadı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "status_id": "VAL_STAT_005",
        "entity_id": "placeholder_series",
        "feature_name": "future_window_test_placeholder",
        "status_label": "validation_placeholder_only",
        "severity": "info",
        "issues_detected": 0,
        "description": "Simülasyon amaçlı yer tutucu kaydı; üretimde kullanılmaz.",
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_feature_store_validation_status_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of validation status records."""
    records = list(VALIDATION_STATUS_ENTRIES)
    df = pd.DataFrame(records)
    summary = {
        "total_validation_statuses": len(records),
        "pass_count": len([r for r in records if r["status_label"] == "validation_pass"]),
        "warning_count": len([r for r in records if r["status_label"] == "validation_pass_with_warnings"]),
        "review_required_count": len([r for r in records if r["status_label"] == "validation_manual_review_required"]),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_validation_status(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize validation status registry."""
    if df.empty:
        return {"total_statuses": 0, "non_signal": True, "source_preserved": True}
    return {
        "total_statuses": len(df),
        "pass_count": int((df.get("status_label", pd.Series()) == "validation_pass").sum()),
        "warning_count": int((df.get("status_label", pd.Series()) == "validation_pass_with_warnings").sum()),
        "review_required_count": int((df.get("status_label", pd.Series()) == "validation_manual_review_required").sum()),
        "all_non_signal": bool(all(df.get("non_signal", [True]))),
        "all_source_preserved": bool(all(df.get("source_preserved", [True]))),
    }
