# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Validation Routines."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    VALIDATION_DOMAIN,
    ACCEPTANCE_READY,
)

FORBIDDEN_PHRASES = [
    "official approval",
    "production ready",
    "broker ready",
    "live trading approved",
    "live trading ready",
    "buy signal",
    "sell signal",
    "target price",
    "model training executed",
    "model fit executed",
    "inference executed",
    "backtest executed",
    "walk forward executed",
    "transaction cost calculated",
    "slippage calculated",
]


def validate_no_forbidden_advanced_ml_acceptance_claims(
    text: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    summary: Optional[Dict[str, Any]] = None,
) -> bool:
    """Check strings, tables, or summaries for unauthorized claims."""
    if text:
        t_lower = text.lower()
        for phrase in FORBIDDEN_PHRASES:
            # Allow disclaimers that mention these phrases in negative context
            if phrase in t_lower and "değildir" not in t_lower and "prohibited" not in t_lower and "false" not in t_lower:
                raise ValueError(f"Forbidden claim detected in text: '{phrase}'")

    if df is not None and not df.empty:
        for col in df.columns:
            if df[col].dtype == object:
                for val in df[col].dropna().astype(str):
                    v_lower = val.lower()
                    for phrase in FORBIDDEN_PHRASES:
                        if phrase in v_lower and "false" not in v_lower and "değildir" not in v_lower and "prohibited" not in v_lower:
                            raise ValueError(f"Forbidden claim detected in column '{col}': '{phrase}'")

    if summary is not None:
        for k, v in summary.items():
            if isinstance(v, str):
                v_lower = v.lower()
                for phrase in FORBIDDEN_PHRASES:
                    if phrase in v_lower and "false" not in v_lower and "değildir" not in v_lower and "prohibited" not in v_lower:
                        raise ValueError(f"Forbidden claim detected in summary '{k}': '{phrase}'")
            elif isinstance(v, bool) and v is True:
                forbidden_bool_keys = [
                    "production_ready", "broker_ready", "live_trading_approved",
                    "production_approved", "broker_ready_approved", "release_approved",
                    "backtest_executed", "model_training_executed", "model_predict_executed",
                    "artifact_persisted", "model_registry_written",
                ]
                if k in forbidden_bool_keys:
                    raise ValueError(f"Forbidden positive boolean flag detected: '{k}=True'")
    return True


def validate_advanced_ml_acceptance_profile_registry(
    df: pd.DataFrame, profile: AdvancedMlAcceptanceProfile
) -> bool:
    """Validate acceptance profile DataFrame."""
    if df.empty:
        raise ValueError("Profile DataFrame is empty")
    for _, row in df.iterrows():
        if row.get("current_phase") != 145:
            raise ValueError(f"Invalid current_phase: {row.get('current_phase')}")
        if row.get("target_final_phase") != 160:
            raise ValueError(f"Invalid target_final_phase: {row.get('target_final_phase')}")
        if row.get("next_phase") != 146:
            raise ValueError(f"Invalid next_phase: {row.get('next_phase')}")
        if row.get("allow_live_trading") is not False:
            raise ValueError("Profile allows live trading")
        if row.get("allow_broker_integration") is not False:
            raise ValueError("Profile allows broker integration")
        if row.get("allow_signal_generation") is not False:
            raise ValueError("Profile allows signal generation")
    return True


def validate_advanced_ml_component_checkpoints(
    df: pd.DataFrame, profile: AdvancedMlAcceptanceProfile
) -> bool:
    """Validate component checkpoints DataFrame."""
    if df.empty:
        raise ValueError("Checkpoints DataFrame is empty")
    for _, row in df.iterrows():
        if row.get("contract_only") is not True:
            raise ValueError("Checkpoint is not contract_only")
        if row.get("non_production") is not True:
            raise ValueError("Checkpoint is not non_production")
        if row.get("production_ready") is not False:
            raise ValueError("Checkpoint marks production_ready=True")
        if row.get("broker_ready") is not False:
            raise ValueError("Checkpoint marks broker_ready=True")
        if row.get("signal_ready") is not False:
            raise ValueError("Checkpoint marks signal_ready=True")
    return True


def validate_phase_acceptance_registries(
    df_map: Dict[str, pd.DataFrame], profile: AdvancedMlAcceptanceProfile
) -> bool:
    """Validate all phase-level acceptance DataFrames."""
    for phase_key, df in df_map.items():
        if df.empty:
            raise ValueError(f"Phase acceptance DataFrame for '{phase_key}' is empty")
        if "passed" in df.columns and not df["passed"].all():
            raise ValueError(f"Phase acceptance checks failed in '{phase_key}'")
    return True


def validate_advanced_ml_boundaries(
    df_map: Dict[str, pd.DataFrame], profile: AdvancedMlAcceptanceProfile
) -> bool:
    """Validate boundary DataFrames."""
    for name, df in df_map.items():
        if df.empty:
            raise ValueError(f"Boundary DataFrame '{name}' is empty")
    return True


def validate_advanced_ml_acceptance_manifest(
    df: pd.DataFrame, profile: AdvancedMlAcceptanceProfile
) -> bool:
    """Validate acceptance manifest DataFrame against strict negative invariants."""
    if df.empty:
        raise ValueError("Manifest DataFrame is empty")
    row = df.iloc[0]

    # Required positive flags
    if not bool(row.get("advanced_ml_block_completed")):
        raise ValueError("Manifest advanced_ml_block_completed must be True")
    if not bool(row.get("phase_146_handoff_ready")):
        raise ValueError("Manifest phase_146_handoff_ready must be True")
    if not bool(row.get("non_signal")):
        raise ValueError("Manifest non_signal must be True")
    if not bool(row.get("local_only")) or not bool(row.get("dry_run")):
        raise ValueError("Manifest local_only and dry_run must be True")

    # Required negative flags
    negative_keys = [
        "production_ready", "broker_ready", "production_approved", "broker_ready_approved",
        "live_trading_approved", "release_approved", "real_audit_log", "dataset_materialized",
        "feature_snapshot_materialized", "contains_target_or_prediction", "contains_trading_recommendation",
        "contains_full_article_text", "contains_article_body", "contains_raw_content", "contains_scraped_html",
        "contains_embedding", "contains_vector", "sentiment_model_output", "real_training_executed",
        "model_training_executed", "model_fit_executed", "model_predict_executed", "model_inference_executed",
        "probability_prediction_executed", "calibration_executed", "uncertainty_estimation_executed",
        "drift_calculation_executed", "explainability_calculation_executed", "feature_attribution_calculation_executed",
        "backtest_executed", "walk_forward_executed", "transaction_cost_calculated", "slippage_calculated",
        "benchmark_calculated", "metric_calculation_executed", "performance_claim_generated",
        "artifact_persisted", "model_registry_written", "model_deployed", "production_deployed",
        "destructive_action_allowed", "auto_fix_allowed", "auto_drop_allowed",
    ]
    for key in negative_keys:
        if bool(row.get(key)):
            raise ValueError(f"Manifest invariant violation: '{key}' must be False, got {row.get(key)}")

    return True


def build_advanced_ml_acceptance_validation_report(
    tables: Dict[str, pd.DataFrame],
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated validation report for Phase 145."""
    active = profile or get_advanced_ml_acceptance_profile()

    checks = [
        {"rule_id": "VAL-01", "rule": "current_phase_145", "passed": active.current_phase == 145},
        {"rule_id": "VAL-02", "rule": "target_final_phase_160", "passed": active.target_final_phase == 160},
        {"rule_id": "VAL-03", "rule": "next_phase_146", "passed": active.next_phase == 146},
        {"rule_id": "VAL-04", "rule": "non_production_enforced", "passed": active.non_production is True},
        {"rule_id": "VAL-05", "rule": "dry_run_default_enforced", "passed": active.dry_run_default is True},
        {"rule_id": "VAL-06", "rule": "no_live_trading", "passed": active.allow_live_trading is False},
        {"rule_id": "VAL-07", "rule": "no_broker_integration", "passed": active.allow_broker_integration is False},
        {"rule_id": "VAL-08", "rule": "no_signal_generation", "passed": active.allow_signal_generation is False},
        {"rule_id": "VAL-09", "rule": "no_training_execution", "passed": active.allow_model_training is False},
        {"rule_id": "VAL-10", "rule": "no_prediction_execution", "passed": active.allow_model_predict is False},
        {"rule_id": "VAL-11", "rule": "no_backtest_execution", "passed": active.allow_backtest_execution is False},
        {"rule_id": "VAL-12", "rule": "no_cost_slippage_calculation", "passed": active.allow_transaction_cost_calculation is False and active.allow_slippage_calculation is False},
        {"rule_id": "VAL-13", "rule": "no_production_approval", "passed": active.allow_production_approval is False},
        {"rule_id": "VAL-14", "rule": "no_broker_ready_approval", "passed": active.allow_broker_ready_approval is False},
        {"rule_id": "VAL-15", "rule": "no_model_registry_write", "passed": active.allow_model_registry_write is False},
        {"rule_id": "VAL-16", "rule": "no_artifact_persistence", "passed": active.allow_artifact_persistence is False},
        {"rule_id": "VAL-17", "rule": "no_dataset_materialization", "passed": active.allow_dataset_materialization is False},
        {"rule_id": "VAL-18", "rule": "source_preservation_enforced", "passed": active.allow_source_overwrite is False},
    ]

    df = pd.DataFrame(checks)
    all_passed = bool(df["passed"].all())

    summary: Dict[str, Any] = {
        "domain": VALIDATION_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_rules": len(df),
        "passed_rules": int(df["passed"].sum()),
        "all_passed": all_passed,
        "non_signal": True,
        "status": "PASS" if all_passed else "FAIL",
    }
    return df, summary
