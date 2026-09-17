# -*- coding: utf-8 -*-
"""Phase 148: Stress Scenario Leakage Guards.

Prevents strategy knowledge or optimization snooping into historical crisis windows
(Scenario Leakage Prevention).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem


def build_stress_scenario_leakage_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of scenario leakage guards."""
    guard = StressGuardItem(
        guard_name="stress_scenario_leakage_guard",
        guard_type="INFORMATION_LEAKAGE",
        description="Stres senaryosu parametrelerinin veya kriz tarihlerinin model optimizasyonuna sızmasını engeller.",
        enforcement_level="STRICT",
        active=True,
        violating_columns=["leak", "leakage", "scenario_snoop", "crisis_peek"],
    )
    rows = [
        {
            "guard_name": guard.guard_name,
            "guard_type": guard.guard_type,
            "description": guard.description,
            "enforcement_level": guard.enforcement_level,
            "active": guard.active,
            "non_signal": True,
            "local_only": True,
        }
    ]
    df = pd.DataFrame(rows)
    summary = {
        "guard_active": guard.active,
        "enforcement_level": guard.enforcement_level,
        "non_signal": True,
    }
    return df, summary


def validate_stress_scenario_leakage_request(request: Any) -> Dict[str, Any]:
    """Inspect a request to detect any prohibited scenario parameter tuning or leakage."""
    req_text = str(request).lower()
    prohibited_patterns = [
        "leak",
        "scenario_snoop",
        "tune_to_scenario",
        "fit_to_crisis",
        "optimize_for_2008",
        "optimize_for_covid",
    ]
    violations = [p for p in prohibited_patterns if p in req_text]
    return {
        "is_safe": len(violations) == 0,
        "violations": violations,
        "action_taken": "BLOCKED" if len(violations) > 0 else "PASSED",
        "non_signal": True,
    }
