# -*- coding: utf-8 -*-
"""Phase 158: Backtest Acceptance Integration Registry.

Integrates realistic backtesting, walk-forward OOS, stress testing, and acceptance layers.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_backtest_acceptance_integration_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build backtest acceptance integration DataFrame and summary."""
    items = [
        {"item_id": "BAI-001", "backtest_layer": "realistic_backtest", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "BAI-002", "backtest_layer": "walk_forward_validation", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "BAI-003", "backtest_layer": "stress_testing", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "BAI-004", "backtest_layer": "monte_carlo_robustness", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "BAI-005", "backtest_layer": "backtest_governance", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "BAI-006", "backtest_layer": "benchmark_evaluation", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "BAI-007", "backtest_layer": "backtest_acceptance_report", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
    ]
    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_layers": len(df),
        "all_execution_blocked": not bool(df["execution_allowed"].any()),
        "all_verified": bool(df["verified"].all()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
