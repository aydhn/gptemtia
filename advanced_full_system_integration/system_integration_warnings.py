# -*- coding: utf-8 -*-
"""Phase 158: System Integration Warnings Registry.

Maintains mandatory operational warnings and governance caveats for Phase 158.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile

INTEGRATION_WARNINGS = [
    ("WRN-158-001", "contract_only_integration", "Integration layer provides contracts and metadata only; no live code runs.", "INFO"),
    ("WRN-158-002", "placeholder_only_evidence", "Interface components (Telegram, Paper Trading) are placeholders only.", "INFO"),
    ("WRN-158-003", "no_real_system_execution", "Real full-system execution is blocked by policy.", "WARNING"),
    ("WRN-158-004", "no_live_trading", "Live trading is prohibited across all profiles.", "WARNING"),
    ("WRN-158-005", "no_broker_execution", "Broker connections are disabled at contract boundary.", "WARNING"),
    ("WRN-158-006", "no_model_training", "Model training and fitting are disabled.", "WARNING"),
    ("WRN-158-007", "no_prediction", "Model predictions and inference are disabled.", "WARNING"),
    ("WRN-158-008", "no_backtest_execution", "Backtesting engine runs are disabled.", "WARNING"),
    ("WRN-158-009", "no_portfolio_execution", "Portfolio optimization runs are disabled.", "WARNING"),
    ("WRN-158-010", "no_risk_execution", "Risk calculations are disabled.", "WARNING"),
    ("WRN-158-011", "no_scenario_execution", "Scenario stress simulations are disabled.", "WARNING"),
    ("WRN-158-012", "manual_review_required", "Operator manual review required across 10 review gates.", "WARNING"),
    ("WRN-158-013", "phase_159_must_remain_non_live", "Phase 159 Release Candidate must remain local, offline, and non-live.", "WARNING"),
]


def build_system_integration_warning_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system integration warning registry DataFrame and summary."""
    records = []
    for wid, wtype, msg, sev in INTEGRATION_WARNINGS:
        records.append({
            "warning_id": wid,
            "warning_type": wtype,
            "message": msg,
            "severity": sev,
            "contract_only": True,
            "non_production": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_warnings": len(df),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
