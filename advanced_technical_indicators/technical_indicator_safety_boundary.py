from typing import Tuple, Dict, Any
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile

NO_GO_RULES = [
    {"rule_id": "NG_01", "name": "no_live_trading", "desc": "Canlı emir gönderilemez."},
    {"rule_id": "NG_02", "name": "no_broker_integration", "desc": "Broker API veya aracı kurum entegrasyonu kurulamaz."},
    {"rule_id": "NG_03", "name": "no_real_order", "desc": "Gerçek pozisyon açılamaz."},
    {"rule_id": "NG_04", "name": "no_exact_buy_sell", "desc": "Kesin AL/SAT talimatı verilemez."},
    {"rule_id": "NG_05", "name": "no_investment_advice", "desc": "Yatırım tavsiyesi verilemez."},
    {"rule_id": "NG_06", "name": "no_indicator_as_signal", "desc": "İndikatörler alım/satım sinyali olarak sunulamaz."},
    {"rule_id": "NG_07", "name": "no_directional_certainty", "desc": "Gelecek yön kesinliği iddia edilemez."},
    {"rule_id": "NG_08", "name": "no_strategy_generation", "desc": "Al/sat kuralları veya trade stratejisi üretilemez."},
    {"rule_id": "NG_09", "name": "no_backtest_execution", "desc": "Backtest simülasyonu çalıştırılamaz."},
    {"rule_id": "NG_10", "name": "no_optimizer_execution", "desc": "Strateji parametre optimizasyonu yapılamaz."},
    {"rule_id": "NG_11", "name": "no_target_label_columns", "desc": "Target, label, prediction kolonları üretilemez."},
    {"rule_id": "NG_12", "name": "no_model_deployment", "desc": "Model deployment veya production servisi başlatılamaz."},
    {"rule_id": "NG_13", "name": "no_web_scraping", "desc": "Web / HTML scraping veya browser otomasyonu yapılamaz."},
    {"rule_id": "NG_14", "name": "no_hidden_api_reverse_engineering", "desc": "Tersine mühendislik veya paywall bypass yapılamaz."},
    {"rule_id": "NG_15", "name": "no_credential_output", "desc": "API anahtarı veya gizli kimlik basılamaz."},
    {"rule_id": "NG_16", "name": "no_source_overwrite", "desc": "Kaynak veriler üzerine yazma veya yıkıcı temizlik yapılamaz."},
    {"rule_id": "NG_17", "name": "no_future_lookahead", "desc": "shift(-1) veya ileri vadeli getiri feature'ı üretilemez."},
    {"rule_id": "NG_18", "name": "no_official_approval_claim", "desc": "Resmi regülasyon veya provider onayı iddia edilemez."},
]

SAFE_GO_RULES = [
    {"rule_id": "SG_01", "name": "local_offline_indicator_registry", "desc": "Local ve offline teknik indikatör kayıt defteri."},
    {"rule_id": "SG_02", "name": "non_signal_computation", "desc": "AL/SAT üretmeyen saf matematiksel indikatör hesaplaması."},
    {"rule_id": "SG_03", "name": "immutable_dataframe_transform", "desc": "Girdi dataframe'ini koruyan df.copy() dönüşümleri."},
    {"rule_id": "SG_04", "name": "pure_python_numpy_pandas", "desc": "TA-Lib zorunluluğu olmaksızın çalışan bağımsız hesaplama."},
    {"rule_id": "SG_05", "name": "no_lookahead_verification", "desc": "Sadece geçmiş barları kullanan zaman serisi güvenliği."},
    {"rule_id": "SG_06", "name": "warmup_nan_policy", "desc": "Başlangıç pencerelerindeki NaN değerleri koruma politikası."},
    {"rule_id": "SG_07", "name": "indicator_output_schema", "desc": "Yasaklı kolon filtrelemeli çıktı şemaları."},
    {"rule_id": "SG_08", "name": "synthetic_rehearsal_suite", "desc": "Sentetik verilerle doğrulama ve prova motoru."},
    {"rule_id": "SG_09", "name": "phase_118_multi_window_grid_handoff", "desc": "Phase 118 çoklu pencere grid altyapısına hazır devir."},
]


def build_technical_indicator_no_go_conditions(profile: TechnicalIndicatorProfile) -> pd.DataFrame:
    df = pd.DataFrame(NO_GO_RULES)
    df["status"] = "ENFORCED"
    return df


def build_technical_indicator_safe_go_conditions(profile: TechnicalIndicatorProfile) -> pd.DataFrame:
    df = pd.DataFrame(SAFE_GO_RULES)
    df["status"] = "ALLOWED"
    return df


def build_technical_indicator_safety_boundary(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    no_go = build_technical_indicator_no_go_conditions(profile)
    safe_go = build_technical_indicator_safe_go_conditions(profile)
    all_rules = pd.concat([no_go, safe_go], ignore_index=True)
    summary = {
        "total_rules": len(all_rules),
        "total_no_go": len(no_go),
        "total_safe_go": len(safe_go),
        "safety_status": "ACTIVE",
        "current_phase": profile.current_phase,
    }
    return all_rules, summary


def summarize_technical_indicator_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rules": len(df),
        "safety_status": "ACTIVE",
    }
