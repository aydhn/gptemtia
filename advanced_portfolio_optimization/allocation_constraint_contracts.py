# -*- coding: utf-8 -*-
"""Phase 154: Allocation Constraint Contracts.

Defines 22 standardized allocation constraint specifications.
Strictly offline, local, formula metadata mode, zero live enforcement.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

CONSTRAINTS_CATALOG = [
    ("long_only_constraint", "weight", "Sadece uzun pozisyon kisiti", r"w_i \ge 0, \forall i", "lower_bound"),
    ("max_weight_constraint", "weight", "Maksimum varlik agirligi tavan kisiti", r"w_i \le w_{\max}, \forall i", "upper_bound"),
    ("min_weight_constraint", "weight", "Minimum varlik agirligi taban kisiti", r"w_i \ge w_{\min}, \forall i", "lower_bound"),
    ("group_weight_constraint", "weight", "Sektor veya varlik grubu agirlik kisiti", r"\sum_{i \in G_k} w_i \le W_{G_k}", "upper_bound"),
    ("asset_count_constraint", "cardinality", "Portfoy aktif varlik adedi kisiti", r"\sum_{i=1}^N \mathbf{1}_{\{w_i > 0\}} \le K", "cardinality_bound"),
    ("concentration_constraint", "concentration", "Portfoy yogunlasma (Herfindahl) kisiti", r"\sum_{i=1}^N w_i^2 \le HHI_{\max}", "upper_bound"),
    ("exposure_constraint", "exposure", "Toplam portfoy maruziyet kisiti", r"\sum_{i=1}^N w_i = 1", "equality"),
    ("gross_exposure_constraint", "exposure", "Brut maruziyet kisiti", r"\sum_{i=1}^N |w_i| \le L_{\text{gross}}", "upper_bound"),
    ("net_exposure_constraint", "exposure", "Net maruziyet kisiti", r"|\sum_{i=1}^N w_i| \le L_{\text{net}}", "box"),
    ("currency_exposure_constraint", "currency", "Para birimi maruziyet tavan kisiti", r"\sum_{i \in \text{CCY}_c} |w_i| \le L_{\text{ccy}}", "upper_bound"),
    ("cross_asset_exposure_constraint", "cross_asset", "Capraz varlik sinifi maruziyet kisiti", r"\sum_{i \in \text{AssetClass}_m} w_i \le L_{\text{class}}", "upper_bound"),
    ("correlation_constraint", "correlation", "Varliklar arasi maksimum korelasyon kisiti", r"\text{Corr}(i, j) \le \rho_{\max}", "pairwise_bound"),
    ("liquidity_constraint", "liquidity", "Likidite ve ortalama gunluk hacim (ADV) kisiti", r"w_i \cdot V_{\text{port}} \le \alpha \cdot \text{ADV}_i", "upper_bound"),
    ("turnover_constraint", "turnover", "Portfoy devir hizi tavan kisiti", r"\sum_{i=1}^N |w_i - w_{i,0}| \le \tau_{\max}", "upper_bound"),
    ("transaction_cost_constraint", "cost", "Toplam islem maliyeti tavan kisiti", r"\sum_{i=1}^N c_i |w_i - w_{i,0}| \le C_{\max}", "upper_bound"),
    ("slippage_constraint", "slippage", "Piyasa kaymasi etkisi tavan kisiti", r"\sum_{i=1}^N \eta_i |w_i - w_{i,0}|^{1.5} \le S_{\max}", "upper_bound"),
    ("risk_budget_constraint", "risk_budget", "Risk butcesi uyum kisiti", r"\frac{w_i (\Sigma w)_i}{w^T \Sigma w} \le b_i", "upper_bound"),
    ("volatility_constraint", "volatility", "Portfoy yillik volatilite tavan kisiti", r"\sqrt{w^T \Sigma w} \le \sigma_{\max}", "upper_bound"),
    ("drawdown_constraint", "drawdown", "Maksimum portfoy dusus butcesi kisiti", r"\text{MaxDD}(w) \le \text{DD}_{\max}", "upper_bound"),
    ("leverage_constraint", "leverage", "Maksimum kaldirac tavan kisiti", r"\sum_{i=1}^N |w_i| \le 1.0", "upper_bound"),
    ("margin_constraint", "margin", "Baslangic teminati tavan kisiti", r"\sum_{i=1}^N m_i |w_i| \le M_{\max}", "upper_bound"),
    ("rebalance_constraint", "rebalance", "Yeniden dengeleme esik kisiti", r"|w_i - w_{i,0}| > \delta_{\text{reb}}", "trigger_bound"),
]


def build_allocation_constraint_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build registered allocation constraint contracts table."""
    records = []
    for name, family, desc, formulation, bound_type in CONSTRAINTS_CATALOG:
        records.append({
            "constraint_name": name,
            "constraint_family": family,
            "description": desc,
            "mathematical_formulation": formulation,
            "bound_type": bound_type,
            "is_placeholder": True,
            "is_enforced_live": False,
            "allows_weight_generation": False,
            "allows_allocation_generation": False,
            "manual_review_required": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "constraint_count": len(records),
        "all_constraints_placeholders": True,
        "zero_live_enforcement": True,
        "zero_weight_generation": True,
    }
    return df, summary


def validate_allocation_constraint_contract(contract: dict) -> dict:
    """Validate allocation constraint contract invariants."""
    is_valid = True
    reasons = []
    if contract.get("is_enforced_live", False) is True:
        is_valid = False
        reasons.append("is_enforced_live must be False")
    if contract.get("allows_weight_generation", False) is True:
        is_valid = False
        reasons.append("allows_weight_generation must be False")
    if contract.get("allows_allocation_generation", False) is True:
        is_valid = False
        reasons.append("allows_allocation_generation must be False")
    return {
        "constraint_name": contract.get("constraint_name", "unknown"),
        "is_valid": is_valid,
        "reasons": reasons,
    }


def summarize_allocation_constraint_contracts(df: pd.DataFrame) -> Dict:
    """Summarize constraint contract registry."""
    return {
        "constraint_count": len(df),
        "constraints": df["constraint_name"].tolist() if "constraint_name" in df.columns else [],
        "is_placeholder_all": bool((df["is_placeholder"] == True).all()) if "is_placeholder" in df.columns else False,
        "zero_live_enforced_all": bool((df["is_enforced_live"] == False).all()) if "is_enforced_live" in df.columns else False,
    }
