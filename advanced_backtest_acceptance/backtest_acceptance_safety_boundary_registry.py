# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Safety Boundary Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    SAFETY_BOUNDARY_DOMAIN,
    ACCEPTANCE_READY,
)

SAFETY_BOUNDARIES: List[Dict[str, Any]] = [
    {"boundary_id": "SFT-152-01", "name": "prohibit_live_trading", "rule": "Live trading and order generation strictly forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-02", "name": "prohibit_broker_api", "rule": "Broker API calls, FIX engines, web sockets strictly forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-03", "name": "prohibit_backtest_execution", "rule": "Real backtest loop execution and PnL generation forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-04", "name": "prohibit_benchmark_execution", "rule": "Real benchmark performance computation forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-05", "name": "prohibit_metric_calculation", "rule": "Sharpe, drawdown, VaR, alpha, beta calculation forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-06", "name": "prohibit_strategy_approval", "rule": "Strategy approval and production sign-off forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-07", "name": "prohibit_capital_allocation", "rule": "Capital allocation and portfolio construction forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-08", "name": "prohibit_position_sizing", "rule": "Position sizing execution forbidden in this phase.", "enforced": True},
    {"boundary_id": "SFT-152-09", "name": "prohibit_optimizer_execution", "rule": "Parameter grid search and optimizer execution forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-10", "name": "prohibit_model_training_inference", "rule": "Model training, fitting, inference forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-11", "name": "prohibit_model_registry_writes", "rule": "Model registry writes and artifact persistence forbidden.", "enforced": True},
    {"boundary_id": "SFT-152-12", "name": "prohibit_scraping_and_full_text", "rule": "Web scraping, credential exposure, full text news forbidden.", "enforced": True},
]


def build_backtest_acceptance_safety_boundary_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Backtest acceptance safety boundaries."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for sb in SAFETY_BOUNDARIES:
        records.append({
            "boundary_id": sb["boundary_id"],
            "boundary_name": sb["name"],
            "rule": sb["rule"],
            "enforced": sb["enforced"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": SAFETY_BOUNDARY_DOMAIN,
        "active_profile": active.profile_name,
        "total_boundaries": len(records),
        "enforced_boundaries": len([r for r in records if r["enforced"]]),
        "all_enforced": all(r["enforced"] for r in records),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
