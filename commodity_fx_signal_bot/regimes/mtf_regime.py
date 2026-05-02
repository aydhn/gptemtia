"""
MTF regime detection module.
"""

import pandas as pd
import numpy as np

from regimes.regime_config import RegimeProfile, get_default_regime_profile
from regimes.regime_labels import MTF_ALIGNED_TREND, MTF_CONFLICT, UNKNOWN
from regimes.regime_features import safe_get_column, combine_scores


def calculate_mtf_regime_score(df: pd.DataFrame) -> pd.Series:
    """Calculate MTF alignment score (-1 to 1)."""
    scores = []

    align = safe_get_column(df, ["mtf_trend_alignment_score"])
    if align is not None:
        scores.append(align)

    mom_align = safe_get_column(df, ["mtf_momentum_alignment_score"])
    if mom_align is not None:
        scores.append(mom_align)

    combined = combine_scores(scores)
    if not combined.empty:
        return combined.clip(-1, 1)
    return pd.Series(np.nan, index=df.index)


def detect_mtf_regime(
    df: pd.DataFrame, profile: RegimeProfile | None = None
) -> tuple[pd.DataFrame, dict]:
    """Detect MTF regimes."""
    if profile is None:
        profile = get_default_regime_profile()

    out_df = pd.DataFrame(index=df.index)
    summary = {"input_rows": len(df), "warnings": [], "used_columns": []}

    score = calculate_mtf_regime_score(df)

    conflict = safe_get_column(df, ["mtf_conflict_score"])

    out_df["regime_mtf_score"] = score

    if score.isna().all():
        summary["warnings"].append("Insufficient data to calculate MTF regimes.")
        out_df["regime_mtf_label"] = UNKNOWN
        return out_df, summary

    is_aligned = score.abs() > 0.6

    is_conflict = False
    if conflict is not None:
        is_conflict = conflict > 0.6
        out_df["regime_is_mtf_conflict"] = is_conflict
    else:
        out_df["regime_is_mtf_conflict"] = False

    out_df["regime_is_mtf_aligned"] = is_aligned & ~out_df["regime_is_mtf_conflict"]

    labels = pd.Series(UNKNOWN, index=df.index)

    labels[out_df["regime_is_mtf_conflict"]] = MTF_CONFLICT
    labels[out_df["regime_is_mtf_aligned"]] = MTF_ALIGNED_TREND

    out_df["regime_mtf_label"] = labels

    return out_df, summary
