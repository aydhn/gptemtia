# -*- coding: utf-8 -*-
"""Phase 148: Stress Multiple Testing Guards.

Provides safeguards against statistical multiple-hypothesis testing errors in scenario variations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem


def build_stress_multiple_testing_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of multiple testing guards."""
    guard = StressGuardItem(
        guard_name="stress_multiple_testing_guard",
        guard_type="MULTIPLE_TESTING_PENALTY",
        description="Çok sayıda senaryo varyasyonunda şans eseri başarılı çıkma riskini kontrol eder.",
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
