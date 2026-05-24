import pandas as pd
from typing import Optional

from experiments.experiment_models import ExperimentComparison, build_experiment_comparison_id

def compare_experiment_metrics(baseline_metrics: dict, candidate_metrics: dict) -> dict:
    deltas = {}
    improved = []
    deteriorated = []
    neutral = []

    # Positive delta is good
    positive_is_good = [
        "quality_adjusted_score",
        "consensus_score",
        "confidence_score",
        "validation_score",
        "backtest_score",
        "factor_ic_proxy",
        "factor_stability_score",
        "portfolio_diversification_score",
        "regime_stress_score",
        "paper_virtual_return",
        "quality_score",
        "reproducibility_score"
    ]

    # Negative delta is good
    negative_is_good = [
        "uncertainty_score",
        "conflict_score",
        "paper_virtual_drawdown",
        "warning_count",
        "missing_source_count"
    ]

    all_keys = set(baseline_metrics.keys()).union(set(candidate_metrics.keys()))

    for k in all_keys:
        b_val = baseline_metrics.get(k, 0.0)
        c_val = candidate_metrics.get(k, 0.0)

        if not isinstance(b_val, (int, float)) or not isinstance(c_val, (int, float)):
            continue

        delta = c_val - b_val
        deltas[k] = delta

        if abs(delta) < 1e-6:
            neutral.append(k)
        elif k in positive_is_good:
            if delta > 0:
                improved.append(k)
            else:
                deteriorated.append(k)
        elif k in negative_is_good:
            if delta < 0:
                improved.append(k)
            else:
                deteriorated.append(k)
        else:
            # Custom metrics: assume positive is good if not specified
            if delta > 0:
                improved.append(k)
            else:
                deteriorated.append(k)

    return {
        "deltas": deltas,
        "improved": improved,
        "deteriorated": deteriorated,
        "neutral": neutral
    }

def infer_comparison_label(comparison_results: dict) -> str:
    improved = len(comparison_results["improved"])
    deteriorated = len(comparison_results["deteriorated"])

    if improved == 0 and deteriorated == 0:
        return "insufficient_comparison_data"
    elif improved > deteriorated and deteriorated == 0:
        return "candidate_better"
    elif deteriorated > improved and improved == 0:
        return "baseline_better"
    elif improved > 0 and deteriorated > 0:
        # Check core metrics for tie-breaking
        deltas = comparison_results["deltas"]
        q_delta = deltas.get("quality_adjusted_score", 0.0)
        if q_delta > 0.05:
            return "candidate_better"
        elif q_delta < -0.05:
            return "baseline_better"
        return "mixed_result"
    else:
        return "no_material_difference"

def compare_experiment_runs(baseline_manifest: Optional[dict], candidate_manifest: dict) -> ExperimentComparison:
    baseline_id = baseline_manifest.get("run_id") if baseline_manifest else None
    candidate_id = candidate_manifest.get("run_id", "unknown")

    cmp_id = build_experiment_comparison_id(baseline_id, candidate_id)

    b_metrics = baseline_manifest.get("metrics", {}) if baseline_manifest else {}
    c_metrics = candidate_manifest.get("metrics", {})

    results = compare_experiment_metrics(b_metrics, c_metrics)
    label = infer_comparison_label(results)

    summary = {
        "total_metrics_compared": len(results["deltas"]),
        "improved_count": len(results["improved"]),
        "deteriorated_count": len(results["deteriorated"])
    }

    return ExperimentComparison(
        comparison_id=cmp_id,
        baseline_run_id=baseline_id,
        candidate_run_id=candidate_id,
        comparison_label=label,
        metric_deltas=results["deltas"],
        improved_metrics=results["improved"],
        deteriorated_metrics=results["deteriorated"],
        neutral_metrics=results["neutral"],
        summary=summary,
        warnings=[]
    )

def build_experiment_comparison_table(comparisons: list[ExperimentComparison]) -> pd.DataFrame:
    rows = []
    for c in comparisons:
        row = {
            "comparison_id": c.comparison_id,
            "baseline_run_id": c.baseline_run_id,
            "candidate_run_id": c.candidate_run_id,
            "comparison_label": c.comparison_label,
            "improved_count": len(c.improved_metrics),
            "deteriorated_count": len(c.deteriorated_metrics)
        }
        for k, v in c.metric_deltas.items():
            row[f"delta_{k}"] = v
        rows.append(row)
    return pd.DataFrame(rows)

def summarize_experiment_comparisons(comparison_df: pd.DataFrame) -> dict:
    if comparison_df.empty:
        return {}

    return {
        "total_comparisons": len(comparison_df),
        "by_label": comparison_df["comparison_label"].value_counts().to_dict() if "comparison_label" in comparison_df.columns else {}
    }
