import pandas as pd
from typing import Optional, Any
from experiments.experiment_models import ExperimentRunManifest

def extract_metrics_from_meta_research(report: Optional[dict] = None, ranking_df: Optional[pd.DataFrame] = None) -> dict:
    metrics = {}
    if report:
        summary = report.get("summary", {})
        metrics["quality_adjusted_score"] = summary.get("mean_quality_score", 0.0)
        metrics["consensus_score"] = summary.get("mean_consensus", 0.0)
        metrics["uncertainty_score"] = summary.get("mean_uncertainty", 0.0)
        metrics["conflict_score"] = summary.get("conflict_ratio", 0.0)
        metrics["warning_count"] = summary.get("warning_count", 0)
        metrics["missing_source_count"] = summary.get("missing_sources", 0)

    if ranking_df is not None and not ranking_df.empty:
        if "quality_adjusted_score" in ranking_df.columns:
            metrics["quality_adjusted_score"] = ranking_df["quality_adjusted_score"].mean()

    return metrics

def extract_metrics_from_factor_research(report: Optional[dict] = None, backtest_df: Optional[pd.DataFrame] = None) -> dict:
    metrics = {}
    if report:
        metrics["factor_ic_proxy"] = report.get("mean_ic", 0.0)
        metrics["factor_stability_score"] = report.get("stability_score", 0.0)
    return metrics

def extract_metrics_from_portfolio_research(report: Optional[dict] = None, performance_df: Optional[pd.DataFrame] = None) -> dict:
    metrics = {}
    if report:
        metrics["portfolio_diversification_score"] = report.get("diversification_score", 0.0)
        metrics["regime_stress_score"] = report.get("stress_score", 0.0)
    return metrics

def extract_metrics_from_validation(report: Optional[dict] = None) -> dict:
    metrics = {}
    if report:
        metrics["validation_score"] = report.get("mean_validation_score", 0.0)
    return metrics

def extract_metrics_from_paper(report: Optional[dict] = None) -> dict:
    metrics = {}
    if report:
        metrics["paper_virtual_return"] = report.get("virtual_return", 0.0)
        metrics["paper_virtual_drawdown"] = report.get("virtual_drawdown", 0.0)
    return metrics

def normalize_experiment_metrics(metrics: dict) -> dict:
    standard_keys = [
        "research_score",
        "quality_adjusted_score",
        "consensus_score",
        "confidence_score",
        "uncertainty_score",
        "conflict_score",
        "validation_score",
        "backtest_score",
        "factor_ic_proxy",
        "factor_stability_score",
        "portfolio_diversification_score",
        "regime_stress_score",
        "paper_virtual_return",
        "paper_virtual_drawdown",
        "warning_count",
        "missing_source_count",
        "quality_score",
        "reproducibility_score"
    ]

    normalized = {}
    for key in standard_keys:
        if key in metrics:
            normalized[key] = metrics[key]

    # Include any custom keys that are numbers
    for k, v in metrics.items():
        if k not in normalized and isinstance(v, (int, float)):
            normalized[k] = v

    return normalized

def build_experiment_metric_table(run_manifests: list[ExperimentRunManifest] | list[dict]) -> pd.DataFrame:
    rows = []
    for m in run_manifests:
        if isinstance(m, dict):
            run_id = m.get("run_id")
            metrics = m.get("metrics", {})
        else:
            run_id = m.run_id
            metrics = m.metrics

        row = {"run_id": run_id}
        norm = normalize_experiment_metrics(metrics)
        row.update(norm)
        rows.append(row)

    return pd.DataFrame(rows)

def summarize_experiment_metrics(metric_df: pd.DataFrame) -> dict:
    if metric_df.empty:
        return {}

    summary = {}
    for col in metric_df.columns:
        if col != "run_id" and pd.api.types.is_numeric_dtype(metric_df[col]):
            summary[f"mean_{col}"] = metric_df[col].mean()
            summary[f"max_{col}"] = metric_df[col].max()
            summary[f"min_{col}"] = metric_df[col].min()

    return summary
