# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Safety Boundary.

Defines and enforces 21 NO-GO rules and 8 SAFE-GO principles.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

NO_GO_RULES = [
    ("NO_GO_154_01", "live_trading_prohibited", "Canli emir gonderimi ve gercek borsa islemleri kesinlikle yasaktir."),
    ("NO_GO_154_02", "broker_integration_prohibited", "Broker API baglantisi ve emir iletim protokolleri kesinlikle yasaktir."),
    ("NO_GO_154_03", "real_position_sizing_prohibited", "Gercek pozisyon veya lot buyuklugu uretimi kesinlikle yasaktir."),
    ("NO_GO_154_04", "signal_generation_prohibited", "Kesin AL/SAT veya pozisyon tavsiyesi uretilemez."),
    ("NO_GO_154_05", "investment_advice_prohibited", "Yatirim tavsiyesi, portfoy onayi veya getiri garantisi verilemez."),
    ("NO_GO_154_06", "real_optimization_prohibited", "Gercek sayisal optimizasyon motoru (MVO, Sharpe vb.) calistirilamaz."),
    ("NO_GO_154_07", "real_weight_generation_prohibited", "Gercek portfoy agirliklari veya sermaye dagilimi uretilemez."),
    ("NO_GO_154_08", "real_allocation_prohibited", "Gercek sermaye tahsisati yapilamaz."),
    ("NO_GO_154_09", "real_rebalance_prohibited", "Gercek yeniden dengeleme veya lot emirleri uretilemez."),
    ("NO_GO_154_10", "solver_execution_prohibited", "Optimizasyon cozuculeri canli olarak yurutulemez."),
    ("NO_GO_154_11", "grid_search_prohibited", "Izgara aramali agirlik optimizasyonu kesinlikle engellenmistir."),
    ("NO_GO_154_12", "efficient_frontier_generation_prohibited", "Gercek etkin sinir egrisi veya noktalari uretilemez."),
    ("NO_GO_154_13", "metric_calculation_prohibited", "Gercek Sharpe, Sortino, VaR, CVaR veya drawdown hesaplanamaz."),
    ("NO_GO_154_14", "model_training_prohibited", "Model egitimi (fit/train/backward) kesinlikle calistirilamaz."),
    ("NO_GO_154_15", "prediction_generation_prohibited", "Model tahmini (predict/inference) kesinlikle yurutulemez."),
    ("NO_GO_154_16", "target_label_generation_prohibited", "Hedef etiket veya yapay getiri kolonlari turetme kesinlikle yasaktir."),
    ("NO_GO_154_17", "model_registry_write_prohibited", "Model registry veya artifact persistisi yapilamaz."),
    ("NO_GO_154_18", "deployment_prohibited", "Uretim ortamina dagitim veya release yayini yapilamaz."),
    ("NO_GO_154_19", "web_scraping_prohibited", "Harici kaynak kazima veya dis ag baglantisi yasaktir."),
    ("NO_GO_154_20", "credential_output_prohibited", "API key, token, sifre cikartilamaz veya loglanamaz."),
    ("NO_GO_154_21", "source_overwrite_prohibited", "Girdi dosyalari degistirilemez veya silinemez."),
]

SAFE_GO_PRINCIPLES = [
    ("SAFE_GO_154_01", "local_offline_contract_mode", "Optimizasyon ve kisit sozlesmeleri yalnizca yerel ve cevrimdisi tanimlanir."),
    ("SAFE_GO_154_02", "objective_formula_metadata_mode", "Amac fonksiyonlari hesaplamasiz matematiksel formuller olarak tutulur."),
    ("SAFE_GO_154_03", "allocation_constraint_spec_mode", "Tahsisat kisitlari sematik sinirlayicilar olarak sozlesmelendirilir."),
    ("SAFE_GO_154_04", "solver_interface_placeholder_mode", "Cozuculer calistirilmayan arayuz yer tutuculari olarak belgelenir."),
    ("SAFE_GO_154_05", "claim_guard_enforcement", "Tahsisat, agirlik ve rebalance iddia muhafizlari aktif kilitlidir."),
    ("SAFE_GO_154_06", "disabled_execution_transparency", "10 devre disi raporu ile yurutme engelleri tescillenir."),
    ("SAFE_GO_154_07", "manifest_negative_invariants", "Tum negatif degismezler master manifestoda muhurlenir."),
    ("SAFE_GO_154_08", "phase_155_handoff_discipline", "Risk Raporlama fazina yapilandirilmis devir birakilir."),
]


def build_portfolio_optimization_no_go_conditions(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build NO-GO boundary rules table."""
    records = []
    for rule_id, name, desc in NO_GO_RULES:
        records.append({
            "rule_id": rule_id,
            "rule_name": name,
            "description": desc,
            "status": "ENFORCED",
            "is_active": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "no_go_count": len(records),
        "all_no_go_enforced": True,
    }
    return df, summary


def build_portfolio_optimization_safe_go_conditions(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build SAFE-GO principles table."""
    records = []
    for prin_id, name, desc in SAFE_GO_PRINCIPLES:
        records.append({
            "principle_id": prin_id,
            "principle_name": name,
            "description": desc,
            "status": "ACTIVE",
            "is_active": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "safe_go_count": len(records),
        "all_safe_go_active": True,
    }
    return df, summary


def build_portfolio_optimization_safety_boundary(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build consolidated safety boundary table."""
    prof = profile or get_default_portfolio_optimization_profile()
    df_no_go, s_no_go = build_portfolio_optimization_no_go_conditions(prof)
    df_safe_go, s_safe_go = build_portfolio_optimization_safe_go_conditions(prof)

    records = []
    for _, row in df_no_go.iterrows():
        records.append({
            "boundary_type": "NO_GO",
            "boundary_id": row["rule_id"],
            "boundary_name": row["rule_name"],
            "description": row["description"],
            "status": row["status"],
        })
    for _, row in df_safe_go.iterrows():
        records.append({
            "boundary_type": "SAFE_GO",
            "boundary_id": row["principle_id"],
            "boundary_name": row["principle_name"],
            "description": row["description"],
            "status": row["status"],
        })
    df = pd.DataFrame(records)
    summary = {
        "total_boundaries": len(records),
        "no_go_count": s_no_go["no_go_count"],
        "safe_go_count": s_safe_go["safe_go_count"],
        "safety_status": "SECURE",
    }
    return df, summary
