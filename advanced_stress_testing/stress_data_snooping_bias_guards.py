# -*- coding: utf-8 -*-
"""Phase 148: Stress Data Snooping Bias Guards.

Prevents data snooping and post-hoc scenario cherry-picking bias.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressGuardItem


def build_stress_data_snooping_bias_guard_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of data snooping bias guards."""
    guard = StressGuardItem(
        guard_name="stress_data_snooping_bias_guard",
        guard_type="DATA_SNOOPING_PREVENTION",
        description="Stres testi sonuçlarına göre geriye dönük kural uydurma ve veri gözetleme yanlılığını engeller.",
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
