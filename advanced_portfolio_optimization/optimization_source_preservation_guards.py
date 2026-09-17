# -*- coding: utf-8 -*-
"""Phase 154: Source Preservation Guards."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_source_preservation_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build source preservation guard registry."""
    records = [{
        "guard_name": "optimization_source_preservation_guard",
        "description": "Kaynak verilerin ezilmesini, silinmesini ve yikici temizligini engelleme",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_source_preservation_guard",
        "is_active": True,
    }
    return df, summary


def validate_optimization_source_preservation_action(action: str) -> Dict:
    """Ensure action does not overwrite source data."""
    prohibited = ["overwrite", "delete", "drop_in_place", "destructive_cleaning", "auto_impute"]
    blocked = any(p in action.lower() for p in prohibited)
    return {
        "blocked": blocked,
        "action": action,
        "message": f"Action '{action}' is blocked by source preservation guard" if blocked else "OK",
    }
