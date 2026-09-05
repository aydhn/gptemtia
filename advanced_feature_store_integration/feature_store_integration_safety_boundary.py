"""Phase 124 Feature Store Integration Safety Boundary."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

NO_GO_CONDITIONS: List[Dict[str, str]] = [
    {"rule_id": "NOGO_01", "name": "no_live_trading", "description": "Canlı emir gönderilemez, broker API bağlanamaz."},
    {"rule_id": "NOGO_02", "name": "no_broker_integration", "description": "Broker API bağlama ve credential kullanımı yasaktır."},
    {"rule_id": "NOGO_03", "name": "no_real_order", "description": "Gerçek pozisyon açılamaz, emir iletilemez."},
    {"rule_id": "NOGO_04", "name": "no_investment_advice", "description": "Kesin al-sat tavsiyesi ve yatırım danışmanlığı üretilemez."},
    {"rule_id": "NOGO_05", "name": "no_store_as_signal", "description": "Feature store kayıtları alım-satım sinyali olarak sunulamaz."},
    {"rule_id": "NOGO_06", "name": "no_directional_claims", "description": "Yönsel kesinlik, fiyat artış/azalış garantisi üretilemez."},
    {"rule_id": "NOGO_07", "name": "no_strategy_backtest", "description": "Strateji kuralı üretimi, backtest ve optimizer çalıştırılamaz."},
    {"rule_id": "NOGO_08", "name": "no_model_training", "description": "Model eğitimi, tahmin üretimi ve model deployment yapılamaz."},
    {"rule_id": "NOGO_09", "name": "no_target_label", "description": "Target, label, future return ve shift(-1) üretimi yasaktır."},
    {"rule_id": "NOGO_10", "name": "no_official_approval", "description": "Production-ready, broker-ready ve resmi onay iddiası üretilemez."},
    {"rule_id": "NOGO_11", "name": "no_auto_imputation", "description": "Otomatik doldurma ve kolon mutasyonu yapılamaz."},
    {"rule_id": "NOGO_12", "name": "no_auto_feature_drop", "description": "Hatalı feature'ların otomatik silinmesi yasaktır; incelemeye yönlendirilir."},
    {"rule_id": "NOGO_13", "name": "no_source_overwrite", "description": "Kaynak dosya üzerine yazma, taşıma ve yıkıcı temizlik yasaktır."},
    {"rule_id": "NOGO_14", "name": "no_full_article_scraping", "description": "Haber tam metni kullanımı, web scraping ve paywall bypass yasaktır."},
    {"rule_id": "NOGO_15", "name": "no_credential_leak", "description": "API anahtarları, gizli anahtarlar ve token'lar çıktılarda yer alamaz."},
    {"rule_id": "NOGO_16", "name": "no_cloud_or_archive_publish", "description": "Docker push, git tag, bulut yayını ve gerçek ZIP arşivi üretilemez."},
]

SAFE_GO_CONDITIONS: List[Dict[str, str]] = [
    {"rule_id": "SAFEGO_01", "name": "local_offline_metadata_integration", "description": "Local/offline araştırma odaklı feature store metaveri entegrasyonu."},
    {"rule_id": "SAFEGO_02", "name": "validation_aware_catalogs", "description": "Validasyon durumu ve sızıntı denetimi içeren özellik katalogları."},
    {"rule_id": "SAFEGO_03", "name": "quality_drift_score_tracking", "description": "0.0-1.0 aralığında tanı kalite ve drift skor takibi."},
    {"rule_id": "SAFEGO_04", "name": "factor_metadata_and_lineage", "description": "Faktör taksonomisi ve köken referanslarının merkezi saklanması."},
    {"rule_id": "SAFEGO_05", "name": "manual_review_queue_preservation", "description": "Silme yapmadan insan denetim engellerinin izlenmesi."},
    {"rule_id": "SAFEGO_06", "name": "non_signal_contract_enforcement", "description": "Sinyal ve hedef içermeyen okuma/yazma/sorgulama sözleşmeleri."},
    {"rule_id": "SAFEGO_07", "name": "source_preservation_guarantee", "description": "Orijinal veri bütünlüğünü koruyan değişmez snapshot politikası."},
    {"rule_id": "SAFEGO_08", "name": "phase_125_acceptance_handoff", "description": "Phase 125 kabul raporu için eksiksiz ve doğrulanmış devir şartnamesi."},
]


def build_feature_store_integration_no_go_conditions(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> pd.DataFrame:
    """Return DataFrame of NO-GO conditions."""
    return pd.DataFrame(NO_GO_CONDITIONS)


def build_feature_store_integration_safe_go_conditions(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> pd.DataFrame:
    """Return DataFrame of SAFE-GO conditions."""
    return pd.DataFrame(SAFE_GO_CONDITIONS)


def build_feature_store_integration_safety_boundary(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build unified safety boundary report."""
    no_go = [dict(x, boundary_type="NO_GO", status="ENFORCED") for x in NO_GO_CONDITIONS]
    safe_go = [dict(x, boundary_type="SAFE_GO", status="ACTIVE") for x in SAFE_GO_CONDITIONS]
    all_conditions = no_go + safe_go

    df = pd.DataFrame(all_conditions)
    summary = {
        "safety_status": "SECURE",
        "total_conditions": len(all_conditions),
        "no_go_count": len(no_go),
        "safe_go_count": len(safe_go),
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_feature_store_integration_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    if df.empty:
        return {"safety_status": "UNKNOWN", "total_conditions": 0}
    no_go_cnt = int((df.get("boundary_type", pd.Series()) == "NO_GO").sum())
    safe_go_cnt = int((df.get("boundary_type", pd.Series()) == "SAFE_GO").sum())
    return {
        "safety_status": "SECURE",
        "total_conditions": len(df),
        "no_go_count": no_go_cnt,
        "safe_go_count": safe_go_cnt,
        "non_signal": True,
        "source_preserved": True,
    }
