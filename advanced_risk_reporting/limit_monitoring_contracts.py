# -*- coding: utf-8 -*-
"""Phase 155: Limit Monitoring Contracts Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import LimitMonitoringContract


DEFAULT_LIMIT_MONITORING_CONTRACTS = [
    {
        "contract_name": "exposure_limit_monitoring_contract",
        "limit_family": "exposure_limit",
        "description": "Brut ve net exposure tavan sinir izleme sozlesmesi",
        "limit_type": "hard_limit",
        "threshold_metadata": "gross_exposure <= 1.5, net_exposure in [-0.5, 0.5]",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "concentration_limit_monitoring_contract",
        "limit_family": "concentration_limit",
        "description": "Tekil varlik ve grup bazinda konsantrasyon sinir izleme sozlesmesi",
        "limit_type": "hard_limit",
        "threshold_metadata": "max_single_asset <= 0.25, top_3_assets <= 0.60",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "leverage_limit_monitoring_contract",
        "limit_family": "leverage_limit",
        "description": "Maksimum portfoy kaldirac orani izleme sozlesmesi",
        "limit_type": "hard_limit",
        "threshold_metadata": "leverage_ratio <= 2.0",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "margin_limit_monitoring_contract",
        "limit_family": "margin_limit",
        "description": "Teminat yeterliligi ve baslangic teminati kullanim izleme sozlesmesi",
        "limit_type": "soft_warning",
        "threshold_metadata": "initial_margin_usage <= 0.70",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "liquidity_limit_monitoring_contract",
        "limit_family": "liquidity_limit",
        "description": "Tasfiye gunu ve gunluk ortalama hacim payi izleme sozlesmesi",
        "limit_type": "hard_limit",
        "threshold_metadata": "days_to_liquidate <= 3.0, adv_participation <= 0.10",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "drawdown_limit_monitoring_contract",
        "limit_family": "drawdown_limit",
        "description": "Zirveden gerileme (Drawdown) esik izleme sozlesmesi",
        "limit_type": "hard_limit",
        "threshold_metadata": "max_drawdown <= 0.15, warning_drawdown <= 0.10",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "volatility_limit_monitoring_contract",
        "limit_family": "volatility_limit",
        "description": "Yilliklandirilmis portfoy oynaklik tavan izleme sozlesmesi",
        "limit_type": "soft_warning",
        "threshold_metadata": "annualized_volatility <= 0.20",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "turnover_limit_monitoring_contract",
        "limit_family": "turnover_limit",
        "description": "Donemsel portfoy donus hizi tavan izleme sozlesmesi",
        "limit_type": "soft_warning",
        "threshold_metadata": "turnover_per_period <= 0.30",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
    {
        "contract_name": "risk_budget_limit_monitoring_contract",
        "limit_family": "risk_budget_limit",
        "description": "Risk butcesi sapma ve risk katki tavan izleme sozlesmesi",
        "limit_type": "hard_limit",
        "threshold_metadata": "component_risk_contrib_max <= 0.35",
        "is_placeholder": True,
        "is_enforced_live": False,
        "allows_execution": False,
        "allows_alerting": False,
    },
]


def build_limit_monitoring_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of limit monitoring contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for c in DEFAULT_LIMIT_MONITORING_CONTRACTS:
        model = LimitMonitoringContract(**c)
        data = model.model_dump()
        data["current_phase"] = profile.current_phase
        data["target_final_phase"] = profile.target_final_phase
        data["next_phase"] = profile.next_phase
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = summarize_limit_monitoring_contracts(df)
    return df, summary


def validate_limit_monitoring_contract(contract: dict) -> dict:
    """Validate that a limit monitoring contract satisfies safety invariants."""
    violations = []
    if contract.get("is_enforced_live", False) is True:
        violations.append("is_enforced_live must be False")
    if contract.get("allows_execution", False) is True:
        violations.append("allows_execution must be False")
    if contract.get("allows_alerting", False) is True:
        violations.append("allows_alerting must be False")
    if contract.get("is_placeholder", True) is not True:
        violations.append("is_placeholder must be True")
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_limit_monitoring_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Produce summary dictionary for limit monitoring contracts."""
    return {
        "contract_count": len(df),
        "total_contracts": len(df),
        "all_contracts_placeholder": bool(df["is_placeholder"].all()) if not df.empty else True,
        "zero_live_enforcement": bool((df["is_enforced_live"] == False).all()) if not df.empty else True,
        "zero_execution_allowed": bool((df["allows_execution"] == False).all()) if not df.empty else True,
        "zero_alerting_allowed": bool((df["allows_alerting"] == False).all()) if not df.empty else True,
    }
