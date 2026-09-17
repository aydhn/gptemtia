# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Safety Boundary.

Defines non-negotiable NO-GO and SAFE-GO operating rules for backtest governance and bias control.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile

NO_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "NO_GO_01", "rule_name": "no_live_trading", "description": "Gerçek sermaye ile piyasada işlem açmak kesinlikle yasaktır."},
    {"rule_id": "NO_GO_02", "rule_name": "no_broker_integration", "description": "Aracı kurum API entegrasyonu ve emir iletimi yasaktır."},
    {"rule_id": "NO_GO_03", "rule_name": "no_investment_advice", "description": "Kesin AL/SAT veya yatırım tavsiyesi üretmek yasaktır."},
    {"rule_id": "NO_GO_04", "rule_name": "no_signal_generation", "description": "Yönetişim veya yanlılık kontrollerini trade sinyali olarak sunmak yasaktır."},
    {"rule_id": "NO_GO_05", "rule_name": "no_backtest_execution", "description": "Gerçek backtest simülasyonu çalıştırmak yasaktır; yalnızca sözleşme kurulabilir."},
    {"rule_id": "NO_GO_06", "rule_name": "no_benchmark_execution", "description": "Gerçek benchmark simülasyonu ve kıyaslama yürütmek yasaktır."},
    {"rule_id": "NO_GO_07", "rule_name": "no_parameter_optimization", "description": "Parametre optimizasyonu, curve-fitting veya grid search çalıştırmak yasaktır."},
    {"rule_id": "NO_GO_08", "rule_name": "no_result_claims", "description": "Doğrulanmamış backtest sonuç iddiası ve genelleme yapmak yasaktır."},
    {"rule_id": "NO_GO_09", "rule_name": "no_performance_claims", "description": "Kesin getiri, Sharpe veya başarı iddiasında bulunmak yasaktır."},
    {"rule_id": "NO_GO_10", "rule_name": "no_strategy_approvals", "description": "Stratejileri canlı veya üretime hazır olarak onaylamak yasaktır."},
    {"rule_id": "NO_GO_11", "rule_name": "no_metric_calculation", "description": "Gerçek Sharpe, win-rate, alpha veya drawdown hesaplamak yasaktır."},
    {"rule_id": "NO_GO_12", "rule_name": "no_model_training_prediction", "description": "Model eğitimi, fit, predict veya hedef etiket üretimi yasaktır."},
    {"rule_id": "NO_GO_13", "rule_name": "no_model_registry_deployment", "description": "Model kaydı yazmak veya üretim sunucularına dağıtım yapmak yasaktır."},
    {"rule_id": "NO_GO_14", "rule_name": "no_web_scraping_credentials", "description": "Haber kazıma, tam metin indirme veya API anahtarı yazdırma yasaktır."},
    {"rule_id": "NO_GO_15", "rule_name": "no_source_overwrite", "description": "Kaynak verileri silmek veya üzerine yazmak yasaktır."},
]

SAFE_GO_RULES: List[Dict[str, str]] = [
    {"rule_id": "SAFE_GO_01", "rule_name": "local_backtest_governance_contracts", "description": "Yerel backtest yönetişim sözleşmelerini tanımlamak."},
    {"rule_id": "SAFE_GO_02", "rule_name": "bias_control_contracts_definition", "description": "Lookahead, survivorship ve data snooping yanlılık kontrollerini kurmak."},
    {"rule_id": "SAFE_GO_03", "rule_name": "claim_boundary_enforcement", "description": "Metrik ve performans iddia sınırlarını sıkı kurallarla kilitlemek."},
    {"rule_id": "SAFE_GO_04", "rule_name": "execution_realism_governance", "description": "İşlem maliyeti, kayma, likidite ve eşleşme gerçekçilik kurallarını belirlemek."},
    {"rule_id": "SAFE_GO_05", "rule_name": "audit_and_evidence_policies", "description": "Denetim izi ve doğrulama kanıtı kayıt defterlerini oluşturmak."},
    {"rule_id": "SAFE_GO_06", "rule_name": "manual_review_gates_configuration", "description": "10 adet insan onay kapısını devreye almak."},
    {"rule_id": "SAFE_GO_07", "rule_name": "disabled_execution_reporting", "description": "Yasaklı yürütme motorlarını belgeleyen engelleme raporları üretmek."},
    {"rule_id": "SAFE_GO_08", "rule_name": "phase_151_handoff_preparation", "description": "Phase 151 Benchmark Karşılaştırma ve Strateji Değerlendirme devir paketini hazırlamak."},
]


def build_backtest_governance_no_go_conditions(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame of all strict NO-GO constraints."""
    df = pd.DataFrame(NO_GO_RULES)
    df["enforced"] = True
    df["non_signal"] = True
    df["local_only"] = True
    summary = {
        "total_no_go_rules": len(df),
        "all_enforced": True,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary


def build_backtest_governance_safe_go_conditions(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame of all permitted SAFE-GO research activities."""
    df = pd.DataFrame(SAFE_GO_RULES)
    df["authorized"] = True
    df["non_signal"] = True
    df["local_only"] = True
    summary = {
        "total_safe_go_rules": len(df),
        "all_authorized": True,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary


def build_backtest_governance_safety_boundary(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a consolidated DataFrame of safety boundaries."""
    df_no, _ = build_backtest_governance_no_go_conditions(profile)
    df_safe, _ = build_backtest_governance_safe_go_conditions(profile)

    combined_rows = []
    for _, r in df_no.iterrows():
        combined_rows.append({
            "type": "NO_GO",
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforced": True,
        })
    for _, r in df_safe.iterrows():
        combined_rows.append({
            "type": "SAFE_GO",
            "rule_id": r["rule_id"],
            "rule_name": r["rule_name"],
            "description": r["description"],
            "enforced": True,
        })

    df = pd.DataFrame(combined_rows)
    df["non_signal"] = True
    df["local_only"] = True
    summary = {
        "safety_status": "SECURE",
        "no_go_count": len(df_no),
        "safe_go_count": len(df_safe),
        "live_trading_prohibited": True,
        "broker_execution_prohibited": True,
        "backtest_execution_prohibited": True,
        "benchmark_execution_prohibited": True,
        "parameter_optimization_prohibited": True,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary


enforce_backtest_governance_safety_boundary = build_backtest_governance_safety_boundary
