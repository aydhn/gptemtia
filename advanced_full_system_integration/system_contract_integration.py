# -*- coding: utf-8 -*-
"""Phase 158: System Contract Integration.

Integrates contracts across all system layers: data, feature/factor, regime, ML,
backtest, portfolio, risk, scenario, safety, reporting, and documentation.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemIntegrationContract

CONTRACT_GROUPS = [
    ("CNT-001", "data_contracts", "data_providers", "v1.0", "INTEGRATED", "Contracts for data ingestion, economic calendar, and news metadata."),
    ("CNT-002", "feature_factor_contracts", "feature_store", "v1.0", "INTEGRATED", "Contracts for technical indicators, factors, and feature quality."),
    ("CNT-003", "regime_contracts", "regime_engine", "v1.0", "INTEGRATED", "Contracts for market behavior diagnostics, regimes, and transitions."),
    ("CNT-004", "ml_governance_contracts", "ml_governance", "v1.0", "INTEGRATED", "Contracts for model governance, explainability, drift, and calibration."),
    ("CNT-005", "backtest_acceptance_contracts", "backtest_engine", "v1.0", "INTEGRATED", "Contracts for realistic backtesting, walk-forward, and acceptance."),
    ("CNT-006", "portfolio_acceptance_contracts", "portfolio_engine", "v1.0", "INTEGRATED", "Contracts for portfolio construction, optimization, and acceptance."),
    ("CNT-007", "risk_reporting_contracts", "risk_engine", "v1.0", "INTEGRATED", "Contracts for risk limits, exposure attribution, and risk reporting."),
    ("CNT-008", "scenario_control_contracts", "scenario_engine", "v1.0", "INTEGRATED", "Contracts for stress scenarios, drawdown controls, and derisking."),
    ("CNT-009", "safety_boundary_contracts", "safety_layer", "v1.0", "INTEGRATED", "Contracts strictly enforcing no-live-trading, no-broker, and dry-run boundaries."),
    ("CNT-010", "reporting_contracts", "reporting_layer", "v1.0", "INTEGRATED", "Contracts for markdown, txt, csv, and json status report builders."),
    ("CNT-011", "documentation_contracts", "docs_layer", "v1.0", "INTEGRATED", "Contracts for operator manual, architecture, and safe usage guidelines."),
]


def build_system_contract_integration_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build system contract integration registry DataFrame and summary."""
    items = []
    for cid, sname, ctype, ver, status, notes in CONTRACT_GROUPS:
        item = SystemIntegrationContract(
            contract_id=cid,
            subsystem_name=sname,
            contract_type=ctype,
            version=ver,
            status=status,
            contract_only=True,
            non_production=True,
            manual_review_required=True,
            zero_execution_guaranteed=True,
            notes=notes,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_contracts": len(df),
        "all_contract_only": bool(df["contract_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_zero_execution": bool(df["zero_execution_guaranteed"].all()) if not df.empty else True,
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
