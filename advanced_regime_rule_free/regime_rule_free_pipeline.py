"""Phase 128: Regime Rule-Free Master Pipeline.

Orchestrates all Phase 128 registries, contracts, schemas, safety guards, and handoffs
with DataLake persistence and zero-execution dry-run support.
"""

from pathlib import Path
from typing import Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    RegimeRuleFreeProfile,
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_profile_registry import (
    build_regime_rule_free_profile_registry,
)
from advanced_regime_rule_free.regime_rule_free_domain_registry import (
    build_regime_rule_free_domain_registry,
)
from advanced_regime_rule_free.rule_free_labeling_contracts import (
    build_rule_free_labeling_contract_registry,
)
from advanced_regime_rule_free.candidate_state_assignment_policies import (
    build_candidate_state_assignment_policy_registry,
)
from advanced_regime_rule_free.candidate_state_schema import (
    build_candidate_state_schema_registry,
)
from advanced_regime_rule_free.pseudo_state_schema import (
    build_pseudo_state_schema_registry,
)
from advanced_regime_rule_free.unsupervised_prep_contracts import (
    build_unsupervised_prep_contract_registry,
)
from advanced_regime_rule_free.clustering_input_contracts import (
    build_clustering_input_contract_registry,
)
from advanced_regime_rule_free.clustering_algorithm_placeholders import (
    build_clustering_algorithm_placeholder_registry,
)
from advanced_regime_rule_free.distance_metric_placeholders import (
    build_distance_metric_placeholder_registry,
)
from advanced_regime_rule_free.normalization_prep_contracts import (
    build_normalization_prep_contract_registry,
)
from advanced_regime_rule_free.scaling_prep_contracts import (
    build_scaling_prep_contract_registry,
)
from advanced_regime_rule_free.dimensionality_reduction_placeholders import (
    build_dimensionality_reduction_placeholder_registry,
)
from advanced_regime_rule_free.regime_candidate_feature_sets import (
    build_regime_candidate_feature_set_registry,
)
from advanced_regime_rule_free.regime_candidate_state_context import (
    build_regime_candidate_state_context_registry,
)
from advanced_regime_rule_free.regime_candidate_state_metadata import (
    build_regime_candidate_state_metadata_registry,
)
from advanced_regime_rule_free.regime_candidate_state_namespace import (
    build_regime_candidate_state_namespace_registry,
)
from advanced_regime_rule_free.regime_candidate_state_integrity_contracts import (
    build_regime_candidate_state_integrity_contract_registry,
)
from advanced_regime_rule_free.regime_candidate_state_integrity_manifest import (
    build_regime_candidate_state_integrity_manifest,
)
from advanced_regime_rule_free.regime_candidate_state_no_lookahead_guard import (
    build_regime_candidate_state_no_lookahead_guard_registry,
)
from advanced_regime_rule_free.regime_candidate_state_timestamp_policies import (
    build_regime_candidate_state_timestamp_policy_registry,
)
from advanced_regime_rule_free.regime_candidate_state_quality_dependencies import (
    build_regime_candidate_state_quality_dependency_registry,
)
from advanced_regime_rule_free.regime_candidate_state_validation_dependencies import (
    build_regime_candidate_state_validation_dependency_registry,
)
from advanced_regime_rule_free.regime_candidate_state_manual_review import (
    build_regime_candidate_state_manual_review_queue,
)
from advanced_regime_rule_free.regime_rule_free_non_signal_policies import (
    build_regime_rule_free_non_signal_policy_registry,
)
from advanced_regime_rule_free.regime_rule_free_forbidden_claims import (
    build_regime_rule_free_forbidden_claim_registry,
)
from advanced_regime_rule_free.regime_rule_free_source_preservation_policies import (
    build_regime_rule_free_source_preservation_policy_registry,
)
from advanced_regime_rule_free.regime_rule_free_safety_boundary import (
    build_regime_rule_free_safety_boundary,
)
from advanced_regime_rule_free.regime_rule_free_health import (
    build_regime_rule_free_health_check,
)
from advanced_regime_rule_free.regime_rule_free_validation import (
    build_regime_rule_free_validation_report,
)
from advanced_regime_rule_free.phase_129_handoff import (
    build_phase_129_market_behavior_diagnostics_handoff_report,
)


class RegimeRuleFreePipeline:
    """Master pipeline orchestrator for Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[RegimeRuleFreeProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_regime_rule_free_profile()

    def build_profiles_domains_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_prof, s_prof = build_regime_rule_free_profile_registry(self.profile)
        df_dom, s_dom = build_regime_rule_free_domain_registry(self.profile)
        df_cont, s_cont = build_rule_free_labeling_contract_registry(self.profile)
        df_pol, s_pol = build_candidate_state_assignment_policy_registry(self.profile)

        tables = {
            "profiles": df_prof,
            "domains": df_dom,
            "labeling_contracts": df_cont,
            "assignment_policies": df_pol,
        }
        summaries = {
            "profiles": s_prof,
            "domains": s_dom,
            "labeling_contracts": s_cont,
            "assignment_policies": s_pol,
        }

        if save and hasattr(self.data_lake, "save_regime_rule_free_profile_registry"):
            self.data_lake.save_regime_rule_free_profile_registry(df_prof, s_prof)
            self.data_lake.save_regime_rule_free_domain_registry(df_dom, s_dom)
            self.data_lake.save_rule_free_labeling_contract_registry(df_cont, s_cont)
            self.data_lake.save_candidate_state_assignment_policy_registry(df_pol, s_pol)

        return tables, summaries

    def build_candidate_state_schemas(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_cs, s_cs = build_candidate_state_schema_registry(self.profile)
        df_ps, s_ps = build_pseudo_state_schema_registry(self.profile)
        df_ns, s_ns = build_regime_candidate_state_namespace_registry(self.profile)

        tables = {
            "candidate_state_schema": df_cs,
            "pseudo_state_schema": df_ps,
            "namespace": df_ns,
        }
        summaries = {
            "candidate_state_schema": s_cs,
            "pseudo_state_schema": s_ps,
            "namespace": s_ns,
        }

        if save and hasattr(self.data_lake, "save_candidate_state_schema_registry"):
            self.data_lake.save_candidate_state_schema_registry(df_cs, s_cs)
            self.data_lake.save_pseudo_state_schema_registry(df_ps, s_ps)
            self.data_lake.save_regime_candidate_state_namespace_registry(df_ns, s_ns)

        return tables, summaries

    def build_unsupervised_prep_registries(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_prep, s_prep = build_unsupervised_prep_contract_registry(self.profile)
        df_cinp, s_cinp = build_clustering_input_contract_registry(self.profile)
        df_calg, s_calg = build_clustering_algorithm_placeholder_registry(self.profile)
        df_dist, s_dist = build_distance_metric_placeholder_registry(self.profile)
        df_norm, s_norm = build_normalization_prep_contract_registry(self.profile)
        df_scal, s_scal = build_scaling_prep_contract_registry(self.profile)
        df_dimr, s_dimr = build_dimensionality_reduction_placeholder_registry(self.profile)

        tables = {
            "unsupervised_prep": df_prep,
            "clustering_inputs": df_cinp,
            "clustering_algorithms": df_calg,
            "distance_metrics": df_dist,
            "normalization": df_norm,
            "scaling": df_scal,
            "dimensionality_reduction": df_dimr,
        }
        summaries = {
            "unsupervised_prep": s_prep,
            "clustering_inputs": s_cinp,
            "clustering_algorithms": s_calg,
            "distance_metrics": s_dist,
            "normalization": s_norm,
            "scaling": s_scal,
            "dimensionality_reduction": s_dimr,
        }

        if save and hasattr(self.data_lake, "save_unsupervised_prep_contract_registry"):
            self.data_lake.save_unsupervised_prep_contract_registry(df_prep, s_prep)
            self.data_lake.save_clustering_input_contract_registry(df_cinp, s_cinp)
            self.data_lake.save_clustering_algorithm_placeholder_registry(df_calg, s_calg)
            self.data_lake.save_distance_metric_placeholder_registry(df_dist, s_dist)
            self.data_lake.save_normalization_prep_contract_registry(df_norm, s_norm)
            self.data_lake.save_scaling_prep_contract_registry(df_scal, s_scal)
            self.data_lake.save_dimensionality_reduction_placeholder_registry(df_dimr, s_dimr)

        return tables, summaries

    def build_candidate_feature_metadata(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_cfs, s_cfs = build_regime_candidate_feature_set_registry(self.profile)
        df_ctx, s_ctx = build_regime_candidate_state_context_registry(self.profile)
        df_meta, s_meta = build_regime_candidate_state_metadata_registry(self.profile)

        tables = {
            "candidate_feature_sets": df_cfs,
            "candidate_context": df_ctx,
            "candidate_metadata": df_meta,
        }
        summaries = {
            "candidate_feature_sets": s_cfs,
            "candidate_context": s_ctx,
            "candidate_metadata": s_meta,
        }

        if save and hasattr(self.data_lake, "save_regime_candidate_feature_set_registry"):
            self.data_lake.save_regime_candidate_feature_set_registry(df_cfs, s_cfs)
            self.data_lake.save_regime_candidate_state_context_registry(df_ctx, s_ctx)
            self.data_lake.save_regime_candidate_state_metadata_registry(df_meta, s_meta)

        return tables, summaries

    def build_integrity_guards_dependencies(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_ic, s_ic = build_regime_candidate_state_integrity_contract_registry(self.profile)
        df_nolook, s_nolook = build_regime_candidate_state_no_lookahead_guard_registry(self.profile)
        df_ts, s_ts = build_regime_candidate_state_timestamp_policy_registry(self.profile)
        df_qd, s_qd = build_regime_candidate_state_quality_dependency_registry(self.profile)
        df_vd, s_vd = build_regime_candidate_state_validation_dependency_registry(self.profile)

        tables = {
            "integrity_contracts": df_ic,
            "no_lookahead": df_nolook,
            "timestamp_policy": df_ts,
            "quality_dependencies": df_qd,
            "validation_dependencies": df_vd,
        }
        summaries = {
            "integrity_contracts": s_ic,
            "no_lookahead": s_nolook,
            "timestamp_policy": s_ts,
            "quality_dependencies": s_qd,
            "validation_dependencies": s_vd,
        }

        if save and hasattr(self.data_lake, "save_regime_candidate_state_integrity_contract_registry"):
            self.data_lake.save_regime_candidate_state_integrity_contract_registry(df_ic, s_ic)
            self.data_lake.save_regime_candidate_state_no_lookahead_guard_registry(df_nolook, s_nolook)
            self.data_lake.save_regime_candidate_state_timestamp_policy_registry(df_ts, s_ts)
            self.data_lake.save_regime_candidate_state_quality_dependency_registry(df_qd, s_qd)
            self.data_lake.save_regime_candidate_state_validation_dependency_registry(df_vd, s_vd)

        return tables, summaries

    def build_policies_review_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_rev, s_rev = build_regime_candidate_state_manual_review_queue(self.profile)
        df_nsp, s_nsp = build_regime_rule_free_non_signal_policy_registry(self.profile)
        df_fc, s_fc = build_regime_rule_free_forbidden_claim_registry(self.profile)
        df_sp, s_sp = build_regime_rule_free_source_preservation_policy_registry(self.profile)
        df_man, s_man = build_regime_candidate_state_integrity_manifest(self.profile)

        tables = {
            "manual_review": df_rev,
            "non_signal_policies": df_nsp,
            "forbidden_claims": df_fc,
            "source_preservation": df_sp,
            "integrity_manifest": df_man,
        }
        summaries = {
            "manual_review": s_rev,
            "non_signal_policies": s_nsp,
            "forbidden_claims": s_fc,
            "source_preservation": s_sp,
            "integrity_manifest": s_man,
        }

        if save and hasattr(self.data_lake, "save_regime_candidate_state_manual_review_queue"):
            self.data_lake.save_regime_candidate_state_manual_review_queue(df_rev, s_rev)
            self.data_lake.save_regime_rule_free_non_signal_policy_registry(df_nsp, s_nsp)
            self.data_lake.save_regime_rule_free_forbidden_claim_registry(df_fc, s_fc)
            self.data_lake.save_regime_rule_free_source_preservation_policy_registry(df_sp, s_sp)
            self.data_lake.save_regime_candidate_state_integrity_manifest(df_man, s_man)

        return tables, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict]:
        df_health, s_health = build_regime_rule_free_health_check(self.project_root, self.profile)
        df_safe, s_safe = build_regime_rule_free_safety_boundary(self.profile)
        df_h129, s_h129 = build_phase_129_market_behavior_diagnostics_handoff_report(self.profile)

        # Build validation using available tables
        p_tables, _ = self.build_profiles_domains_contracts(save=False)
        s_tables, _ = self.build_candidate_state_schemas(save=False)
        u_tables, _ = self.build_unsupervised_prep_registries(save=False)
        m_tables, _ = self.build_policies_review_manifest(save=False)

        val_input_tables = {**p_tables, **s_tables, **u_tables, **m_tables}
        df_val, s_val = build_regime_rule_free_validation_report(val_input_tables, self.profile)

        tables = {
            "health": df_health,
            "safety": df_safe,
            "validation": df_val,
            "phase_129_handoff": df_h129,
        }
        summaries = {
            "health": s_health,
            "safety": s_safe,
            "validation": s_val,
            "phase_129_handoff": s_h129,
        }

        if save and hasattr(self.data_lake, "save_regime_rule_free_health_check"):
            self.data_lake.save_regime_rule_free_health_check(df_health, s_health)
            self.data_lake.save_regime_rule_free_safety_boundary(df_safe, s_safe)
            self.data_lake.save_regime_rule_free_validation_report(df_val, s_val)
            self.data_lake.save_phase_129_market_behavior_diagnostics_handoff_report(df_h129, s_h129)

        return tables, summaries

    def build_regime_rule_free_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict]:
        """Aggregate master Phase 128 pipeline status."""
        h_tables, h_summaries = self.build_health_validation_safety_handoff(save=save)
        val_sum = h_summaries["validation"]
        health_sum = h_summaries["health"]
        safe_sum = h_summaries["safety"]
        h129_sum = h_summaries["phase_129_handoff"]

        status_rows = [
            {"component": "profile_registry", "status": "READY", "details": self.profile.profile_name},
            {"component": "labeling_contracts", "status": "READY", "details": "8 candidate state contracts"},
            {"component": "candidate_state_schema", "status": "READY", "details": "12 standard columns, zero targets"},
            {"component": "pseudo_state_schema", "status": "READY", "details": "8 pseudo-states, non-signal"},
            {"component": "unsupervised_prep_contracts", "status": "READY", "details": "6 prep contracts, no execution"},
            {"component": "clustering_input_contracts", "status": "READY", "details": "5 clustering input specs"},
            {"component": "algorithm_placeholders", "status": "READY", "details": "6 clustering, 5 distance, 4 dim reduction"},
            {"component": "integrity_manifest", "status": "VALID", "details": "Zero execution, zero lookahead"},
            {"component": "health_check", "status": health_sum.get("health_status", "HEALTHY"), "details": f"{health_sum.get('passed_checks')}/{health_sum.get('total_checks')} passed"},
            {"component": "validation_report", "status": val_sum.get("validation_status", "VALIDATION_PASS"), "details": f"{val_sum.get('passed_checks')}/{val_sum.get('total_checks')} passed"},
            {"component": "safety_boundary", "status": safe_sum.get("safety_status", "SECURE"), "details": f"{safe_sum.get('no_go_count')} NO-GO, {safe_sum.get('safe_go_count')} SAFE-GO"},
            {"component": "phase_129_handoff", "status": h129_sum.get("handoff_status", "READY"), "details": "12 items verified"},
        ]

        df_status = pd.DataFrame(status_rows)
        overall_ready = (
            health_sum.get("all_healthy", False)
            and val_sum.get("validation_status") == "VALIDATION_PASS"
            and safe_sum.get("safety_status") == "SECURE"
            and h129_sum.get("handoff_status") == "READY"
        )

        summary = {
            "profile_name": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "next_phase": self.profile.next_phase,
            "target_final_phase": self.profile.target_final_phase,
            "overall_status": "READY" if overall_ready else "NEEDS_REVIEW",
            "non_signal": True,
            "zero_execution": True,
            "components_count": len(df_status),
        }

        if save and hasattr(self.data_lake, "save_regime_rule_free_report"):
            self.data_lake.save_regime_rule_free_report(self.profile.profile_name, summary)

        return df_status, summary
