# -*- coding: utf-8 -*-
"""Phase 147: Validation Overfitting Guards.

Guards monitoring complexity, generalization gaps, and parameter explosion.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_overfitting_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for overfitting guards."""
    rows = [
        {
            "guard_name": "train_oos_divergence_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Egitim performansi ile OOS performans arasindaki fark asiri acildiginda bayrak kaldiran muhafiz.",
            "non_signal": True,
        },
        {
            "guard_name": "parameter_complexity_budget_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Model parametre sayisinin orneklem sayisina oranini sinirlandiran asiri ogrenme muhafizi.",
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
