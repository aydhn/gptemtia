# -*- coding: utf-8 -*-
"""Phase 146: Backtest Scope Registry.

Defines in-scope and out-of-scope functional boundaries for Phase 146.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

SCOPE_ITEMS: List[Dict[str, Any]] = [
    # In-Scope Items
    {"scope_id": "SCP-146-01", "name": "Backtest Engine Contracts", "status": "IN_SCOPE", "description": "Olay tabanli, vektorize ve portfoy seviyesi motor sozlesmeleri."},
    {"scope_id": "SCP-146-02", "name": "Order Simulation Contracts", "status": "IN_SCOPE", "description": "Piyasa, limit, stop emir simule sozlesmeleri."},
    {"scope_id": "SCP-146-03", "name": "Fill & Price Model Contracts", "status": "IN_SCOPE", "description": "Gerceklesme fiyati ve gerceklesme kurallari sozlesmeleri."},
    {"scope_id": "SCP-146-04", "name": "Transaction Cost Models", "status": "IN_SCOPE", "description": "Komisyon, borsa ucreti, alis-satis farki sozlesmeleri."},
    {"scope_id": "SCP-146-05", "name": "Slippage Models", "status": "IN_SCOPE", "description": "Sabit, oynaklik ve likidite tabanli kayma modelleri."},
    {"scope_id": "SCP-146-06", "name": "Execution Realism Placeholders", "status": "IN_SCOPE", "description": "Piyasa etkisi, gecikme ve kismi gerceklesme yer tutuculari."},
    {"scope_id": "SCP-146-07", "name": "Accounting & Lifecycle Contracts", "status": "IN_SCOPE", "description": "PnL, nakit, teminat ve pozisyon yasam dongusu sozlesmeleri."},
    {"scope_id": "SCP-146-08", "name": "Bias & Lookahead Guards", "status": "IN_SCOPE", "description": "Lookahead, survivorship, data snooping ve overfitting muhafizlari."},
    {"scope_id": "SCP-146-09", "name": "Disabled Execution Reports", "status": "IN_SCOPE", "description": "Canli islem, broker, egitim ve tahmin yasaklari denetimi."},
    {"scope_id": "SCP-146-10", "name": "Phase 147 Handoff", "status": "IN_SCOPE", "description": "Walk-Forward ve OOS karsilastirma fazi icin devir hazirligi."},
    # Out-of-Scope Items
    {"scope_id": "SCP-146-11", "name": "Live Trading Execution", "status": "OUT_OF_SCOPE", "description": "Canli emir gonderimi ve gercek pozisyon yonetimi kesinlikle yasaktir."},
    {"scope_id": "SCP-146-12", "name": "Broker API Integration", "status": "OUT_OF_SCOPE", "description": "Araci kurum baglantisi veya emir rotalama yapilmaz."},
    {"scope_id": "SCP-146-13", "name": "Investment Advice", "status": "OUT_OF_SCOPE", "description": "Kesin AL/SAT veya pozisyon tavsiyesi uretilmez."},
    {"scope_id": "SCP-146-14", "name": "Real Backtest Execution", "status": "OUT_OF_SCOPE", "description": "Gercek portfoy uzerinde backtest calistirilmaz, contract duzeyindedir."},
    {"scope_id": "SCP-146-15", "name": "Optimizer Execution", "status": "OUT_OF_SCOPE", "description": "Strateji veya hiperparametre optimizasyonu calistirilmaz."},
    {"scope_id": "SCP-146-16", "name": "Walk-Forward Execution", "status": "OUT_OF_SCOPE", "description": "Walk-forward simulasyonu Phase 147 konusudur, bu fazda calistirilmaz."},
    {"scope_id": "SCP-146-17", "name": "Benchmark Comparison Execution", "status": "OUT_OF_SCOPE", "description": "Strateji karsilastirma benchmarklari bu fazda yurutulmez."},
    {"scope_id": "SCP-146-18", "name": "Stress Test & Monte Carlo Execution", "status": "OUT_OF_SCOPE", "description": "Stres testi (Phase 148) ve Monte Carlo (Phase 149) bu fazda yurutulmez."},
    {"scope_id": "SCP-146-19", "name": "Model Training & Inference", "status": "OUT_OF_SCOPE", "description": "Gercek ML model egitimi, fit ve tahmin calistirilmaz."},
    {"scope_id": "SCP-146-20", "name": "Performance Claims", "status": "OUT_OF_SCOPE", "description": "Getiri garantisi veya Sharpe/Win-rate performans iddialari yasaktir."},
    {"scope_id": "SCP-146-21", "name": "Model Deployment & Registry Write", "status": "OUT_OF_SCOPE", "description": "Model kayit defterine yazim ve uretim dagitimi yapilmaz."},
    {"scope_id": "SCP-146-22", "name": "News Full-Text Scraping", "status": "OUT_OF_SCOPE", "description": "Haber tam metni, makale govdesi ve kazima kesinlikle yasaktir."},
]


def build_backtest_scope_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of scope boundaries."""
    rows = []
    for item in SCOPE_ITEMS:
        rows.append(
            {
                "scope_id": item["scope_id"],
                "name": item["name"],
                "status": item["status"],
                "description": item["description"],
                "is_in_scope": item["status"] == "IN_SCOPE",
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_scopes(df)
    return df, summary


def summarize_backtest_scopes(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize scope breakdown."""
    in_scope_count = int((df["status"] == "IN_SCOPE").sum()) if not df.empty else 0
    out_scope_count = int((df["status"] == "OUT_OF_SCOPE").sum()) if not df.empty else 0
    return {
        "total_items": len(df),
        "in_scope_count": in_scope_count,
        "out_of_scope_count": out_scope_count,
        "live_trading_prohibited": True,
        "broker_integration_prohibited": True,
        "optimizer_prohibited": True,
        "walk_forward_prohibited": True,
        "benchmark_prohibited": True,
        "model_training_prohibited": True,
        "non_signal": True,
    }


summarize_backtest_scope_registry = summarize_backtest_scopes
