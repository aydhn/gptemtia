# -*- coding: utf-8 -*-
"""Phase 154: Optimization Objective Contracts.

Defines mathematical formulation contracts for portfolio optimization objectives.
Strictly formula metadata mode, zero numerical evaluation.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

OBJECTIVE_CONTRACTS_CATALOG = [
    (
        "mean_variance_objective",
        "mean_variance",
        "Markowitz ortalama-varyans amaci",
        r"\max_w (w^T \mu - \frac{\lambda}{2} w^T \Sigma w)",
        "expected_return_and_variance",
        "covariance_matrix",
    ),
    (
        "min_variance_objective",
        "minimum_variance",
        "Minimum portfoy varyansi amaci",
        r"\min_w (w^T \Sigma w)",
        "portfolio_variance",
        "covariance_matrix",
    ),
    (
        "max_sharpe_objective",
        "maximum_sharpe",
        "Maksimum Sharpe orani amaci",
        r"\max_w \frac{w^T \mu - r_f}{\sqrt{w^T \Sigma w}}",
        "sharpe_ratio",
        "covariance_matrix",
    ),
    (
        "risk_parity_objective",
        "risk_parity",
        "Risk paritesi (esit risk katkisi) amaci",
        r"\min_w \sum_{i=1}^N \sum_{j=1}^N (w_i (\Sigma w)_i - w_j (\Sigma w)_j)^2",
        "risk_contribution_dispersion",
        "marginal_risk_contribution",
    ),
    (
        "cvar_objective",
        "cvar",
        "Kosullu Riske Maruz Deger (CVaR / Expected Shortfall) amaci",
        r"\min_{w, \gamma} (\gamma + \frac{1}{1-\alpha} \frac{1}{T} \sum_{t=1}^T [-w^T r_t - \gamma]^+)",
        "cvar_tail_loss",
        "historical_returns_distribution",
    ),
    (
        "drawdown_minimization_objective",
        "drawdown_minimization",
        "Maksimum portfoy dususunu minimize etme amaci",
        r"\min_w \max_{t} (M_t - P_t(w))",
        "maximum_drawdown",
        "path_dependent_equity_curve",
    ),
    (
        "turnover_minimization_objective",
        "turnover_minimization",
        "Portfoy devir hizini (turnover) minimize etme amaci",
        r"\min_w \sum_{i=1}^N |w_i - w_{i,0}|",
        "portfolio_turnover",
        "rebalance_vector",
    ),
    (
        "cost_aware_objective",
        "cost_aware",
        "Islem maliyeti duzeltmeli getiri optimizasyon amaci",
        r"\max_w (w^T \mu - \sum_{i=1}^N c_i |w_i - w_{i,0}| - \frac{\lambda}{2} w^T \Sigma w)",
        "cost_adjusted_utility",
        "transaction_cost_profile",
    ),
    (
        "slippage_aware_objective",
        "slippage_aware",
        "Piyasa kaymasi (slippage) duzeltmeli optimizasyon amaci",
        r"\max_w (w^T \mu - \sum_{i=1}^N \eta_i |w_i - w_{i,0}|^{1.5} - \frac{\lambda}{2} w^T \Sigma w)",
        "slippage_adjusted_utility",
        "slippage_impact_model",
    ),
    (
        "regime_aware_objective",
        "regime_aware",
        "Rejim sartlandirmali optimizasyon amaci",
        r"\max_w (w^T \mu_{S_t} - \frac{\lambda_{S_t}}{2} w^T \Sigma_{S_t} w)",
        "regime_conditioned_utility",
        "regime_state_covariance",
    ),
    (
        "robust_optimization_objective",
        "robust_optimization",
        "Kotu senaryo (worst-case) saglam optimizasyon amaci",
        r"\max_w \min_{\mu \in \mathcal{U}} (w^T \mu - \frac{\lambda}{2} w^T \Sigma w)",
        "worst_case_utility",
        "uncertainty_set",
    ),
]


def build_optimization_objective_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build registered optimization objectives table."""
    records = []
    for (
        name,
        obj_type,
        desc,
        formulation,
        target_var,
        risk_ref,
    ) in OBJECTIVE_CONTRACTS_CATALOG:
        records.append({
            "objective_name": name,
            "objective_type": obj_type,
            "description": desc,
            "mathematical_formulation": formulation,
            "target_variable": target_var,
            "risk_metric_ref": risk_ref,
            "is_placeholder": True,
            "actual_objective_calculated": None,
            "is_calculated": False,
            "allows_execution": False,
            "manual_review_required": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "objective_count": len(records),
        "all_objectives_placeholders": True,
        "zero_objective_calculated": True,
        "zero_execution_allowed": True,
    }
    return df, summary


def validate_optimization_objective_contract(contract: dict) -> dict:
    """Ensure objective contract does not allow execution or return calculated values."""
    is_valid = True
    reasons = []
    if contract.get("allows_execution", False) is True:
        is_valid = False
        reasons.append("allows_execution must be False")
    if contract.get("is_calculated", False) is True:
        is_valid = False
        reasons.append("is_calculated must be False")
    if contract.get("actual_objective_calculated") is not None:
        is_valid = False
        reasons.append("actual_objective_calculated must be None")
    return {
        "objective_name": contract.get("objective_name", "unknown"),
        "is_valid": is_valid,
        "reasons": reasons,
    }


def summarize_optimization_objective_contracts(df: pd.DataFrame) -> Dict:
    """Summarize objective contract registry."""
    return {
        "objective_count": len(df),
        "objectives": df["objective_name"].tolist() if "objective_name" in df.columns else [],
        "is_placeholder_all": bool((df["is_placeholder"] == True).all()) if "is_placeholder" in df.columns else False,
        "zero_calculated_all": bool((df["is_calculated"] == False).all()) if "is_calculated" in df.columns else False,
    }
