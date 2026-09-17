# -*- coding: utf-8 -*-
"""Phase 153: Portfolio No-Lookahead Guards Module.

Guards portfolio construction datasets against forward-looking leakage,
negative shifts, future returns, and future join violations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

PORTFOLIO_LOOKAHEAD_PATTERNS = [
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "realized_future_pnl",
    "future_pnl",
    "next_close",
    "shift(-1)",
    "shift_-1",
    "lead_return",
    "future_weight",
    "realized_drawdown_future",
]

PORTFOLIO_LOOKAHEAD_GUARDS: List[Dict[str, Any]] = [
    {
        "guard_id": "GUARD_PORTFOLIO_NO_LOOKAHEAD_COLS",
        "guard_name": "Portfolio No-Lookahead Column Pattern Guard",
        "detection_target": "future_return_and_lead_columns",
        "description": "Gelecege bakan veya shift(-1) iceren kolon isimlerini engelleyen portfoy muhafizi.",
    },
    {
        "guard_id": "GUARD_PORTFOLIO_NO_FUTURE_JOIN",
        "guard_name": "Portfolio Backward Monotonic Asof Join Guard",
        "detection_target": "future_timestamp_leakage",
        "description": "Portfoy veri birlestirmelerinde gelecege yonelik join yapilmasini engelleyen muhafiz.",
    },
    {
        "guard_id": "GUARD_PORTFOLIO_STRICT_TIMESTAMP_ORDER",
        "guard_name": "Portfolio Chronological Monotonicity Guard",
        "detection_target": "out_of_order_timestamps",
        "description": "Portfoy veri satirlarinin kesin monoton artan zaman siralamasini denetleyen muhafiz.",
    },
]


def build_portfolio_no_lookahead_guard_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of portfolio no-lookahead guards."""
    rows: List[Dict[str, Any]] = []

    for g in PORTFOLIO_LOOKAHEAD_GUARDS:
        rows.append({
            "guard_id": g["guard_id"],
            "guard_name": g["guard_name"],
            "detection_target": g["detection_target"],
            "description": g["description"],
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "is_active": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_GUARD_DOMAIN,
        "guard_category": "no_lookahead",
        "active_profile": profile.profile_name,
        "total_guards": len(df),
        "all_active": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_no_lookahead_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that no lookahead or future return column exists in the provided list."""
    detected: List[str] = []
    for col in column_names:
        c_lower = str(col).lower()
        for pat in PORTFOLIO_LOOKAHEAD_PATTERNS:
            if pat in c_lower:
                detected.append(col)
                break

    is_clean = len(detected) == 0
    return {
        "is_clean": is_clean,
        "lookahead_detected": not is_clean,
        "detected_columns": detected,
        "status": "PASS" if is_clean else "BLOCKED_BY_LOOKAHEAD_GUARD",
        "contract_only": True,
    }
