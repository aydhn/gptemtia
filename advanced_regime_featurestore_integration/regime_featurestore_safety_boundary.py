"""Phase 134: Regime FeatureStore Safety Boundary.

Enforces absolute NO-GO prohibitions (live trading, signals, model training, scraping)
and declares verified SAFE-GO research boundaries.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_STORE_READY,
    SAFETY_DOMAIN,
)

CANONICAL_NO_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "no_go_live_trading", "rule": "Canlı emir gönderme", "category": "execution", "status": "ENFORCED"},
    {"rule_id": "no_go_broker_api", "rule": "Broker API bağlama", "category": "execution", "status": "ENFORCED"},
    {"rule_id": "no_go_real_order", "rule": "Gerçek pozisyon açma", "category": "execution", "status": "ENFORCED"},
    {"rule_id": "no_go_signals", "rule": "AL/SAT, long/short sinyali üretme", "category": "signals", "status": "ENFORCED"},
    {"rule_id": "no_go_store_as_signal", "rule": "FeatureStore kaydını trade sinyali olarak sunma", "category": "signals", "status": "ENFORCED"},
    {"rule_id": "no_go_readiness_as_live", "rule": "Regime store ready durumunu canlı işlem hazır olarak iddia etme", "category": "claims", "status": "ENFORCED"},
    {"rule_id": "no_go_validation_as_production", "rule": "Validation accepted durumunu production-ready olarak iddia etme", "category": "claims", "status": "ENFORCED"},
    {"rule_id": "no_go_directional_claim", "rule": "Rejim durumlarını işlem yönü olarak yorumlama", "category": "interpretation", "status": "ENFORCED"},
    {"rule_id": "no_go_model_training", "rule": "Gerçek model eğitimi veya fitting çalıştırma", "category": "ml", "status": "ENFORCED"},
    {"rule_id": "no_go_clustering", "rule": "Gerçek clustering execution veya unsupervised segmentation çalıştırma", "category": "ml", "status": "ENFORCED"},
    {"rule_id": "no_go_prediction", "rule": "Supervised/unsupervised model prediction üretme", "category": "ml", "status": "ENFORCED"},
    {"rule_id": "no_go_target_label", "rule": "Hedef/etiket/tahmin üretimi", "category": "ml", "status": "ENFORCED"},
    {"rule_id": "no_go_sentiment", "rule": "Sentiment model output, embedding veya vector üretme", "category": "nlp", "status": "ENFORCED"},
    {"rule_id": "no_go_raw_news", "rule": "Haber tam metni, article_body, raw_content, scraped_html kullanma", "category": "news", "status": "ENFORCED"},
    {"rule_id": "no_go_lookahead", "rule": "Future return, forward return, next return veya shift(-1) kullanma", "category": "integrity", "status": "ENFORCED"},
    {"rule_id": "no_go_future_timestamp", "rule": "Gelecek timestamp'i geçmiş rejim kaydına bağlama", "category": "integrity", "status": "ENFORCED"},
    {"rule_id": "no_go_scraping", "rule": "Gerçek provider API çağrısı, scraping, browser automation yapma", "category": "network", "status": "ENFORCED"},
    {"rule_id": "no_go_credentials", "rule": "Provider credential, API key, token veya secret yazdırma", "category": "security", "status": "ENFORCED"},
    {"rule_id": "no_go_source_overwrite", "rule": "Kaynak veriyi silme, üzerine yazma veya taşıma", "category": "preservation", "status": "ENFORCED"},
    {"rule_id": "no_go_destructive_clean", "rule": "Tahribatlı temizlik, auto-imputation veya auto-feature-drop yapma", "category": "preservation", "status": "ENFORCED"},
    {"rule_id": "no_go_deployment", "rule": "Model deployment, production deployment, docker push, git tag yapma", "category": "deployment", "status": "ENFORCED"},
]

CANONICAL_SAFE_GO_CONDITIONS: List[Dict[str, Any]] = [
    {"rule_id": "safe_go_local_storage", "rule": "Local/offline rejim metaveri depolama", "status": "ACTIVE"},
    {"rule_id": "safe_go_validation_catalog", "rule": "Doğrulama kabulü referanslı rejim kataloğu", "status": "ACTIVE"},
    {"rule_id": "safe_go_no_lookahead_refs", "rule": "No-lookahead doğrulanmış geriye dönük asof referansları", "status": "ACTIVE"},
    {"rule_id": "safe_go_metadata_only_news", "rule": "Yalnızca metaveri haber bağlamı referansları", "status": "ACTIVE"},
    {"rule_id": "safe_go_source_preservation", "rule": "Kaynak korumalı FeatureStore sözleşmeleri", "status": "ACTIVE"},
    {"rule_id": "safe_go_non_signal_queries", "rule": "Sinyal ve tahmin içermeyen salt metaveri sorguları", "status": "ACTIVE"},
    {"rule_id": "safe_go_read_write_contracts", "rule": "Okuma, yazma ve sorgulama sözleşme disiplini", "status": "ACTIVE"},
    {"rule_id": "safe_go_phase_135_handoff", "rule": "Phase 135 rejim kabul raporu için devir paketi", "status": "ACTIVE"},
]


def build_regime_featurestore_no_go_conditions(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of NO-GO prohibitions."""
    df = pd.DataFrame(CANONICAL_NO_GO_CONDITIONS)
    return df, {"total_no_go": len(df), "all_enforced": True}


def build_regime_featurestore_safe_go_conditions(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of SAFE-GO permitted operations."""
    df = pd.DataFrame(CANONICAL_SAFE_GO_CONDITIONS)
    return df, {"total_safe_go": len(df), "all_active": True}


def build_regime_featurestore_safety_boundary(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct combined safety boundary DataFrame."""
    active_profile = profile or get_regime_featurestore_profile()
    no_go_df, _ = build_regime_featurestore_no_go_conditions(active_profile)
    safe_go_df, _ = build_regime_featurestore_safe_go_conditions(active_profile)

    combined_rows = []
    for _, r in no_go_df.iterrows():
        combined_rows.append({
            "boundary_type": "NO_GO",
            "rule_id": r["rule_id"],
            "rule": r["rule"],
            "status": r["status"],
            "non_signal": True,
        })
    for _, r in safe_go_df.iterrows():
        combined_rows.append({
            "boundary_type": "SAFE_GO",
            "rule_id": r["rule_id"],
            "rule": r["rule"],
            "status": r["status"],
            "non_signal": True,
        })

    df = pd.DataFrame(combined_rows)
    summary = {
        "domain": SAFETY_DOMAIN,
        "total_rules": len(df),
        "no_go_count": len(no_go_df),
        "safe_go_count": len(safe_go_df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "safety_status": "SECURE",
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def summarize_regime_featurestore_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    return {
        "total_rules": len(df),
        "no_go_count": int((df["boundary_type"] == "NO_GO").sum()) if not df.empty else 0,
        "safe_go_count": int((df["boundary_type"] == "SAFE_GO").sum()) if not df.empty else 0,
        "safety_status": "SECURE",
    }
