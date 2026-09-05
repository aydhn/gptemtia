"""Phase 128: Distance Metric Placeholders.

Defines non-executable distance metric placeholders for future geometric state computations.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import AlgorithmPlaceholder

DISTANCE_METRIC_PLACEHOLDERS = [
    AlgorithmPlaceholder(
        algorithm_id="euclidean_placeholder",
        family="distance_metric",
        description="Standard L2 Euclidean distance specification for normalized continuous features.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="cosine_placeholder",
        family="distance_metric",
        description="Cosine angular distance specification for directional feature vectors.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="manhattan_placeholder",
        family="distance_metric",
        description="L1 Manhattan distance specification robust to isolated outliers.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="correlation_distance_placeholder",
        family="distance_metric",
        description="1 - Pearson correlation distance specification for cross-asset behavior shape similarity.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="dynamic_time_warping_placeholder",
        family="distance_metric",
        description="Dynamic Time Warping (DTW) distance specification for non-linear temporal sequence alignment.",
    ),
]


def build_distance_metric_placeholder_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for distance metric placeholders."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for m in DISTANCE_METRIC_PLACEHOLDERS:
        row = m.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_distance_metric_placeholders(df)
    return df, summary


def summarize_distance_metric_placeholders(df: pd.DataFrame) -> Dict:
    """Summarize distance metric placeholders."""
    total = len(df)
    all_placeholders = bool(df["is_placeholder_only"].all()) if not df.empty else True
    all_non_executable = bool((~df["execution_permitted"]).all()) if not df.empty else True

    return {
        "total_distance_metrics": total,
        "all_placeholders_only": all_placeholders,
        "all_execution_forbidden": all_non_executable,
        "metrics_status": "VALID" if all_placeholders and all_non_executable else "INVALID",
    }
