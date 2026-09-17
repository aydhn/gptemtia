# -*- coding: utf-8 -*-
"""Phase 143: Explainability Pipeline Orchestration."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)
from advanced_explainability_attribution.explainability_domain_registry import (
    build_explainability_domain_registry,
)
from advanced_explainability_attribution.explainability_profile_registry import (
    build_explainability_profile_registry,
)
from advanced_explainability_attribution.explainability_report_contracts import (
    build_explainability_report_contracts,
)
from advanced_explainability_attribution.feature_attribution_contracts import (
    build_feature_attribution_contracts,
)
from advanced_explainability_attribution.global_explanation_contracts import (
    build_global_explanation_contract_registry,
)
from advanced_explainability_attribution.local_explanation_contracts import (
    build_local_explanation_contract_registry,
)
from advanced_explainability_attribution.feature_importance_placeholders import (
    build_feature_importance_placeholder_registry,
)
from advanced_explainability_attribution.feature_contribution_placeholders import (
    build_feature_contribution_placeholder_registry,
)
from advanced_explainability_attribution.shap_placeholders import (
    build_shap_placeholder_registry,
)
from advanced_explainability_attribution.lime_placeholders import (
    build_lime_placeholder_registry,
)
from advanced_explainability_attribution.permutation_importance_placeholders import (
    build_permutation_importance_placeholder_registry,
)
from advanced_explainability_attribution.partial_dependence_placeholders import (
    build_partial_dependence_placeholder_registry,
)
from advanced_explainability_attribution.ice_placeholders import (
    build_ice_placeholder_registry,
)
from advanced_explainability_attribution.surrogate_model_placeholders import (
    build_surrogate_model_placeholder_registry,
)
from advanced_explainability_attribution.counterfactual_placeholders import (
    build_counterfactual_placeholder_registry,
)
from advanced_explainability_attribution.reason_code_placeholders import (
    build_reason_code_placeholder_registry,
)
from advanced_explainability_attribution.attribution_method_policies import (
    build_attribution_method_policy_registry,
)
from advanced_explainability_attribution.attribution_scope_policies import (
    build_attribution_scope_policy_registry,
)
from advanced_explainability_attribution.attribution_input_contracts import (
    build_attribution_input_contract_registry,
)
from advanced_explainability_attribution.attribution_output_contracts import (
    build_attribution_output_contract_registry,
)
from advanced_explainability_attribution.explainability_execution_disabled import (
    verify_explainability_execution_disabled,
)
from advanced_explainability_attribution.attribution_calculation_disabled import (
    verify_attribution_calculation_disabled,
)
from advanced_explainability_attribution.shap_execution_disabled import (
    verify_shap_execution_disabled,
)
from advanced_explainability_attribution.lime_execution_disabled import (
    verify_lime_execution_disabled,
)
from advanced_explainability_attribution.permutation_importance_disabled import (
    verify_permutation_importance_disabled,
)
from advanced_explainability_attribution.pdp_ice_execution_disabled import (
    verify_pdp_ice_execution_disabled,
)
from advanced_explainability_attribution.surrogate_model_execution_disabled import (
    verify_surrogate_model_execution_disabled,
)
from advanced_explainability_attribution.counterfactual_execution_disabled import (
    verify_counterfactual_execution_disabled,
)
from advanced_explainability_attribution.explanation_model_action_disabled import (
    verify_explanation_model_action_disabled,
)
from advanced_explainability_attribution.explainability_metric_placeholders import (
    build_explainability_metric_placeholder_registry,
)
from advanced_explainability_attribution.attribution_quality_gates import (
    build_attribution_quality_gate_registry,
)
from advanced_explainability_attribution.explanation_stability_placeholders import (
    build_explanation_stability_placeholder_registry,
)
from advanced_explainability_attribution.attribution_drift_linkage import (
    build_attribution_drift_linkage_registry,
)
from advanced_explainability_attribution.featurestore_explainability_linkage import (
    build_featurestore_explainability_linkage_registry,
)
from advanced_explainability_attribution.regime_explainability_linkage import (
    build_regime_explainability_linkage_registry,
)
from advanced_explainability_attribution.drift_explainability_linkage import (
    build_drift_explainability_linkage_registry,
)
from advanced_explainability_attribution.calibration_uncertainty_explainability_linkage import (
    build_calibration_uncertainty_explainability_linkage_registry,
)
from advanced_explainability_attribution.explainability_validation_dependencies import (
    verify_explainability_validation_dependencies,
)
from advanced_explainability_attribution.explainability_quality_dependencies import (
    verify_explainability_quality_dependencies,
)
from advanced_explainability_attribution.explainability_runtime_dependencies import (
    verify_explainability_runtime_dependencies,
)
from advanced_explainability_attribution.explainability_candidate_model_dependencies import (
    verify_explainability_candidate_model_dependencies,
)
from advanced_explainability_attribution.explainability_ensemble_dependencies import (
    verify_explainability_ensemble_dependencies,
)
from advanced_explainability_attribution.explainability_no_lookahead_guards import (
    verify_explainability_no_lookahead_guards,
)
from advanced_explainability_attribution.explainability_metadata_only_news_guards import (
    verify_explainability_metadata_only_news_guards,
)
from advanced_explainability_attribution.explainability_source_preservation_guards import (
    verify_explainability_source_preservation_guards,
)
from advanced_explainability_attribution.explainability_forbidden_column_policies import (
    build_forbidden_column_policy_registry,
)
from advanced_explainability_attribution.explainability_lineage import (
    build_explainability_lineage_registry,
)
from advanced_explainability_attribution.explainability_experiment_linkage import (
    build_explainability_experiment_linkage_registry,
)
from advanced_explainability_attribution.explainability_audit_placeholders import (
    build_explainability_audit_placeholder_registry,
)
from advanced_explainability_attribution.explainability_manual_review import (
    build_explainability_manual_review_queue,
)
from advanced_explainability_attribution.explainability_findings import (
    build_explainability_findings_registry,
)
from advanced_explainability_attribution.explainability_readiness_scoring import (
    calculate_explainability_readiness_score,
    build_explainability_readiness_dataframe,
)
from advanced_explainability_attribution.explainability_manifest import (
    build_explainability_manifest,
    summarize_explainability_manifest,
)


def run_explainability_pipeline(
    profile: Optional[ExplainabilityProfile] = None,
) -> Dict[str, Any]:
    """Execute the full Phase 143 explainability contract pipeline in dry-run mode."""
    prof = profile or get_explainability_profile()

    # 1. Registries & Profiles
    df_profiles, sum_profiles = build_explainability_profile_registry()
    df_domains, sum_domains = build_explainability_domain_registry(prof)
    df_reports, sum_reports = build_explainability_report_contracts(prof)
    df_attrib, sum_attrib = build_feature_attribution_contracts(prof)
    df_global, sum_global = build_global_explanation_contract_registry(prof)
    df_local, sum_local = build_local_explanation_contract_registry(prof)

    # 2. Placeholders
    df_fimp, sum_fimp = build_feature_importance_placeholder_registry(prof)
    df_fcontrib, sum_fcontrib = build_feature_contribution_placeholder_registry(prof)
    df_shap, sum_shap = build_shap_placeholder_registry(prof)
    df_lime, sum_lime = build_lime_placeholder_registry(prof)
    df_perm, sum_perm = build_permutation_importance_placeholder_registry(prof)
    df_pdp, sum_pdp = build_partial_dependence_placeholder_registry(prof)
    df_ice, sum_ice = build_ice_placeholder_registry(prof)
    df_surr, sum_surr = build_surrogate_model_placeholder_registry(prof)
    df_cf, sum_cf = build_counterfactual_placeholder_registry(prof)
    df_rc, sum_rc = build_reason_code_placeholder_registry(prof)

    # 3. Policies & I/O Contracts
    df_mpol, sum_mpol = build_attribution_method_policy_registry(prof)
    df_spol, sum_spol = build_attribution_scope_policy_registry(prof)
    df_in_c, sum_in_c = build_attribution_input_contract_registry(prof)
    df_out_c, sum_out_c = build_attribution_output_contract_registry(prof)

    # 4. Disabled Execution Safeguards (9 suites, 36 checks)
    df_dis_exp, sum_dis_exp = verify_explainability_execution_disabled(prof)
    df_dis_att, sum_dis_att = verify_attribution_calculation_disabled(prof)
    df_dis_shap, sum_dis_shap = verify_shap_execution_disabled(prof)
    df_dis_lime, sum_dis_lime = verify_lime_execution_disabled(prof)
    df_dis_perm, sum_dis_perm = verify_permutation_importance_disabled(prof)
    df_dis_pdp, sum_dis_pdp = verify_pdp_ice_execution_disabled(prof)
    df_dis_surr, sum_dis_surr = verify_surrogate_model_execution_disabled(prof)
    df_dis_cf, sum_dis_cf = verify_counterfactual_execution_disabled(prof)
    df_dis_act, sum_dis_act = verify_explanation_model_action_disabled(prof)

    # 5. Metrics, Quality & Stability
    df_metric, sum_metric = build_explainability_metric_placeholder_registry(prof)
    df_qgate, sum_qgate = build_attribution_quality_gate_registry(prof)
    df_stab, sum_stab = build_explanation_stability_placeholder_registry(prof)

    # 6. Linkages
    df_drift_link, sum_drift_link = build_attribution_drift_linkage_registry(prof)
    df_fs_link, sum_fs_link = build_featurestore_explainability_linkage_registry(prof)
    df_reg_link, sum_reg_link = build_regime_explainability_linkage_registry(prof)
    df_mon_link, sum_mon_link = build_drift_explainability_linkage_registry(prof)
    df_cal_link, sum_cal_link = build_calibration_uncertainty_explainability_linkage_registry(prof)

    # 7. Dependencies & Guards
    df_val_dep, sum_val_dep = verify_explainability_validation_dependencies(prof)
    df_qua_dep, sum_qua_dep = verify_explainability_quality_dependencies(prof)
    df_run_dep, sum_run_dep = verify_explainability_runtime_dependencies(prof)
    df_can_dep, sum_can_dep = verify_explainability_candidate_model_dependencies(prof)
    df_ens_dep, sum_ens_dep = verify_explainability_ensemble_dependencies(prof)

    df_guard_look, sum_guard_look = verify_explainability_no_lookahead_guards(prof)
    df_guard_meta, sum_guard_meta = verify_explainability_metadata_only_news_guards(prof)
    df_guard_pres, sum_guard_pres = verify_explainability_source_preservation_guards(prof)
    df_forbid, sum_forbid = build_forbidden_column_policy_registry(prof)

    # 8. Lineage, Experiments, Audit, Reviews & Findings
    df_lineage, sum_lineage = build_explainability_lineage_registry(prof)
    df_exp_link, sum_exp_link = build_explainability_experiment_linkage_registry(prof)
    df_audit, sum_audit = build_explainability_audit_placeholder_registry(prof)
    df_reviews, sum_reviews = build_explainability_manual_review_queue(prof)
    df_findings, sum_findings = build_explainability_findings_registry(prof)

    # 9. Readiness & Manifest
    score_obj = calculate_explainability_readiness_score(
        profile=prof,
        finding_count=len(df_findings),
        manual_review_count=len(df_reviews),
    )
    df_readiness, sum_readiness = build_explainability_readiness_dataframe(score_obj)

    manifest_obj = build_explainability_manifest(
        profile=prof,
        explainability_contract_count=len(df_reports),
        attribution_contract_count=len(df_attrib),
        disabled_execution_report_count=(
            len(df_dis_exp) + len(df_dis_att) + len(df_dis_shap) + len(df_dis_lime)
            + len(df_dis_perm) + len(df_dis_pdp) + len(df_dis_surr) + len(df_dis_cf)
            + len(df_dis_act)
        ),
        finding_count=len(df_findings),
        manual_review_count=len(df_reviews),
        readiness_score=score_obj.readiness_score,
    )
    sum_manifest = summarize_explainability_manifest(manifest_obj)

    return {
        "profile": prof.profile_name,
        "manifest": sum_manifest,
        "readiness": sum_readiness,
        "reports_summary": sum_reports,
        "attribution_summary": sum_attrib,
        "safeguards_summary": {
            "all_execution_disabled": (
                sum_dis_exp["all_disabled"]
                and sum_dis_att["all_disabled"]
                and sum_dis_shap["all_disabled"]
                and sum_dis_lime["all_disabled"]
                and sum_dis_perm["all_disabled"]
                and sum_dis_pdp["all_disabled"]
                and sum_dis_surr["all_disabled"]
                and sum_dis_cf["all_disabled"]
                and sum_dis_act["all_disabled"]
            ),
            "zero_violations": (
                sum_guard_look["zero_violations"]
                and sum_guard_meta["zero_violations"]
                and sum_guard_pres["zero_violations"]
            ),
        },
        "success": True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
