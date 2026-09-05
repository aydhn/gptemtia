"""Phase 125: Feature Engine Block Manual Review Queue.

Maintains non-destructive human review items across the 10-phase feature engine block.
Strictly forbids automatic destructive actions, automated imputations, or signal generations.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureEngineManualReviewItem,
)

SAMPLE_REVIEW_ITEMS = [
    FeatureEngineManualReviewItem(
        review_id="rev_01_news_boundary",
        phase_number=120,
        module_name="advanced_feature_fusion",
        review_reason="Haber metaveri sınırlarının (no-full-text) periyodik denetimi.",
        severity="LOW",
        suggested_action="Haber şemalarında metin gövdesi veya scraping çıktısı olmadığını doğrula; ham dosyaları koru.",
        status="RESOLVED_SAFE",
    ),
    FeatureEngineManualReviewItem(
        review_id="rev_02_lookahead_asof",
        phase_number=121,
        module_name="advanced_feature_validation",
        review_reason="Backward asof join ve strictly increasing zaman damgası kuralları.",
        severity="MEDIUM",
        suggested_action="Zaman serisi hizalamalarında geleceğe sızıntı olmadığını doğrula; otomatik kolon silme yapma.",
        status="RESOLVED_SAFE",
    ),
    FeatureEngineManualReviewItem(
        review_id="rev_03_quality_drift_blockers",
        phase_number=123,
        module_name="advanced_feature_quality_drift",
        review_reason="Tanısal anomaliler ve PSI/KS drift eşik aşımları incelemesi.",
        severity="MEDIUM",
        suggested_action="Kalite kusurlarını raporla, otomatik doldurma (imputation) veya otomatik feature silme yapma.",
        status="RESOLVED_SAFE",
    ),
    FeatureEngineManualReviewItem(
        review_id="rev_04_feature_store_immutability",
        phase_number=124,
        module_name="advanced_feature_store_integration",
        review_reason="Feature store kaynak koruma ve bölümleme (partition) immutability kontrolü.",
        severity="LOW",
        suggested_action="Ham veri gölü çıktılarının üzerine yazılmadığını teyit et.",
        status="RESOLVED_SAFE",
    ),
    FeatureEngineManualReviewItem(
        review_id="rev_05_phase_126_handoff_readiness",
        phase_number=125,
        module_name="phase_126_handoff",
        review_reason="Phase 126 rejim sınıflandırma girdi önkoşullarının gözden geçirilmesi.",
        severity="INFO",
        suggested_action="Phase 126 rejim modellerinin sinyal/alım-satım tavsiyesi olmadığını baştan teyit et.",
        status="PENDING_HANDOFF",
    ),
]


def build_feature_engine_block_manual_review_queue(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the manual review queue DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    rows = [item.__dict__ for item in SAMPLE_REVIEW_ITEMS]
    df = pd.DataFrame(rows)

    pending_count = len(df[df["status"] != "RESOLVED_SAFE"])
    summary = {
        "profile_name": active_profile.profile_name,
        "total_items": len(df),
        "pending_items": pending_count,
        "resolved_safe_items": len(df[df["status"] == "RESOLVED_SAFE"]),
        "destructive_actions_prevented": True,
        "auto_imputation_prevented": True,
        "auto_drop_prevented": True,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_engine_block_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue DataFrame."""
    return {
        "total_reviews": len(df),
        "open_issues": len(df[df["status"] == "PENDING_HANDOFF"]) if "status" in df.columns else 0,
        "destructive_allowed": False,
        "non_signal": True,
    }
