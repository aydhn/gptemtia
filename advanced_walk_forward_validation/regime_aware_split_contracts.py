# -*- coding: utf-8 -*-
"""Phase 147: Regime-Aware Split Contracts.

Specifications for partitioning validation folds based on market regimes without data leakage.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

REGIME_SPLIT_SPECS: List[Dict[str, Any]] = [
    {
        "split_name": "high_volatility_regime_split",
        "target_regime": "HIGH_VOLATILITY",
        "min_bars_per_regime": 63,
        "transition_embargo_bars": 10,
        "description": "Yuksek oynaklik donemlerini ayri bir test kumesi olarak izole eden rejim duyarlilik sozlesmesi.",
    },
    {
        "split_name": "trending_bull_bear_regime_split",
        "target_regime": "TREND_REGIME",
        "min_bars_per_regime": 126,
        "transition_embargo_bars": 15,
        "description": "Trendli piyasa kosullarini izole ederek modelin yonlu ortamlardaki tutarliligini test etmeye yonelik bolumleme.",
    },
    {
        "split_name": "mean_reverting_choppy_regime_split",
        "target_regime": "MEAN_REVERTING_CHOPPY",
        "min_bars_per_regime": 63,
        "transition_embargo_bars": 10,
        "description": "Yatay ve dalgali piyasa donemlerini dogrulama havuzunda temsil eden sozlesme.",
    },
]


def build_regime_aware_split_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime-aware split contract registry."""
    rows = []
    for r in REGIME_SPLIT_SPECS:
        rows.append(
            {
                "split_name": r["split_name"],
                "target_regime": r["target_regime"],
                "min_bars_per_regime": r["min_bars_per_regime"],
                "transition_embargo_bars": r["transition_embargo_bars"],
                "description": r["description"],
                "split_executed": False,
                "regime_labels_simulated_only": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_regime_splits": len(df),
        "all_splits_unexecuted": True,
        "non_signal": True,
    }
    return df, summary
