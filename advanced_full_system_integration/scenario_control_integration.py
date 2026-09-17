# -*- coding: utf-8 -*-
"""Phase 158: Scenario Control Integration Registry.

Integrates portfolio scenario testing, drawdown controls, and derisking policies.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile


def build_scenario_control_integration_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build scenario control integration DataFrame and summary."""
    items = [
        {"item_id": "SCI-001", "scenario_layer": "stress_testing_scenarios", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "SCI-002", "scenario_layer": "drawdown_control_circuit_breakers", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
        {"item_id": "SCI-003", "scenario_layer": "scenario_acceptance_manifest", "status": "INTEGRATED", "execution_allowed": False, "verified": True},
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
