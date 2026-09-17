# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Scope Registry.

Registers all 16 research and offline boundary scopes for Phase 154.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

SCOPES_CATALOG = [
    ("offline_optimization_contracts", "Cevrimdisi Sozlesmeler", "Yalnizca yerel ve cevrimdisi calisma"),
    ("zero_live_trading", "Sifir Canli Islem", "Canli emir ve borsa baglantisi yok"),
    ("zero_broker_execution", "Sifir Broker Iletimi", "Broker API ve emir gonderimi yok"),
    ("zero_real_optimization", "Sifir Gercek Optimizasyon", "Sayisal optimizasyon motoru calistirilmaz"),
    ("zero_weight_generation", "Sifir Agirlik Uretimi", "Gercek portfoy agirliklari uretilmez"),
    ("zero_allocation_generation", "Sifir Sermaye Tahsisi", "Gercek sermaye tahsisati yapilmaz"),
    ("zero_rebalance_orders", "Sifir Rebalance Emri", "Rebalance ve lot emirleri uretilmez"),
    ("zero_metric_calculation", "Sifir Metrik Hesabi", "Gercek Sharpe, CVaR vb. hesaplanmaz"),
    ("objective_contract_mode", "Amac Sozlesme Modu", "Amac fonksiyonlari formullerle tanimlanir"),
    ("constraint_contract_mode", "Kisit Sozlesme Modu", "Tahsisat kisitlari sema olarak tutulur"),
    ("solver_placeholder_mode", "Cozucu Yer Tutucu Modu", "Cozuculer arayuz yer tutucusu olarak kalir"),
    ("efficient_frontier_placeholder_mode", "Etkin Sinir Yer Tutucusu", "Etkin sinir cizilmez, semalandirilir"),
    ("no_lookahead_enforcement", "No-Lookahead Muhafizi", "Zaman serisi sizintisi engellenir"),
    ("no_investment_advice", "Yatirim Tavsiyesi Yasagi", "Mevzuata uygun non-advisory calisma"),
    ("source_data_preservation", "Kaynak Veri Koruma", "Girdi dosyalari degistirilemez"),
    ("phase_155_handoff_ready", "Phase 155 Devir Kapsami", "Risk raporlama fazina devir hazirligi"),
]


def build_portfolio_optimization_scope_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build scope registry table."""
    records = []
    for scope_id, name, desc in SCOPES_CATALOG:
        records.append({
            "scope_id": scope_id,
            "scope_name": name,
            "description": desc,
            "is_enforced": True,
            "local_only": True,
            "non_production": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "scope_count": len(records),
        "all_scopes_enforced": True,
        "all_scopes_local_only": True,
    }
    return df, summary
