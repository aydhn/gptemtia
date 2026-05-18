"""
Registry of all available pipeline jobs in the system.
"""

from typing import List, Dict
from orchestration.orchestration_models import PipelineJob

def build_core_data_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="universe_build_job",
            job_name="Universe Build",
            job_type="data_job",
            description="Builds the universe of symbols.",
            script_module="scripts.run_universe_preview",
            callable_path=None,
            required_inputs=[],
            expected_outputs=["universe_list"],
            dependencies=[],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="data_download_job",
            job_name="Data Download",
            job_type="data_job",
            description="Downloads raw data from providers.",
            script_module="scripts.run_data_lake_update",
            callable_path=None,
            required_inputs=["universe_list"],
            expected_outputs=["raw_ohlcv"],
            dependencies=["universe_build_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="data_quality_job",
            job_name="Data Quality Check",
            job_type="data_job",
            description="Audits raw data quality.",
            script_module="scripts.run_data_quality_audit",
            callable_path=None,
            required_inputs=["raw_ohlcv"],
            expected_outputs=["data_quality_report"],
            dependencies=["data_download_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="processed_ohlcv_job",
            job_name="Process OHLCV",
            job_type="data_job",
            description="Cleans and processes raw data.",
            script_module="scripts.run_data_cleaning",
            callable_path=None,
            required_inputs=["raw_ohlcv"],
            expected_outputs=["processed_ohlcv"],
            dependencies=["data_download_job"],
            optional_dependencies=["data_quality_job"]
        )
    ]

def build_feature_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="technical_features_job",
            job_name="Technical Features",
            job_type="feature_job",
            description="Calculates technical indicators.",
            script_module="scripts.run_feature_generation", # Assumed existing or generic name
            callable_path=None,
            required_inputs=["processed_ohlcv"],
            expected_outputs=["technical_features"],
            dependencies=["processed_ohlcv_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="indicator_events_job",
            job_name="Indicator Events",
            job_type="feature_job",
            description="Generates indicator event features.",
            script_module="scripts.run_indicator_events",
            callable_path=None,
            required_inputs=["technical_features"],
            expected_outputs=["indicator_events"],
            dependencies=["technical_features_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="mtf_features_job",
            job_name="MTF Features",
            job_type="feature_job",
            description="Calculates multi-timeframe features.",
            script_module="scripts.run_mtf_features",
            callable_path=None,
            required_inputs=["processed_ohlcv"],
            expected_outputs=["mtf_features"],
            dependencies=["processed_ohlcv_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="regime_features_job",
            job_name="Regime Features",
            job_type="feature_job",
            description="Calculates regime classification features.",
            script_module="scripts.run_regime_features",
            callable_path=None,
            required_inputs=["processed_ohlcv", "technical_features"],
            expected_outputs=["regime_features"],
            dependencies=["technical_features_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="macro_features_job",
            job_name="Macro Features",
            job_type="feature_job",
            description="Calculates macro economic features.",
            script_module="scripts.run_macro_features",
            callable_path=None,
            required_inputs=["processed_ohlcv"],
            expected_outputs=["macro_features"],
            dependencies=["processed_ohlcv_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="asset_profile_features_job",
            job_name="Asset Profile Features",
            job_type="feature_job",
            description="Calculates asset profiling features.",
            script_module="scripts.run_asset_profile_batch_build",
            callable_path=None,
            required_inputs=["processed_ohlcv"],
            expected_outputs=["asset_profile_features"],
            dependencies=["processed_ohlcv_job"],
            optional_dependencies=[]
        )
    ]

def build_candidate_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="signal_candidates_job",
            job_name="Signal Candidates",
            job_type="candidate_job",
            description="Generates pre-signal candidates.",
            script_module="scripts.run_signal_candidates",
            callable_path=None,
            required_inputs=["technical_features", "indicator_events"],
            expected_outputs=["signal_candidates"],
            dependencies=["indicator_events_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="decision_candidates_job",
            job_name="Decision Candidates",
            job_type="candidate_job",
            description="Evaluates candidates for directional bias.",
            script_module="scripts.run_decision_candidates",
            callable_path=None,
            required_inputs=["signal_candidates"],
            expected_outputs=["decision_candidates"],
            dependencies=["signal_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="strategy_candidates_job",
            job_name="Strategy Candidates",
            job_type="candidate_job",
            description="Generates strategy-level candidates.",
            script_module="scripts.run_strategy_candidates",
            callable_path=None,
            required_inputs=["decision_candidates"],
            expected_outputs=["strategy_candidates"],
            dependencies=["decision_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="strategy_rule_candidates_job",
            job_name="Strategy Rule Candidates",
            job_type="candidate_job",
            description="Evaluates strategy rules.",
            script_module="scripts.run_strategy_rule_candidates",
            callable_path=None,
            required_inputs=["strategy_candidates"],
            expected_outputs=["strategy_rule_candidates"],
            dependencies=["strategy_candidates_job"],
            optional_dependencies=[]
        )
    ]

def build_risk_sizing_level_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="risk_candidates_job",
            job_name="Risk Candidates",
            job_type="risk_job",
            description="Evaluates risk metrics.",
            script_module="scripts.run_risk_candidates",
            callable_path=None,
            required_inputs=["strategy_candidates"],
            expected_outputs=["risk_candidates"],
            dependencies=["strategy_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="sizing_candidates_job",
            job_name="Sizing Candidates",
            job_type="sizing_job",
            description="Calculates position sizing candidates.",
            script_module="scripts.run_sizing_candidates",
            callable_path=None,
            required_inputs=["risk_candidates"],
            expected_outputs=["sizing_candidates"],
            dependencies=["risk_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="level_candidates_job",
            job_name="Level Candidates",
            job_type="level_job",
            description="Calculates take profit / stop loss levels.",
            script_module="scripts.run_level_candidates",
            callable_path=None,
            required_inputs=["sizing_candidates"],
            expected_outputs=["level_candidates"],
            dependencies=["sizing_candidates_job"],
            optional_dependencies=[]
        )
    ]

def build_backtest_performance_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="backtest_job",
            job_name="Backtest",
            job_type="backtest_job",
            description="Runs historical backtests on candidates.",
            script_module="scripts.run_backtest_batch",
            callable_path=None,
            required_inputs=["level_candidates"],
            expected_outputs=["backtest_trades", "backtest_equity_curve"],
            dependencies=["level_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="performance_analysis_job",
            job_name="Performance Analysis",
            job_type="performance_job",
            description="Analyzes backtest performance.",
            script_module="scripts.run_performance_analysis",
            callable_path=None,
            required_inputs=["backtest_trades", "backtest_equity_curve"],
            expected_outputs=["performance_summary"],
            dependencies=["backtest_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="benchmark_comparison_job",
            job_name="Benchmark Comparison",
            job_type="performance_job",
            description="Compares performance to benchmarks.",
            script_module="scripts.run_benchmark_comparison_preview",
            callable_path=None,
            required_inputs=["performance_summary"],
            expected_outputs=["benchmark_comparison"],
            dependencies=["performance_analysis_job"],
            optional_dependencies=[]
        )
    ]

def build_validation_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="walk_forward_validation_job",
            job_name="Walk Forward Validation",
            job_type="validation_job",
            description="Runs WFA on strategies.",
            script_module="scripts.run_wfa_preview",
            callable_path=None,
            required_inputs=["strategy_candidates"],
            expected_outputs=["validation_summary"],
            dependencies=["strategy_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="parameter_sensitivity_job",
            job_name="Parameter Sensitivity",
            job_type="validation_job",
            description="Analyzes strategy sensitivity.",
            script_module="scripts.run_sensitivity_preview",
            callable_path=None,
            required_inputs=["strategy_candidates"],
            expected_outputs=["sensitivity_summary"],
            dependencies=["strategy_candidates_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="optimizer_candidate_job",
            job_name="Optimizer",
            job_type="validation_job",
            description="Optimizes strategy parameters.",
            script_module="scripts.run_optimizer_preview",
            callable_path=None,
            required_inputs=["strategy_candidates"],
            expected_outputs=["optimizer_summary"],
            dependencies=["strategy_candidates_job"],
            optional_dependencies=[]
        )
    ]

def build_ml_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="ml_dataset_job",
            job_name="ML Dataset Builder",
            job_type="ml_dataset_job",
            description="Builds dataset for ML.",
            script_module="scripts.run_dataset_preview",
            callable_path=None,
            required_inputs=["technical_features", "indicator_events"],
            expected_outputs=["ml_dataset"],
            dependencies=["indicator_events_job"],
            optional_dependencies=["regime_features_job", "mtf_features_job"]
        ),
        PipelineJob(
            job_id="ml_training_job",
            job_name="ML Model Training",
            job_type="ml_training_job",
            description="Trains baseline ML models offline.",
            script_module="scripts.run_training_pipeline_preview",
            callable_path=None,
            required_inputs=["ml_dataset"],
            expected_outputs=["ml_model_registry"],
            dependencies=["ml_dataset_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="ml_prediction_job",
            job_name="ML Prediction",
            job_type="ml_prediction_job",
            description="Generates offline predictions.",
            script_module="scripts.run_prediction_pipeline_preview",
            callable_path=None,
            required_inputs=["ml_model_registry", "ml_dataset"],
            expected_outputs=["ml_predictions"],
            dependencies=["ml_training_job"],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="ml_integration_job",
            job_name="ML Integration",
            job_type="ml_integration_job",
            description="Integrates ML context with signals.",
            script_module="scripts.run_ml_integration_preview",
            callable_path=None,
            required_inputs=["ml_predictions", "signal_candidates"],
            expected_outputs=["ml_integration"],
            dependencies=["ml_prediction_job", "signal_candidates_job"],
            optional_dependencies=[]
        )
    ]

def build_paper_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="paper_trading_job",
            job_name="Paper Trading Simulation",
            job_type="paper_job",
            description="Simulates trading via paper execution.",
            script_module="scripts.run_paper_simulation",
            callable_path=None,
            required_inputs=["level_candidates"],
            expected_outputs=["paper_summary"],
            dependencies=["level_candidates_job"],
            optional_dependencies=["ml_integration_job"]
        )
    ]

def build_notification_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="notification_status_job",
            job_name="Notification Status",
            job_type="notification_job",
            description="Checks notification system status.",
            script_module="scripts.run_notification_status",
            callable_path=None,
            required_inputs=[],
            expected_outputs=["notification_logs"],
            dependencies=[],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="telegram_daily_digest_job",
            job_name="Telegram Daily Digest",
            job_type="notification_job",
            description="Sends daily digest via Telegram.",
            script_module="scripts.run_telegram_digest",
            callable_path=None,
            required_inputs=["paper_summary"],
            expected_outputs=["notification_logs"],
            dependencies=["paper_trading_job"],
            optional_dependencies=[]
        )
    ]

def build_healthcheck_jobs() -> List[PipelineJob]:
    return [
        PipelineJob(
            job_id="dependency_check_job",
            job_name="Dependency Check",
            job_type="healthcheck_job",
            description="Checks orchestration dependencies.",
            script_module="scripts.run_dependency_check",
            callable_path=None,
            required_inputs=[],
            expected_outputs=[],
            dependencies=[],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="workflow_status_job",
            job_name="Workflow Status",
            job_type="healthcheck_job",
            description="Reports workflow status.",
            script_module="scripts.run_workflow_status",
            callable_path=None,
            required_inputs=[],
            expected_outputs=[],
            dependencies=[],
            optional_dependencies=[]
        ),
        PipelineJob(
            job_id="quality_status_job",
            job_name="Quality Status",
            job_type="healthcheck_job",
            description="Reports orchestration quality.",
            script_module="scripts.run_orchestration_quality",
            callable_path=None,
            required_inputs=[],
            expected_outputs=[],
            dependencies=[],
            optional_dependencies=[]
        )
    ]

_ALL_JOBS = (
    build_core_data_jobs() +
    build_feature_jobs() +
    build_candidate_jobs() +
    build_risk_sizing_level_jobs() +
    build_backtest_performance_jobs() +
    build_validation_jobs() +
    build_ml_jobs() +
    build_paper_jobs() +
    build_notification_jobs() +
    build_healthcheck_jobs()
)

def list_registered_jobs(enabled_only: bool = True) -> List[PipelineJob]:
    if enabled_only:
        return [job for job in _ALL_JOBS if job.enabled]
    return list(_ALL_JOBS)

def get_registered_job(job_id_or_name: str) -> PipelineJob:
    for job in _ALL_JOBS:
        if job.job_id == job_id_or_name or job.job_name == job_id_or_name:
            return job
    raise ValueError(f"Job not found: {job_id_or_name}")

def validate_registered_jobs() -> dict:
    job_ids = set()
    duplicates = []
    invalid_deps = []

    for job in _ALL_JOBS:
        if job.job_id in job_ids:
            duplicates.append(job.job_id)
        job_ids.add(job.job_id)

    for job in _ALL_JOBS:
        for dep in job.dependencies:
            if dep not in job_ids:
                 invalid_deps.append(f"{job.job_id} -> {dep}")
        for dep in job.optional_dependencies:
            if dep not in job_ids:
                 invalid_deps.append(f"{job.job_id} -> {dep} (optional)")

    return {
        "valid": len(duplicates) == 0 and len(invalid_deps) == 0,
        "duplicates": duplicates,
        "invalid_dependencies": invalid_deps
    }
