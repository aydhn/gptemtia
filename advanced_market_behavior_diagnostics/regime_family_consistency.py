"""Phase 129: Regime Family Consistency Report.

Evaluates inter-family consistency and validation dependency alignment across regime families.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.regime_family_quality import CORE_REGIME_FAMILIES


def build_regime_family_consistency_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build regime family consistency report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_REGIME_FAMILIES:
        rows.append(
            {
                "family_name": item["family_name"],
                "consistency_score": item["consistency_score"],
                "quality_drift_aligned": item["quality_drift_dependency_available"],
                "validation_aligned": item["validation_dependency_available"],
                "blocker_count": item["manual_review_blocker_count"],
                "consistency_status": "behavior_quality_ready" if item["consistency_score"] >= 0.85 else "behavior_quality_ready_with_warnings",
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_regime_family_consistency(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_family_consistency(df: pd.DataFrame) -> dict:
    """Summarize regime family consistency."""
    if df.empty:
        return {
            "total_families": 0,
            "average_consistency": 0.0,
            "non_signal": True,
        }
    return {
        "total_families": len(df),
        "average_consistency": float(df["consistency_score"].mean()) if "consistency_score" in df.columns else 0.0,
        "total_blockers": int(df["blocker_count"].sum()) if "blocker_count" in df.columns else 0,
        "non_signal": True,
    }
