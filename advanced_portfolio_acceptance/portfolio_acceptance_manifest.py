# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Master Manifest.

Assembles the master manifest certifying the closure of the Phase 153-157
Portfolio/Risk block with strict non-production invariants.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    MANIFEST_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def build_portfolio_acceptance_manifest(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build master manifest for Phase 157 Portfolio Acceptance."""
    active = profile or get_portfolio_acceptance_profile()

    manifest_data = {
        "manifest_id": "MNF-157-PORTFOLIO-ACCEPTANCE-001",
        "profile_name": active.profile_name,
        "current_phase": 157,
        "target_final_phase": 160,
        "next_phase": 158,
        "portfolio_block_completed": True,
        "non_signal": True,
        "local_only": True,
        "dry_run": True,
        "non_production": True,
        "research_only": True,
        "production_ready": False,
        "broker_ready": False,
        "live_trading_ready": False,
        "official_approval": False,
        "portfolio_constructed": False,
        "position_sizing_generated": False,
        "portfolio_optimized": False,
        "capital_allocation_generated": False,
        "portfolio_weights_generated": False,
        "allocation_generated": False,
        "rebalance_generated": False,
        "orders_generated": False,
        "risk_budget_generated": False,
        "risk_report_generated": False,
        "exposure_attribution_generated": False,
        "limit_monitoring_executed": False,
        "scenario_executed": False,
        "drawdown_control_executed": False,
        "portfolio_adjustment_generated": False,
        "hedge_derisk_generated": False,
        "alert_generated": False,
        "dashboard_generated": False,
        "metric_calculated": False,
        "var_calculated": False,
        "expected_shortfall_calculated": False,
        "optimizer_executed": False,
        "model_training_executed": False,
        "prediction_generated": False,
        "target_label_generated": False,
        "broker_order_sent": False,
        "live_order_sent": False,
        "artifact_persisted": False,
        "model_registry_written": False,
        "model_deployed": False,
        "production_deployed": False,
        "source_preserved": True,
        "manual_review_required": True,
        "phase_158_handoff_ready": True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }

    df = pd.DataFrame([manifest_data])
    summary = summarize_portfolio_acceptance_manifest(df)
    return df, summary


def summarize_portfolio_acceptance_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize master manifest."""
    row = df.iloc[0].to_dict() if not df.empty else {}
    return {
        "domain": MANIFEST_DOMAIN,
        "manifest_id": row.get("manifest_id", ""),
        "current_phase": row.get("current_phase", 157),
        "target_final_phase": row.get("target_final_phase", 160),
        "next_phase": row.get("next_phase", 158),
        "portfolio_block_completed": row.get("portfolio_block_completed", True),
        "production_ready": row.get("production_ready", False),
        "broker_ready": row.get("broker_ready", False),
        "live_trading_ready": row.get("live_trading_ready", False),
        "phase_158_handoff_ready": row.get("phase_158_handoff_ready", True),
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
