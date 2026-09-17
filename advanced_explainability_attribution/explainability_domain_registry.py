# -*- coding: utf-8 -*-
"""Phase 143: Explainability Domain Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)
from advanced_explainability_attribution.explainability_labels import (
    EXPLAINABILITY_DOMAIN_LABELS,
    validate_explainability_domain_label,
)


def build_explainability_domain_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability domains."""
    prof = profile or get_explainability_profile()

    domains_meta = [
        ("explainability_profile_domain", "Profile registry and configuration management", "profiles"),
        ("explainability_domain", "Core explainability governance and boundaries", "governance"),
        ("explainability_report_contract_domain", "Explainability report contract specifications", "report_contracts"),
        ("feature_attribution_contract_domain", "Feature attribution contracts layer", "attribution_contracts"),
        ("global_explanation_contract_domain", "Global model explanation contract specifications", "global_explanations"),
        ("local_explanation_contract_domain", "Local instance-level explanation contracts", "local_explanations"),
        ("feature_importance_placeholder_domain", "Feature importance non-executing placeholders", "feature_importance"),
        ("feature_contribution_placeholder_domain", "Feature contribution score placeholders", "feature_contributions"),
        ("shap_placeholder_domain", "SHAP value non-executing placeholder contracts", "shap_placeholders"),
        ("lime_placeholder_domain", "LIME explanation non-executing placeholder contracts", "lime_placeholders"),
        ("permutation_importance_placeholder_domain", "Permutation feature importance placeholders", "permutation_importance"),
        ("partial_dependence_placeholder_domain", "Partial dependence plot (PDP) placeholders", "pdp_placeholders"),
        ("ice_placeholder_domain", "Individual conditional expectation (ICE) placeholders", "ice_placeholders"),
        ("surrogate_model_placeholder_domain", "Interpretable surrogate model placeholders", "surrogate_placeholders"),
        ("counterfactual_placeholder_domain", "Counterfactual explanation placeholders", "counterfactual_placeholders"),
        ("reason_code_placeholder_domain", "Top factor reason code placeholder layer", "reason_codes"),
        ("attribution_method_policy_domain", "Policies governing allowed attribution methods", "method_policies"),
        ("attribution_scope_policy_domain", "Policies governing explanation scopes and horizons", "scope_policies"),
        ("attribution_input_contract_domain", "Contract definitions for attribution inputs", "input_contracts"),
        ("attribution_output_contract_domain", "Contract definitions for attribution outputs", "output_contracts"),
        ("explainability_execution_disabled_domain", "Enforcement of zero explainability computation", "execution_disabled"),
        ("attribution_calculation_disabled_domain", "Enforcement of zero attribution score calculation", "attribution_disabled"),
        ("shap_execution_disabled_domain", "Enforcement of zero SHAP value computation", "shap_disabled"),
        ("lime_execution_disabled_domain", "Enforcement of zero LIME explanation computation", "lime_disabled"),
        ("permutation_importance_disabled_domain", "Enforcement of zero permutation importance execution", "permutation_disabled"),
        ("pdp_ice_execution_disabled_domain", "Enforcement of zero PDP/ICE plot generation", "pdp_ice_disabled"),
        ("surrogate_model_execution_disabled_domain", "Enforcement of zero surrogate model training", "surrogate_disabled"),
        ("counterfactual_execution_disabled_domain", "Enforcement of zero counterfactual generation", "counterfactual_disabled"),
        ("explanation_model_action_disabled_domain", "Enforcement of zero automated model modification from XAI", "model_action_disabled"),
        ("explainability_metric_placeholder_domain", "Explainability quality & stability metric placeholders", "metric_placeholders"),
        ("attribution_quality_gate_domain", "Quality gates for explainability contract completeness", "quality_gates"),
        ("explanation_stability_placeholder_domain", "Placeholders for explanation stability tracking", "stability_placeholders"),
        ("attribution_drift_linkage_domain", "Linkage between attribution shifts and drift monitoring", "drift_linkage"),
        ("featurestore_explainability_linkage_domain", "Linkage between feature catalog and attribution contracts", "featurestore_linkage"),
        ("regime_explainability_linkage_domain", "Linkage between market regimes and explainability context", "regime_linkage"),
        ("drift_explainability_linkage_domain", "Linkage between drift contracts and explainability reports", "drift_linkage"),
        ("calibration_uncertainty_explainability_linkage_domain", "Linkage with calibration & uncertainty estimation", "calibration_linkage"),
        ("validation_dependency_domain", "Validation prerequisites across Phase 121-142", "validation_deps"),
        ("quality_dependency_domain", "Quality prerequisites from Phase 123", "quality_deps"),
        ("runtime_dependency_domain", "Runtime prerequisites from Phase 136", "runtime_deps"),
        ("candidate_model_dependency_domain", "Model candidate dependencies from Phase 138/140", "candidate_deps"),
        ("ensemble_dependency_domain", "Ensemble dependencies from Phase 140", "ensemble_deps"),
        ("no_lookahead_guard_domain", "Temporal integrity and future timestamp safeguards", "no_lookahead_guards"),
        ("metadata_only_news_guard_domain", "Text body, full article, and embedding prevention", "news_guards"),
        ("source_preservation_guard_domain", "Source immutability and zero-overwrite safeguards", "source_guards"),
        ("forbidden_column_policy_domain", "Forbidden column policy enforcement", "forbidden_columns"),
        ("lineage_domain", "End-to-end provenance and lineage tracking", "lineage"),
        ("experiment_linkage_domain", "Linkage to ML experiment registry from Phase 137", "experiment_linkage"),
        ("audit_placeholder_domain", "Audit trail record placeholders", "audit_placeholders"),
        ("manual_review_domain", "Human manual review queue and signoff boundaries", "manual_review"),
        ("finding_domain", "Explainability findings and defect registry", "findings"),
        ("readiness_score_domain", "Readiness scoring and classification", "readiness_scoring"),
        ("manifest_domain", "Comprehensive explainability layer manifest", "manifest"),
        ("health_domain", "Health check diagnostics and dependency verification", "health"),
        ("validation_domain", "Contract and invariant validation rules", "validation"),
        ("safety_domain", "Safety boundaries and NO-GO enforcement", "safety"),
        ("phase_144_handoff_domain", "Structured handoff to Phase 144 Model Governance", "phase_144_handoff"),
        ("unknown_explainability_domain", "Fallback domain for unclassified items", "unknown"),
    ]

    rows: List[Dict[str, Any]] = []
    for domain_label, desc, category in domains_meta:
        rows.append({
            "domain_label": domain_label,
            "description": desc,
            "category": category,
            "current_phase": prof.current_phase,
            "target_final_phase": prof.target_final_phase,
            "next_phase": prof.next_phase,
            "is_enabled": True,
            "is_contract_only": True,
            "is_non_signal": True,
            "is_calculation_allowed": False,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_domains(df)
    return df, summary


def summarize_explainability_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability domain registry statistics."""
    total_domains = len(df)
    categories = df["category"].nunique() if not df.empty else 0

    return {
        "total_domains": total_domains,
        "unique_categories": categories,
        "all_contract_only": bool(df["is_contract_only"].all()) if not df.empty else True,
        "all_non_signal": bool(df["is_non_signal"].all()) if not df.empty else True,
        "all_zero_calculation": bool((~df["is_calculation_allowed"]).all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }


def validate_domain_label(label: str) -> bool:
    """Validate a domain label string."""
    return validate_explainability_domain_label(label)
