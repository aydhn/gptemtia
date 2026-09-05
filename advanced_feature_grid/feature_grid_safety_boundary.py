from typing import Tuple, Dict, Any
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


NO_GO_ITEMS = [
    {"rule_id": "no_go_01", "name": "Live Trading Prohibition", "detail": "Canlı emir gönderme, broker API veya socket bağlantısı yasaktır."},
    {"rule_id": "no_go_02", "name": "Broker Integration Prohibition", "detail": "Broker credential, hesap bağlama veya pozisyon açma kesinlikle yasaktır."},
    {"rule_id": "no_go_03", "name": "Exact Buy/Sell Sinyal Yasağı", "detail": "Kesin AL/SAT veya alım-satım talimatı üretilemez."},
    {"rule_id": "no_go_04", "name": "Investment Advice Prohibition", "detail": "Yatırım tavsiyesi, portföy önerisi veya getiri vaadi sunulamaz."},
    {"rule_id": "no_go_05", "name": "Feature-Grid-as-Signal Yasağı", "detail": "Feature grid değerleri trade sinyali olarak kullanılamaz veya yorumlanamaz."},
    {"rule_id": "no_go_06", "name": "Directional Claim Yasağı", "detail": "EMA/RSI grid yukarı yönlü kesin hareket gösteriyor gibi yönlü iddia üretilemez."},
    {"rule_id": "no_go_07", "name": "Strategy Generation Prohibition", "detail": "Al-sat kuralları veya otomatik strateji şablonları üretilemez."},
    {"rule_id": "no_go_08", "name": "Backtest Execution Prohibition", "detail": "Tarihsel getiri simülasyonu veya backtest çalıştırılamaz."},
    {"rule_id": "no_go_09", "name": "Optimizer Execution Prohibition", "detail": "Parametre optimizasyonu, curve-fitting veya grid search optimizer çalıştırılamaz."},
    {"rule_id": "no_go_10", "name": "Target/Label/Prediction Yasağı", "detail": "Target, label, classification veya regression prediction üretilemez."},
    {"rule_id": "no_go_11", "name": "Model/Production Deployment Yasağı", "detail": "Model serving, microservice, Docker push veya production deployment yapılamaz."},
    {"rule_id": "no_go_12", "name": "Scraping & Browser Automation Yasağı", "detail": "Web scraping, HTML parsing, haber sitesi scraping veya browser automation yasaktır."},
    {"rule_id": "no_go_13", "name": "Hidden API & Paywall Bypass Yasağı", "detail": "Reverse engineering, paywall aşma veya rate limit suiistimali yasaktır."},
    {"rule_id": "no_go_14", "name": "Credential Leakage Prohibition", "detail": "API key, token, secret veya şifrelerin loglara veya raporlara yazdırılması yasaktır."},
    {"rule_id": "no_go_15", "name": "Destructive File Modification Yasağı", "detail": "Kaynak dosyaların üzerine yazma (source overwrite), silme veya taşıma yasaktır."},
    {"rule_id": "no_go_16", "name": "Official Compliance Claim Yasağı", "detail": "Resmi uyumluluk, hukuki onay veya lisanslı kurum onayı iddiası üretilemez."},
]

SAFE_GO_ITEMS = [
    {"rule_id": "safe_go_01", "name": "Local/Offline Feature Grid", "detail": "Ağ çağrısı gerektirmeyen tamamen yerel ve çevrimdışı feature grid mimarisi."},
    {"rule_id": "safe_go_02", "name": "Non-Signal Research Features", "detail": "Sadece araştırma amaçlı parametrik feature üretimi; sinyal üretimi yok."},
    {"rule_id": "safe_go_03", "name": "Copy-Based Data Transformations", "detail": "Girdi DataFrame'ini mutate etmeyen güvenli df.copy() hesaplamaları."},
    {"rule_id": "safe_go_04", "name": "No-Lookahead Guard Enforced", "detail": "shift(-1) ve geleceğe bakan kolonların engellendiği geriye dönük yapı."},
    {"rule_id": "safe_go_05", "name": "Duplicate Feature Detection", "detail": "Mükerrer feature hesaplamalarını tespit eden ve raporlayan denetim."},
    {"rule_id": "safe_go_06", "name": "Warmup NaN Policy", "detail": "Rolling pencerelerin doğal başlangıç NaN değerlerini silmeden koruyan politika."},
    {"rule_id": "safe_go_07", "name": "Output Schema Validation", "detail": "Sayısal tip ve yasaklı alias kontrolü sağlayan çıktı şeması doğrulayıcısı."},
    {"rule_id": "safe_go_08", "name": "Phase 119 Alignment Handoff", "detail": "Varlıklar arası zaman ve sembol hizalaması için hazır feature sözleşmeleri."},
]


def build_feature_grid_no_go_conditions(profile: FeatureGridProfile | None = None) -> pd.DataFrame:
    df = pd.DataFrame(NO_GO_ITEMS)
    df["boundary_type"] = "NO_GO"
    df["enforced"] = True
    return df


def build_feature_grid_safe_go_conditions(profile: FeatureGridProfile | None = None) -> pd.DataFrame:
    df = pd.DataFrame(SAFE_GO_ITEMS)
    df["boundary_type"] = "SAFE_GO"
    df["enabled"] = True
    return df


def build_feature_grid_safety_boundary(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df_no_go = build_feature_grid_no_go_conditions(active_profile)
    df_safe_go = build_feature_grid_safe_go_conditions(active_profile)
    df = pd.concat([df_no_go, df_safe_go], ignore_index=True)
    summary = summarize_feature_grid_safety_boundary(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_conditions": 0, "status": "EMPTY"}

    no_go_count = int((df["boundary_type"] == "NO_GO").sum()) if "boundary_type" in df.columns else 0
    safe_go_count = int((df["boundary_type"] == "SAFE_GO").sum()) if "boundary_type" in df.columns else 0

    return {
        "total_conditions": len(df),
        "total_no_go": no_go_count,
        "total_safe_go": safe_go_count,
        "strict_boundaries_enforced": True,
        "safety_status": "ACTIVE",
    }
