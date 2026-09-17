# -*- coding: utf-8 -*-
"""Phase 147: Validation Data Snooping Bias Guards.

Guards preventing data snooping bias, test set peeking, and repeated evaluations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_data_snooping_bias_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for data snooping bias guards."""
    rows = [
        {
            "guard_name": "oos_peeking_prevention_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Model tasarimi veya hiperparametre secimi asamasinda OOS test kumesine erisimi engelleyen muhafiz.",
            "non_signal": True,
        },
        {
            "guard_name": "repeated_trial_penalty_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Ayni veri kumesi uzerinde cok sayida deneme yapildiginda anlamlilik esigini yukselten muhafiz.",
            "non_signal": True,
        },
    ]
    df = pd.DataFrame(rows)
    summary = {
        "total_guards": len(df),
        "all_active": True,
        "strict_enforcement": True,
        "non_signal": True,
    }
    return df, summary
