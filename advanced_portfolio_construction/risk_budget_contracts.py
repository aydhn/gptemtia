# -*- coding: utf-8 -*-
"""Phase 153: Risk Budget Contracts."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    RISK_BUDGET_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


BUDGET_CONTRACT_TEMPLATES = [
    {
        "budget_name": "local_risk_budget_contract",
        "risk_budget_family": "local_baseline_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_PORTFOLIO_VAR",
        "output_ref": "OUT_RISK_BUDGET_BASELINE",
        "description": "Temel yerel risk butcesi sozlesmesi.",
    },
    {
        "budget_name": "per_asset_risk_budget_contract",
        "risk_budget_family": "per_asset_budget",
        "asset_scope": "single_asset",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_PER_ASSET_RISK",
        "output_ref": "OUT_PER_ASSET_BUDGET",
        "description": "Varlik basina risk butcesi sozlesmesi.",
    },
    {
        "budget_name": "per_strategy_risk_budget_contract",
        "risk_budget_family": "per_strategy_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "single_strategy",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_PER_STRATEGY_RISK",
        "output_ref": "OUT_PER_STRATEGY_BUDGET",
        "description": "Strateji basina risk butcesi sozlesmesi.",
    },
    {
        "budget_name": "per_regime_risk_budget_contract",
        "risk_budget_family": "per_regime_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "all_strategies",
        "regime_scope": "single_regime",
        "limit_ref": "LIMIT_PER_REGIME_RISK",
        "output_ref": "OUT_PER_REGIME_BUDGET",
        "description": "Rejim basina risk butcesi sozlesmesi.",
    },
    {
        "budget_name": "drawdown_budget_contract",
        "risk_budget_family": "drawdown_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_MAX_DRAWDOWN",
        "output_ref": "OUT_DRAWDOWN_BUDGET",
        "description": "Cekilme risk butcesi sozlesmesi.",
    },
    {
        "budget_name": "volatility_budget_contract",
        "risk_budget_family": "volatility_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_TARGET_VOLATILITY",
        "output_ref": "OUT_VOLATILITY_BUDGET",
        "description": "Volatilite risk butcesi sozlesmesi.",
    },
    {
        "budget_name": "exposure_budget_contract",
        "risk_budget_family": "exposure_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_GROSS_NET_EXPOSURE",
        "output_ref": "OUT_EXPOSURE_BUDGET",
        "description": "Maruziyet butcesi sozlesmesi.",
    },
    {
        "budget_name": "concentration_budget_contract",
        "risk_budget_family": "concentration_budget",
        "asset_scope": "asset_groups",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_MAX_CONCENTRATION",
        "output_ref": "OUT_CONCENTRATION_BUDGET",
        "description": "Yogunlasma butcesi sozlesmesi.",
    },
    {
        "budget_name": "cost_slippage_budget_contract",
        "risk_budget_family": "friction_budget",
        "asset_scope": "all_assets",
        "strategy_scope": "all_strategies",
        "regime_scope": "all_regimes",
        "limit_ref": "LIMIT_MAX_FRICTION_COST",
        "output_ref": "OUT_FRICTION_BUDGET",
        "description": "Maliyet ve kayma risk butcesi sozlesmesi.",
    },
]


def build_risk_budget_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for risk budget contracts."""
    rows = []
    for item in BUDGET_CONTRACT_TEMPLATES:
        rows.append({
            "budget_name": item["budget_name"],
            "risk_budget_family": item["risk_budget_family"],
            "asset_scope": item["asset_scope"],
            "strategy_scope": item["strategy_scope"],
            "regime_scope": item["regime_scope"],
            "limit_ref": item["limit_ref"],
            "output_ref": item["output_ref"],
            "description": item["description"],
            "risk_budget_generation_allowed": profile.allow_risk_budget_generation,
            "capital_allocation_allowed": profile.allow_capital_allocation,
            "position_sizing_allowed": profile.allow_position_sizing,
            "live_trading_allowed": profile.allow_live_trading,
            "broker_execution_allowed": profile.allow_broker_integration,
            "manual_review_required": True,
            "contract_only": True,
            "non_production": True,
            "broker_ready": False,
            "production_ready": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": RISK_BUDGET_DOMAIN,
        "active_profile": profile.profile_name,
        "total_contracts": len(df),
        "all_budget_generation_blocked": not any(df["risk_budget_generation_allowed"]),
        "all_allocation_blocked": not any(df["capital_allocation_allowed"]),
        "all_sizing_blocked": not any(df["position_sizing_allowed"]),
        "all_live_trading_blocked": not any(df["live_trading_allowed"]),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_risk_budget_contract(contract: Dict) -> Dict:
    """Validate single risk budget contract."""
    is_valid = True
    errors = []

    if contract.get("risk_budget_generation_allowed", False):
        is_valid = False
        errors.append("risk_budget_generation_allowed must be False.")
    if contract.get("capital_allocation_allowed", False):
        is_valid = False
        errors.append("capital_allocation_allowed must be False.")
    if contract.get("position_sizing_allowed", False):
        is_valid = False
        errors.append("position_sizing_allowed must be False.")
    if contract.get("live_trading_allowed", False):
        is_valid = False
        errors.append("live_trading_allowed must be False.")
    if contract.get("broker_execution_allowed", False):
        is_valid = False
        errors.append("broker_execution_allowed must be False.")

    return {
        "budget_name": contract.get("budget_name", "unknown"),
        "is_valid": is_valid,
        "errors": errors,
        "status": PORTFOLIO_CONTRACT_READY if is_valid else "RISK_BUDGET_CONTRACT_INVALID",
    }


def summarize_risk_budget_contracts(df: pd.DataFrame) -> Dict:
    """Summarize risk budget contracts."""
    return {
        "total_contracts": len(df),
        "contracts": df["budget_name"].tolist() if not df.empty else [],
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "non_signal": True,
    }
