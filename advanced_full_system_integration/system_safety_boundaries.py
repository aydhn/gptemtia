# -*- coding: utf-8 -*-
"""Phase 158: System Safety Boundaries.

Enforces system-wide safety boundaries prohibiting live actions and unauthorized execution.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

SAFETY_RULES = [
    ("SFT-158-001", "safety_boundary", "no_live_trading", "execution", False, "Live trading is strictly prohibited."),
    ("SFT-158-002", "safety_boundary", "no_broker_integration", "network", False, "Connecting to live broker APIs is strictly prohibited."),
    ("SFT-158-003", "safety_boundary", "no_real_order_generation", "order", False, "Generating real orders is strictly prohibited."),
    ("SFT-158-004", "safety_boundary", "no_investment_advice", "advice", False, "Providing investment or financial advice is strictly prohibited."),
    ("SFT-158-005", "safety_boundary", "no_signal_generation", "signal", False, "Outputting trade signals is strictly prohibited in Phase 158."),
    ("SFT-158-006", "safety_boundary", "no_system_execution", "execution", False, "Real full-system execution is blocked by contract."),
    ("SFT-158-007", "safety_boundary", "no_end_to_end_bot_run", "execution", False, "Running live bot workflows is blocked by policy."),
    ("SFT-158-008", "safety_boundary", "no_model_training", "ml", False, "Training or fitting ML models is forbidden."),
    ("SFT-158-009", "safety_boundary", "no_prediction_inference", "ml", False, "Running model prediction or inference is forbidden."),
    ("SFT-158-010", "safety_boundary", "no_backtest_execution", "backtest", False, "Executing real backtests is forbidden."),
    ("SFT-158-011", "safety_boundary", "no_portfolio_execution", "portfolio", False, "Executing portfolio construction or optimization is forbidden."),
    ("SFT-158-012", "safety_boundary", "no_risk_execution", "risk", False, "Executing live risk calculations is forbidden."),
    ("SFT-158-013", "safety_boundary", "no_scenario_execution", "scenario", False, "Executing real scenario stress testing is forbidden."),
    ("SFT-158-014", "safety_boundary", "no_web_scraping", "network", False, "Scraping external websites or bypassing paywalls is forbidden."),
    ("SFT-158-015", "safety_boundary", "no_credential_leakage", "security", False, "Exposing API keys, tokens, or secrets is forbidden."),
    ("SFT-158-016", "safety_boundary", "source_preservation", "storage", True, "Raw source data must be preserved immutably."),
    ("SFT-158-017", "safety_boundary", "dry_run_enforcement", "runtime", True, "All operations must run in dry-run mode."),
    ("SFT-158-018", "safety_boundary", "local_offline_isolation", "runtime", True, "Operations must remain strictly local and offline."),
]


def build_system_safety_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system safety boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in SAFETY_RULES:
        item = SystemBoundaryItem(
            boundary_id=bid,
            boundary_type=btype,
            rule_name=rname,
            action_type=atype,
            is_allowed=is_allowed,
            reason=reason,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "prohibited_actions_count": int((df["is_allowed"] == False).sum()),
        "allowed_actions_count": int((df["is_allowed"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
