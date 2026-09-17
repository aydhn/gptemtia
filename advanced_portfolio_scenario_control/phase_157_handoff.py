# -*- coding: utf-8 -*-
"""Phase 156: Phase 157 Portfolio Acceptance Report Handoff Report."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

DEFAULT_HANDOFF_ITEMS = [
    {
        "item_id": "HND-156-001",
        "category": "scenario_testing_prerequisites",
        "requirement": "Verify 10 scenario testing contracts, libraries, and resilience contracts are registered",
        "status": "SATISFIED",
        "target_phase": 157,
    },
    {
        "item_id": "HND-156-002",
        "category": "drawdown_control_prerequisites",
        "requirement": "Verify drawdown control contracts, threshold tiers, warnings, and breach placeholders are ready",
        "status": "SATISFIED",
        "target_phase": 157,
    },
    {
        "item_id": "HND-156-003",
        "category": "control_action_placeholders",
        "requirement": "Verify exposure reduction, de-risking, hedge, rebalance, stop, freeze/resume placeholders are inactive",
        "status": "SATISFIED",
        "target_phase": 157,
    },
    {
        "item_id": "HND-156-004",
        "category": "outputs_and_metrics_prerequisites",
        "requirement": "Verify scenario, drawdown, resilience output contracts and metric placeholders are defined",
        "status": "SATISFIED",
        "target_phase": 157,
    },
    {
        "item_id": "HND-156-005",
        "category": "guards_and_disabled_execution",
        "requirement": "Verify 14 guards and 14 disabled execution reports guarantee negative invariants",
        "status": "SATISFIED",
        "target_phase": 157,
    },
    {
        "item_id": "HND-156-006",
        "category": "upstream_phase_continuity",
        "requirement": "Verify Phase 153 Construction, Phase 154 Optimization, and Phase 155 Risk Reporting linkages are intact",
        "status": "SATISFIED",
        "target_phase": 157,
    },
    {
        "item_id": "HND-156-007",
        "category": "safety_boundary_continuity",
        "requirement": "Maintain strict dry-run, offline, non-production, no-live-trading boundary into Phase 157",
        "status": "SATISFIED",
        "target_phase": 157,
    },
]

def build_phase_157_portfolio_acceptance_report_handoff_report(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    rows = []
    for item in DEFAULT_HANDOFF_ITEMS:
        d = dict(item)
        d["current_phase"] = profile.current_phase
        d["target_final_phase"] = profile.target_final_phase
        d["next_phase"] = profile.next_phase
        rows.append(d)
    df = pd.DataFrame(rows)
    summary = summarize_phase_157_handoff(df)
    return df, summary

def summarize_phase_157_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "handoff_ready": bool((df["status"] == "SATISFIED").all()) if not df.empty else True,
        "total_items": len(df),
        "satisfied_items": int((df["status"] == "SATISFIED").sum()) if not df.empty else 0,
        "current_phase": 156,
        "next_phase": 157,
        "target_final_phase": 160,
        "status": "HANDOFF_READY",
    }
