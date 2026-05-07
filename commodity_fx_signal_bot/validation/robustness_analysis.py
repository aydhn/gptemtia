"""
Robustness analysis for validation results.
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


def calculate_train_test_degradation(train_metric: float, test_metric: float) -> float:
    """
    Calculates the degradation from train to test period.
    Returns a value where 0 is no degradation (or improvement) and 1 is total degradation.
    """
    if train_metric <= 0:
        if test_metric > 0:
            return 0.0 # Improved from negative to positive
        elif test_metric > train_metric:
            return 0.0 # Still negative but improved
        else:
            return 1.0 # Was bad, got worse

    if test_metric >= train_metric:
        return 0.0 # No degradation

    if test_metric <= 0:
        return 1.0 # Complete degradation

    return (train_metric - test_metric) / train_metric


def calculate_split_consistency(walk_forward_df: pd.DataFrame, metric_col: str = "test_sharpe_ratio") -> float:
    """
    Calculates consistency of a metric across walk-forward splits.
    Returns a score from 0 (inconsistent) to 1 (highly consistent).
    """
    if walk_forward_df.empty or metric_col not in walk_forward_df.columns:
        return 0.0

    metric_series = walk_forward_df[metric_col]

    # If all values are 0, it's consistent but not good
    if metric_series.abs().max() < 1e-6:
        return 0.0

    std_val = metric_series.std()
    mean_val = metric_series.mean()

    # Coeff of variation
    if abs(mean_val) < 1e-6:
        cv = 1.0 # High relative variance
    else:
        cv = std_val / abs(mean_val)

    # Convert CV to a 0-1 score
    score = max(0.0, 1.0 - min(1.0, cv))
    return float(score)


def calculate_positive_split_ratio(walk_forward_df: pd.DataFrame, metric_col: str = "test_total_return_pct") -> float:
    """Calculates the ratio of splits with a positive metric."""
    if walk_forward_df.empty or metric_col not in walk_forward_df.columns:
        return 0.0
    return float((walk_forward_df[metric_col] > 0).mean())


def calculate_metric_variability(walk_forward_df: pd.DataFrame, metric_col: str = "test_sharpe_ratio") -> float:
    """Calculates standard deviation of a metric across splits."""
    if walk_forward_df.empty or metric_col not in walk_forward_df.columns:
        return 0.0
    return float(walk_forward_df[metric_col].std())


def calculate_robustness_score(walk_forward_df: pd.DataFrame, primary_metric: str = "test_sharpe_ratio") -> dict:
    """
    Calculates an overall robustness score based on split consistency, positive ratio, and degradation.
    """
    if walk_forward_df.empty:
        return {
            "robustness_score": 0.0,
            "components": {}
        }

    # Basic metrics
    consistency = calculate_split_consistency(walk_forward_df, primary_metric)

    return_metric = "test_total_return_pct" if "test_total_return_pct" in walk_forward_df.columns else primary_metric
    positive_ratio = calculate_positive_split_ratio(walk_forward_df, return_metric)

    # Degradation across all valid splits
    avg_train = walk_forward_df["train_sharpe_ratio"].mean() if "train_sharpe_ratio" in walk_forward_df.columns else 0.0
    avg_test = walk_forward_df["test_sharpe_ratio"].mean() if "test_sharpe_ratio" in walk_forward_df.columns else 0.0
    degradation = calculate_train_test_degradation(avg_train, avg_test)

    # Composite score (weights are heuristic)
    score = (consistency * 0.4) + (positive_ratio * 0.4) + ((1.0 - degradation) * 0.2)
    score = max(0.0, min(1.0, score))

    return {
        "robustness_score": float(score),
        "components": {
            "consistency": consistency,
            "positive_ratio": positive_ratio,
            "degradation": degradation
        }
    }


def build_robustness_report(walk_forward_df: pd.DataFrame) -> dict:
    """Builds a comprehensive robustness report."""
    if walk_forward_df.empty:
        return {
            "robustness_score": 0.0,
            "positive_split_ratio": 0.0,
            "split_consistency": 0.0,
            "train_test_degradation": 1.0,
            "metric_variability": 0.0,
            "warnings": ["Empty walk-forward data provided"]
        }

    warnings = []
    if len(walk_forward_df) < 3:
        warnings.append("Less than 3 walk-forward splits. Robustness score may not be reliable.")

    robustness = calculate_robustness_score(walk_forward_df)
    comp = robustness["components"]

    if comp.get("positive_ratio", 0.0) < 0.5:
        warnings.append("Less than 50% of test splits were profitable.")

    if comp.get("degradation", 0.0) > 0.5:
         warnings.append("Severe performance degradation from train to test periods.")

    return {
        "robustness_score": robustness["robustness_score"],
        "positive_split_ratio": comp.get("positive_ratio", 0.0),
        "split_consistency": comp.get("consistency", 0.0),
        "train_test_degradation": comp.get("degradation", 1.0),
        "metric_variability": calculate_metric_variability(walk_forward_df),
        "warnings": warnings
    }
