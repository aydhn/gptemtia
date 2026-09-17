# -*- coding: utf-8 -*-
"""Phase 147: Holdout Period Contracts.

Specifications for strictly protected holdout periods that must remain unaccessed during model calibration.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

HOLDOUT_SPECS: List[Dict[str, Any]] = [
    {
        "holdout_id": "HLD-001",
        "name": "sealed_terminal_holdout_contract",
        "lock_status": "SEALED",
        "access_policy": "NO_PRE_VALIDATION_PEEKING",
        "description": "Model tasarimi ve parametre secimi sirasinda kesinlikle bakilamayacak muhurlu nihai test kumesi.",
    },
    {
        "holdout_id": "HLD-002",
        "name": "recent_market_regime_holdout",
        "lock_status": "SEALED",
        "access_policy": "STRICT_GOVERNANCE_GATE",
        "description": "En son gerceklesen piyasa kosullarini temsil eden ve erisimi yonetisim onayina bagli donem sozlesmesi.",
    },
]


def build_holdout_period_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for holdout period contracts."""
    rows = []
    for h in HOLDOUT_SPECS:
        rows.append(
            {
                "holdout_id": h["holdout_id"],
                "name": h["name"],
                "lock_status": h["lock_status"],
                "access_policy": h["access_policy"],
                "description": h["description"],
                "is_sealed": True,
                "peek_prohibited": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_holdouts": len(df),
        "all_sealed": True,
        "peek_prohibited_all": True,
        "non_signal": True,
    }
    return df, summary
