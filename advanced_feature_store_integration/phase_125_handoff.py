"""Phase 125 Feature/Factor Engine Acceptance Handoff Specification."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

HANDOFF_ITEMS = [
    {
        "item_id": "item_feature_engine_acceptance_prereq",
        "title": "Feature Engine Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 116 temel feature şemalarının feature store entegrasyonu tamamlandı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_technical_indicators_prereq",
        "title": "Indicator Catalog Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 117 teknik indikatörlerinin sözleşmeleri ve kayıtları hazır.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_feature_grid_prereq",
        "title": "Multi-Window Grid Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 118 çoklu pencere grid çıktıları feature store şemasına bağlandı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_cross_asset_prereq",
        "title": "Cross-Asset Alignment Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 119 çapraz varlık asof join sözleşmeleri ve bağlamları entegre edildi.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_macro_calendar_news_prereq",
        "title": "Macro/Calendar/News Fusion Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 120 füzyon metaverileri no-full-text ilkesiyle kaydedildi.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_validation_no_lookahead_prereq",
        "title": "Validation/No-Lookahead Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 121 no-lookahead ve sızıntı denetimi doğrulama durumu kataloğuna aktarıldı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_factor_metadata_prereq",
        "title": "Factor Metadata Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 122 faktör aileleri ve bağımlılıkları faktör kataloğunda arşivlendi.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_quality_drift_prereq",
        "title": "Quality/Drift Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 123 kalite ve drift tanı skorları feature store skor kayıtlarına bağlandı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_feature_store_integration_prereq",
        "title": "Feature Store Integration Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 124 sözleşmeler, entity, şema, namespace ve manifest katmanları hazır.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_documentation_acceptance_prereq",
        "title": "Documentation Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "README, ARCHITECTURE, ROADMAP ve SAFE_USAGE kılavuzları güncellendi.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_safety_boundary_acceptance_prereq",
        "title": "Safety Boundary Acceptance Prerequisites",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Kesin al-sat, broker, model training ve kaynak silme yasakları uygulandı.",
        "non_signal": True,
        "source_preserved": True,
    },
    {
        "item_id": "item_manual_review_blockers_tracking",
        "title": "Manual Review Blockers Tracking",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "status": "READY",
        "description": "Phase 125 acceptance raporu öncesi çözülmemiş tüm engeller izleniyor.",
        "non_signal": True,
        "source_preserved": True,
    },
]


def build_phase_125_feature_factor_engine_acceptance_handoff_report(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 125 acceptance handoff report DataFrame and summary."""
    records = list(HANDOFF_ITEMS)
    df = pd.DataFrame(records)
    summary = {
        "handoff_status": "READY",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "total_items": len(records),
        "ready_items": len([r for r in records if r["status"] == "READY"]),
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_phase_125_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 125 handoff DataFrame."""
    if df.empty:
        return {
            "total_items": 0,
            "ready_items": 0,
            "handoff_status": "BLOCKED",
            "source_phase": 124,
            "next_phase": 125,
            "target_final_phase": 160,
        }
    ready_count = int((df.get("status", pd.Series()) == "READY").sum())
    return {
        "total_items": len(df),
        "ready_items": ready_count,
        "handoff_status": "READY" if ready_count == len(df) else "PARTIAL",
        "source_phase": 124,
        "next_phase": 125,
        "target_final_phase": 160,
        "non_signal": bool(all(df.get("non_signal", [True]))),
        "source_preserved": bool(all(df.get("source_preserved", [True]))),
    }
