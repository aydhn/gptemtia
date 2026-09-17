# -*- coding: utf-8 -*-
"""Phase 153: Position Sizing Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    POSITION_SIZING_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


SIZING_CONTRACT_TEMPLATES = [
    {
        "sizing_name": "local_position_sizing_contract",
        "sizing_family": "local_baseline_sizing",
        "risk_budget_ref": "RISK_BUDGET_BASELINE",
        "exposure_limit_ref": "EXPOSURE_LIMIT_BASELINE",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_BASELINE",
        "volatility_budget_ref": "VOL_BUDGET_BASELINE",
        "drawdown_budget_ref": "DD_BUDGET_BASELINE",
        "liquidity_limit_ref": "LIQ_LIMIT_BASELINE",
        "transaction_cost_ref": "COST_REF_BASELINE",
        "slippage_model_ref": "SLIPPAGE_REF_BASELINE",
        "description": "Temel yerel pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "fixed_fractional_sizing_contract",
        "sizing_family": "fixed_fractional",
        "risk_budget_ref": "RISK_BUDGET_FRACTIONAL",
        "exposure_limit_ref": "EXPOSURE_LIMIT_FRACTIONAL",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_FRACTIONAL",
        "volatility_budget_ref": "VOL_BUDGET_FRACTIONAL",
        "drawdown_budget_ref": "DD_BUDGET_FRACTIONAL",
        "liquidity_limit_ref": "LIQ_LIMIT_FRACTIONAL",
        "transaction_cost_ref": "COST_REF_FRACTIONAL",
        "slippage_model_ref": "SLIPPAGE_REF_FRACTIONAL",
        "description": "Sabit fraksiyonel pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "volatility_targeting_sizing_contract",
        "sizing_family": "volatility_targeting",
        "risk_budget_ref": "RISK_BUDGET_VOL_TARGET",
        "exposure_limit_ref": "EXPOSURE_LIMIT_VOL_TARGET",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_VOL_TARGET",
        "volatility_budget_ref": "VOL_BUDGET_TARGET_15PCT",
        "drawdown_budget_ref": "DD_BUDGET_VOL_TARGET",
        "liquidity_limit_ref": "LIQ_LIMIT_VOL_TARGET",
        "transaction_cost_ref": "COST_REF_VOL_TARGET",
        "slippage_model_ref": "SLIPPAGE_REF_VOL_TARGET",
        "description": "Volatilite hedefli pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "risk_budget_sizing_contract",
        "sizing_family": "risk_budget_allocated",
        "risk_budget_ref": "RISK_BUDGET_ALLOCATED",
        "exposure_limit_ref": "EXPOSURE_LIMIT_RISK_BUDGET",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_RISK_BUDGET",
        "volatility_budget_ref": "VOL_BUDGET_ALLOCATED",
        "drawdown_budget_ref": "DD_BUDGET_ALLOCATED",
        "liquidity_limit_ref": "LIQ_LIMIT_RISK_BUDGET",
        "transaction_cost_ref": "COST_REF_RISK_BUDGET",
        "slippage_model_ref": "SLIPPAGE_REF_RISK_BUDGET",
        "description": "Risk butcesi tabanli pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "drawdown_aware_sizing_contract",
        "sizing_family": "drawdown_adaptive",
        "risk_budget_ref": "RISK_BUDGET_DD_ADAPTIVE",
        "exposure_limit_ref": "EXPOSURE_LIMIT_DD_ADAPTIVE",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_DD_ADAPTIVE",
        "volatility_budget_ref": "VOL_BUDGET_DD_ADAPTIVE",
        "drawdown_budget_ref": "DD_BUDGET_MAX_10PCT",
        "liquidity_limit_ref": "LIQ_LIMIT_DD_ADAPTIVE",
        "transaction_cost_ref": "COST_REF_DD_ADAPTIVE",
        "slippage_model_ref": "SLIPPAGE_REF_DD_ADAPTIVE",
        "description": "Cekilme duyarli pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "confidence_aware_sizing_contract",
        "sizing_family": "confidence_scaled",
        "risk_budget_ref": "RISK_BUDGET_CONFIDENCE",
        "exposure_limit_ref": "EXPOSURE_LIMIT_CONFIDENCE",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_CONFIDENCE",
        "volatility_budget_ref": "VOL_BUDGET_CONFIDENCE",
        "drawdown_budget_ref": "DD_BUDGET_CONFIDENCE",
        "liquidity_limit_ref": "LIQ_LIMIT_CONFIDENCE",
        "transaction_cost_ref": "COST_REF_CONFIDENCE",
        "slippage_model_ref": "SLIPPAGE_REF_CONFIDENCE",
        "description": "Model guven olcutu duyarli pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "regime_aware_sizing_contract",
        "sizing_family": "regime_scaled",
        "risk_budget_ref": "RISK_BUDGET_REGIME_SCALED",
        "exposure_limit_ref": "EXPOSURE_LIMIT_REGIME_SCALED",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_REGIME_SCALED",
        "volatility_budget_ref": "VOL_BUDGET_REGIME_SCALED",
        "drawdown_budget_ref": "DD_BUDGET_REGIME_SCALED",
        "liquidity_limit_ref": "LIQ_LIMIT_REGIME_SCALED",
        "transaction_cost_ref": "COST_REF_REGIME_SCALED",
        "slippage_model_ref": "SLIPPAGE_REF_REGIME_SCALED",
        "description": "Rejim kosullu pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "liquidity_aware_sizing_contract",
        "sizing_family": "liquidity_constrained",
        "risk_budget_ref": "RISK_BUDGET_LIQUIDITY",
        "exposure_limit_ref": "EXPOSURE_LIMIT_LIQUIDITY",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_LIQUIDITY",
        "volatility_budget_ref": "VOL_BUDGET_LIQUIDITY",
        "drawdown_budget_ref": "DD_BUDGET_LIQUIDITY",
        "liquidity_limit_ref": "LIQ_LIMIT_ADV_1PCT",
        "transaction_cost_ref": "COST_REF_LIQUIDITY",
        "slippage_model_ref": "SLIPPAGE_REF_LIQUIDITY",
        "description": "Likidite kisitli pozisyon boyutlandirma sozlesmesi.",
    },
    {
        "sizing_name": "cost_slippage_aware_sizing_contract",
        "sizing_family": "friction_constrained",
        "risk_budget_ref": "RISK_BUDGET_FRICTION",
        "exposure_limit_ref": "EXPOSURE_LIMIT_FRICTION",
        "concentration_limit_ref": "CONCENTRATION_LIMIT_FRICTION",
        "volatility_budget_ref": "VOL_BUDGET_FRICTION",
        "drawdown_budget_ref": "DD_BUDGET_FRICTION",
        "liquidity_limit_ref": "LIQ_LIMIT_FRICTION",
        "transaction_cost_ref": "COST_REF_FRICTION",
        "slippage_model_ref": "SLIPPAGE_REF_FRICTION",
        "description": "Maliyet ve kayma kisitli pozisyon boyutlandirma sozlesmesi.",
    },
]


def build_position_sizing_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for position sizing contracts."""
    rows = []
    for item in SIZING_CONTRACT_TEMPLATES:
        rows.append({
            "sizing_name": item["sizing_name"],
            "sizing_family": item["sizing_family"],
            "risk_budget_ref": item["risk_budget_ref"],
            "exposure_limit_ref": item["exposure_limit_ref"],
            "concentration_limit_ref": item["concentration_limit_ref"],
            "volatility_budget_ref": item["volatility_budget_ref"],
            "drawdown_budget_ref": item["drawdown_budget_ref"],
            "liquidity_limit_ref": item["liquidity_limit_ref"],
            "transaction_cost_ref": item["transaction_cost_ref"],
            "slippage_model_ref": item["slippage_model_ref"],
            "description": item["description"],
            "position_sizing_allowed": profile.allow_position_sizing,
            "capital_allocation_allowed": profile.allow_capital_allocation,
            "order_generation_allowed": profile.allow_order_generation,
            "broker_execution_allowed": profile.allow_broker_integration,
            "investment_advice_allowed": profile.allow_investment_advice,
            "manual_review_required": True,
            "contract_only": True,
            "non_production": True,
            "broker_ready": False,
            "production_ready": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": POSITION_SIZING_DOMAIN,
        "active_profile": profile.profile_name,
        "total_contracts": len(df),
        "all_sizing_blocked": not any(df["position_sizing_allowed"]),
        "all_allocation_blocked": not any(df["capital_allocation_allowed"]),
        "all_order_generation_blocked": not any(df["order_generation_allowed"]),
        "all_broker_execution_blocked": not any(df["broker_execution_allowed"]),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_position_sizing_contract(contract: Dict) -> Dict:
    """Validate single position sizing contract."""
    is_valid = True
    errors = []

    if contract.get("position_sizing_allowed", False):
        is_valid = False
        errors.append("position_sizing_allowed must be False.")
    if contract.get("capital_allocation_allowed", False):
        is_valid = False
        errors.append("capital_allocation_allowed must be False.")
    if contract.get("order_generation_allowed", False):
        is_valid = False
        errors.append("order_generation_allowed must be False.")
    if contract.get("broker_execution_allowed", False):
        is_valid = False
        errors.append("broker_execution_allowed must be False.")
    if contract.get("investment_advice_allowed", False):
        is_valid = False
        errors.append("investment_advice_allowed must be False.")

    return {
        "sizing_name": contract.get("sizing_name", "unknown"),
        "is_valid": is_valid,
        "errors": errors,
        "status": PORTFOLIO_CONTRACT_READY if is_valid else "SIZING_CONTRACT_INVALID",
    }


def summarize_position_sizing_contracts(df: pd.DataFrame) -> Dict:
    """Summarize position sizing contracts."""
    return {
        "total_contracts": len(df),
        "contracts": df["sizing_name"].tolist() if not df.empty else [],
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "non_signal": True,
    }
