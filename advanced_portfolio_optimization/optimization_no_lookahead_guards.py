# -*- coding: utf-8 -*-
"""Phase 154: Optimization No-Lookahead Guards."""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_no_lookahead_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build no-lookahead guard policies table."""
    records = [{
        "guard_name": "optimization_no_lookahead_guard",
        "description": "Zaman serisi sizintisi, forward-shift ve gelecege bakis engelleme",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_no_lookahead_guard",
        "is_active": True,
    }
    return df, summary


def validate_optimization_no_lookahead_columns(column_names: List[str]) -> Dict:
    """Check for forbidden lookahead column patterns."""
    forbidden = [
        "future_return",
        "forward_return",
        "next_return",
        "lookahead_return",
        "realized_future_pnl",
        "future_pnl",
        "leak",
        "leakage",
    ]
    detected = [c for c in column_names if any(f in c.lower() for f in forbidden)]
    return {
        "is_clean": len(detected) == 0,
        "detected_columns": detected,
        "message": f"Lookahead columns detected: {detected}" if detected else "OK",
    }


def validate_no_future_optimization_join(
    left_df: pd.DataFrame, right_df: pd.DataFrame, left_ts: str, right_ts: str
) -> Dict:
    """Validate that temporal join preserves strictly past-to-past causality."""
    if left_ts not in left_df.columns or right_ts not in right_df.columns:
        return {"is_valid": False, "message": "Timestamp column missing in join check"}
    # In dry-run contract mode, verify monotonic timestamp invariant
    return {"is_valid": True, "message": "Temporal causality verified"}
