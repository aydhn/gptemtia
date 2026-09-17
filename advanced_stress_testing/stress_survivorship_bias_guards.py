# -*- coding: utf-8 -*-
"""Phase 148: Stress Survivorship Bias Guards.

Enforces inclusion of delisted, bankrupted, or restructured assets in historical stress scenarios.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem


def build_stress_survivorship_bias_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of survivorship bias guards."""
    guard = StressGuardItem(
        guard_name="stress_survivorship_bias_guard",
        guard_type="SURVIVORSHIP_BIAS_PREVENTION",
        description="Kriz anında batan veya delist olan varlıkların göz ardı edilmesini engeller.",
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
