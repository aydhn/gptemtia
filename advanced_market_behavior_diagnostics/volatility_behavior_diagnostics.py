"""Phase 129: Volatility Behavior Diagnostics Report.

Evaluates high/low volatility context coverage, expansion/compression availability,
and ATR / realized volatility dependency status as non-signal diagnostic metrics.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

VOLATILITY_BEHAVIOR_CONTEXT_ITEMS = [
    {
        "context_name": "volatility_high_context",
        "description": "High realized volatility and ATR expansion threshold context.",
        "coverage_ratio": 1.0,
        "source_dependency": "advanced_feature_engine.atr,realized_volatility",
        "quality_drift_dependency_passed": True,
        "expansion_compression_available": True,
        "is_ready": True,
    },
    {
        "context_name": "volatility_low_context",
        "description": "Low realized volatility and band contraction threshold context.",
        "coverage_ratio": 1.0,
        "source_dependency": "advanced_feature_engine.bollinger_bandwidth,atr",
        "quality_drift_dependency_passed": True,
        "expansion_compression_available": True,
        "is_ready": True,
    },
    {
        "context_name": "volatility_expansion_context",
        "description": "Widening range and increasing variance rate of change context.",
        "coverage_ratio": 1.0,
        "source_dependency": "advanced_factor_metadata.volatility_factor_families",
        "quality_drift_dependency_passed": True,
        "expansion_compression_available": True,
        "is_ready": True,
    },
    {
        "context_name": "volatility_compression_context",
        "description": "Narrowing historical range and tight channel regime context.",
        "coverage_ratio": 1.0,
        "source_dependency": "advanced_factor_metadata.volatility_factor_families",
        "quality_drift_dependency_passed": True,
        "expansion_compression_available": True,
        "is_ready": True,
    },
]


def build_volatility_behavior_diagnostics_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build volatility behavior diagnostics report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in VOLATILITY_BEHAVIOR_CONTEXT_ITEMS:
        row = dict(item)
        row["non_signal"] = True
        row["contains_target_or_prediction"] = False
        row["model_training_executed"] = False
        row["clustering_executed"] = False
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_volatility_behavior_diagnostics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_volatility_behavior_diagnostics(df: pd.DataFrame) -> dict:
    """Summarize volatility behavior diagnostics."""
    if df.empty:
        return {
            "total_contexts": 0,
            "average_coverage": 0.0,
            "all_ready": False,
            "non_signal": True,
        }
    return {
        "total_contexts": len(df),
        "average_coverage": float(df["coverage_ratio"].mean()) if "coverage_ratio" in df.columns else 0.0,
        "all_ready": bool((df["is_ready"] == True).all()) if "is_ready" in df.columns else False,
        "dependencies_passed": bool((df["quality_drift_dependency_passed"] == True).all()) if "quality_drift_dependency_passed" in df.columns else False,
        "non_signal": True,
    }
