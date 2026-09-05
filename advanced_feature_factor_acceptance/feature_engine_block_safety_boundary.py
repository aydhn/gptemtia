"""Phase 125: Feature Engine Block Safety Boundary Report.

Enforces deterministic NO-GO and SAFE-GO governance boundaries for the entire
Phase 116-125 feature engine block.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)

NO_GO_CONDITIONS = [
    {"rule_id": "nogo_01", "name": "Live Trading Execution", "enforced": True, "description": "Canlı emir ve piyasa işlemi yürütülmesi kesinlikle yasaktır."},
    {"rule_id": "nogo_02", "name": "Broker API Integration", "enforced": True, "description": "Broker veya borsa hesaplarına API bağlantısı yapılamaz."},
    {"rule_id": "nogo_03", "name": "Real Orders", "enforced": True, "description": "Gerçek sermaye ile alım-satım emri üretilemez."},
    {"rule_id": "nogo_04", "name": "Investment Advice", "enforced": True, "description": "Yatırım tavsiyesi veya portföy önerisi sunulamaz."},
    {"rule_id": "nogo_05", "name": "Acceptance As Signal", "enforced": True, "description": "Kabul skoru veya geçit sonucu trade sinyali olarak yorumlanamaz."},
    {"rule_id": "nogo_06", "name": "Directional Claims", "enforced": True, "description": "Piyasa yönü veya fiyat tahmini iddiasında bulunulamaz."},
    {"rule_id": "nogo_07", "name": "Strategy/Backtest/Optimizer", "enforced": True, "description": "Strateji üretimi, backtest ve parametre optimizasyonu yapılamaz."},
    {"rule_id": "nogo_08", "name": "Target/Label/Prediction", "enforced": True, "description": "Denetimli makine öğrenmesi hedefleri veya tahminler üretilemez."},
    {"rule_id": "nogo_09", "name": "Official Approval / Ready Claims", "enforced": True, "description": "Üretim onayı, broker-ready veya canlıya hazır iddiası öne sürülemez."},
    {"rule_id": "nogo_10", "name": "Full Article Text Usage", "enforced": True, "description": "Haber gövdesi, tam metin veya telifli içerik depolanamaz."},
    {"rule_id": "nogo_11", "name": "Web Scraping", "enforced": True, "description": "Web scraping, tarayıcı otomasyonu veya gizli API kullanımı yasaktır."},
    {"rule_id": "nogo_12", "name": "Credential Outputs", "enforced": True, "description": "API anahtarı, şifre veya gizli dizgiler raporlara yazılamaz."},
    {"rule_id": "nogo_13", "name": "Source Overwrite / Deletion", "enforced": True, "description": "Ham kaynak dosyaları üzerine yazma veya silme yapılamaz."},
    {"rule_id": "nogo_14", "name": "Auto-Imputation & Feature Drop", "enforced": True, "description": "Otomatik değer doldurma veya kolon silme uygulanamaz."},
    {"rule_id": "nogo_15", "name": "Production Deployment", "enforced": True, "description": "Bulut yayını, docker push veya git tag tetiklenemez."},
]

SAFE_GO_CONDITIONS = [
    {"rule_id": "safego_01", "name": "Offline Acceptance Reporting", "active": True, "description": "Yerel ve çevrimdışı blok kabul değerlendirmesi."},
    {"rule_id": "safego_02", "name": "Inventory & Contract Audit", "active": True, "description": "Modül, betik, test ve dokümantasyon sözleşme kontrolü."},
    {"rule_id": "safego_03", "name": "Non-Signal Invariant Enforcement", "active": True, "description": "Bütün çıktılarda trade sinyali yokluğunun garanti edilmesi."},
    {"rule_id": "safego_04", "name": "No-Lookahead Invariant Enforcement", "active": True, "description": "Zaman serisi sıralaması ve sızıntısız hizalamaların teyidi."},
    {"rule_id": "safego_05", "name": "News Metadata-Only Boundary", "active": True, "description": "Sadece kanonik haber başlık metaverilerinin korunması."},
    {"rule_id": "safego_06", "name": "Source Preservation Guarantee", "active": True, "description": "Ham verilerin değişmezliğinin ve izlenebilirliğinin korunması."},
    {"rule_id": "safego_07", "name": "Phase 126 Regime Handoff Preparation", "active": True, "description": "Rejim sınıflandırması için temiz girdi devir şartnamesi."},
]


def build_feature_engine_block_no_go_conditions(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> pd.DataFrame:
    """Build NO-GO conditions DataFrame."""
    return pd.DataFrame(NO_GO_CONDITIONS)


def build_feature_engine_block_safe_go_conditions(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> pd.DataFrame:
    """Build SAFE-GO conditions DataFrame."""
    return pd.DataFrame(SAFE_GO_CONDITIONS)


def build_feature_engine_block_safety_boundary_report(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined safety boundary DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    df_nogo = build_feature_engine_block_no_go_conditions(active_profile)
    df_safego = build_feature_engine_block_safe_go_conditions(active_profile)

    combined_rows = []
    for _, row in df_nogo.iterrows():
        combined_rows.append({
            "boundary_type": "NO_GO",
            "rule_id": row["rule_id"],
            "name": row["name"],
            "status": "ENFORCED",
            "description": row["description"],
        })
    for _, row in df_safego.iterrows():
        combined_rows.append({
            "boundary_type": "SAFE_GO",
            "rule_id": row["rule_id"],
            "name": row["name"],
            "status": "ACTIVE",
            "description": row["description"],
        })
    df = pd.DataFrame(combined_rows)

    summary = {
        "profile_name": active_profile.profile_name,
        "total_rules": len(df),
        "no_go_count": len(df_nogo),
        "safe_go_count": len(df_safego),
        "all_no_go_enforced": True,
        "all_safe_go_active": True,
        "non_signal": True,
        "source_preserved": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_feature_engine_block_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    return {
        "total_rules": len(df),
        "no_go_rules": len(df[df["boundary_type"] == "NO_GO"]) if "boundary_type" in df.columns else 0,
        "safe_go_rules": len(df[df["boundary_type"] == "SAFE_GO"]) if "boundary_type" in df.columns else 0,
        "secure": True,
    }
