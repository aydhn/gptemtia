"""
Parameter sensitivity analysis module.
"""

import logging
import pandas as pd
import numpy as np
from typing import Tuple

logger = logging.getLogger(__name__)


def build_parameter_result_table(results: list[dict]) -> pd.DataFrame:
    """
    Builds a flat DataFrame combining parameters and performance metrics.
    """
    if not results:
        return pd.DataFrame()

    flat_results = []
    for res in results:
        flat_res = {}
        # Assuming res has a 'parameters' dict or similar structure
        if 'parameters' in res:
            for k, v in res['parameters'].items():
                flat_res[f"param_{k}"] = v

        # Also copy over the performance metrics directly
        for k, v in res.items():
            if k != 'parameters' and not isinstance(v, dict) and not isinstance(v, list):
                flat_res[k] = v

        # If there are nested summaries, extract primary metrics
        if 'test_summary' in res and isinstance(res['test_summary'], dict):
            flat_res['test_sharpe_ratio'] = res['test_summary'].get('sharpe_ratio', 0.0)
            flat_res['test_total_return_pct'] = res['test_summary'].get('total_return_pct', 0.0)
            flat_res['test_max_drawdown_pct'] = res['test_summary'].get('max_drawdown_pct', 0.0)

        flat_results.append(flat_res)

    return pd.DataFrame(flat_results)


def calculate_parameter_sensitivity(result_table: pd.DataFrame, metric: str = "test_sharpe_ratio") -> pd.DataFrame:
    """
    Calculates sensitivity of a metric to different parameter values.
    """
    if result_table.empty or metric not in result_table.columns:
        logger.warning(f"Result table is empty or missing metric '{metric}'")
        return pd.DataFrame()

    param_cols = [c for c in result_table.columns if c.startswith('param_')]

    sensitivity_rows = []
    for p_col in param_cols:
        param_name = p_col.replace('param_', '')

        # Group by parameter value
        grouped = result_table.groupby(p_col)[metric]

        for p_val, group in grouped:
            mean_val = group.mean()
            std_val = group.std() if len(group) > 1 else 0.0

            sensitivity_rows.append({
                "parameter_name": param_name,
                "parameter_value": str(p_val),
                "metric_mean": float(mean_val),
                "metric_median": float(group.median()),
                "metric_std": float(std_val),
                "metric_min": float(group.min()),
                "metric_max": float(group.max()),
                "metric_range": float(group.max() - group.min()),
                "sample_count": len(group)
            })

    sensitivity_df = pd.DataFrame(sensitivity_rows)

    # Calculate sensitivity score (normalized range relative to mean)
    if not sensitivity_df.empty:
        overall_mean = result_table[metric].mean()
        if abs(overall_mean) > 1e-6:
            sensitivity_df['sensitivity_score'] = sensitivity_df['metric_range'] / abs(overall_mean)
        else:
            sensitivity_df['sensitivity_score'] = sensitivity_df['metric_range']

        # Determine fragility warning
        sensitivity_df['fragility_warning'] = sensitivity_df.apply(
            lambda row: "High variance" if row['metric_std'] > abs(row['metric_mean']) and row['sample_count'] > 2 else "",
            axis=1
        )

    return sensitivity_df


def calculate_metric_stability_across_parameters(result_table: pd.DataFrame, metric: str = "test_sharpe_ratio") -> dict:
    """
    Calculates overall stability of a metric across all parameter combinations.
    """
    if result_table.empty or metric not in result_table.columns:
        return {"stability_score": 0.0, "is_stable": False}

    metric_series = result_table[metric]
    mean_val = metric_series.mean()
    std_val = metric_series.std() if len(metric_series) > 1 else 0.0

    cv = std_val / abs(mean_val) if abs(mean_val) > 1e-6 else float('inf')

    # Score from 0 to 1, where lower CV is better
    stability_score = max(0.0, 1.0 - min(1.0, cv))

    positive_ratio = (metric_series > 0).mean()

    return {
        "metric": metric,
        "mean": float(mean_val),
        "std": float(std_val),
        "cv": float(cv),
        "stability_score": float(stability_score),
        "positive_ratio": float(positive_ratio),
        "is_stable": stability_score >= 0.5 and positive_ratio >= 0.5
    }


def identify_fragile_parameters(result_table: pd.DataFrame, metric: str = "test_sharpe_ratio") -> pd.DataFrame:
    """Identifies specific parameters that cause significant metric degradation."""
    sensitivity_df = calculate_parameter_sensitivity(result_table, metric)
    if sensitivity_df.empty:
        return pd.DataFrame()

    fragile = sensitivity_df[sensitivity_df['fragility_warning'] != ""]
    return fragile


def build_parameter_sensitivity_report(result_table: pd.DataFrame, primary_metric: str = "test_sharpe_ratio") -> Tuple[pd.DataFrame, dict]:
    """Builds a comprehensive parameter sensitivity report."""
    if result_table.empty:
         return pd.DataFrame(), {"warnings": ["Empty result table"]}

    if primary_metric not in result_table.columns:
         # Fallback to another metric if the primary is missing
         possible_metrics = ['sharpe_ratio', 'total_return_pct', 'test_sharpe_ratio', 'test_total_return_pct']
         for m in possible_metrics:
              if m in result_table.columns:
                   primary_metric = m
                   logger.info(f"Primary metric not found, falling back to {primary_metric}")
                   break
         else:
             return pd.DataFrame(), {"warnings": [f"Metric {primary_metric} not found in result table"]}

    sensitivity_df = calculate_parameter_sensitivity(result_table, primary_metric)
    stability = calculate_metric_stability_across_parameters(result_table, primary_metric)
    fragile_df = identify_fragile_parameters(result_table, primary_metric)

    warnings = []
    if not fragile_df.empty:
        warnings.append(f"Found {len(fragile_df)} fragile parameter values")
    if stability['stability_score'] < 0.3:
        warnings.append("Overall parameter stability is very low")

    summary = {
        "primary_metric": primary_metric,
        "combinations_tested": len(result_table),
        "overall_stability_score": stability['stability_score'],
        "positive_ratio": stability['positive_ratio'],
        "fragile_parameter_count": len(fragile_df),
        "warnings": warnings
    }

    return sensitivity_df, summary
