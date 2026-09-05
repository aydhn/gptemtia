"""Phase 125: Feature Factor Acceptance Domain Registry.

Defines the domains covered by the Phase 116-125 feature engine block
and the Phase 126 regime classification handoff.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

DOMAINS = [
    {
        "domain_id": "dom_phase_116_feature_engine",
        "phase": 116,
        "domain_name": "Feature Engine Foundation",
        "package": "advanced_feature_engine",
        "description": "Temel hesaplama arayüzleri, bağımlılık grafiği, şema kayıtları ve temel özellikler.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_117_technical_indicators",
        "phase": 117,
        "domain_name": "Technical Indicator Expansion",
        "package": "advanced_technical_indicators",
        "description": "Gelişmiş trend, osilatör, volatilite, hacim ve fiyat hareketi indikatör katalogları.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_118_feature_grid",
        "phase": 118,
        "domain_name": "Multi-Window Feature Grid",
        "package": "advanced_feature_grid",
        "description": "Çoklu pencere grid yapılandırmaları, varyans ve getiri hesaplama çerçevesi.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_119_cross_asset",
        "phase": 119,
        "domain_name": "Cross-Asset Feature Alignment",
        "package": "advanced_cross_asset_alignment",
        "description": "Çapraz varlık zaman hizalama, asof join politikaları ve matris sözleşmeleri.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_120_feature_fusion",
        "phase": 120,
        "domain_name": "Macro/Calendar/News Feature Fusion",
        "package": "advanced_feature_fusion",
        "description": "Makro ekonomik bültenler, takvim olay pencereleri ve metadata-only haber füzyonu.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_121_feature_validation",
        "phase": 121,
        "domain_name": "Feature Validation and No-Lookahead Guard",
        "package": "advanced_feature_validation",
        "description": "Geleceğe sızıntı (lookahead) denetimleri, yasaklı kolon politikaları ve ısınma kuralları.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_122_factor_metadata",
        "phase": 122,
        "domain_name": "Factor Metadata and Factor Families",
        "package": "advanced_factor_metadata",
        "description": "12 faktör ailesi, faktör sözleşmeleri ve faktör soybağı kayıtları.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_123_quality_drift",
        "phase": 123,
        "domain_name": "Feature Quality and Drift Diagnostics",
        "package": "advanced_feature_quality_drift",
        "description": "Eksik veri, sonsuz değer, dağılım kayması (PSI/KS) ve yuvarlanan kararlılık tanıları.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_124_feature_store",
        "phase": 124,
        "domain_name": "Feature Store Integration Expansion",
        "package": "advanced_feature_store_integration",
        "description": "Doğrulama duyarlı merkezi özellik deposu, kalite/drift metaveri depolama ve kataloglar.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_125_acceptance",
        "phase": 125,
        "domain_name": "Feature/Factor Engine Acceptance Report",
        "package": "advanced_feature_factor_acceptance",
        "description": "Uçtan uca blok kabul raporu, güvenlik geçitleri ve nihai blok manifestosu.",
        "status": "ACCEPTED",
        "non_signal": True,
    },
    {
        "domain_id": "dom_phase_126_regime_handoff",
        "phase": 126,
        "domain_name": "Phase 126 Regime Classification Handoff",
        "package": "phase_126_handoff",
        "description": "Rejim sınıflandırması ve piyasa davranış modelleri için girdi devir şartnamesi.",
        "status": "READY",
        "non_signal": True,
    },
]


def build_feature_factor_acceptance_domain_registry(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build acceptance domain registry DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    df = pd.DataFrame(DOMAINS)
    summary = {
        "profile_name": active_profile.profile_name,
        "total_domains": len(df),
        "block_domains": len(df[df["phase"] <= 125]),
        "handoff_domains": len(df[df["phase"] == 126]),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_factor_acceptance_domain_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domain registry DataFrame."""
    return {
        "total_domains": len(df),
        "phases_covered": df["phase"].tolist() if "phase" in df.columns else [],
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
