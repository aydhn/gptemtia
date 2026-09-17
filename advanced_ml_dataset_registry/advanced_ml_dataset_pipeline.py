# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Unified Pipeline Orchestrator.

Orchestrates all dataset contracts, source catalogs, schemas, split policies,
leakage guards, feature snapshot contracts, experiment registries, findings,
readiness scoring, manifest generation, health checks, validation, and Phase 138 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_advanced_ml_dataset_profile,
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_profile_registry import (
    build_advanced_ml_dataset_profile_registry,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_domain_registry import (
    build_advanced_ml_dataset_domain_registry,
)
from advanced_ml_dataset_registry.ml_dataset_contracts import (
    build_ml_dataset_contract_registry,
)
from advanced_ml_dataset_registry.ml_dataset_source_catalog import (
    build_ml_dataset_source_catalog_registry,
)
from advanced_ml_dataset_registry.ml_dataset_schema import (
    build_ml_dataset_schema_registry,
)
from advanced_ml_dataset_registry.ml_dataset_feature_namespace import (
    build_ml_dataset_feature_namespace_registry,
)
from advanced_ml_dataset_registry.ml_dataset_version_policies import (
    build_ml_dataset_version_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_partition_policies import (
    build_ml_dataset_partition_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_time_index_policies import (
    build_ml_dataset_time_index_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_time_series_split_policies import (
    build_ml_dataset_time_series_split_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_walk_forward_split_policies import (
    build_ml_dataset_walk_forward_split_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_purged_split_placeholders import (
    build_ml_dataset_purged_split_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_dataset_leakage_guards import (
    build_ml_dataset_leakage_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_no_lookahead_guards import (
    build_ml_dataset_no_lookahead_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_metadata_only_news_guards import (
    build_ml_dataset_metadata_only_news_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_source_preservation_guards import (
    build_ml_dataset_source_preservation_guard_registry,
)
from advanced_ml_dataset_registry.ml_dataset_forbidden_column_policies import (
    build_ml_dataset_forbidden_column_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_target_label_disabled_policies import (
    build_ml_dataset_target_label_disabled_policy_registry,
)
from advanced_ml_dataset_registry.ml_dataset_feature_snapshot_contracts import (
    build_ml_dataset_feature_snapshot_contract_registry,
)
from advanced_ml_dataset_registry.ml_dataset_feature_snapshot_manifest_placeholders import (
    build_feature_snapshot_manifest_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_dataset_quality_gates import (
    build_ml_dataset_quality_gate_registry,
)
from advanced_ml_dataset_registry.ml_dataset_validation_dependencies import (
    build_ml_dataset_validation_dependency_registry,
)
from advanced_ml_dataset_registry.ml_dataset_quality_dependencies import (
    build_ml_dataset_quality_dependency_registry,
)
from advanced_ml_dataset_registry.ml_dataset_lineage import (
    build_ml_dataset_lineage_registry,
)
from advanced_ml_dataset_registry.ml_experiment_registry import (
    build_ml_experiment_registry,
)
from advanced_ml_dataset_registry.ml_experiment_templates import (
    build_ml_experiment_template_registry,
)
from advanced_ml_dataset_registry.ml_experiment_permissions import (
    build_ml_experiment_permission_registry,
)
from advanced_ml_dataset_registry.ml_experiment_run_plan_placeholders import (
    build_ml_experiment_run_plan_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_model_family_placeholders import (
    build_ml_model_family_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_metric_placeholders import (
    build_ml_metric_placeholder_registry,
)
from advanced_ml_dataset_registry.ml_training_harness_disabled_contracts import (
    build_ml_training_harness_disabled_contract_registry,
)
from advanced_ml_dataset_registry.ml_prediction_disabled_contracts import (
    build_ml_prediction_disabled_contract_registry,
)
from advanced_ml_dataset_registry.ml_artifact_disabled_contracts import (
    build_ml_artifact_disabled_contract_registry,
)
from advanced_ml_dataset_registry.ml_dataset_manual_review import (
    build_ml_dataset_manual_review_queue,
)
from advanced_ml_dataset_registry.ml_dataset_findings import (
    build_ml_dataset_findings_registry,
)
from advanced_ml_dataset_registry.ml_dataset_readiness_scoring import (
    build_ml_dataset_readiness_score_report,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_manifest import (
    build_advanced_ml_dataset_manifest,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_health import (
    build_advanced_ml_dataset_health_check,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_validation import (
    build_advanced_ml_dataset_validation_report,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_safety_boundary import (
    build_advanced_ml_dataset_safety_boundary,
)
from advanced_ml_dataset_registry.phase_138_handoff import (
    build_phase_138_baseline_ml_model_contracts_handoff_report,
)


class AdvancedMlDatasetPipeline:
    """Unified pipeline for Phase 137 Advanced ML Dataset Contracts and Experiment Registry."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[AdvancedMlDatasetProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.data_lake = data_lake or DataLake()
        self.project_root = project_root or Path.cwd()
        self.profile = profile or get_default_advanced_ml_dataset_profile()

    def build_profiles_domains_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 1: Profiles, domains, dataset contracts, and source catalog."""
        p_df, p_sum = build_advanced_ml_dataset_profile_registry(self.profile)
        d_df, d_sum = build_advanced_ml_dataset_domain_registry(self.profile)
        c_df, c_sum = build_ml_dataset_contract_registry(self.profile)
        sc_df, sc_sum = build_ml_dataset_source_catalog_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_dataset_profile_registry"):
            self.data_lake.save_advanced_ml_dataset_profile_registry(p_df, p_sum)
            self.data_lake.save_advanced_ml_dataset_domain_registry(d_df, d_sum)
            self.data_lake.save_ml_dataset_contract_registry(c_df, c_sum)
            self.data_lake.save_ml_dataset_source_catalog_registry(sc_df, sc_sum)

        tables = {"profiles": p_df, "domains": d_df, "contracts": c_df, "source_catalog": sc_df}
        summaries = {"profiles": p_sum, "domains": d_sum, "contracts": c_sum, "source_catalog": sc_sum}
        return tables, summaries

    def build_schema_namespace_policies(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 2: Schemas, namespaces, version, partition, and time index policies."""
        s_df, s_sum = build_ml_dataset_schema_registry(self.profile)
        ns_df, ns_sum = build_ml_dataset_feature_namespace_registry(self.profile)
        vp_df, vp_sum = build_ml_dataset_version_policy_registry(self.profile)
        pp_df, pp_sum = build_ml_dataset_partition_policy_registry(self.profile)
        ti_df, ti_sum = build_ml_dataset_time_index_policy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_ml_dataset_schema_registry"):
            self.data_lake.save_ml_dataset_schema_registry(s_df, s_sum)
            self.data_lake.save_ml_dataset_feature_namespace_registry(ns_df, ns_sum)
            self.data_lake.save_ml_dataset_version_policy_registry(vp_df, vp_sum)
            self.data_lake.save_ml_dataset_partition_policy_registry(pp_df, pp_sum)
            self.data_lake.save_ml_dataset_time_index_policy_registry(ti_df, ti_sum)

        tables = {
            "schemas": s_df,
            "feature_namespace": ns_df,
            "version_policies": vp_df,
            "partition_policies": pp_df,
            "time_index_policies": ti_df,
        }
        summaries = {
            "schemas": s_sum,
            "feature_namespace": ns_sum,
            "version_policies": vp_sum,
            "partition_policies": pp_sum,
            "time_index_policies": ti_sum,
        }
        return tables, summaries

    def build_split_policies_guards(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 3: Split policies and safety guards."""
        ts_df, ts_sum = build_ml_dataset_time_series_split_policy_registry(self.profile)
        wf_df, wf_sum = build_ml_dataset_walk_forward_split_policy_registry(self.profile)
        ps_df, ps_sum = build_ml_dataset_purged_split_placeholder_registry(self.profile)
        lg_df, lg_sum = build_ml_dataset_leakage_guard_registry(self.profile)
        nl_df, nl_sum = build_ml_dataset_no_lookahead_guard_registry(self.profile)
        mn_df, mn_sum = build_ml_dataset_metadata_only_news_guard_registry(self.profile)
        sp_df, sp_sum = build_ml_dataset_source_preservation_guard_registry(self.profile)
        fc_df, fc_sum = build_ml_dataset_forbidden_column_policy_registry(self.profile)
        tl_df, tl_sum = build_ml_dataset_target_label_disabled_policy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_ml_dataset_time_series_split_policy_registry"):
            self.data_lake.save_ml_dataset_time_series_split_policy_registry(ts_df, ts_sum)
            self.data_lake.save_ml_dataset_walk_forward_split_policy_registry(wf_df, wf_sum)
            self.data_lake.save_ml_dataset_purged_split_placeholder_registry(ps_df, ps_sum)
            self.data_lake.save_ml_dataset_leakage_guard_registry(lg_df, lg_sum)
            self.data_lake.save_ml_dataset_no_lookahead_guard_registry(nl_df, nl_sum)
            self.data_lake.save_ml_dataset_metadata_only_news_guard_registry(mn_df, mn_sum)
            self.data_lake.save_ml_dataset_source_preservation_guard_registry(sp_df, sp_sum)
            self.data_lake.save_ml_dataset_forbidden_column_policy_registry(fc_df, fc_sum)
            self.data_lake.save_ml_dataset_target_label_disabled_policy_registry(tl_df, tl_sum)

        tables = {
            "time_series_splits": ts_df,
            "walk_forward_splits": wf_df,
            "purged_splits": ps_df,
            "leakage_guards": lg_df,
            "no_lookahead_guards": nl_df,
            "metadata_only_news_guards": mn_df,
            "source_preservation_guards": sp_df,
            "forbidden_columns": fc_df,
            "target_label_disabled": tl_df,
        }
        summaries = {
            "time_series_splits": ts_sum,
            "walk_forward_splits": wf_sum,
            "purged_splits": ps_sum,
            "leakage_guards": lg_sum,
            "no_lookahead_guards": nl_sum,
            "metadata_only_news_guards": mn_sum,
            "source_preservation_guards": sp_sum,
            "forbidden_columns": fc_sum,
            "target_label_disabled": tl_sum,
        }
        return tables, summaries

    def build_snapshot_quality_lineage(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 4: Snapshot contracts, manifest placeholders, quality gates, dependencies, lineage."""
        sc_df, sc_sum = build_ml_dataset_feature_snapshot_contract_registry(self.profile)
        sm_df, sm_sum = build_feature_snapshot_manifest_placeholder_registry(self.profile)
        qg_df, qg_sum = build_ml_dataset_quality_gate_registry(self.profile)
        vd_df, vd_sum = build_ml_dataset_validation_dependency_registry(self.profile)
        qd_df, qd_sum = build_ml_dataset_quality_dependency_registry(self.profile)
        lin_df, lin_sum = build_ml_dataset_lineage_registry(self.profile)

        if save and hasattr(self.data_lake, "save_ml_dataset_feature_snapshot_contract_registry"):
            self.data_lake.save_ml_dataset_feature_snapshot_contract_registry(sc_df, sc_sum)
            self.data_lake.save_ml_dataset_feature_snapshot_manifest_placeholder_registry(sm_df, sm_sum)
            self.data_lake.save_ml_dataset_quality_gate_registry(qg_df, qg_sum)
            self.data_lake.save_ml_dataset_validation_dependency_registry(vd_df, vd_sum)
            self.data_lake.save_ml_dataset_quality_dependency_registry(qd_df, qd_sum)
            self.data_lake.save_ml_dataset_lineage_registry(lin_df, lin_sum)

        tables = {
            "snapshot_contracts": sc_df,
            "snapshot_manifest_placeholders": sm_df,
            "quality_gates": qg_df,
            "validation_dependencies": vd_df,
            "quality_dependencies": qd_df,
            "lineage": lin_df,
        }
        summaries = {
            "snapshot_contracts": sc_sum,
            "snapshot_manifest_placeholders": sm_sum,
            "quality_gates": qg_sum,
            "validation_dependencies": vd_sum,
            "quality_dependencies": qd_sum,
            "lineage": lin_sum,
        }
        return tables, summaries

    def build_experiment_registry(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 5: Experiment registry, templates, permissions, placeholders, disabled contracts."""
        er_df, er_sum = build_ml_experiment_registry(self.profile)
        et_df, et_sum = build_ml_experiment_template_registry(self.profile)
        ep_df, ep_sum = build_ml_experiment_permission_registry(self.profile)
        rp_df, rp_sum = build_ml_experiment_run_plan_placeholder_registry(self.profile)
        mf_df, mf_sum = build_ml_model_family_placeholder_registry(self.profile)
        mp_df, mp_sum = build_ml_metric_placeholder_registry(self.profile)
        th_df, th_sum = build_ml_training_harness_disabled_contract_registry(self.profile)
        pd_df, pd_sum = build_ml_prediction_disabled_contract_registry(self.profile)
        ad_df, ad_sum = build_ml_artifact_disabled_contract_registry(self.profile)

        if save and hasattr(self.data_lake, "save_ml_experiment_registry"):
            self.data_lake.save_ml_experiment_registry(er_df, er_sum)
            self.data_lake.save_ml_experiment_template_registry(et_df, et_sum)
            self.data_lake.save_ml_experiment_permission_registry(ep_df, ep_sum)
            self.data_lake.save_ml_experiment_run_plan_placeholder_registry(rp_df, rp_sum)
            self.data_lake.save_ml_model_family_placeholder_registry(mf_df, mf_sum)
            self.data_lake.save_ml_metric_placeholder_registry(mp_df, mp_sum)
            self.data_lake.save_ml_training_harness_disabled_contract_registry(th_df, th_sum)
            self.data_lake.save_ml_prediction_disabled_contract_registry(pd_df, pd_sum)
            self.data_lake.save_ml_artifact_disabled_contract_registry(ad_df, ad_sum)

        tables = {
            "experiments": er_df,
            "templates": et_df,
            "permissions": ep_df,
            "run_plan_placeholders": rp_df,
            "model_families": mf_df,
            "metrics": mp_df,
            "training_disabled": th_df,
            "prediction_disabled": pd_df,
            "artifact_disabled": ad_df,
        }
        summaries = {
            "experiments": er_sum,
            "templates": et_sum,
            "permissions": ep_sum,
            "run_plan_placeholders": rp_sum,
            "model_families": mf_sum,
            "metrics": mp_sum,
            "training_disabled": th_sum,
            "prediction_disabled": pd_sum,
            "artifact_disabled": ad_sum,
        }
        return tables, summaries

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 6: Findings, manual review queue, readiness scoring, and top manifest."""
        find_df, find_sum = build_ml_dataset_findings_registry(self.profile)
        mr_df, mr_sum = build_ml_dataset_manual_review_queue(self.profile)
        sc_df, sc_sum = build_ml_dataset_readiness_score_report(self.profile)
        man_df, man_sum = build_advanced_ml_dataset_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_ml_dataset_findings_registry"):
            self.data_lake.save_ml_dataset_findings_registry(find_df, find_sum)
            self.data_lake.save_ml_dataset_manual_review_queue(mr_df, mr_sum)
            self.data_lake.save_ml_dataset_readiness_score_report(sc_df, sc_sum)
            self.data_lake.save_advanced_ml_dataset_manifest(man_df, man_sum)

        tables = {
            "findings": find_df,
            "manual_review": mr_df,
            "scoring": sc_df,
            "manifest": man_df,
        }
        summaries = {
            "findings": find_sum,
            "manual_review": mr_sum,
            "scoring": sc_sum,
            "manifest": man_sum,
        }
        return tables, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 7: Health check, safety boundary, validation report, and Phase 138 handoff."""
        h_df, h_sum = build_advanced_ml_dataset_health_check(self.project_root, self.profile)
        sb_df, sb_sum = build_advanced_ml_dataset_safety_boundary(self.profile)
        ho_df, ho_sum = build_phase_138_baseline_ml_model_contracts_handoff_report(self.profile)

        val_tables = {
            "profiles": pd.DataFrame(),
            "contracts": pd.DataFrame(),
            "manifest": pd.DataFrame(),
        }
        v_df, v_sum = build_advanced_ml_dataset_validation_report(val_tables, self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_dataset_health_check"):
            self.data_lake.save_advanced_ml_dataset_health_check(h_df, h_sum)
            self.data_lake.save_advanced_ml_dataset_safety_boundary(sb_df, sb_sum)
            self.data_lake.save_advanced_ml_dataset_validation_report(v_df, v_sum)
            self.data_lake.save_phase_138_baseline_ml_model_contracts_handoff_report(ho_df, ho_sum)

        tables = {
            "health": h_df,
            "safety": sb_df,
            "validation": v_df,
            "handoff": ho_df,
        }
        summaries = {
            "health": h_sum,
            "safety": sb_sum,
            "validation": v_sum,
            "handoff": ho_sum,
        }
        return tables, summaries

    def build_advanced_ml_dataset_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Step 8: Aggregate overall status of the dataset registry."""
        man_df, man_sum = build_advanced_ml_dataset_manifest(self.profile)
        row = {
            "pipeline": "AdvancedMlDatasetPipeline",
            "current_phase": 137,
            "target_final_phase": 160,
            "next_phase": 138,
            "status": "OPERATIONAL",
            "dataset_materialization_allowed": False,
            "feature_snapshot_materialization_allowed": False,
            "model_training_allowed": False,
            "prediction_allowed": False,
            "non_signal": True,
            "source_preserved": True,
        }
        df = pd.DataFrame([row])
        summary = {
            "pipeline_status": "OPERATIONAL",
            "current_phase": 137,
            "next_phase": 138,
            "non_signal": True,
        }
        return df, summary

    def run_all(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Run all pipeline steps end-to-end and optionally persist all artifacts."""
        all_tables = {}
        all_summaries = {}

        t1, s1 = self.build_profiles_domains_contracts(save=save)
        all_tables.update(t1)
        all_summaries.update(s1)

        t2, s2 = self.build_schema_namespace_policies(save=save)
        all_tables.update(t2)
        all_summaries.update(s2)

        t3, s3 = self.build_split_policies_guards(save=save)
        all_tables.update(t3)
        all_summaries.update(s3)

        t4, s4 = self.build_snapshot_quality_lineage(save=save)
        all_tables.update(t4)
        all_summaries.update(s4)

        t5, s5 = self.build_experiment_registry(save=save)
        all_tables.update(t5)
        all_summaries.update(s5)

        t6, s6 = self.build_findings_scoring_manifest(save=save)
        all_tables.update(t6)
        all_summaries.update(s6)

        t7, s7 = self.build_health_validation_safety_handoff(save=save)
        all_tables.update(t7)
        all_summaries.update(s7)

        status_df, status_sum = self.build_advanced_ml_dataset_status(save=save)
        all_tables["status"] = status_df
        all_summaries["status"] = status_sum

        return all_tables, all_summaries
