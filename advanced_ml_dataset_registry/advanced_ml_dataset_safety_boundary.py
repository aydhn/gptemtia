# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Safety Boundary Specification.

Formalizes strict NO-GO and SAFE-GO operating conditions.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)

NO_GO_CONDITIONS = [
    {"rule_id": "NG-01", "name": "Live Trading Prohibition", "category": "execution", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-02", "name": "Broker Integration Block", "category": "execution", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-03", "name": "Real Order Execution Block", "category": "execution", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-04", "name": "Investment Advice Prohibition", "category": "governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-05", "name": "Signal Generation Prohibition", "category": "governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-06", "name": "Directional Return Claim Block", "category": "governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-07", "name": "Dataset Materialization Block", "category": "storage", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-08", "name": "Feature Snapshot Materialization Block", "category": "storage", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-09", "name": "Strategy Backtest Optimizer Block", "category": "execution", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-10", "name": "Model Training / Fit Block", "category": "ml_lifecycle", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-11", "name": "Model Predict / Inference Block", "category": "ml_lifecycle", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-12", "name": "Clustering / Unsupervised Execution Block", "category": "ml_lifecycle", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-13", "name": "Ensemble / Calibration Execution Block", "category": "ml_lifecycle", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-14", "name": "Target / Label Generation Block", "category": "ml_lifecycle", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-15", "name": "Sentiment Model Output Block", "category": "nlp_governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-16", "name": "Full Text / HTML Scraping Block", "category": "nlp_governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-17", "name": "Embedding / Vector Generation Block", "category": "nlp_governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-18", "name": "Artifact / Weights Persistence Block", "category": "storage", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-19", "name": "Official Approval / Production Claim Block", "category": "governance", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-20", "name": "Source Overwrite / Deletion Block", "category": "data_integrity", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-21", "name": "Auto-Imputation / Auto-Drop Block", "category": "data_integrity", "status": "STRICTLY_ENFORCED"},
    {"rule_id": "NG-22", "name": "Provider Credential Output Block", "category": "security", "status": "STRICTLY_ENFORCED"},
]

SAFE_GO_CONDITIONS = [
    {"rule_id": "SG-01", "name": "Local Offline Dataset Contract Registry", "category": "contract", "status": "ACTIVE"},
    {"rule_id": "SG-02", "name": "Source Catalog Metadata Reference Generation", "category": "metadata", "status": "ACTIVE"},
    {"rule_id": "SG-03", "name": "Schema / Namespace / Version / Partition Policies", "category": "policy", "status": "ACTIVE"},
    {"rule_id": "SG-04", "name": "Time-Index and Split Policy Placeholders", "category": "policy", "status": "ACTIVE"},
    {"rule_id": "SG-05", "name": "Leakage and No-Lookahead Guards", "category": "guard", "status": "ACTIVE"},
    {"rule_id": "SG-06", "name": "Metadata-Only News Event Guards", "category": "guard", "status": "ACTIVE"},
    {"rule_id": "SG-07", "name": "Source Preservation and Immutability Guards", "category": "guard", "status": "ACTIVE"},
    {"rule_id": "SG-08", "name": "Feature Snapshot Contracts Without Materialization", "category": "contract", "status": "ACTIVE"},
    {"rule_id": "SG-09", "name": "Experiment Registry Metadata & Templates", "category": "registry", "status": "ACTIVE"},
    {"rule_id": "SG-10", "name": "Model Family Placeholders Without Execution", "category": "metadata", "status": "ACTIVE"},
    {"rule_id": "SG-11", "name": "Metric Placeholders Without Calculation", "category": "metadata", "status": "ACTIVE"},
    {"rule_id": "SG-12", "name": "Phase 138 Dry-Run Training Harness Handoff", "category": "handoff", "status": "ACTIVE"},
]


def build_advanced_ml_dataset_no_go_conditions(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build NO-GO conditions DataFrame and summary."""
    df = pd.DataFrame(NO_GO_CONDITIONS)
    return df, {"total_no_go": len(df), "all_enforced": True, "non_signal": True}


def build_advanced_ml_dataset_safe_go_conditions(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build SAFE-GO conditions DataFrame and summary."""
    df = pd.DataFrame(SAFE_GO_CONDITIONS)
    return df, {"total_safe_go": len(df), "all_active": True, "non_signal": True}


def build_advanced_ml_dataset_safety_boundary(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build unified safety boundary DataFrame and summary."""
    p = profile or get_default_advanced_ml_dataset_profile()

    records = []
    for ng in NO_GO_CONDITIONS:
        records.append({
            "boundary_type": "NO_GO",
            "rule_id": ng["rule_id"],
            "name": ng["name"],
            "category": ng["category"],
            "status": ng["status"],
            "is_enforced": True,
            "non_signal": True,
        })
    for sg in SAFE_GO_CONDITIONS:
        records.append({
            "boundary_type": "SAFE_GO",
            "rule_id": sg["rule_id"],
            "name": sg["name"],
            "category": sg["category"],
            "status": sg["status"],
            "is_enforced": True,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_advanced_ml_dataset_safety_boundary(df)
    return df, summary


def summarize_advanced_ml_dataset_safety_boundary(df: pd.DataFrame) -> Dict:
    """Summarize safety boundaries."""
    no_go_count = int((df["boundary_type"] == "NO_GO").sum()) if "boundary_type" in df.columns else len(NO_GO_CONDITIONS)
    safe_go_count = int((df["boundary_type"] == "SAFE_GO").sum()) if "boundary_type" in df.columns else len(SAFE_GO_CONDITIONS)
    return {
        "total_boundaries": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "safety_status": "SECURE",
        "live_trading_prohibited": True,
        "model_training_blocked": True,
        "non_signal": True,
    }
