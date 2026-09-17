# -*- coding: utf-8 -*-
"""Phase 147: Validation Survivorship Bias Guards.

Guards preventing survivorship bias in instrument universe selection and historical series.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile


def build_validation_survivorship_bias_guard_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for survivorship bias guards."""
    rows = [
        {
            "guard_name": "delisted_instrument_accounting_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Gecmiste islem gormus ancak gunumuzde delist olmus enstrumanlarin evrenden silinmesini engelleyen muhafiz.",
            "non_signal": True,
        },
        {
            "guard_name": "point_in_time_universe_guard",
            "enforcement_level": "STRICT",
            "active": True,
            "description": "Enstruman evreninin sadece o an mevcut olan varliklardan olusmasini denetleyen point-in-time muhafizi.",
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
