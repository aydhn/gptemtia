"""Phase 125: Phase 126 Regime Classification Handoff Report.

Outlines all feature/factor prerequisites, taxonomy inputs, and non-signal boundaries
required for Phase 126 (Regime Classification and Market Behavior Foundation).
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

HANDOFF_ITEMS = [
    {
        "item_id": "handoff_01_regime_prereq",
        "title": "Regime Classification Prerequisites",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Phase 116-125 feature bloğu kabul edilmiş ve doğrulanmış durumdadır.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_02_market_behavior_taxonomy",
        "title": "Market Behavior Taxonomy Prerequisites",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Trend, volatilite, likidite ve makro rejim aday göstergeleri Phase 122 ve 124'ten aktarılacaktır.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_03_validated_feature_families",
        "title": "Validated Feature Families",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "No-lookahead garantili teknik, grid, çapraz varlık ve füzyon feature setleri hazırdır.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_04_factor_family_inputs",
        "title": "Factor Family Inputs for Regimes",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Momentum, volatilite, mean reversion, getiri ve makro bağlam faktörleri rejim girdisi olarak sunulur.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_05_quality_drift_dependencies",
        "title": "Quality and Drift Metadata Dependencies",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Kararlılık ve drift skorları rejim modellerinde feature güvenilirliği referansı olarak kullanılır.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_06_feature_store_dependencies",
        "title": "Feature Store Metadata Dependencies",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Merkezi depodan point-in-time okuma sözleşmeleri ile rejim girdileri çekilecektir.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_07_no_lookahead_regime_constraint",
        "title": "No-Lookahead Constraints for Regime Labels",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Rejim etiketleri geçmişe dönük hesaplanırken asof t anındaki veriyi aşamaz.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_08_regime_label_non_signal_warning",
        "title": "Regime Label Non-Signal Boundary",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Rejim etiketi (bull, bear, high-vol, low-vol vb.) AL/SAT sinyali veya trade emri değildir.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_09_macro_context_for_regimes",
        "title": "Macro/Calendar Context for Regimes",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Faiz farkı, enflasyon eğilimi ve takvim olay pencereleri rejim bağlamı olarak aktarılır.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_10_cross_asset_context_for_regimes",
        "title": "Cross-Asset Context for Regimes",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "DXY, US10Y, SPX ve Brent-WTI çapraz varlık bağlamları rejim girdisi olarak sunulur.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_11_acceptance_blockers",
        "title": "Phase 126 Acceptance Blockers",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Açık kabul engelleyicisi kalmamıştır; 16 kabul kapısı PASSED durumundadır.",
        "non_signal": True,
    },
    {
        "item_id": "handoff_12_implementation_boundaries",
        "title": "Phase 126 Implementation Boundaries",
        "source_phase": 125,
        "next_phase": 126,
        "status": "READY",
        "description": "Phase 126 da yerel, çevrimdışı ve non-signal olarak geliştirilecek; broker/live trading yapılmayacaktır.",
        "non_signal": True,
    },
]


def build_phase_126_regime_classification_handoff_report(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 126 regime classification handoff DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    df = pd.DataFrame(HANDOFF_ITEMS)

    summary = {
        "profile_name": active_profile.profile_name,
        "source_phase": 125,
        "next_phase": 126,
        "target_final_phase": 160,
        "total_handoff_items": len(df),
        "ready_items": len(df[df["status"] == "READY"]),
        "handoff_status": "READY",
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_phase_126_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 126 handoff DataFrame."""
    return {
        "handoff_items_count": len(df),
        "all_ready": bool((df["status"] == "READY").all()) if "status" in df.columns else False,
        "non_signal": True,
    }
