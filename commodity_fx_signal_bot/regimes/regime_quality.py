"""
Quality reporting for regimes.
"""

import pandas as pd
import numpy as np

def check_regime_missing_columns(df: pd.DataFrame, required_candidates: dict) -> dict:
    """Check which required features are missing."""
    missing = []

    for feature_type, candidates in required_candidates.items():
        found = False
        for c in candidates:
            if c in df.columns and not df[c].isna().all():
                found = True
                break
        if not found:
            missing.append(feature_type)

    return {
        "missing_key_columns": missing,
        "is_missing": len(missing) > 0
    }

def check_regime_label_distribution(regime_df: pd.DataFrame) -> dict:
    """Analyze the distribution of regime labels."""
    if "regime_primary_label" not in regime_df.columns:
        return {}

    counts = regime_df["regime_primary_label"].value_counts().to_dict()
    total = len(regime_df)

    distribution = {}
    if total > 0:
        for k, v in counts.items():
            distribution[str(k)] = float(v / total)

    return distribution

def check_regime_confidence(regime_df: pd.DataFrame) -> dict:
    """Analyze the confidence levels."""
    if "regime_confidence" not in regime_df.columns:
        return {"average_confidence": 0.0, "low_confidence_ratio": 1.0}

    conf = regime_df["regime_confidence"]
    # Exclude NaNs
    valid_conf = conf.dropna()

    if valid_conf.empty:
        return {"average_confidence": 0.0, "low_confidence_ratio": 1.0}

    avg = float(valid_conf.mean())
    low_ratio = float((valid_conf < 0.5).sum() / len(valid_conf))

    return {
        "average_confidence": avg,
        "low_confidence_ratio": low_ratio
    }

def check_regime_stability(regime_df: pd.DataFrame, window: int = 20) -> dict:
    """Analyze how stable the regimes are over time."""
    if "regime_primary_label" not in regime_df.columns:
        return {"transition_count": 0, "stability_score": 0.0}

    labels = regime_df["regime_primary_label"]
    valid_labels = labels.dropna()

    if len(valid_labels) < 2:
        return {"transition_count": 0, "stability_score": 1.0}

    # Count transitions
    transitions = (valid_labels != valid_labels.shift(1)).sum() - 1 # Subtract 1 for the first element
    if transitions < 0:
        transitions = 0

    # Stability score: 1.0 = no transitions, 0.0 = transitioning every bar
    # A transition every N bars gives a score of 1 - 1/N
    max_transitions = len(valid_labels) - 1
    if max_transitions > 0:
        stability = 1.0 - (transitions / max_transitions)
    else:
        stability = 1.0

    return {
        "transition_count": int(transitions),
        "stability_score": float(stability)
    }

def build_regime_quality_report(regime_df: pd.DataFrame, summary: dict) -> dict:
    """Build the comprehensive quality report."""

    dist = check_regime_label_distribution(regime_df)
    conf = check_regime_confidence(regime_df)
    stab = check_regime_stability(regime_df)

    # Check if we have the critical score columns
    critical_scores = {
        "trend": ["regime_trend_score"],
        "volatility": ["regime_volatility_score"],
        "range": ["regime_range_score"],
        "momentum": ["regime_momentum_score"]
    }
    missing = check_regime_missing_columns(regime_df, critical_scores)

    warnings = list(summary.get("warnings", []))

    if conf["low_confidence_ratio"] > 0.5:
        warnings.append("High ratio of low confidence regimes.")

    if stab["stability_score"] < 0.3:
        warnings.append("Regimes are highly unstable (frequent transitions).")

    if missing["is_missing"]:
        warnings.append(f"Missing critical scores: {missing['missing_key_columns']}")

    passed = len(warnings) == 0 and conf["average_confidence"] > 0.4

    return {
        "rows": len(regime_df),
        "columns": len(regime_df.columns),
        "label_distribution": dist,
        "average_confidence": conf["average_confidence"],
        "low_confidence_ratio": conf["low_confidence_ratio"],
        "transition_count": stab["transition_count"],
        "stability_score": stab["stability_score"],
        "missing_key_columns": missing["missing_key_columns"],
        "warnings": warnings,
        "passed": passed
    }
