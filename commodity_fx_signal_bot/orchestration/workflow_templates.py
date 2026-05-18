"""
Predefined workflow templates representing sequences of jobs.
"""

from dataclasses import dataclass, asdict
from typing import List, Tuple
from orchestration.orchestration_models import PipelineJob

@dataclass(frozen=True)
class WorkflowTemplate:
    name: str
    description: str
    job_names: Tuple[str, ...]
    enabled: bool = True
    notes: str = ""

_TEMPLATES = [
    WorkflowTemplate(
        name="healthcheck_workflow",
        description="Checks system dependencies and status.",
        job_names=(
            "dependency_check_job",
            "workflow_status_job",
            "quality_status_job"
        )
    ),
    WorkflowTemplate(
        name="daily_research_workflow",
        description="Standard daily research run through paper trading.",
        job_names=(
            "data_download_job",
            "data_quality_job",
            "processed_ohlcv_job",
            "technical_features_job",
            "indicator_events_job",
            "mtf_features_job",
            "regime_features_job",
            "macro_features_job",
            "asset_profile_features_job",
            "signal_candidates_job",
            "decision_candidates_job",
            "strategy_candidates_job",
            "strategy_rule_candidates_job",
            "risk_candidates_job",
            "sizing_candidates_job",
            "level_candidates_job",
            "paper_trading_job",
            "notification_status_job"
        )
    ),
    WorkflowTemplate(
        name="full_research_workflow",
        description="Complete research run including ML and backtesting.",
        job_names=(
            "data_download_job",
            "data_quality_job",
            "processed_ohlcv_job",
            "technical_features_job",
            "indicator_events_job",
            "mtf_features_job",
            "regime_features_job",
            "macro_features_job",
            "asset_profile_features_job",
            "signal_candidates_job",
            "decision_candidates_job",
            "strategy_candidates_job",
            "strategy_rule_candidates_job",
            "risk_candidates_job",
            "sizing_candidates_job",
            "level_candidates_job",
            "backtest_job",
            "performance_analysis_job",
            "benchmark_comparison_job",
            "walk_forward_validation_job",
            "parameter_sensitivity_job",
            "ml_dataset_job",
            "ml_training_job",
            "ml_prediction_job",
            "ml_integration_job",
            "paper_trading_job",
            "telegram_daily_digest_job"
        )
    ),
    WorkflowTemplate(
        name="paper_reporting_workflow",
        description="Focused on execution candidates and reporting.",
        job_names=(
            "risk_candidates_job",
            "sizing_candidates_job",
            "level_candidates_job",
            "paper_trading_job",
            "telegram_daily_digest_job"
        )
    ),
    WorkflowTemplate(
        name="ml_research_workflow",
        description="Focused on ML dataset, training, and prediction.",
        job_names=(
            "ml_dataset_job",
            "ml_training_job",
            "ml_prediction_job",
            "ml_integration_job"
        )
    ),
    WorkflowTemplate(
        name="debug_symbol_workflow",
        description="Quick path for debugging a single symbol.",
        job_names=(
            "processed_ohlcv_job",
            "technical_features_job",
            "signal_candidates_job",
            "decision_candidates_job",
            "strategy_candidates_job",
            "risk_candidates_job",
            "sizing_candidates_job",
            "level_candidates_job",
            "paper_trading_job"
        )
    )
]

def list_workflow_templates(enabled_only: bool = True) -> List[WorkflowTemplate]:
    if enabled_only:
        return [t for t in _TEMPLATES if t.enabled]
    return list(_TEMPLATES)

def get_workflow_template(name: str) -> WorkflowTemplate:
    for t in _TEMPLATES:
        if t.name == name:
            return t
    raise ValueError(f"Unknown workflow template: {name}")

def validate_workflow_templates(registered_jobs: List[PipelineJob]) -> dict:
    registered_ids = {j.job_id for j in registered_jobs}
    invalid_refs = []

    for template in _TEMPLATES:
        for job_name in template.job_names:
            if job_name not in registered_ids:
                invalid_refs.append(f"{template.name} -> {job_name}")

    return {
        "valid": len(invalid_refs) == 0,
        "invalid_references": invalid_refs
    }

def workflow_template_to_dict(template: WorkflowTemplate) -> dict:
    return asdict(template)
