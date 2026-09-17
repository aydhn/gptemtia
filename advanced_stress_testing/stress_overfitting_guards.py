# -*- coding: utf-8 -*-
"""Phase 148: Stress Overfitting Guards.

Prevents curve-fitting, p-hacking, and strategy over-optimization on stress test scenarios.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem


def build_stress_overfitting_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of overfitting guards."""
    guard = StressGuardItem(
        guard_name="stress_overfitting_guard",
        guard_type="OVERFITTING_PREVENTION",
        description="Stres senaryolarına özel aşırı uyum (curve-fitting) ve parametre hilesini engeller.",
        enforcement_level="STRICT",
        active=True,
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
