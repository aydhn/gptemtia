# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Domain Registry.

Registers all 36 functional domains covering optimization, objectives, constraints,
solvers, frontiers, outputs, metrics, guards, disabled execution, and governance.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile
from .portfolio_optimization_labels import (
    PORTFOLIO_OPTIMIZATION_PROFILE_DOMAIN,
    PORTFOLIO_OPTIMIZATION_DOMAIN,
    PORTFOLIO_OPTIMIZATION_SCOPE_DOMAIN,
    OPTIMIZATION_CONTRACT_DOMAIN,
    OBJECTIVE_CONTRACT_DOMAIN,
    OBJECTIVE_PLACEHOLDER_DOMAIN,
    ALLOCATION_CONSTRAINT_DOMAIN,
    EXPOSURE_CONSTRAINT_DOMAIN,
    TURNOVER_CONSTRAINT_DOMAIN,
    RISK_BUDGET_CONSTRAINT_DOMAIN,
    VOLATILITY_CONSTRAINT_DOMAIN,
    DRAWDOWN_CONSTRAINT_DOMAIN,
    LEVERAGE_MARGIN_CONSTRAINT_DOMAIN,
    SOLVER_CONTRACT_DOMAIN,
    SOLVER_PLACEHOLDER_DOMAIN,
    EFFICIENT_FRONTIER_PLACEHOLDER_DOMAIN,
    OUTPUT_CONTRACT_DOMAIN,
    METRIC_PLACEHOLDER_DOMAIN,
    DEPENDENCY_DOMAIN,
    CLAIM_GUARD_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    FINDING_DOMAIN,
    READINESS_SCORE_DOMAIN,
    MANIFEST_DOMAIN,
    HEALTH_DOMAIN,
    VALIDATION_DOMAIN,
    SAFETY_DOMAIN,
    PHASE_155_HANDOFF_DOMAIN,
)

DOMAINS_CATALOG = [
    (PORTFOLIO_OPTIMIZATION_PROFILE_DOMAIN, "Profil Yonetimi", "Yerel ve cevrimdisi portfoy optimizasyon profil tescili"),
    (PORTFOLIO_OPTIMIZATION_DOMAIN, "Portfoy Optimizasyonu", "Portfoy optimizasyon sozlesme ve mimari etki alani"),
    (PORTFOLIO_OPTIMIZATION_SCOPE_DOMAIN, "Arastirma Kapsami", "Cevrimdisi calisma ve arastirma sinirlari"),
    (OPTIMIZATION_CONTRACT_DOMAIN, "Optimizasyon Sozlesmeleri", "Optimizasyon problem tanim sozlesmeleri"),
    (OBJECTIVE_CONTRACT_DOMAIN, "Amac Fonksiyonu Sozlesmeleri", "Optimizasyon amac sozlesmeleri"),
    (OBJECTIVE_PLACEHOLDER_DOMAIN, "Amac Yer Tutuculari", "Mean-variance, Sharpe, CVaR vb. yer tutuculari"),
    (ALLOCATION_CONSTRAINT_DOMAIN, "Tahsisat Kisit Sozlesmeleri", "Portfoy tahsisat ve agirlik kisitlari"),
    (EXPOSURE_CONSTRAINT_DOMAIN, "Maruziyet Kisitlari", "Brut ve net maruziyet kisit yer tutuculari"),
    (TURNOVER_CONSTRAINT_DOMAIN, "Devir Hizi Kisitlari", "Portfoy devir hizi tavan kisitlari"),
    (RISK_BUDGET_CONSTRAINT_DOMAIN, "Risk Butcesi Kisitlari", "Risk butcesi uyum kisitlari"),
    (VOLATILITY_CONSTRAINT_DOMAIN, "Volatilite Kisitlari", "Hedef ve tavan volatilite kisitlari"),
    (DRAWDOWN_CONSTRAINT_DOMAIN, "Dususe Duyarli Kisitlar", "Maksimum drawdown bütçesi kisitlari"),
    (LEVERAGE_MARGIN_CONSTRAINT_DOMAIN, "Kaldirac ve Teminat Kisitlari", "Maksimum kaldirac ve teminat kisitlari"),
    (SOLVER_CONTRACT_DOMAIN, "Cozucu Sozlesmeleri", "Optimizasyon cozucu arayuz sozlesmeleri"),
    (SOLVER_PLACEHOLDER_DOMAIN, "Cozucu Yer Tutuculari", "Konveks ve sezgisel cozucu yer tutuculari"),
    (EFFICIENT_FRONTIER_PLACEHOLDER_DOMAIN, "Etkin Sinir Yer Tutuculari", "Efficient frontier sema ve yer tutuculari"),
    (OUTPUT_CONTRACT_DOMAIN, "Cikti Sozlesmeleri", "Optimizasyon sonuc ve rebalance cikti semalari"),
    (METRIC_PLACEHOLDER_DOMAIN, "Metrik Yer Tutuculari", "Hesaplamasiz metrik ve formuller"),
    (DEPENDENCY_DOMAIN, "Yukari Akis Bagimliliklari", "Phase 153-130 faz bagimlilik tescili"),
    (CLAIM_GUARD_DOMAIN, "Iddia Muhafizlari", "Tahsisat, agirlik ve rebalance iddia engelleri"),
    (DISABLED_EXECUTION_DOMAIN, "Devre Disi Yurutme", "Gercek yurutme engelleme tescili"),
    (FINDING_DOMAIN, "Teshis Bulgulari", "Teshis bulgulari ve otomatik aksiyon yasaklari"),
    (READINESS_SCORE_DOMAIN, "Hazirlik Puani", "1.00 sozlesme hazirlik skoru"),
    (MANIFEST_DOMAIN, "Master Manifesto", "Bütünlük ve negatif degismez manifestosu"),
    (HEALTH_DOMAIN, "Sistem Saglik Kontrolu", "Modul ve bagimlilik saglik testi"),
    (VALIDATION_DOMAIN, "Validasyon Raporu", "6 asamali sozlesme dogrulama"),
    (SAFETY_DOMAIN, "Guvenlik Sinirlari", "21 NO-GO ve 8 SAFE-GO kurallari"),
    (PHASE_155_HANDOFF_DOMAIN, "Phase 155 Devri", "Phase 155 Risk Reporting devir paketi"),
    ("mean_variance_objective_domain", "Mean-Variance Amac", "Ortalama-varyans optimizasyon amaci"),
    ("minimum_variance_objective_domain", "Min-Variance Amac", "Minimum varyans optimizasyon amaci"),
    ("maximum_sharpe_objective_domain", "Max-Sharpe Amac", "Maksimum Sharpe orani amaci"),
    ("risk_parity_objective_domain", "Risk Parity Amac", "Risk paritesi dengeleme amaci"),
    ("cvar_objective_domain", "CVaR Amac", "Kosullu Riske Maruz Deger amaci"),
    ("drawdown_minimization_domain", "Drawdown Minimizasyonu", "Maksimum drawdown minimizasyon amaci"),
    ("cost_slippage_aware_domain", "Maliyet/Kayma Duyarli", "Maliyet ve kayma duyarlilik amaci"),
    ("regime_aware_optimization_domain", "Rejim Duyarli Optimizasyon", "Piyasa rejimi duyarlilik amaci"),
]


def build_portfolio_optimization_domain_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build functional domain registry table."""
    records = []
    for domain_id, name, desc in DOMAINS_CATALOG:
        records.append({
            "domain_id": domain_id,
            "domain_name": name,
            "description": desc,
            "is_active": True,
            "local_only": True,
            "non_production": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "domain_count": len(records),
        "all_domains_active": True,
        "all_domains_local_only": True,
    }
    return df, summary
