# -*- coding: utf-8 -*-
"""Phase 147: Out-of-Sample Split Contracts.

Specifications for dedicated out-of-sample (OOS) partitions strictly isolating evaluation periods.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

OOS_SPLIT_SPECS: List[Dict[str, Any]] = [
    {
        "oos_split_name": "primary_oos_contract_1y",
        "oos_type": "FINAL_HOLDOUT",
        "horizon_months": 12,
        "embargo_days": 14,
        "description": "Son 1 yili (12 ay) tamamen dokunulmamis nihai OOS test seti olarak kilitleyen sozlesme.",
    },
    {
        "oos_split_name": "rolling_oos_quarterly_contract",
        "oos_type": "ROLLING_CHUNK",
        "horizon_months": 3,
        "embargo_days": 7,
        "description": "Her ceyrekte 3 aylik dilimlerle OOS test araliklari olusturan sozlesme.",
    },
    {
        "oos_split_name": "stress_regime_oos_contract",
        "oos_type": "REGIME_SPECIFIC_OOS",
        "horizon_months": 6,
        "embargo_days": 21,
        "description": "Ozellikle yuksek volatilite ve kriz donemlerini OOS olarak ayiran rejim odakli sozlesme.",
    },
]


def build_out_of_sample_split_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for out-of-sample split contracts."""
    rows = []
    for s in OOS_SPLIT_SPECS:
        rows.append(
            {
                "oos_split_name": s["oos_split_name"],
                "oos_type": s["oos_type"],
                "horizon_months": s["horizon_months"],
                "embargo_days": s["embargo_days"],
                "description": s["description"],
                "is_isolated": True,
                "split_executed": False,
                "targets_generated": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_oos_splits": len(df),
        "all_splits_isolated": True,
        "zero_split_executed": True,
        "zero_targets_generated": True,
        "non_signal": True,
    }
    return df, summary
