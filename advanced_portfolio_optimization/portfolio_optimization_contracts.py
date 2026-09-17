# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Contracts.

Defines 11 standard portfolio optimization contract specifications.
Strictly offline, local, non-production, and zero real execution.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

OPTIMIZATION_CONTRACTS_CATALOG = [
    (
        "local_portfolio_optimization_contract",
        "local_offline_generic",
        "Temel yerel/cevrimdisi portfoy optimizasyon sozlesmesi",
        "mean_variance_objective",
        "long_only_and_max_weight",
        "convex_solver",
    ),
    (
        "mean_variance_optimization_contract",
        "mean_variance",
        "Markowitz ortalama-varyans optimizasyon sozlesmesi",
        "mean_variance_objective",
        "gross_exposure_and_box_weights",
        "convex_solver",
    ),
    (
        "minimum_variance_optimization_contract",
        "minimum_variance",
        "Minimum varyans (en dusuk portfoy oynakligi) sozlesmesi",
        "min_variance_objective",
        "long_only_full_investment",
        "convex_solver",
    ),
    (
        "maximum_sharpe_optimization_contract",
        "maximum_sharpe",
        "Maksimum Sharpe orani (tanjant portfoy) sozlesmesi",
        "max_sharpe_objective",
        "long_only_and_budget_constraints",
        "convex_solver",
    ),
    (
        "risk_parity_optimization_contract",
        "risk_parity",
        "Risk paritesi (esit risk katkisi) optimizasyon sozlesmesi",
        "risk_parity_objective",
        "positive_weights_and_risk_budget",
        "heuristic_solver",
    ),
    (
        "cvar_optimization_contract",
        "cvar",
        "Kosullu Riske Maruz Deger (CVaR / Expected Shortfall) minimizasyon sozlesmesi",
        "cvar_objective",
        "cvar_loss_threshold_and_weights",
        "convex_solver",
    ),
    (
        "drawdown_aware_optimization_contract",
        "drawdown_aware",
        "Dususe duyarli (maximum drawdown kısıtlı) optimizasyon sozlesmesi",
        "drawdown_minimization_objective",
        "drawdown_budget_and_exposure",
        "heuristic_solver",
    ),
    (
        "cost_slippage_aware_optimization_contract",
        "cost_slippage_aware",
        "Islem maliyeti ve piyasa kaymasi duzeltmeli optimizasyon sozlesmesi",
        "cost_and_slippage_aware_objective",
        "turnover_and_cost_ceiling",
        "convex_solver",
    ),
    (
        "regime_aware_optimization_contract",
        "regime_aware",
        "Piyasa rejimi baglamina duyarlı portfoy optimizasyon sozlesmesi",
        "regime_aware_objective",
        "regime_specific_exposure_limits",
        "heuristic_solver",
    ),
    (
        "robust_optimization_contract",
        "robust_optimization",
        "Belirsizlik kumesi duyarlı saglam (robust) optimizasyon sozlesmesi",
        "robust_optimization_objective",
        "ellipsoidal_uncertainty_bounds",
        "convex_solver",
    ),
    (
        "governance_aware_optimization_contract",
        "governance_aware",
        "Model yonetisim ve denetim standartlarina uyumlu optimizasyon sozlesmesi",
        "governance_aligned_objective",
        "comprehensive_risk_limits",
        "convex_solver",
    ),
]


def build_portfolio_optimization_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build registered optimization contracts table."""
    records = []
    for (
        c_name,
        c_family,
        desc,
        obj_ref,
        con_ref,
        solv_ref,
    ) in OPTIMIZATION_CONTRACTS_CATALOG:
        records.append({
            "contract_name": c_name,
            "optimization_family": c_family,
            "description": desc,
            "portfolio_construction_ref": "advanced_portfolio_construction_v153",
            "risk_budget_ref": "risk_budget_contract_v153",
            "allocation_constraint_ref": con_ref,
            "objective_ref": obj_ref,
            "solver_ref": solv_ref,
            "backtest_acceptance_ref": "advanced_backtest_acceptance_v152",
            "benchmark_evaluation_ref": "advanced_benchmark_evaluation_v151",
            "model_governance_ref": "advanced_model_governance_v145",
            "regime_context_ref": "advanced_regime_acceptance_v135",
            "featurestore_ref": "featurestore_v2_v134",
            "no_lookahead_guard_ref": "optimization_no_lookahead_guards",
            "investment_advice_guard_ref": "optimization_investment_advice_guards",
            "portfolio_optimization_allowed": False,
            "solver_execution_allowed": False,
            "weight_generation_allowed": False,
            "allocation_generation_allowed": False,
            "rebalance_generation_allowed": False,
            "order_generation_allowed": False,
            "optimizer_execution_allowed": False,
            "live_trading_allowed": False,
            "broker_execution_allowed": False,
            "signal_generation_allowed": False,
            "manual_review_required": True,
            "is_contract_valid": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "contract_count": len(records),
        "all_contracts_disallow_optimization": True,
        "all_contracts_disallow_weight_generation": True,
        "all_contracts_disallow_live_trading": True,
        "manual_review_required_all": True,
    }
    return df, summary


def validate_portfolio_optimization_contract(contract: dict) -> dict:
    """Validate that an individual optimization contract enforces negative invariants."""
    is_valid = True
    reasons = []

    if contract.get("portfolio_optimization_allowed", False) is True:
        is_valid = False
        reasons.append("portfolio_optimization_allowed must be False")

    if contract.get("weight_generation_allowed", False) is True:
        is_valid = False
        reasons.append("weight_generation_allowed must be False")

    if contract.get("allocation_generation_allowed", False) is True:
        is_valid = False
        reasons.append("allocation_generation_allowed must be False")

    if contract.get("solver_execution_allowed", False) is True:
        is_valid = False
        reasons.append("solver_execution_allowed must be False")

    if contract.get("live_trading_allowed", False) is True:
        is_valid = False
        reasons.append("live_trading_allowed must be False")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "reasons": reasons,
    }


def summarize_portfolio_optimization_contracts(df: pd.DataFrame) -> Dict:
    """Summarize the optimization contract registry."""
    return {
        "contract_count": len(df),
        "contracts": df["contract_name"].tolist() if "contract_name" in df.columns else [],
        "zero_weight_generation_all": bool((df["weight_generation_allowed"] == False).all()) if "weight_generation_allowed" in df.columns else False,
        "zero_optimization_all": bool((df["portfolio_optimization_allowed"] == False).all()) if "portfolio_optimization_allowed" in df.columns else False,
    }
