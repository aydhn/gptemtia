# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Go / No-Go Boundaries.

Enforces clear decision gates distinguishing permissible contract/research operations
from strictly prohibited live execution, broker, or trading actions.
"""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    GO_NO_GO_BOUNDARY_DOMAIN,
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_BROKER_EXECUTION,
    NO_GO_INVESTMENT_ADVICE,
    NO_GO_SIGNAL_GENERATION,
    NO_GO_PORTFOLIO_CONSTRUCTION,
    NO_GO_POSITION_SIZING,
    NO_GO_PORTFOLIO_OPTIMIZATION,
    NO_GO_ALLOCATION,
    NO_GO_REBALANCE,
    NO_GO_ORDER_GENERATION,
    NO_GO_RISK_REPORTING,
    NO_GO_LIMIT_MONITORING,
    NO_GO_SCENARIO_EXECUTION,
    NO_GO_DRAWDOWN_CONTROL,
    NO_GO_PORTFOLIO_ADJUSTMENT,
    NO_GO_HEDGE_DERISK,
    NO_GO_METRIC_CALCULATION,
    NO_GO_MODEL_TRAINING,
    NO_GO_PREDICTION,
    NO_GO_DEPLOYMENT,
    NO_GO_UNKNOWN,
    PORTFOLIO_ACCEPTANCE_READY,
)

GO_ACTIONS = [
    ("proceed_to_phase_158_full_system_integration_contracts", "Advance to Phase 158 contract specifications"),
    ("proceed_to_advanced_acceptance_rehearsal_design", "Advance to dry-run acceptance rehearsal design"),
    ("proceed_to_non_live_system_wide_validation_design", "Design cross-block offline validation routines"),
    ("proceed_to_final_integration_boundary_design", "Establish final integration boundary conditions"),
]

NO_GO_ACTIONS = [
    ("live_trading", NO_GO_LIVE_TRADING, "Real-money order transmission prohibited"),
    ("broker_execution", NO_GO_BROKER_EXECUTION, "Broker API interactions prohibited"),
    ("investment_advice", NO_GO_INVESTMENT_ADVICE, "Providing investment or trading advice prohibited"),
    ("signal_generation", NO_GO_SIGNAL_GENERATION, "Generating actionable trade signals prohibited"),
    ("portfolio_construction", NO_GO_PORTFOLIO_CONSTRUCTION, "Real portfolio construction prohibited"),
    ("position_sizing", NO_GO_POSITION_SIZING, "Real position size calculation prohibited"),
    ("portfolio_optimization", NO_GO_PORTFOLIO_OPTIMIZATION, "Executing numerical portfolio optimizer prohibited"),
    ("allocation_generation", NO_GO_ALLOCATION, "Generating capital allocation prohibited"),
    ("weight_generation", NO_GO_ALLOCATION, "Generating live portfolio weights prohibited"),
    ("rebalance_generation", NO_GO_REBALANCE, "Generating rebalance trade lists prohibited"),
    ("order_generation", NO_GO_ORDER_GENERATION, "Generating orders prohibited"),
    ("risk_reporting_execution", NO_GO_RISK_REPORTING, "Live risk report execution prohibited"),
    ("exposure_attribution_execution", NO_GO_RISK_REPORTING, "Real exposure attribution calculation prohibited"),
    ("limit_monitoring_execution", NO_GO_LIMIT_MONITORING, "Active limit monitoring prohibited"),
    ("scenario_execution", NO_GO_SCENARIO_EXECUTION, "Executing scenario simulation on live books prohibited"),
    ("drawdown_control_execution", NO_GO_DRAWDOWN_CONTROL, "Triggering automated drawdown control prohibited"),
    ("portfolio_adjustment", NO_GO_PORTFOLIO_ADJUSTMENT, "Automated portfolio adjustments prohibited"),
    ("hedge_derisk", NO_GO_HEDGE_DERISK, "Automated hedge or de-risking actions prohibited"),
    ("alert_generation", NO_GO_RISK_REPORTING, "Generating live push alerts prohibited"),
    ("dashboard_generation", NO_GO_RISK_REPORTING, "Real-time dashboard deployment prohibited"),
    ("metric_calculation", NO_GO_METRIC_CALCULATION, "Real Sharpe/VaR/ES/drawdown calculation prohibited"),
    ("optimizer_execution", NO_GO_PORTFOLIO_OPTIMIZATION, "Active solver execution prohibited"),
    ("model_training", NO_GO_MODEL_TRAINING, "Real machine learning model training prohibited"),
    ("prediction", NO_GO_PREDICTION, "Generating model predictions prohibited"),
    ("deployment", NO_GO_DEPLOYMENT, "Production deployment prohibited"),
    ("model_registry_write", NO_GO_DEPLOYMENT, "Writing model artifacts to registry prohibited"),
]


def build_portfolio_acceptance_go_no_go_boundary_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of all Go and No-Go boundaries."""
    active = profile or get_portfolio_acceptance_profile()
    records = []

    for action_name, desc in GO_ACTIONS:
        records.append({
            "action_name": action_name,
            "decision": "GO",
            "boundary_label": GO_CONTRACT_ONLY,
            "description": desc,
            "is_permitted": True,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })

    for action_name, boundary_label, desc in NO_GO_ACTIONS:
        records.append({
            "action_name": action_name,
            "decision": "NO-GO",
            "boundary_label": boundary_label,
            "description": desc,
            "is_permitted": False,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })

    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_go_no_go(df)
    return df, summary


def validate_portfolio_acceptance_go_no_go_request(
    request: Union[Dict[str, Any], str],
) -> Dict[str, Any]:
    """Validate whether an action request is permitted under Go / No-Go policy."""
    action = request if isinstance(request, str) else request.get("action", "")
    action_clean = action.strip().lower()

    # Check against No-Go list
    for no_go_name, boundary_label, desc in NO_GO_ACTIONS:
        if no_go_name in action_clean:
            return {
                "action": action,
                "decision": "NO-GO",
                "permitted": False,
                "boundary_label": boundary_label,
                "reason": f"Prohibited operation: {desc}",
                "status": "BLOCKED_BY_POLICY",
            }

    # Check against Go list
    for go_name, desc in GO_ACTIONS:
        if go_name in action_clean:
            return {
                "action": action,
                "decision": "GO",
                "permitted": True,
                "boundary_label": GO_CONTRACT_ONLY,
                "reason": f"Permitted contract/offline operation: {desc}",
                "status": PORTFOLIO_ACCEPTANCE_READY,
            }

    return {
        "action": action,
        "decision": "NO-GO",
        "permitted": False,
        "boundary_label": NO_GO_UNKNOWN,
        "reason": f"Unrecognized action '{action}' default-blocked under strict zero-trust boundary.",
        "status": "BLOCKED_BY_DEFAULT",
    }


def summarize_portfolio_acceptance_go_no_go(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Go / No-Go boundaries."""
    go_count = len(df[df["decision"] == "GO"]) if not df.empty and "decision" in df.columns else 0
    no_go_count = len(df[df["decision"] == "NO-GO"]) if not df.empty and "decision" in df.columns else 0
    return {
        "domain": GO_NO_GO_BOUNDARY_DOMAIN,
        "total_rules": len(df),
        "go_count": go_count,
        "no_go_count": no_go_count,
        "zero_trust_enforced": True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
