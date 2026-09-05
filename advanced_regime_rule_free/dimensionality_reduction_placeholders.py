"""Phase 128: Dimensionality Reduction Placeholders.

Defines non-executable metadata placeholders for PCA, UMAP, t-SNE, and Autoencoder techniques.
"""

from typing import Dict, Tuple
import pandas as pd

from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_models import AlgorithmPlaceholder

DIMENSIONALITY_REDUCTION_PLACEHOLDERS = [
    AlgorithmPlaceholder(
        algorithm_id="pca_placeholder",
        family="dimensionality_reduction",
        description="Placeholder for Principal Component Analysis (PCA) orthogonal projection specification.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="umap_placeholder",
        family="dimensionality_reduction",
        description="Placeholder for Uniform Manifold Approximation and Projection (UMAP) non-linear manifold specification.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="tsne_placeholder",
        family="dimensionality_reduction",
        description="Placeholder for t-Distributed Stochastic Neighbor Embedding (t-SNE) low-dimensional visualization specification.",
    ),
    AlgorithmPlaceholder(
        algorithm_id="autoencoder_placeholder",
        family="dimensionality_reduction",
        description="Placeholder for neural Autoencoder bottleneck representation specification (no model training executed).",
    ),
]


def build_dimensionality_reduction_placeholder_registry(
    profile: RegimeRuleFreeProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary metadata for dimensionality reduction placeholders."""
    active_profile = profile or get_default_regime_rule_free_profile()

    rows = []
    for d in DIMENSIONALITY_REDUCTION_PLACEHOLDERS:
        row = d.__dict__.copy()
        row["current_phase"] = active_profile.current_phase
        row["next_phase"] = active_profile.next_phase
        row["target_final_phase"] = active_profile.target_final_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_dimensionality_reduction_placeholders(df)
    return df, summary


def summarize_dimensionality_reduction_placeholders(df: pd.DataFrame) -> Dict:
    """Summarize dimensionality reduction placeholders."""
    total = len(df)
    all_placeholders = bool(df["is_placeholder_only"].all()) if not df.empty else True
    all_non_executable = bool((~df["execution_permitted"]).all()) if not df.empty else True
    all_non_signal = bool(df["non_signal"].all()) if not df.empty else True

    return {
        "total_dim_reduction_placeholders": total,
        "all_placeholders_only": all_placeholders,
        "all_execution_forbidden": all_non_executable,
        "all_non_signal": all_non_signal,
        "status": "VALID" if all_placeholders and all_non_executable else "INVALID",
    }
