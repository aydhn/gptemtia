"""
Standard error definitions and taxonomy for the observability layer.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Tuple, Optional

import pandas as pd


@dataclass(frozen=True)
class ErrorDefinition:
    """A standard error definition."""
    error_code: str
    category: str
    severity: str
    title: str
    description: str
    suggested_action: str
    retryable: bool = False


# Initial error definitions registry
_ERROR_DEFINITIONS: Dict[str, ErrorDefinition] = {
    "CFG_001": ErrorDefinition(
        error_code="CFG_001", category="config_error", severity="warning",
        title="missing_env_setting", description="A recommended environment setting is missing and a default was used.",
        suggested_action="Check your .env file and ensure all settings are configured.", retryable=False
    ),
    "CFG_002": ErrorDefinition(
        error_code="CFG_002", category="config_error", severity="error",
        title="invalid_config_value", description="An invalid configuration value was provided.",
        suggested_action="Review and correct the configuration value in settings or .env.", retryable=False
    ),
    "PATH_001": ErrorDefinition(
        error_code="PATH_001", category="io_error", severity="warning",
        title="missing_directory", description="A required directory does not exist and needs to be created.",
        suggested_action="Run the path initialization script to create required directories.", retryable=False
    ),
    "DATA_001": ErrorDefinition(
        error_code="DATA_001", category="data_error", severity="error",
        title="missing_raw_data", description="Required raw data is missing.",
        suggested_action="Run the data download pipeline to fetch missing data.", retryable=True
    ),
    "DATA_002": ErrorDefinition(
        error_code="DATA_002", category="data_error", severity="error",
        title="missing_processed_data", description="Required processed data is missing.",
        suggested_action="Run the data processing pipeline to generate processed data.", retryable=True
    ),
    "DATA_003": ErrorDefinition(
        error_code="DATA_003", category="data_error", severity="warning",
        title="stale_data", description="Data is older than the configured freshness threshold.",
        suggested_action="Update data by running the data pipeline.", retryable=True
    ),
    "DATA_004": ErrorDefinition(
        error_code="DATA_004", category="schema_error", severity="error",
        title="invalid_ohlcv_schema", description="OHLCV data does not conform to the expected schema.",
        suggested_action="Check the data source and processing logic for schema violations.", retryable=False
    ),
    "FEAT_001": ErrorDefinition(
        error_code="FEAT_001", category="dependency_error", severity="warning",
        title="missing_feature_set", description="A required feature set is missing.",
        suggested_action="Run the feature generation pipeline.", retryable=True
    ),
    "FEAT_002": ErrorDefinition(
        error_code="FEAT_002", category="quality_error", severity="warning",
        title="feature_nan_ratio_high", description="The feature set contains a high ratio of NaN values.",
        suggested_action="Check the feature calculation logic or input data quality.", retryable=False
    ),
    "CAND_001": ErrorDefinition(
        error_code="CAND_001", category="dependency_error", severity="warning",
        title="missing_candidate_frame", description="A candidate frame is missing for a pipeline stage.",
        suggested_action="Ensure upstream pipelines have executed successfully.", retryable=True
    ),
    "RISK_001": ErrorDefinition(
        error_code="RISK_001", category="quality_error", severity="warning",
        title="risk_candidate_quality_failed", description="Risk candidates failed quality checks.",
        suggested_action="Review risk calculation logic and thresholds.", retryable=False
    ),
    "BT_001": ErrorDefinition(
        error_code="BT_001", category="validation_error", severity="warning",
        title="backtest_no_trades", description="Backtest resulted in zero trades.",
        suggested_action="Review strategy logic and signal generation parameters.", retryable=False
    ),
    "BT_002": ErrorDefinition(
        error_code="BT_002", category="leakage_error", severity="critical",
        title="lookahead_violation", description="Lookahead bias detected in backtesting.",
        suggested_action="Inspect signal generation to ensure future data is not used.", retryable=False
    ),
    "ML_001": ErrorDefinition(
        error_code="ML_001", category="leakage_error", severity="critical",
        title="ml_dataset_leakage_risk", description="High risk of data leakage detected in ML dataset.",
        suggested_action="Ensure proper embargo gaps and chronological splitting are applied.", retryable=False
    ),
    "ML_002": ErrorDefinition(
        error_code="ML_002", category="artifact_error", severity="error",
        title="model_artifact_missing", description="Required ML model artifact is missing.",
        suggested_action="Train models using the ML training pipeline.", retryable=True
    ),
    "ML_003": ErrorDefinition(
        error_code="ML_003", category="quality_error", severity="warning",
        title="model_quality_failed", description="Model evaluation quality below threshold.",
        suggested_action="Review ML training features and model hyperparameters.", retryable=False
    ),
    "PAPER_001": ErrorDefinition(
        error_code="PAPER_001", category="quality_error", severity="warning",
        title="paper_no_virtual_orders", description="Paper trading generated no virtual orders.",
        suggested_action="Check signal and strategy logic for paper trading universe.", retryable=False
    ),
    "PAPER_002": ErrorDefinition(
        error_code="PAPER_002", category="quality_error", severity="error",
        title="paper_position_overlap", description="Invalid overlapping paper positions detected.",
        suggested_action="Review paper portfolio state management logic.", retryable=False
    ),
    "NOTIF_001": ErrorDefinition(
        error_code="NOTIF_001", category="notification_error", severity="warning",
        title="telegram_not_configured", description="Telegram configuration is missing.",
        suggested_action="Configure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env.", retryable=False
    ),
    "NOTIF_002": ErrorDefinition(
        error_code="NOTIF_002", category="notification_error", severity="error",
        title="telegram_delivery_failed", description="Failed to deliver Telegram message.",
        suggested_action="Check network connectivity and Telegram bot token validity.", retryable=True
    ),
    "ORCH_001": ErrorDefinition(
        error_code="ORCH_001", category="dependency_error", severity="warning",
        title="dependency_missing", description="An orchestration job failed due to missing dependencies.",
        suggested_action="Ensure upstream jobs in the orchestration workflow have succeeded.", retryable=True
    ),
    "ORCH_002": ErrorDefinition(
        error_code="ORCH_002", category="orchestration_error", severity="error",
        title="job_failed", description="An orchestration job failed to execute.",
        suggested_action="Check the specific job logs for errors.", retryable=True
    ),
    "ORCH_003": ErrorDefinition(
        error_code="ORCH_003", category="orchestration_error", severity="error",
        title="workflow_failed", description="An entire orchestration workflow failed.",
        suggested_action="Investigate failing jobs within the workflow.", retryable=True
    ),
    "SYS_000": ErrorDefinition(
        error_code="SYS_000", category="unknown_error", severity="error",
        title="unknown_system_error", description="An unclassified system error occurred.",
        suggested_action="Review full stack trace and add new error definition to taxonomy.", retryable=False
    ),
}


def list_error_definitions() -> List[ErrorDefinition]:
    """List all registered error definitions."""
    return list(_ERROR_DEFINITIONS.values())


def get_error_definition(error_code: str) -> ErrorDefinition:
    """Get an error definition by its code."""
    if error_code in _ERROR_DEFINITIONS:
        return _ERROR_DEFINITIONS[error_code]
    return _ERROR_DEFINITIONS["SYS_000"]


def classify_exception(exc: Exception) -> Dict[str, Any]:
    """Classify an arbitrary exception into a basic error taxonomy format."""
    # Basic classification logic - can be expanded later
    exc_type = type(exc).__name__

    if isinstance(exc, FileNotFoundError) or "No such file" in str(exc):
        return error_definition_to_dict(_ERROR_DEFINITIONS["PATH_001"])
    elif isinstance(exc, ValueError) and "config" in str(exc).lower():
        return error_definition_to_dict(_ERROR_DEFINITIONS["CFG_002"])

    # Default to unknown error but attach exception info
    unknown = error_definition_to_dict(_ERROR_DEFINITIONS["SYS_000"])
    unknown["exception_type"] = exc_type
    unknown["exception_message"] = str(exc)
    return unknown


def build_error_event(error_code: str, component: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Build a structured event dictionary from an error code."""
    error_def = get_error_definition(error_code)

    event = {
        "event_name": error_def.title,
        "error_code": error_def.error_code,
        "error_category": error_def.category,
        "severity": error_def.severity,
        "message": error_def.description,
        "component": component,
        "suggested_action": error_def.suggested_action,
        "retryable": error_def.retryable,
    }

    if metadata:
        event["metadata"] = metadata

    return event


def error_definition_to_dict(definition: ErrorDefinition) -> Dict[str, Any]:
    """Convert an ErrorDefinition to a dictionary."""
    return {
        "error_code": definition.error_code,
        "category": definition.category,
        "severity": definition.severity,
        "title": definition.title,
        "description": definition.description,
        "suggested_action": definition.suggested_action,
        "retryable": definition.retryable,
    }


def build_error_taxonomy_report() -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a complete report of the current error taxonomy."""
    definitions = list_error_definitions()

    # Exclude SYS_000 from primary metrics if desired, but good to include in list
    df = pd.DataFrame([error_definition_to_dict(d) for d in definitions])

    summary = {
        "total_errors_defined": len(definitions),
        "by_category": df['category'].value_counts().to_dict() if not df.empty else {},
        "by_severity": df['severity'].value_counts().to_dict() if not df.empty else {},
    }

    return df, summary
