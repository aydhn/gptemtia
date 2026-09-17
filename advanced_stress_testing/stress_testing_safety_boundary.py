# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing Safety Boundary.

Defines non-negotiable NO-GO and SAFE-GO operating rules for stress testing contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile

NO_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "NO_GO_01", "rule_name": "no_live_trading", "description": "Gerçek sermaye ile piyasada işlem açmak kesinlikle yasaktır."},
    {"rule_id": "NO_GO_02", "rule_name": "no_broker_integration", "description": "Aracı kurum API entegrasyonu ve emir iletimi yasaktır."},
    {"rule_id": "NO_GO_03", "rule_name": "no_investment_advice", "description": "Kesin AL/SAT veya yatırım tavsiyesi üretmek yasaktır."},
    {"rule_id": "NO_GO_04", "rule_name": "no_signal_generation", "description": "Stres hazırlık skorunu trade sinyali olarak sunmak yasaktır."},
    {"rule_id": "NO_GO_05", "rule_name": "no_true_stress_execution", "description": "Gerçek stres testi çalıştırmak yasaktır; yalnızca sözleşme kurulabilir."},
    {"rule_id": "NO_GO_06", "rule_name": "no_scenario_simulation_execution", "description": "Gerçek senaryo simülasyonu yürütmek yasaktır."},
    {"rule_id": "NO_GO_07", "rule_name": "no_metric_calculation", "description": "Gerçek stres PnL, VaR veya drawdown hesaplamak yasaktır."},
    {"rule_id": "NO_GO_08", "rule_name": "no_optimizer_execution", "description": "Stres parametrelerine göre optimizasyon çalıştırmak yasaktır."},
    {"rule_id": "NO_GO_09", "rule_name": "no_monte_carlo_execution", "description": "Monte Carlo çalıştırmak yasaktır (Phase 149 konusudur)."},
    {"rule_id": "NO_GO_10", "rule_name": "no_model_training_prediction", "description": "Model eğitimi, fit, predict veya hedef etiket üretimi yasaktır."},
    {"rule_id": "NO_GO_11", "rule_name": "no_model_registry_write", "description": "Model kaydı yazmak veya yapay zeka modeli deploy etmek yasaktır."},
    {"rule_id": "NO_GO_12", "rule_name": "no_performance_guarantee", "description": "Geleceğe dönük getiri veya başarı garantisi vermek yasaktır."},
    {"rule_id": "NO_GO_13", "rule_name": "no_web_scraping_credentials", "description": "Haber kazıma, tam metin indirme veya API anahtarı yazdırma yasaktır."},
    {"rule_id": "NO_GO_14", "rule_name": "no_source_overwrite", "description": "Kaynak verileri silmek veya üzerine yazmak yasaktır."},
]

SAFE_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "SAFE_GO_01", "rule_name": "local_scenario_contract_generation", "description": "Yerel stres ve kriz senaryo sözleşmelerini tanımlamak."},
    {"rule_id": "SAFE_GO_02", "rule_name": "shock_placeholder_generation", "description": "Volatilite, likidite, spread ve gap şok yer tutucularını oluşturmak."},
    {"rule_id": "SAFE_GO_03", "rule_name": "scenario_library_metadata", "description": "Tarihsel ve varsayımsal senaryo kütüphane metaverisini derlemek."},
    {"rule_id": "SAFE_GO_04", "rule_name": "stress_metric_placeholders", "description": "VaR, ES ve drawdown için hesaplama yapmayan formül yer tutucuları oluşturmak."},
    {"rule_id": "SAFE_GO_05", "rule_name": "bias_and_leakage_guards", "description": "No-lookahead, senaryo sızıntısı ve yasaklı kolon muhafızlarını kurmak."},
    {"rule_id": "SAFE_GO_06", "rule_name": "disabled_execution_reporting", "description": "Yasaklı yürütme yollarını belgeleyen engelleme raporları üretmek."},
    {"rule_id": "SAFE_GO_07", "rule_name": "phase_149_handoff_preparation", "description": "Phase 149 Monte Carlo ve parametre stabilitesi devir paketini hazırlamak."},
]


def build_stress_testing_no_go_conditions(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame of all strict NO-GO constraints."""
    df = pd.DataFrame(NO_GO_RULES)
    df["enforced"] = True
    df["non_signal"] = True
    summary = {"total_no_go_rules": len(df), "all_enforced": True, "non_signal": True}
    return df, summary


def build_stress_testing_safe_go_conditions(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame of all permitted SAFE-GO research activities."""
    df = pd.DataFrame(SAFE_GO_RULES)
    df["authorized"] = True
    df["non_signal"] = True
    summary = {"total_safe_go_rules": len(df), "all_authorized": True, "non_signal": True}
    return df, summary


def build_stress_testing_safety_boundary(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a consolidated DataFrame of safety boundaries."""
    df_no, _ = build_stress_testing_no_go_conditions(profile)
    df_safe, _ = build_stress_testing_safe_go_conditions(profile)

    combined_rows = []
    for _, r in df_no.iterrows():
        combined_rows.append({"type": "NO_GO", "rule_id": r["rule_id"], "rule_name": r["rule_name"], "description": r["description"]})
    for _, r in df_safe.iterrows():
        combined_rows.append({"type": "SAFE_GO", "rule_id": r["rule_id"], "rule_name": r["rule_name"], "description": r["description"]})

    df = pd.DataFrame(combined_rows)
    df["non_signal"] = True
    df["local_only"] = True
    summary = {
        "safety_status": "SECURE",
        "no_go_count": len(df_no),
        "safe_go_count": len(df_safe),
        "live_trading_prohibited": True,
        "broker_execution_prohibited": True,
        "non_signal": True,
    }
    return df, summary
enforce_stress_testing_safety_boundary = build_stress_testing_safety_boundary

