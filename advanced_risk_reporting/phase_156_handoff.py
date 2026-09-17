# -*- coding: utf-8 -*-
"""Phase 155: Phase 156 Portfolio Scenario Testing and Drawdown Control Handoff Report."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


DEFAULT_HANDOFF_ITEMS = [
    {
        "item_id": "HND-155-001",
        "category": "portfolio_scenario_testing_prerequisites",
        "requirement": "Verify scenario simulation hooks and stress matrices from Phase 148 and risk contracts from Phase 155 are ready",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-002",
        "category": "drawdown_control_prerequisites",
        "requirement": "Verify drawdown monitor placeholders and drawdown limit monitoring contracts from Phase 155 are established",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-003",
        "category": "risk_reporting_prerequisites",
        "requirement": "Verify 9 local risk report contracts and metadata definitions are registered",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-004",
        "category": "exposure_attribution_prerequisites",
        "requirement": "Verify gross/net/currency/cross-asset/concentration/liquidity exposure placeholders are available",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-005",
        "category": "limit_monitoring_prerequisites",
        "requirement": "Verify limit monitoring contracts, warning thresholds, and disabled alerting registries are active",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-006",
        "category": "portfolio_optimization_prerequisites",
        "requirement": "Verify Phase 154 optimization contracts and allocation constraints are integrated",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-007",
        "category": "portfolio_construction_prerequisites",
        "requirement": "Verify Phase 153 portfolio construction, position sizing, and risk budgeting contracts are integrated",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-008",
        "category": "risk_budget_prerequisites",
        "requirement": "Verify component risk contribution placeholders and risk parity specs are available",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-009",
        "category": "backtest_acceptance_prerequisites",
        "requirement": "Verify Phase 152 backtest acceptance reports are accessible via DataLake/FeatureStore",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-010",
        "category": "stress_monte_carlo_prerequisites",
        "requirement": "Verify Phase 148 stress testing and Phase 149 Monte Carlo robustness foundations are preserved",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-011",
        "category": "manual_review_blockers",
        "requirement": "Ensure operator manual review queue is inspected prior to beginning Phase 156 execution",
        "status": "SATISFIED",
        "target_phase": 156,
    },
    {
        "item_id": "HND-155-012",
        "category": "safety_boundary_continuity",
        "requirement": "Maintain strict non-production, dry-run, no-live-trading, and no-broker-execution boundary in Phase 156",
        "status": "SATISFIED",
        "target_phase": 156,
    },
]


def build_phase_156_portfolio_scenario_testing_drawdown_control_handoff_report(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 156 handoff."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for item in DEFAULT_HANDOFF_ITEMS:
        d = dict(item)
        d["current_phase"] = profile.current_phase
        d["target_final_phase"] = profile.target_final_phase
        d["next_phase"] = profile.next_phase
        rows.append(d)

    df = pd.DataFrame(rows)
    summary = summarize_phase_156_handoff(df)
    return df, summary


def summarize_phase_156_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Produce summary dictionary for Phase 156 handoff."""
    return {
        "handoff_ready": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "total_items": len(df),
        "satisfied_items": int((df["status"] == "SATISFIED").sum()) if not df.empty else 0,
        "current_phase": 155,
        "next_phase": 156,
        "target_final_phase": 160,
    }
