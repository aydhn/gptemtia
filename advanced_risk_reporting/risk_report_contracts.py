# -*- coding: utf-8 -*-
"""Phase 155: Risk Report Contracts Registry."""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportContract


DEFAULT_RISK_REPORT_CONTRACTS = [
    {
        "contract_name": "local_risk_report_contract",
        "report_family": "local_offline_risk_reports",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "portfolio_risk_summary_contract",
        "report_family": "risk_summary",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "exposure_summary_contract",
        "report_family": "exposure_summary",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "limit_monitoring_summary_contract",
        "report_family": "limit_monitoring_summary",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "drawdown_monitoring_report_contract",
        "report_family": "drawdown_monitoring",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "liquidity_risk_report_contract",
        "report_family": "liquidity_risk",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "leverage_margin_risk_report_contract",
        "report_family": "leverage_margin_risk",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "cost_slippage_risk_report_contract",
        "report_family": "cost_slippage_risk",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
    {
        "contract_name": "governance_aware_risk_report_contract",
        "report_family": "governance_risk",
        "portfolio_construction_ref": "REF-PC-153",
        "portfolio_optimization_ref": "REF-PO-154",
        "backtest_acceptance_ref": "REF-BA-152",
        "model_governance_ref": "REF-MG-144",
        "regime_context_ref": "REF-REG-135",
        "featurestore_ref": "REF-FS-134",
        "no_lookahead_guard_ref": "REF-NLG-155",
        "investment_advice_guard_ref": "REF-IAG-155",
        "risk_reporting_execution_allowed": False,
        "exposure_attribution_allowed": False,
        "limit_monitoring_allowed": False,
        "metric_calculation_allowed": False,
        "alert_generation_allowed": False,
        "dashboard_generation_allowed": False,
        "portfolio_adjustment_allowed": False,
        "live_trading_allowed": False,
        "broker_execution_allowed": False,
        "signal_generation_allowed": False,
        "manual_review_required": True,
    },
]


def build_risk_report_contract_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary of risk report contracts."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for c in DEFAULT_RISK_REPORT_CONTRACTS:
        model = RiskReportContract(**c)
        data = model.model_dump()
        data["current_phase"] = profile.current_phase
        data["target_final_phase"] = profile.target_final_phase
        data["next_phase"] = profile.next_phase
        rows.append(data)

    df = pd.DataFrame(rows)
    summary = summarize_risk_report_contracts(df)
    return df, summary


def validate_risk_report_contract(contract: dict) -> dict:
    """Validate that a single risk report contract satisfies safety invariants."""
    allowed_keys = [
        "risk_reporting_execution_allowed",
        "exposure_attribution_allowed",
        "limit_monitoring_allowed",
        "metric_calculation_allowed",
        "alert_generation_allowed",
        "dashboard_generation_allowed",
        "portfolio_adjustment_allowed",
        "live_trading_allowed",
        "broker_execution_allowed",
        "signal_generation_allowed",
    ]
    violations = []
    for k in allowed_keys:
        if contract.get(k, False) is True:
            violations.append(f"{k} must be False")
    return {
        "contract_name": contract.get("contract_name", "unknown"),
        "is_valid": len(violations) == 0,
        "violations": violations,
    }


def summarize_risk_report_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Produce summary dictionary for risk report contracts."""
    return {
        "contract_count": len(df),
        "total_contracts": len(df),
        "all_contracts_disallow_execution": bool((df["risk_reporting_execution_allowed"] == False).all()) if not df.empty else True,
        "all_contracts_disallow_exposure_attribution": bool((df["exposure_attribution_allowed"] == False).all()) if not df.empty else True,
        "all_contracts_disallow_limit_monitoring": bool((df["limit_monitoring_allowed"] == False).all()) if not df.empty else True,
        "all_contracts_disallow_live_trading": bool((df["live_trading_allowed"] == False).all()) if not df.empty else True,
        "all_contracts_disallow_broker": bool((df["broker_execution_allowed"] == False).all()) if not df.empty else True,
        "manual_review_required_all": bool(df["manual_review_required"].all()) if not df.empty else True,
    }
