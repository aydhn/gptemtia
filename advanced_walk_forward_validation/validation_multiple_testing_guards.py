# -*- coding: utf-8 -*-
"""Phase 147: Validation Multiple Testing Guards.

Guards mitigating multiple hypothesis testing bias (e.g. Bonferroni / False Discovery Rate adjustments).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_multiple_testing_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for multiple testing guards."""
    rows = [
        {
            "guard_name": "bonferroni_haircut_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Deneme sayisi arttikca t-istatistigi ve Sharpe basari esigini cezalandiran Bonferroni kesinti muhafizi.",
            "non_signal": True,
        },
        {
            "guard_name": "false_discovery_rate_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Yanlis kesif oranini (FDR) kontrol altinda tutan coklu hipotez test muhafizi.",
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
