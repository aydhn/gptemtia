# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Governance Safety Boundary."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

NO_GO_CONDITIONS: List[Dict[str, str]] = [
    {"rule_id": "NO_GO_01", "rule": "live_trading", "description": "Prohibit live order dispatch or execution."},
    {"rule_id": "NO_GO_02", "rule": "broker_integration", "description": "Prohibit connecting broker APIs or credentials."},
    {"rule_id": "NO_GO_03", "rule": "real_order", "description": "Prohibit real market order generation."},
    {"rule_id": "NO_GO_04", "rule": "investment_advice", "description": "Prohibit generating investment recommendations."},
    {"rule_id": "NO_GO_05", "rule": "signal_generation", "description": "Prohibit generating buy/sell/directional signals."},
    {"rule_id": "NO_GO_06", "rule": "directional_certainty", "description": "Prohibit directional market claims."},
    {"rule_id": "NO_GO_07", "rule": "dataset_materialization", "description": "Prohibit materializing training datasets to disk."},
    {"rule_id": "NO_GO_08", "rule": "feature_snapshot_materialization", "description": "Prohibit saving feature matrices to disk."},
    {"rule_id": "NO_GO_09", "rule": "strategy_backtest_optimizer", "description": "Prohibit strategy generation, backtests, or optimizers."},
    {"rule_id": "NO_GO_10", "rule": "real_model_training", "description": "Prohibit real model fitting or weight optimization."},
    {"rule_id": "NO_GO_11", "rule": "model_fit_predict_inference", "description": "Prohibit fit, predict, predict_proba, or transform calls."},
    {"rule_id": "NO_GO_12", "rule": "learning_execution", "description": "Prohibit supervised, unsupervised, clustering, ensemble, or calibration execution."},
    {"rule_id": "NO_GO_13", "rule": "target_label_prediction", "description": "Prohibit target, label, or prediction generation."},
    {"rule_id": "NO_GO_14", "rule": "metric_performance_claim", "description": "Prohibit metric calculation or performance claims."},
    {"rule_id": "NO_GO_15", "rule": "sentiment_model_output", "description": "Prohibit sentiment model evaluation or output."},
    {"rule_id": "NO_GO_16", "rule": "raw_content_scraped_html", "description": "Prohibit full article text, raw content, and scraped HTML."},
    {"rule_id": "NO_GO_17", "rule": "embedding_vector_generation", "description": "Prohibit generating dense embeddings or vector DB operations."},
    {"rule_id": "NO_GO_18", "rule": "artifact_persistence", "description": "Prohibit saving model weights or binaries to disk."},
    {"rule_id": "NO_GO_19", "rule": "model_registry_write", "description": "Prohibit writing to local or remote model registries."},
    {"rule_id": "NO_GO_20", "rule": "official_approval_claim", "description": "Prohibit claiming official approval, production-ready, or broker-ready."},
    {"rule_id": "NO_GO_21", "rule": "source_overwrite_destructive", "description": "Prohibit source overwrite, file deletion, and destructive cleaning."},
    {"rule_id": "NO_GO_22", "rule": "auto_imputation_feature_drop", "description": "Prohibit automatic imputation or silent feature dropping."},
    {"rule_id": "NO_GO_23", "rule": "web_scraping_credentials", "description": "Prohibit web scraping or credential output."},
    {"rule_id": "NO_GO_24", "rule": "deployment", "description": "Prohibit model or production deployment."},
]

SAFE_GO_CONDITIONS: List[Dict[str, str]] = [
    {"rule_id": "SAFE_GO_01", "rule": "gpu_resource_policies", "description": "Produce local/offline GPU resource policy contracts."},
    {"rule_id": "SAFE_GO_02", "rule": "device_selection_metadata", "description": "Generate simulated device selection metadata without allocation."},
    {"rule_id": "SAFE_GO_03", "rule": "memory_budget_metadata", "description": "Establish dry-run VRAM memory budget and ceiling policies."},
    {"rule_id": "SAFE_GO_04", "rule": "cpu_fallback_metadata", "description": "Define deterministic CPU fallback policies."},
    {"rule_id": "SAFE_GO_05", "rule": "timeout_watchdog_metadata", "description": "Define training timeout policies and watchdog limits."},
    {"rule_id": "SAFE_GO_06", "rule": "noop_training_loop_contracts", "description": "Create no-op training loop stub contracts."},
    {"rule_id": "SAFE_GO_07", "rule": "blocked_execution_stubs", "description": "Deploy blocked execution harness stubs returning safe contract metadata."},
    {"rule_id": "SAFE_GO_08", "rule": "disabled_execution_reports", "description": "Generate formal reports verifying disabled training and prediction."},
    {"rule_id": "SAFE_GO_09", "rule": "resource_audit_placeholders", "description": "Construct resource and experiment audit schema placeholders."},
    {"rule_id": "SAFE_GO_10", "rule": "phase_140_handoff", "description": "Provide clean, non-signal handoff report to Phase 140 candidate model registry."},
]


def build_gpu_training_governance_no_go_conditions(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build NO-GO boundary rules DataFrame."""
    df = pd.DataFrame(NO_GO_CONDITIONS)
    df["status"] = "ENFORCED"
    df["non_signal"] = True
    return df, {"total_no_go_rules": len(df), "all_enforced": True, "non_signal": True}


def build_gpu_training_governance_safe_go_conditions(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build SAFE-GO permitted activities DataFrame."""
    df = pd.DataFrame(SAFE_GO_CONDITIONS)
    df["status"] = "ACTIVE"
    df["non_signal"] = True
    return df, {"total_safe_go_rules": len(df), "all_active": True, "non_signal": True}


def build_gpu_training_governance_safety_boundary(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build consolidated safety boundary report."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    no_go_df, no_go_sum = build_gpu_training_governance_no_go_conditions(active_profile)
    safe_go_df, safe_go_sum = build_gpu_training_governance_safe_go_conditions(active_profile)

    combined_rows = []
    for _, r in no_go_df.iterrows():
        combined_rows.append({"type": "NO_GO", "rule_id": r["rule_id"], "rule": r["rule"], "status": r["status"]})
    for _, r in safe_go_df.iterrows():
        combined_rows.append({"type": "SAFE_GO", "rule_id": r["rule_id"], "rule": r["rule"], "status": r["status"]})

    df = pd.DataFrame(combined_rows)
    summary = summarize_gpu_training_governance_safety_boundary(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_governance_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    if df.empty:
        return {"total_rules": 0, "safety_status": "UNKNOWN", "non_signal": True}
    no_go_count = int((df["type"] == "NO_GO").sum()) if "type" in df.columns else 0
    safe_go_count = int((df["type"] == "SAFE_GO").sum()) if "type" in df.columns else 0
    return {
        "total_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "safety_status": "SECURE",
        "live_trading_prohibited": True,
        "zero_model_execution": True,
        "current_phase": 139,
        "non_signal": True,
    }
