# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Domain Registry.

Defines the domain components and scope for baseline ML models.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_labels import BASELINE_ML_MODEL_DOMAIN_LABELS


def build_baseline_ml_model_domain_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build domain registry DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    domain_definitions = [
        {"domain_key": "baseline_ml_model_profile_domain", "category": "configuration", "scope": "Profiles & settings"},
        {"domain_key": "baseline_ml_model_domain", "category": "taxonomy", "scope": "High-level domain tracking"},
        {"domain_key": "model_family_domain", "category": "contracts", "scope": "Baseline model algorithm families"},
        {"domain_key": "model_contract_domain", "category": "contracts", "scope": "Formal model contracts"},
        {"domain_key": "model_input_contract_domain", "category": "contracts", "scope": "Feature and dataset inputs"},
        {"domain_key": "model_output_contract_domain", "category": "contracts", "scope": "Blocked prediction outputs"},
        {"domain_key": "training_plan_domain", "category": "training_plan", "scope": "Dry-run simulated plans"},
        {"domain_key": "dry_run_harness_contract_domain", "category": "harness", "scope": "Dry-run harness rules"},
        {"domain_key": "dry_run_harness_interface_domain", "category": "harness", "scope": "Interface contracts"},
        {"domain_key": "trainer_stub_domain", "category": "harness", "scope": "Trainer stubs returning blocked status"},
        {"domain_key": "dry_run_policy_domain", "category": "policies", "scope": "Training simulation policies"},
        {"domain_key": "no_real_training_domain", "category": "safety", "scope": "Zero real training enforcement"},
        {"domain_key": "no_prediction_domain", "category": "safety", "scope": "Zero prediction enforcement"},
        {"domain_key": "no_target_label_domain", "category": "safety", "scope": "Zero target/label generation"},
        {"domain_key": "artifact_disabled_domain", "category": "governance", "scope": "Artifact persistence disabled"},
        {"domain_key": "model_registry_write_disabled_domain", "category": "governance", "scope": "Registry writes disabled"},
        {"domain_key": "metric_placeholder_domain", "category": "placeholders", "scope": "Metric placeholders without compute"},
        {"domain_key": "evaluation_placeholder_domain", "category": "placeholders", "scope": "Future evaluation placeholders"},
        {"domain_key": "validation_dependency_domain", "category": "dependencies", "scope": "Preceding validation linkages"},
        {"domain_key": "quality_dependency_domain", "category": "dependencies", "scope": "Preceding quality linkages"},
        {"domain_key": "lineage_domain", "category": "lineage", "scope": "Full Phase 116-138 lineage"},
        {"domain_key": "featurestore_input_domain", "category": "inputs", "scope": "FeatureStore catalog inputs"},
        {"domain_key": "regime_input_domain", "category": "inputs", "scope": "Regime acceptance inputs"},
        {"domain_key": "no_lookahead_guard_domain", "category": "guards", "scope": "Leakage & future timestamp prevention"},
        {"domain_key": "metadata_only_news_guard_domain", "category": "guards", "scope": "No raw news content enforcement"},
        {"domain_key": "source_preservation_guard_domain", "category": "guards", "scope": "Source preservation guards"},
        {"domain_key": "forbidden_column_policy_domain", "category": "guards", "scope": "Forbidden column enforcement"},
        {"domain_key": "experiment_linkage_domain", "category": "linkage", "scope": "Phase 137 experiment connection"},
        {"domain_key": "manual_review_domain", "category": "governance", "scope": "Manual inspection queue"},
        {"domain_key": "finding_domain", "category": "governance", "scope": "Audit findings and blockers"},
        {"domain_key": "readiness_score_domain", "category": "scoring", "scope": "Phase 138 readiness scoring"},
        {"domain_key": "manifest_domain", "category": "manifest", "scope": "Phase 138 integrity manifest"},
        {"domain_key": "health_domain", "category": "health", "scope": "System health verification"},
        {"domain_key": "validation_domain", "category": "validation", "scope": "Comprehensive validation report"},
        {"domain_key": "safety_domain", "category": "safety", "scope": "Formal NO-GO and SAFE-GO boundaries"},
        {"domain_key": "phase_139_handoff_domain", "category": "handoff", "scope": "Handoff to Phase 139 GPU harness"},
        {"domain_key": "unknown_baseline_ml_model_domain", "category": "fallback", "scope": "Fallback unknown domain"},
    ]

    rows = []
    for d in domain_definitions:
        rows.append({
            "domain_key": d["domain_key"],
            "category": d["category"],
            "scope": d["scope"],
            "active": True,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_baseline_ml_model_domains(df)
    return df, summary


def summarize_baseline_ml_model_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize baseline ML model domain DataFrame."""
    return {
        "total_domains": len(df),
        "categories": sorted(df["category"].unique().tolist()) if not df.empty else [],
        "active_domains": int(df["active"].sum()) if not df.empty else 0,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
