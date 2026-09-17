# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Domain Registry.

Registers all core domains within the realistic backtest and cost modeling block.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile
from advanced_realistic_backtest.realistic_backtest_labels import (
    ACCOUNTING_CONTRACT_DOMAIN,
    BACKTEST_SCOPE_DOMAIN,
    BIAS_GUARD_DOMAIN,
    COMMISSION_MODEL_DOMAIN,
    DEPENDENCY_DOMAIN,
    DISABLED_EXECUTION_DOMAIN,
    ENGINE_CONTRACT_DOMAIN,
    EVENT_DRIVEN_CONTRACT_DOMAIN,
    EXECUTION_PRICE_MODEL_DOMAIN,
    FEE_MODEL_DOMAIN,
    FILL_MODEL_DOMAIN,
    FINDING_DOMAIN,
    HEALTH_DOMAIN,
    LATENCY_PLACEHOLDER_DOMAIN,
    LIFECYCLE_CONTRACT_DOMAIN,
    LIQUIDITY_CONSTRAINT_PLACEHOLDER_DOMAIN,
    MANIFEST_DOMAIN,
    MARKET_IMPACT_PLACEHOLDER_DOMAIN,
    ORDER_SIMULATION_DOMAIN,
    PHASE_147_HANDOFF_DOMAIN,
    PORTFOLIO_CONTRACT_DOMAIN,
    READINESS_SCORE_DOMAIN,
    REALISTIC_BACKTEST_DOMAIN,
    REALISTIC_BACKTEST_PROFILE_DOMAIN,
    SAFETY_DOMAIN,
    SLIPPAGE_MODEL_DOMAIN,
    SPREAD_MODEL_DOMAIN,
    TRANSACTION_COST_DOMAIN,
    VALIDATION_DOMAIN,
    VALIDATION_EVIDENCE_DOMAIN,
    VECTORIZED_CONTRACT_DOMAIN,
)

ALL_DOMAINS: List[Dict[str, Any]] = [
    {"domain_name": REALISTIC_BACKTEST_PROFILE_DOMAIN, "category": "CONFIGURATION", "description": "Backtest profilleri ve guvenlik ayarlari."},
    {"domain_name": REALISTIC_BACKTEST_DOMAIN, "category": "FOUNDATION", "description": "Gercekci backtest mimarisi temel sozlesmeleri."},
    {"domain_name": BACKTEST_SCOPE_DOMAIN, "category": "SCOPE", "description": "Backtest kapsam ve sinir tanimlari."},
    {"domain_name": ENGINE_CONTRACT_DOMAIN, "category": "ENGINE", "description": "Motor sozlesmeleri (event-driven, vectorized, portfolio)."},
    {"domain_name": EVENT_DRIVEN_CONTRACT_DOMAIN, "category": "ENGINE", "description": "Olay tabanli backtest motor sozlesmesi."},
    {"domain_name": VECTORIZED_CONTRACT_DOMAIN, "category": "ENGINE", "description": "Vektorize matris tabanli backtest sozlesmesi."},
    {"domain_name": PORTFOLIO_CONTRACT_DOMAIN, "category": "ENGINE", "description": "Portfoy seviyesi sermaye ve pozisyon yonetimi sozlesmesi."},
    {"domain_name": ORDER_SIMULATION_DOMAIN, "category": "EXECUTION", "description": "Emir simule sozlesmeleri (market, limit, stop)."},
    {"domain_name": FILL_MODEL_DOMAIN, "category": "EXECUTION", "description": "Emir gerceklesme (fill) modeli sozlesmesi."},
    {"domain_name": EXECUTION_PRICE_MODEL_DOMAIN, "category": "EXECUTION", "description": "Islem fiyati belirleme modeli sozlesmesi."},
    {"domain_name": COMMISSION_MODEL_DOMAIN, "category": "TRANSACTION_COST", "description": "Komisyon hesaplama sozlesmeleri."},
    {"domain_name": FEE_MODEL_DOMAIN, "category": "TRANSACTION_COST", "description": "Borsa ve takas ucreti sozlesmeleri."},
    {"domain_name": SPREAD_MODEL_DOMAIN, "category": "TRANSACTION_COST", "description": "Alis-satis farki (spread) sozlesmeleri."},
    {"domain_name": SLIPPAGE_MODEL_DOMAIN, "category": "SLIPPAGE", "description": "Fiyat kaymasi (slippage) sozlesmeleri."},
    {"domain_name": MARKET_IMPACT_PLACEHOLDER_DOMAIN, "category": "EXECUTION_REALISM", "description": "Piyasa etki (market impact) yer tutuculari."},
    {"domain_name": LATENCY_PLACEHOLDER_DOMAIN, "category": "EXECUTION_REALISM", "description": "Gecikme (latency) yer tutuculari."},
    {"domain_name": LIQUIDITY_CONSTRAINT_PLACEHOLDER_DOMAIN, "category": "EXECUTION_REALISM", "description": "Likidite ve hacim kisiti yer tutuculari."},
    {"domain_name": TRANSACTION_COST_DOMAIN, "category": "TRANSACTION_COST", "description": "Toplam islem maliyeti bilesenleri."},
    {"domain_name": ACCOUNTING_CONTRACT_DOMAIN, "category": "ACCOUNTING", "description": "PnL, nakit ve teminat muhasebe sozlesmeleri."},
    {"domain_name": LIFECYCLE_CONTRACT_DOMAIN, "category": "LIFECYCLE", "description": "Islem ve pozisyon yasam dongusu sozlesmeleri."},
    {"domain_name": BIAS_GUARD_DOMAIN, "category": "GUARD", "description": "Lookahead, survivorship ve overfitting muhafizlari."},
    {"domain_name": DISABLED_EXECUTION_DOMAIN, "category": "SAFETY", "description": "Devre disi birakilmis yurutme kontrolleri."},
    {"domain_name": DEPENDENCY_DOMAIN, "category": "GOVERNANCE", "description": "Onceki fazlardan gelen bagimlilik sozlesmeleri."},
    {"domain_name": VALIDATION_EVIDENCE_DOMAIN, "category": "GOVERNANCE", "description": "Dogrulama ve kanit kayitlari."},
    {"domain_name": FINDING_DOMAIN, "category": "DIAGNOSTICS", "description": "Backtest sozlesme bulgulari ve inceleme maddeleri."},
    {"domain_name": READINESS_SCORE_DOMAIN, "category": "SCORING", "description": "Backtest hazirlik skorlamasi."},
    {"domain_name": MANIFEST_DOMAIN, "category": "MANIFEST", "description": "Phase 146 gercekci backtest manifestosu."},
    {"domain_name": HEALTH_DOMAIN, "category": "HEALTH", "description": "Sistem saglik denetimi altyapisi."},
    {"domain_name": VALIDATION_DOMAIN, "category": "VALIDATION", "description": "Kapsamli sozlesme ve yasakli iddia dogrulamasi."},
    {"domain_name": SAFETY_DOMAIN, "category": "SAFETY", "description": "NO-GO ve SAFE-GO guvenlik sinirlari."},
    {"domain_name": PHASE_147_HANDOFF_DOMAIN, "category": "HANDOFF", "description": "Phase 147 Walk-Forward ve OOS devir paketi."},
]


def build_realistic_backtest_domain_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of all realistic backtest domain definitions."""
    rows = []
    for d in ALL_DOMAINS:
        rows.append(
            {
                "domain_name": d["domain_name"],
                "category": d["category"],
                "description": d["description"],
                "is_active": True,
                "local_only": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_realistic_backtest_domains(df)
    return df, summary


def summarize_realistic_backtest_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize realistic backtest domains."""
    return {
        "total_domains": len(df),
        "total_categories": df["category"].nunique() if not df.empty else 0,
        "all_active": bool(df["is_active"].all()) if not df.empty else True,
        "all_local_only": True,
        "non_signal": True,
    }


summarize_realistic_backtest_domain_registry = summarize_realistic_backtest_domains
