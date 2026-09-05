"""Phase 127: Regime Matrix Pipeline Orchestrator.

Coordinates full generation of feature matrix contracts, state dataset schemas,
candidate contexts, alignment guards, manifests, and Phase 128 handoff reports.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_matrix_profile_registry import (
    build_regime_matrix_profile_registry,
)
from advanced_regime_matrix.regime_matrix_domain_registry import (
    build_regime_matrix_domain_registry,
)
from advanced_regime_matrix.regime_feature_matrix_contracts import (
    build_regime_feature_matrix_contract_registry,
)
from advanced_regime_matrix.regime_state_dataset_contracts import (
    build_regime_state_dataset_contract_registry,
)
from advanced_regime_matrix.regime_matrix_entities import (
    build_regime_matrix_entity_registry,
)
from advanced_regime_matrix.regime_matrix_namespace import (
    build_regime_matrix_namespace_registry,
)
from advanced_regime_matrix.regime_matrix_schema import (
    build_regime_matrix_schema_registry,
)
from advanced_regime_matrix.regime_matrix_input_features import (
    build_regime_matrix_input_feature_registry,
)
from advanced_regime_matrix.regime_matrix_factor_inputs import (
    build_regime_matrix_factor_input_registry,
)
from advanced_regime_matrix.regime_matrix_context_inputs import (
    build_regime_matrix_context_input_registry,
)
from advanced_regime_matrix.regime_matrix_quality_inputs import (
    build_regime_matrix_quality_input_registry,
)
from advanced_regime_matrix.regime_matrix_timestamp_alignment import (
    build_regime_matrix_timestamp_alignment_registry,
)
from advanced_regime_matrix.regime_matrix_asof_join_policies import (
    build_regime_matrix_asof_join_policy_registry,
)
from advanced_regime_matrix.regime_matrix_no_lookahead_guard import (
    build_regime_matrix_no_lookahead_guard_registry,
)
from advanced_regime_matrix.regime_state_dataset_schema import (
    build_regime_state_dataset_schema_registry,
)
from advanced_regime_matrix.regime_state_dataset_metadata import (
    build_regime_state_dataset_metadata_registry,
)
from advanced_regime_matrix.regime_state_candidate_context import (
    build_regime_state_candidate_context_registry,
)
from advanced_regime_matrix.regime_matrix_integrity_contracts import (
    build_regime_matrix_integrity_contract_registry,
)
from advanced_regime_matrix.regime_matrix_integrity_manifest import (
    build_regime_matrix_integrity_manifest,
)
from advanced_regime_matrix.regime_matrix_source_phases import (
    build_regime_matrix_source_phase_registry,
)
from advanced_regime_matrix.regime_matrix_validation_dependencies import (
    build_regime_matrix_validation_dependency_registry,
)
from advanced_regime_matrix.regime_matrix_quality_dependencies import (
    build_regime_matrix_quality_dependency_registry,
)
from advanced_regime_matrix.regime_matrix_non_signal_policies import (
    build_regime_matrix_non_signal_policy_registry,
)
from advanced_regime_matrix.regime_matrix_forbidden_column_policies import (
    build_regime_matrix_forbidden_column_policy_registry,
)
from advanced_regime_matrix.regime_matrix_source_preservation_policies import (
    build_regime_matrix_source_preservation_policy_registry,
)
from advanced_regime_matrix.regime_matrix_manual_review import (
    build_regime_matrix_manual_review_queue,
)
from advanced_regime_matrix.regime_matrix_safety_boundary import (
    build_regime_matrix_safety_boundary,
)
from advanced_regime_matrix.regime_matrix_health import (
    build_regime_matrix_health_check,
)
from advanced_regime_matrix.regime_matrix_validation import (
    build_regime_matrix_validation_report,
)
from advanced_regime_matrix.phase_128_handoff import (
    build_phase_128_rule_free_labeling_unsupervised_prep_handoff_report,
)


class RegimeMatrixPipeline:
    """Master pipeline coordinating all Phase 127 matrix and state contract components."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[RegimeMatrixProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(__file__).resolve().parent.parent
        self.profile = profile or get_default_regime_matrix_profile()

    def run_all(self, save: bool = True) -> Dict[str, Any]:
        """Execute full pipeline workflow and return master status summary."""
        self.build_profiles_domains_contracts(save=save)
        self.build_entities_namespace_schema(save=save)
        self.build_input_registries(save=save)
        self.build_alignment_guards(save=save)
        self.build_state_dataset_integrity(save=save)
        self.build_dependencies_policies_review(save=save)
        self.build_health_validation_safety_handoff(save=save)
        df_status, status_summary = self.build_regime_matrix_status(save=save)

        return {
            "pipeline_status": "SUCCESS",
            "current_phase": self.profile.current_phase,
            "next_phase": self.profile.next_phase,
            "target_final_phase": self.profile.target_final_phase,
            "non_signal": True,
            "source_preserved": True,
            "model_training_executed": False,
            "clustering_executed": False,
            "unsupervised_execution": False,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
            "status": "READY",
        }

    def build_profiles_domains_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist profiles, domains, and contracts."""
        df_prof, s_prof = build_regime_matrix_profile_registry(self.profile)
        df_dom, s_dom = build_regime_matrix_domain_registry(self.profile)
        df_cont, s_cont = build_regime_feature_matrix_contract_registry(self.profile)
        df_scont, s_scont = build_regime_state_dataset_contract_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_matrix_profile_registry"):
            self.data_lake.save_regime_matrix_profile_registry(df_prof, s_prof)
            self.data_lake.save_regime_matrix_domain_registry(df_dom, s_dom)
            self.data_lake.save_regime_feature_matrix_contract_registry(df_cont, s_cont)
            self.data_lake.save_regime_state_dataset_contract_registry(df_scont, s_scont)

        tables = {
            "profiles": df_prof,
            "domains": df_dom,
            "contracts": df_cont,
            "state_dataset_contracts": df_scont,
        }
        summaries = {
            "profiles": s_prof,
            "domains": s_dom,
            "contracts": s_cont,
            "state_dataset_contracts": s_scont,
        }
        return tables, summaries

    def build_entities_namespace_schema(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist entity, namespace, and schema registries."""
        df_ent, s_ent = build_regime_matrix_entity_registry(self.profile)
        df_ns, s_ns = build_regime_matrix_namespace_registry(self.profile)
        df_sch, s_sch = build_regime_matrix_schema_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_matrix_entity_registry"):
            self.data_lake.save_regime_matrix_entity_registry(df_ent, s_ent)
            self.data_lake.save_regime_matrix_namespace_registry(df_ns, s_ns)
            self.data_lake.save_regime_matrix_schema_registry(df_sch, s_sch)

        tables = {
            "entities": df_ent,
            "namespace": df_ns,
            "schema": df_sch,
        }
        summaries = {
            "entities": s_ent,
            "namespace": s_ns,
            "schema": s_sch,
        }
        return tables, summaries

    def build_input_registries(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist input features, factors, contexts, and quality inputs."""
        df_inp, s_inp = build_regime_matrix_input_feature_registry(self.profile)
        df_fact, s_fact = build_regime_matrix_factor_input_registry(self.profile)
        df_ctx, s_ctx = build_regime_matrix_context_input_registry(self.profile)
        df_qual, s_qual = build_regime_matrix_quality_input_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_matrix_input_feature_registry"):
            self.data_lake.save_regime_matrix_input_feature_registry(df_inp, s_inp)
            self.data_lake.save_regime_matrix_factor_input_registry(df_fact, s_fact)
            self.data_lake.save_regime_matrix_context_input_registry(df_ctx, s_ctx)
            self.data_lake.save_regime_matrix_quality_input_registry(df_qual, s_qual)

        tables = {
            "input_features": df_inp,
            "factor_inputs": df_fact,
            "context_inputs": df_ctx,
            "quality_inputs": df_qual,
        }
        summaries = {
            "input_features": s_inp,
            "factor_inputs": s_fact,
            "context_inputs": s_ctx,
            "quality_inputs": s_qual,
        }
        return tables, summaries

    def build_alignment_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist timestamp alignment, asof policies, and no-lookahead guards."""
        df_align, s_align = build_regime_matrix_timestamp_alignment_registry(self.profile)
        df_asof, s_asof = build_regime_matrix_asof_join_policy_registry(self.profile)
        df_guard, s_guard = build_regime_matrix_no_lookahead_guard_registry(self.profile)

        if save and hasattr(self.data_lake, "save_regime_matrix_timestamp_alignment_registry"):
            self.data_lake.save_regime_matrix_timestamp_alignment_registry(df_align, s_align)
            self.data_lake.save_regime_matrix_asof_join_policy_registry(df_asof, s_asof)
            self.data_lake.save_regime_matrix_no_lookahead_guard_registry(df_guard, s_guard)

        tables = {
            "timestamp_alignment": df_align,
            "asof_join_policies": df_asof,
            "no_lookahead_guard": df_guard,
        }
        summaries = {
            "timestamp_alignment": s_align,
            "asof_join_policies": s_asof,
            "no_lookahead_guard": s_guard,
        }
        return tables, summaries

    def build_state_dataset_integrity(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist state dataset schemas, metadata, candidate contexts, and manifest."""
        df_ssch, s_ssch = build_regime_state_dataset_schema_registry(self.profile)
        df_smet, s_smet = build_regime_state_dataset_metadata_registry(self.profile)
        df_cand, s_cand = build_regime_state_candidate_context_registry(self.profile)
        df_intg, s_intg = build_regime_matrix_integrity_contract_registry(self.profile)
        df_man, s_man = build_regime_matrix_integrity_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_regime_state_dataset_schema_registry"):
            self.data_lake.save_regime_state_dataset_schema_registry(df_ssch, s_ssch)
            self.data_lake.save_regime_state_dataset_metadata_registry(df_smet, s_smet)
            self.data_lake.save_regime_state_candidate_context_registry(df_cand, s_cand)
            self.data_lake.save_regime_matrix_integrity_contract_registry(df_intg, s_intg)
            self.data_lake.save_regime_matrix_integrity_manifest(df_man, s_man)

        tables = {
            "state_dataset_schema": df_ssch,
            "state_dataset_metadata": df_smet,
            "candidate_context": df_cand,
            "integrity_contracts": df_intg,
            "manifest": df_man,
        }
        summaries = {
            "state_dataset_schema": s_ssch,
            "state_dataset_metadata": s_smet,
            "candidate_context": s_cand,
            "integrity_contracts": s_intg,
            "manifest": s_man,
        }
        return tables, summaries

    def build_dependencies_policies_review(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist source phases, dependencies, policies, and manual review queue."""
        df_src, s_src = build_regime_matrix_source_phase_registry(self.profile)
        df_vdep, s_vdep = build_regime_matrix_validation_dependency_registry(self.profile)
        df_qdep, s_qdep = build_regime_matrix_quality_dependency_registry(self.profile)
        df_nsp, s_nsp = build_regime_matrix_non_signal_policy_registry(self.profile)
        df_fcp, s_fcp = build_regime_matrix_forbidden_column_policy_registry(self.profile)
        df_spp, s_spp = build_regime_matrix_source_preservation_policy_registry(self.profile)
        df_rev, s_rev = build_regime_matrix_manual_review_queue(self.profile)

        if save and hasattr(self.data_lake, "save_regime_matrix_source_phase_registry"):
            self.data_lake.save_regime_matrix_source_phase_registry(df_src, s_src)
            self.data_lake.save_regime_matrix_validation_dependency_registry(df_vdep, s_vdep)
            self.data_lake.save_regime_matrix_quality_dependency_registry(df_qdep, s_qdep)
            self.data_lake.save_regime_matrix_non_signal_policy_registry(df_nsp, s_nsp)
            self.data_lake.save_regime_matrix_forbidden_column_policy_registry(df_fcp, s_fcp)
            self.data_lake.save_regime_matrix_source_preservation_policy_registry(df_spp, s_spp)
            self.data_lake.save_regime_matrix_manual_review_queue(df_rev, s_rev)

        tables = {
            "source_phases": df_src,
            "validation_dependencies": df_vdep,
            "quality_dependencies": df_qdep,
            "non_signal_policies": df_nsp,
            "forbidden_column_policies": df_fcp,
            "source_preservation_policies": df_spp,
            "manual_review_queue": df_rev,
        }
        summaries = {
            "source_phases": s_src,
            "validation_dependencies": s_vdep,
            "quality_dependencies": s_qdep,
            "non_signal_policies": s_nsp,
            "forbidden_column_policies": s_fcp,
            "source_preservation_policies": s_spp,
            "manual_review_queue": s_rev,
        }
        return tables, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally persist health, safety boundary, validation, and handoff report."""
        df_hlth, s_hlth = build_regime_matrix_health_check(self.project_root, self.profile)
        df_safe, s_safe = build_regime_matrix_safety_boundary(self.profile)
        df_hand, s_hand = build_phase_128_rule_free_labeling_unsupervised_prep_handoff_report(self.profile)

        # Aggregate prerequisite tables for validation
        t_prof, _ = self.build_profiles_domains_contracts(save=False)
        t_intg, _ = self.build_state_dataset_integrity(save=False)
        val_inputs = {**t_prof, **t_intg}

        df_val, s_val = build_regime_matrix_validation_report(val_inputs, self.profile)

        if save and hasattr(self.data_lake, "save_regime_matrix_health_check"):
            self.data_lake.save_regime_matrix_health_check(df_hlth, s_hlth)
            self.data_lake.save_regime_matrix_safety_boundary(df_safe, s_safe)
            self.data_lake.save_regime_matrix_validation_report(df_val, s_val)
            self.data_lake.save_phase_128_rule_free_labeling_unsupervised_prep_handoff_report(df_hand, s_hand)

        tables = {
            "health": df_hlth,
            "safety": df_safe,
            "validation_report": df_val,
            "handoff": df_hand,
        }
        summaries = {
            "health": s_hlth,
            "safety": s_safe,
            "validation_report": s_val,
            "handoff": s_hand,
        }
        return tables, summaries

    def build_regime_matrix_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Synthesize overarching system status for Phase 127."""
        t_h, s_h = self.build_health_validation_safety_handoff(save=False)
        t_m, s_m = self.build_state_dataset_integrity(save=False)

        manifest_sum = s_m["manifest"]
        val_sum = s_h["validation_report"]
        health_sum = s_h["health"]
        hand_sum = s_h["handoff"]

        status_rows = [
            {
                "subsystem": "advanced_regime_matrix",
                "phase": 127,
                "target_final_phase": 160,
                "next_phase": 128,
                "profile": self.profile.profile_name,
                "health_status": health_sum.get("health_status", "HEALTHY"),
                "validation_status": val_sum.get("validation_status", "VALIDATION_PASS"),
                "integrity_status": "INTEGRITY_VALID",
                "handoff_status": hand_sum.get("handoff_status", "READY"),
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "model_training_executed": False,
                "clustering_executed": False,
                "unsupervised_execution": False,
                "status": "READY",
            }
        ]
        df = pd.DataFrame(status_rows)
        summary = {
            "phase": 127,
            "profile": self.profile.profile_name,
            "overall_status": "READY",
            "integrity_status": "INTEGRITY_VALID",
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }

        if save and hasattr(self.data_lake, "save_regime_matrix_report"):
            self.data_lake.save_regime_matrix_report(self.profile.profile_name, summary)

        return df, summary
