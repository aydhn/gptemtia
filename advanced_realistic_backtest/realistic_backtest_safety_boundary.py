# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Safety Boundaries.

Enforces explicit NO-GO constraints and SAFE-GO principles for realistic backtesting contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

NO_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "NOGO-146-01", "name": "prohibit_live_trading", "category": "TRADING", "description": "Canli emir gonderme ve gercek pozisyon yonetimi kesinlikle yasaktir."},
    {"rule_id": "NOGO-146-02", "name": "prohibit_broker_execution", "category": "BROKER", "description": "Araci kurum API baglantisi ve emir rotalama kesinlikle yasaktir."},
    {"rule_id": "NOGO-146-03", "name": "prohibit_investment_advice", "category": "REGULATION", "description": "Kesin AL/SAT veya portfoy yonetim tavsiyesi uretilemez."},
    {"rule_id": "NOGO-146-04", "name": "prohibit_signal_generation", "category": "SIGNAL", "description": "Backtest katmani trade sinyali veya alfa uretemez."},
    {"rule_id": "NOGO-146-05", "name": "prohibit_optimizer_execution", "category": "EXECUTION", "description": "Parametre veya strateji optimizasyonu bu fazda calistirilamaz."},
    {"rule_id": "NOGO-146-06", "name": "prohibit_walk_forward_execution", "category": "EXECUTION", "description": "Walk-forward simulasyonu Phase 147'ye ertelenmistir, bu fazda calistirilamaz."},
    {"rule_id": "NOGO-146-07", "name": "prohibit_benchmark_execution", "category": "EXECUTION", "description": "Benchmark karsilastirma simulasyonu sonraki fazlara ertelenmistir."},
    {"rule_id": "NOGO-146-08", "name": "prohibit_model_training", "category": "ML", "description": "Gercek ML model egitimi ve model fit islemleri kesinlikle calistirilamaz."},
    {"rule_id": "NOGO-146-09", "name": "prohibit_model_prediction", "category": "ML", "description": "Gercek model cikarimi ve tahmin uretimi yapilamaz."},
    {"rule_id": "NOGO-146-10", "name": "prohibit_target_label_generation", "category": "ML", "description": "Hedef etiket veya getiri sinifi uretilemez."},
    {"rule_id": "NOGO-146-11", "name": "prohibit_model_registry_write", "category": "GOVERNANCE", "description": "Model kayit defterine yazim yapilamaz."},
    {"rule_id": "NOGO-146-12", "name": "prohibit_production_deployment", "category": "DEPLOYMENT", "description": "Uretim ortamina dagitim veya onay verilmesi yasaktir."},
    {"rule_id": "NOGO-146-13", "name": "prohibit_performance_guarantees", "category": "LEGAL", "description": "Gecmis veya gelecek getiri garantisi iddia edilemez."},
    {"rule_id": "NOGO-146-14", "name": "prohibit_scraping_and_credentials", "category": "DATA", "description": "Web kazima, gizli API cagrisi ve credential yazdirma yasaktir."},
    {"rule_id": "NOGO-146-15", "name": "prohibit_source_overwrite", "category": "DATA", "description": "Ham verinin uzerine yazilmasi veya silinmesi kesinlikle yasaktir."},
]

SAFE_GO_RULES: List[Dict[str, Any]] = [
    {"rule_id": "SAFEGO-146-01", "name": "local_offline_backtest_contracts", "category": "CONTRACT", "description": "Yerel ve cevrimdisi backtest motor sozlesmelerinin kurulmasi."},
    {"rule_id": "SAFEGO-146-02", "name": "transaction_cost_model_contracts", "category": "COST", "description": "Komisyon, borsa ucreti ve alis-satis makas sozlesmelerinin kurulmasi."},
    {"rule_id": "SAFEGO-146-03", "name": "slippage_model_contracts", "category": "SLIPPAGE", "description": "Fiyat kaymasi formullerinin sozlesme modunda hazirlanmasi."},
    {"rule_id": "SAFEGO-146-04", "name": "execution_realism_placeholders", "category": "REALISM", "description": "Gecikme, likidite ve kismi dolum yer tutucularinin kurulmasi."},
    {"rule_id": "SAFEGO-146-05", "name": "accounting_and_lifecycle_contracts", "category": "ACCOUNTING", "description": "PnL, nakit, teminat ve islem yasam dongusu sozlesmelerinin tanimlanmasi."},
    {"rule_id": "SAFEGO-146-06", "name": "bias_and_no_lookahead_guards", "category": "GUARD", "description": "Lookahead, survivorship ve overfitting muhafizlarinin olusturulmasi."},
    {"rule_id": "SAFEGO-146-07", "name": "phase_147_handoff_preparation", "category": "HANDOFF", "description": "Phase 147 Walk-Forward ve OOS karsilastirma fazi icin guvenli devir hazirligi."},
]


def build_realistic_backtest_no_go_conditions(profile: RealisticBacktestProfile) -> List[Dict[str, Any]]:
    """Return all enforced NO-GO conditions."""
    return NO_GO_RULES


def build_realistic_backtest_safe_go_conditions(profile: RealisticBacktestProfile) -> List[Dict[str, Any]]:
    """Return all permitted SAFE-GO conditions."""
    return SAFE_GO_RULES


def build_realistic_backtest_safety_boundary(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build master safety boundaries DataFrame."""
    rows = []
    for r in NO_GO_RULES:
        rows.append(
            {
                "rule_id": r["rule_id"],
                "type": "NO-GO",
                "name": r["name"],
                "category": r["category"],
                "description": r["description"],
                "enforced": True,
                "non_signal": True,
            }
        )
    for r in SAFE_GO_RULES:
        rows.append(
            {
                "rule_id": r["rule_id"],
                "type": "SAFE-GO",
                "name": r["name"],
                "category": r["category"],
                "description": r["description"],
                "enforced": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_realistic_backtest_safety_boundary(df)
    return df, summary


def summarize_realistic_backtest_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundaries."""
    no_go = int((df["type"] == "NO-GO").sum()) if not df.empty else 0
    safe_go = int((df["type"] == "SAFE-GO").sum()) if not df.empty else 0
    return {
        "safety_status": "SECURE",
        "no_go_count": no_go,
        "safe_go_count": safe_go,
        "all_enforced": True,
        "live_trading_prohibited": True,
        "non_signal": True,
    }
