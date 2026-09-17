# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Safety Boundary.

Defines explicit NO-GO (strictly prohibited actions) and SAFE-GO (permitted offline
contract actions) rules.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

NO_GO_RULES = [
    ("no_live_trading", "Live order placement and exchange connectivity are strictly prohibited"),
    ("no_broker_integration", "Broker API integration and execution routing are strictly prohibited"),
    ("no_real_order", "Creation or sending of real orders is strictly prohibited"),
    ("no_investment_advice", "Generating financial or investment advice is strictly prohibited"),
    ("no_signal_generation", "AL/SAT or directional trade signal generation is strictly prohibited"),
    ("no_directional_certainty", "Directional market return claims are strictly prohibited"),
    ("no_dataset_materialization", "Real dataset materialization to disk is prohibited"),
    ("no_feature_snapshot_materialization", "Real feature snapshot materialization to disk is prohibited"),
    ("no_strategy_backtest_optimizer", "Running backtest, optimizer, or strategy engine is prohibited"),
    ("no_real_model_training", "Real machine learning model training is strictly prohibited"),
    ("no_model_fit", "Executing model .fit() calls is strictly prohibited"),
    ("no_model_predict", "Executing model .predict() calls is strictly prohibited"),
    ("no_model_inference", "Forward pass inference execution is strictly prohibited"),
    ("no_model_transform", "Executing state transform calls is strictly prohibited"),
    ("no_clustering_or_unsupervised_execution", "Running unsupervised clustering algorithms is prohibited"),
    ("no_target_label_generation", "Generating target labels or future returns is strictly prohibited"),
    ("no_metric_calculation", "Computing actual performance metrics (accuracy, F1, RMSE) is prohibited"),
    ("no_sentiment_model_output", "Running sentiment NLP models or outputs is strictly prohibited"),
    ("no_full_article_usage", "Using full article text, body text, or scraped HTML is strictly prohibited"),
    ("no_embedding_vector_generation", "Generating embeddings or vector database items is prohibited"),
    ("no_artifact_persistence", "Saving binary weights, pickles, or model files is strictly prohibited"),
    ("no_model_registry_write", "Writing to model registries or MLflow is strictly prohibited"),
    ("no_official_approval_claim", "Claiming official approval or production readiness is prohibited"),
    ("no_source_overwrite", "Overwriting or deleting source data files is strictly prohibited"),
]

SAFE_GO_RULES = [
    ("safe_local_baseline_contracts", "Generating local baseline ML model contract specifications"),
    ("safe_baseline_family_metadata", "Registering baseline model algorithm family metadata"),
    ("safe_dry_run_harness_contracts", "Establishing dry-run training harness contracts and rules"),
    ("safe_dry_run_trainer_stubs", "Providing safe trainer stubs that return blocked execution status"),
    ("safe_disabled_execution_reports", "Generating reports verifying that training and predictions are disabled"),
    ("safe_metric_evaluation_placeholders", "Defining metric and evaluation placeholders without computing values"),
    ("safe_input_metadata_references", "Referencing FeatureStore and regime metadata without materialization"),
    ("safe_no_lookahead_guards", "Enforcing strict no-lookahead and metadata-only input guards"),
    ("safe_phase_139_handoff", "Documenting prerequisites and resource governance for Phase 139"),
]


def build_baseline_ml_model_no_go_conditions(
    profile: Optional[BaselineMlModelProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of all NO-GO safety rules."""
    rows = [{"rule_id": r[0], "rule_type": "NO-GO", "description": r[1], "enforced": True} for r in NO_GO_RULES]
    return pd.DataFrame(rows)


def build_baseline_ml_model_safe_go_conditions(
    profile: Optional[BaselineMlModelProfile] = None,
) -> pd.DataFrame:
    """Build DataFrame of all SAFE-GO principles."""
    rows = [{"rule_id": r[0], "rule_type": "SAFE-GO", "description": r[1], "enforced": True} for r in SAFE_GO_RULES]
    return pd.DataFrame(rows)


def build_baseline_ml_model_safety_boundary(
    profile: Optional[BaselineMlModelProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build combined safety boundary DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    df_nogo = build_baseline_ml_model_no_go_conditions(profile)
    df_safego = build_baseline_ml_model_safe_go_conditions(profile)
    df = pd.concat([df_nogo, df_safego], ignore_index=True)
    summary = summarize_baseline_ml_model_safety_boundary(df)
    return df, summary


def summarize_baseline_ml_model_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize safety boundary DataFrame."""
    no_go_count = int((df["rule_type"] == "NO-GO").sum()) if not df.empty else len(NO_GO_RULES)
    safe_go_count = int((df["rule_type"] == "SAFE-GO").sum()) if not df.empty else len(SAFE_GO_RULES)
    return {
        "total_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "safety_status": "SECURE",
        "all_enforced": True,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
