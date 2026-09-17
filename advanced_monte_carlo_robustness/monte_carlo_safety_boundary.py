# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Safety Boundary.

Defines non-negotiable NO-GO and SAFE-GO operating rules for Monte Carlo robustness and parameter stability contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile

NO_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "NO_GO_01", "rule_name": "no_live_trading", "description": "Gerçek sermaye ile piyasada işlem açmak kesinlikle yasaktır."},
    {"rule_id": "NO_GO_02", "rule_name": "no_broker_integration", "description": "Aracı kurum API entegrasyonu ve emir iletimi yasaktır."},
    {"rule_id": "NO_GO_03", "rule_name": "no_investment_advice", "description": "Kesin AL/SAT veya yatırım tavsiyesi üretmek yasaktır."},
    {"rule_id": "NO_GO_04", "rule_name": "no_signal_generation", "description": "Monte Carlo veya parametre stabilitesi skorunu trade sinyali olarak sunmak yasaktır."},
    {"rule_id": "NO_GO_05", "rule_name": "no_true_monte_carlo_execution", "description": "Gerçek Monte Carlo simülasyonu çalıştırmak yasaktır; yalnızca sözleşme kurulabilir."},
    {"rule_id": "NO_GO_06", "rule_name": "no_bootstrap_simulation_execution", "description": "Gerçek bootstrap veya resampling yürütmek yasaktır."},
    {"rule_id": "NO_GO_07", "rule_name": "no_parameter_optimization", "description": "Parametre optimizasyonu, curve-fitting veya grid search çalıştırmak yasaktır."},
    {"rule_id": "NO_GO_08", "rule_name": "no_parameter_sweep", "description": "Parametre tarama veya yüzey maksimizasyonu yürütmek yasaktır."},
    {"rule_id": "NO_GO_09", "rule_name": "no_metric_calculation", "description": "Gerçek Monte Carlo VaR, ES, drawdown veya getiri dağılımı hesaplamak yasaktır."},
    {"rule_id": "NO_GO_10", "rule_name": "no_model_training_prediction", "description": "Model eğitimi, fit, predict veya hedef etiket üretimi yasaktır."},
    {"rule_id": "NO_GO_11", "rule_name": "no_model_registry_write", "description": "Model kaydı yazmak veya yapay zeka modeli deploy etmek yasaktır."},
    {"rule_id": "NO_GO_12", "rule_name": "no_performance_guarantee", "description": "Geleceğe dönük getiri, dayanıklılık veya başarı garantisi vermek yasaktır."},
    {"rule_id": "NO_GO_13", "rule_name": "no_web_scraping_credentials", "description": "Haber kazıma, tam metin indirme veya API anahtarı yazdırma yasaktır."},
    {"rule_id": "NO_GO_14", "rule_name": "no_source_overwrite", "description": "Kaynak verileri silmek veya üzerine yazmak yasaktır."},
]

SAFE_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "SAFE_GO_01", "rule_name": "local_monte_carlo_contract_generation", "description": "Yerel Monte Carlo ve sağlamlık zarfı sözleşmelerini tanımlamak."},
    {"rule_id": "SAFE_GO_02", "rule_name": "bootstrap_contract_generation", "description": "Blok ve durağan bootstrap sözleşmelerini kurmak."},
    {"rule_id": "SAFE_GO_03", "rule_name": "resampling_placeholder_generation", "description": "Getiri yolu, işlem sırası ve gürültü yer tutucularını oluşturmak."},
    {"rule_id": "SAFE_GO_04", "rule_name": "parameter_stability_contracts", "description": "Parametre duyarlılığı, tedirginliği ve kırılganlık sözleşmelerini tanımlamak."},
    {"rule_id": "SAFE_GO_05", "rule_name": "robustness_envelope_placeholders", "description": "Güven aralığı, kuyruk riski ve drawdown dağılım yer tutucularını oluşturmak."},
    {"rule_id": "SAFE_GO_06", "rule_name": "bias_and_leakage_guards", "description": "Zaman serisi bütünlüğü, veri gözetleme ve no-lookahead muhafızlarını kurmak."},
    {"rule_id": "SAFE_GO_07", "rule_name": "disabled_execution_reporting", "description": "Yasaklı yürütme yollarını belgeleyen engelleme raporları üretmek."},
    {"rule_id": "SAFE_GO_08", "rule_name": "phase_150_handoff_preparation", "description": "Phase 150 Backtest Governance ve Bias Control devir paketini hazırlamak."},
]


def build_monte_carlo_no_go_conditions(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame of all strict NO-GO constraints."""
    df = pd.DataFrame(NO_GO_RULES)
    df["enforced"] = True
    df["non_signal"] = True
    summary = {"total_no_go_rules": len(df), "all_enforced": True, "non_signal": True}
    return df, summary


def build_monte_carlo_safe_go_conditions(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame of all permitted SAFE-GO research activities."""
    df = pd.DataFrame(SAFE_GO_RULES)
    df["authorized"] = True
    df["non_signal"] = True
    summary = {"total_safe_go_rules": len(df), "all_authorized": True, "non_signal": True}
    return df, summary


def build_monte_carlo_safety_boundary(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a consolidated DataFrame of safety boundaries."""
    df_no, _ = build_monte_carlo_no_go_conditions(profile)
    df_safe, _ = build_monte_carlo_safe_go_conditions(profile)

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
        "monte_carlo_execution_prohibited": True,
        "parameter_optimization_prohibited": True,
        "non_signal": True,
    }
    return df, summary


enforce_monte_carlo_safety_boundary = build_monte_carlo_safety_boundary
