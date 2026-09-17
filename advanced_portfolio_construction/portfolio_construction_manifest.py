# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Master Manifest."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_default_portfolio_construction_profile,
)
from .portfolio_construction_labels import (
    PORTFOLIO_MANIFEST_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)
from .portfolio_construction_models import PortfolioConstructionManifest


def build_portfolio_construction_manifest(
    profile: Optional[PortfolioConstructionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the master portfolio construction manifest for Phase 153."""
    active = profile or get_default_portfolio_construction_profile()

    manifest = PortfolioConstructionManifest(
        manifest_id="MNF-153-001",
        manifest_name="portfolio_construction_manifest",
        current_phase=active.current_phase,
        target_final_phase=active.target_final_phase,
        next_phase=active.next_phase,
        non_signal=True,
        local_only=True,
        dry_run=True,
        non_production=True,
        research_only=True,
        production_ready=False,
        broker_ready=False,
        live_trading_ready=False,
        official_approval=False,
        portfolio_constructed=False,
        position_sizing_generated=False,
        capital_allocation_generated=False,
        portfolio_weights_generated=False,
        orders_generated=False,
        risk_budget_generated=False,
        exposure_limits_generated=False,
        leverage_recommendation_generated=False,
        optimizer_executed=False,
        metric_calculated=False,
        result_claim_generated=False,
        performance_claim_generated=False,
        strategy_approved=False,
        backtest_executed=False,
        benchmark_executed=False,
        model_training_executed=False,
        prediction_generated=False,
        target_label_generated=False,
        broker_order_sent=False,
        live_order_sent=False,
        artifact_persisted=False,
        model_registry_written=False,
        model_deployed=False,
        production_deployed=False,
        source_preserved=True,
        manual_review_required=True,
        phase_154_handoff_ready=True,
    )

    records = [{
        "manifest_id": manifest.manifest_id,
        "manifest_name": manifest.manifest_name,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "portfolio_constructed": manifest.portfolio_constructed,
        "position_sizing_generated": manifest.position_sizing_generated,
        "capital_allocation_generated": manifest.capital_allocation_generated,
        "portfolio_weights_generated": manifest.portfolio_weights_generated,
        "orders_generated": manifest.orders_generated,
        "broker_order_sent": manifest.broker_order_sent,
        "live_order_sent": manifest.live_order_sent,
        "optimizer_executed": manifest.optimizer_executed,
        "metric_calculated": manifest.metric_calculated,
        "model_training_executed": manifest.model_training_executed,
        "prediction_generated": manifest.prediction_generated,
        "non_signal": manifest.non_signal,
        "local_only": manifest.local_only,
        "dry_run": manifest.dry_run,
        "non_production": manifest.non_production,
        "research_only": manifest.research_only,
        "source_preserved": manifest.source_preserved,
        "manual_review_required": manifest.manual_review_required,
        "phase_154_handoff_ready": manifest.phase_154_handoff_ready,
        "status": PORTFOLIO_CONTRACT_READY,
    }]

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": PORTFOLIO_MANIFEST_DOMAIN,
        "active_profile": active.profile_name,
        "manifest_id": manifest.manifest_id,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "portfolio_constructed": manifest.portfolio_constructed,
        "position_sizing_generated": manifest.position_sizing_generated,
        "capital_allocation_generated": manifest.capital_allocation_generated,
        "portfolio_weights_generated": manifest.portfolio_weights_generated,
        "orders_generated": manifest.orders_generated,
        "broker_order_sent": manifest.broker_order_sent,
        "live_order_sent": manifest.live_order_sent,
        "phase_154_handoff_ready": manifest.phase_154_handoff_ready,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary
