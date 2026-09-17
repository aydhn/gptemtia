# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Construction Profile Registry."""

from typing import Dict, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile, PROFILES
from .portfolio_construction_labels import (
    PORTFOLIO_CONSTRUCTION_PROFILE_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)


def build_portfolio_construction_profile_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and metadata summary for portfolio construction profiles."""
    rows = []
    for p_name, p in PROFILES.items():
        rows.append({
            "profile_name": p.profile_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "min_readiness_score": p.min_readiness_score,
            "non_signal": True,
            "allow_live_trading": p.allow_live_trading,
            "allow_portfolio_construction": p.allow_portfolio_construction,
            "allow_position_sizing": p.allow_position_sizing,
            "allow_capital_allocation": p.allow_capital_allocation,
            "allow_optimizer_execution": p.allow_optimizer_execution,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_CONSTRUCTION_PROFILE_DOMAIN,
        "active_profile": profile.profile_name,
        "total_profiles": len(df),
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_research_only": bool(df["research_only"].all()),
        "all_non_signal": True,
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def summarize_portfolio_construction_profiles(df: pd.DataFrame) -> Dict:
    """Summarize portfolio construction profiles."""
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty else [],
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "non_signal": True,
    }
