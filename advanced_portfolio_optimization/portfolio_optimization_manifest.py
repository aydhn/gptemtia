# -*- coding: utf-8 -*-
"""Phase 154: Master Portfolio Optimization Manifest."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile
from .portfolio_optimization_models import PortfolioOptimizationManifest


def build_portfolio_optimization_manifest(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build master Phase 154 manifest table."""
    manifest = PortfolioOptimizationManifest()
    records = [{
        "manifest_name": manifest.manifest_name,
        "current_phase": manifest.current_phase,
        "target_final_phase": manifest.target_final_phase,
        "next_phase": manifest.next_phase,
        "non_signal": manifest.non_signal,
        "local_only": manifest.local_only,
        "dry_run": manifest.dry_run,
        "non_production": manifest.non_production,
        "research_only": manifest.research_only,
        "production_ready": manifest.production_ready,
        "broker_ready": manifest.broker_ready,
        "live_trading_ready": manifest.live_trading_ready,
        "official_approval": manifest.official_approval,
        "portfolio_optimized": manifest.portfolio_optimized,
        "portfolio_constructed": manifest.portfolio_constructed,
        "position_sizing_generated": manifest.position_sizing_generated,
        "capital_allocation_generated": manifest.capital_allocation_generated,
        "portfolio_weights_generated": manifest.portfolio_weights_generated,
        "allocation_generated": manifest.allocation_generated,
        "rebalance_generated": manifest.rebalance_generated,
        "orders_generated": manifest.orders_generated,
        "risk_budget_generated": manifest.risk_budget_generated,
        "exposure_limits_generated": manifest.exposure_limits_generated,
        "efficient_frontier_generated": manifest.efficient_frontier_generated,
        "optimizer_executed": manifest.optimizer_executed,
        "solver_executed": manifest.solver_executed,
        "grid_search_executed": manifest.grid_search_executed,
        "metric_calculated": manifest.metric_calculated,
        "result_claim_generated": manifest.result_claim_generated,
        "performance_claim_generated": manifest.performance_claim_generated,
        "strategy_approved": manifest.strategy_approved,
        "backtest_executed": manifest.backtest_executed,
        "benchmark_executed": manifest.benchmark_executed,
        "model_training_executed": manifest.model_training_executed,
        "prediction_generated": manifest.prediction_generated,
        "target_label_generated": manifest.target_label_generated,
        "broker_order_sent": manifest.broker_order_sent,
        "live_order_sent": manifest.live_order_sent,
        "source_preserved": manifest.source_preserved,
        "manual_review_required": manifest.manual_review_required,
        "phase_155_handoff_ready": manifest.phase_155_handoff_ready,
    }]
    df = pd.DataFrame(records)
    summary = {
        "manifest_name": manifest.manifest_name,
        "current_phase": 154,
        "target_final_phase": 160,
        "next_phase": 155,
        "portfolio_optimized": False,
        "portfolio_weights_generated": False,
        "allocation_generated": False,
        "rebalance_generated": False,
        "orders_generated": False,
        "efficient_frontier_generated": False,
        "optimizer_executed": False,
        "solver_executed": False,
        "broker_order_sent": False,
        "live_order_sent": False,
        "phase_155_handoff_ready": True,
    }
    return df, summary
