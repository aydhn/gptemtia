"""Phase 129: Regime Family Coverage Report.

Evaluates coverage of features, factors, and contexts across all recognized regime families.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.regime_family_quality import CORE_REGIME_FAMILIES


def build_regime_family_coverage_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build regime family coverage report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_REGIME_FAMILIES:
        rows.append(
            {
                "family_name": item["family_name"],
                "features_coverage_ratio": 1.0 if item["source_features_available"] else 0.0,
                "factors_coverage_ratio": 1.0 if item["source_factors_available"] else 0.0,
                "context_coverage_ratio": 1.0 if item["source_context_available"] else 0.0,
                "overall_family_coverage": item["coverage_ratio"],
                "coverage_status": "behavior_quality_ready",
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_regime_family_coverage(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_family_coverage(df: pd.DataFrame) -> dict:
    """Summarize regime family coverage."""
    if df.empty:
        return {
            "total_families": 0,
            "average_coverage": 0.0,
            "non_signal": True,
        }
    return {
        "total_families": len(df),
        "average_coverage": float(df["overall_family_coverage"].mean()) if "overall_family_coverage" in df.columns else 0.0,
        "all_families_covered": bool((df["overall_family_coverage"] >= 0.90).all()) if "overall_family_coverage" in df.columns else False,
        "non_signal": True,
    }
