"""Phase 129: Behavior Diagnostics Metric Registry.

Registers and evaluates multi-domain diagnostics metrics across volatility,
trend, range, macro/event, news metadata, cross-asset, transition, and stability.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

CORE_BEHAVIOR_DIAGNOSTICS_METRICS = [
    {
        "metric_name": "volatility_behavior_context_coverage",
        "domain": "volatility_behavior_domain",
        "behavior_family": "volatility",
        "description": "Coverage of high/low/compression/expansion volatility context metrics.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "trend_behavior_context_coverage",
        "domain": "trend_behavior_domain",
        "behavior_family": "trend",
        "description": "Coverage of moving average, momentum, and persistence trend context indicators.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "range_behavior_context_coverage",
        "domain": "range_behavior_domain",
        "behavior_family": "range",
        "description": "Coverage of channel width, z-score deviation, and mean reversion range context.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "macro_event_context_coverage",
        "domain": "macro_event_behavior_domain",
        "behavior_family": "macro_event",
        "description": "Availability of release lag, scheduled event windows, and surprise context.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "news_metadata_context_coverage",
        "domain": "news_metadata_behavior_domain",
        "behavior_family": "news_metadata",
        "description": "Metadata-only news topic and asset tag frequency coverage (zero full-text).",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "cross_asset_context_coverage",
        "domain": "cross_asset_behavior_domain",
        "behavior_family": "cross_asset",
        "description": "Coverage of cross-asset alignment, currency pairs, and commodity benchmarks.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "transition_readiness_score",
        "domain": "transition_readiness_domain",
        "behavior_family": "transition",
        "description": "Score quantifying readiness for Phase 130 state transition sequence analysis.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "stability_readiness_score",
        "domain": "stability_readiness_domain",
        "behavior_family": "stability",
        "description": "Score quantifying readiness for Phase 130 rolling stability diagnostic metrics.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "timestamp_alignment_quality",
        "domain": "market_behavior_diagnostics_domain",
        "behavior_family": "temporal",
        "description": "Quality score verifying UTC timestamp monotonicity and temporal integrity.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
    {
        "metric_name": "no_lookahead_dependency_status",
        "domain": "market_behavior_diagnostics_domain",
        "behavior_family": "safety",
        "description": "Status verifying zero backward leakage and zero future shift across dependencies.",
        "value_type": "float",
        "coverage_ratio": 1.0,
        "is_ready": True,
    },
]


def build_behavior_diagnostics_metric_registry(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and metadata summary for all behavior diagnostics metrics."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_BEHAVIOR_DIAGNOSTICS_METRICS:
        row = dict(item)
        row["non_signal"] = True
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_behavior_diagnostics_metrics(df)
    return df, summary


def summarize_behavior_diagnostics_metrics(df: pd.DataFrame) -> dict:
    """Summarize behavior diagnostics metric inventory."""
    return {
        "total_metrics": len(df),
        "ready_metrics_count": int(df["is_ready"].sum()) if not df.empty and "is_ready" in df.columns else 0,
        "average_coverage": float(df["coverage_ratio"].mean()) if not df.empty and "coverage_ratio" in df.columns else 0.0,
        "all_non_signal": True,
        "metric_names": df["metric_name"].tolist() if not df.empty and "metric_name" in df.columns else [],
    }
