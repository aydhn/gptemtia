# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Contracts."""

from typing import Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_CONTRACT_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


CONTRACT_TEMPLATES = [
    {
        "contract_name": "local_portfolio_construction_contract",
        "portfolio_family": "local_offline_baseline",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_V1_SNAPSHOT",
        "risk_budget_ref": "RISK_BUDGET_CONTRACT_BASELINE",
        "position_sizing_ref": "POSITION_SIZING_CONTRACT_BASELINE",
        "limit_contract_ref": "EXPOSURE_CONCENTRATION_LIMIT_CONTRACT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Temel yerel portfoy insa sozlesmesi.",
    },
    {
        "contract_name": "multi_asset_portfolio_contract",
        "portfolio_family": "cross_asset_commodity_fx",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_131_CROSS_ASSET_REGIME",
        "featurestore_ref": "FEATURESTORE_CROSS_ASSET_CATALOG",
        "risk_budget_ref": "CROSS_ASSET_RISK_BUDGET",
        "position_sizing_ref": "MULTI_ASSET_SIZING_CONTRACT",
        "limit_contract_ref": "CROSS_ASSET_EXPOSURE_LIMIT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Coklu varlik emtia-doviz portfoy sozlesmesi.",
    },
    {
        "contract_name": "regime_aware_portfolio_contract",
        "portfolio_family": "regime_conditioned",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_REGIME_CATALOG",
        "risk_budget_ref": "REGIME_RISK_BUDGET",
        "position_sizing_ref": "REGIME_AWARE_SIZING_CONTRACT",
        "limit_contract_ref": "REGIME_EXPOSURE_LIMIT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Rejim duyarli portfoy sozlesmesi.",
    },
    {
        "contract_name": "cost_aware_portfolio_contract",
        "portfolio_family": "frictional_cost_controlled",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_COST_SNAPSHOT",
        "risk_budget_ref": "COST_RISK_BUDGET",
        "position_sizing_ref": "COST_AWARE_SIZING_CONTRACT",
        "limit_contract_ref": "TURNOVER_LIMIT_CONTRACT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Islem maliyeti duyarli portfoy sozlesmesi.",
    },
    {
        "contract_name": "slippage_aware_portfolio_contract",
        "portfolio_family": "execution_slippage_controlled",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_SLIPPAGE_SNAPSHOT",
        "risk_budget_ref": "SLIPPAGE_RISK_BUDGET",
        "position_sizing_ref": "SLIPPAGE_AWARE_SIZING_CONTRACT",
        "limit_contract_ref": "SLIPPAGE_LIMIT_CONTRACT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Kayma duyarli portfoy sozlesmesi.",
    },
    {
        "contract_name": "risk_budget_aware_portfolio_contract",
        "portfolio_family": "risk_budget_governed",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_RISK_SNAPSHOT",
        "risk_budget_ref": "PORTFOLIO_RISK_BUDGET_CONTRACT",
        "position_sizing_ref": "RISK_BUDGET_SIZING_CONTRACT",
        "limit_contract_ref": "RISK_BUDGET_UTILIZATION_LIMIT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Risk butcesi yonetimli portfoy sozlesmesi.",
    },
    {
        "contract_name": "benchmark_aware_portfolio_contract",
        "portfolio_family": "benchmark_constrained",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_BENCHMARK_SNAPSHOT",
        "risk_budget_ref": "TRACKING_ERROR_RISK_BUDGET",
        "position_sizing_ref": "BENCHMARK_AWARE_SIZING_CONTRACT",
        "limit_contract_ref": "BENCHMARK_DEV_LIMIT_CONTRACT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Gosterge karsilastirmali portfoy sozlesmesi.",
    },
    {
        "contract_name": "drawdown_aware_portfolio_contract",
        "portfolio_family": "drawdown_controlled",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_DRAWDOWN_SNAPSHOT",
        "risk_budget_ref": "DRAWDOWN_RISK_BUDGET",
        "position_sizing_ref": "DRAWDOWN_AWARE_SIZING_CONTRACT",
        "limit_contract_ref": "MAX_DRAWDOWN_LIMIT_CONTRACT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Cekilme duyarli portfoy sozlesmesi.",
    },
    {
        "contract_name": "governance_aware_portfolio_contract",
        "portfolio_family": "compliance_governed",
        "backtest_acceptance_ref": "PHASE_152_BACKTEST_ACCEPTANCE_REPORT",
        "benchmark_evaluation_ref": "PHASE_151_BENCHMARK_EVALUATION",
        "model_governance_ref": "PHASE_144_MODEL_GOVERNANCE",
        "regime_context_ref": "PHASE_135_REGIME_ACCEPTANCE",
        "featurestore_ref": "FEATURESTORE_GOVERNANCE_SNAPSHOT",
        "risk_budget_ref": "GOVERNANCE_RISK_BUDGET",
        "position_sizing_ref": "GOVERNANCE_SIZING_CONTRACT",
        "limit_contract_ref": "POLICY_COMPLIANCE_LIMIT",
        "no_lookahead_guard_ref": "PORTFOLIO_NO_LOOKAHEAD_GUARD",
        "investment_advice_guard_ref": "PORTFOLIO_INVESTMENT_ADVICE_GUARD",
        "description": "Yonetisim ve mevzuat uyumlu portfoy sozlesmesi.",
    },
]


def build_portfolio_construction_contract_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio construction contracts."""
    rows = []
    for item in CONTRACT_TEMPLATES:
        rows.append({
            "contract_name": item["contract_name"],
            "portfolio_family": item["portfolio_family"],
            "backtest_acceptance_ref": item["backtest_acceptance_ref"],
            "benchmark_evaluation_ref": item["benchmark_evaluation_ref"],
            "model_governance_ref": item["model_governance_ref"],
            "regime_context_ref": item["regime_context_ref"],
            "featurestore_ref": item["featurestore_ref"],
            "risk_budget_ref": item["risk_budget_ref"],
            "position_sizing_ref": item["position_sizing_ref"],
            "limit_contract_ref": item["limit_contract_ref"],
            "no_lookahead_guard_ref": item["no_lookahead_guard_ref"],
            "investment_advice_guard_ref": item["investment_advice_guard_ref"],
            "description": item["description"],
            "portfolio_construction_allowed": profile.allow_portfolio_construction,
            "position_sizing_allowed": profile.allow_position_sizing,
            "capital_allocation_allowed": profile.allow_capital_allocation,
            "weight_generation_allowed": profile.allow_weight_generation,
            "order_generation_allowed": profile.allow_order_generation,
            "optimizer_execution_allowed": profile.allow_optimizer_execution,
            "live_trading_allowed": profile.allow_live_trading,
            "broker_execution_allowed": profile.allow_broker_integration,
            "signal_generation_allowed": profile.allow_signal_generation,
            "manual_review_required": True,
            "contract_only": True,
            "non_production": True,
            "broker_ready": False,
            "production_ready": False,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONTRACT_DOMAIN,
        "active_profile": profile.profile_name,
        "total_contracts": len(df),
        "all_construction_blocked": not any(df["portfolio_construction_allowed"]),
        "all_sizing_blocked": not any(df["position_sizing_allowed"]),
        "all_allocation_blocked": not any(df["capital_allocation_allowed"]),
        "all_optimizer_blocked": not any(df["optimizer_execution_allowed"]),
        "all_live_trading_blocked": not any(df["live_trading_allowed"]),
        "all_broker_execution_blocked": not any(df["broker_execution_allowed"]),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_construction_contract(contract: Dict) -> Dict:
    """Validate single portfolio construction contract."""
    is_valid = True
    errors = []

    if contract.get("portfolio_construction_allowed", False):
        is_valid = False
        errors.append("portfolio_construction_allowed must be False.")
    if contract.get("position_sizing_allowed", False):
        is_valid = False
        errors.append("position_sizing_allowed must be False.")
    if contract.get("capital_allocation_allowed", False):
        is_valid = False
        errors.append("capital_allocation_allowed must be False.")
    if contract.get("weight_generation_allowed", False):
        is_valid = False
        errors.append("weight_generation_allowed must be False.")
    if contract.get("live_trading_allowed", False):
        is_valid = False
        errors.append("live_trading_allowed must be False.")
    if contract.get("broker_execution_allowed", False):
        is_valid = False
        errors.append("broker_execution_allowed must be False.")
    if contract.get("production_ready", False):
        is_valid = False
        errors.append("production_ready must be False.")
    if contract.get("broker_ready", False):
        is_valid = False
        errors.append("broker_ready must be False.")

    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": is_valid,
        "errors": errors,
        "status": PORTFOLIO_CONTRACT_READY if is_valid else "PORTFOLIO_CONTRACT_INVALID",
    }


def summarize_portfolio_construction_contracts(df: pd.DataFrame) -> Dict:
    """Summarize portfolio construction contracts."""
    return {
        "total_contracts": len(df),
        "contracts": df["contract_name"].tolist() if not df.empty else [],
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "non_signal": True,
    }
