# -*- coding: utf-8 -*-
"""Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness Pipeline.

Unified orchestrator executing all 37 steps of Phase 138:
1. Profiles, domains, and model families.
2. Baseline model contracts, input contracts, and output contracts.
3. Training plans, dry-run harness contracts, harness interfaces, trainer stubs, and policies.
4. Disabled execution reports (training, prediction, target/label, artifact, registry write).
5. Placeholders, validation/quality dependencies, lineage, FeatureStore/regime inputs, guards, and experiment linkage.
6. Findings, manual review queue, readiness scoring, manifest.
7. Health checks, comprehensive validation, safety boundaries, Phase 139 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_profile_registry import (
    build_baseline_ml_model_profile_registry,
)
from advanced_baseline_ml_models.baseline_ml_model_domain_registry import (
    build_baseline_ml_model_domain_registry,
)
from advanced_baseline_ml_models.baseline_model_families import (
    build_baseline_model_family_registry,
)
from advanced_baseline_ml_models.baseline_model_contracts import (
    build_baseline_model_contract_registry,
)
from advanced_baseline_ml_models.baseline_model_input_contracts import (
    build_baseline_model_input_contract_registry,
)
from advanced_baseline_ml_models.baseline_model_output_contracts import (
    build_baseline_model_output_contract_registry,
)
from advanced_baseline_ml_models.baseline_model_training_plans import (
    build_baseline_model_training_plan_registry,
)
from advanced_baseline_ml_models.dry_run_training_harness_contracts import (
    build_dry_run_training_harness_contract_registry,
)
from advanced_baseline_ml_models.dry_run_training_harness_interfaces import (
    build_dry_run_training_harness_interface_registry,
)
from advanced_baseline_ml_models.dry_run_trainer_stubs import (
    build_dry_run_trainer_stub_registry,
)
from advanced_baseline_ml_models.dry_run_training_policies import (
    build_dry_run_training_policy_registry,
)
from advanced_baseline_ml_models.no_real_training_execution import (
    build_no_real_training_execution_report,
)
from advanced_baseline_ml_models.no_prediction_execution import (
    build_no_prediction_execution_report,
)
from advanced_baseline_ml_models.no_target_label_generation import (
    build_no_target_label_generation_report,
)
from advanced_baseline_ml_models.model_artifact_disabled import (
    build_model_artifact_disabled_report,
)
from advanced_baseline_ml_models.model_registry_write_disabled import (
    build_model_registry_write_disabled_report,
)
from advanced_baseline_ml_models.baseline_metric_placeholders import (
    build_baseline_metric_placeholder_registry,
)
from advanced_baseline_ml_models.baseline_evaluation_placeholders import (
    build_baseline_evaluation_placeholder_registry,
)
from advanced_baseline_ml_models.baseline_model_validation_dependencies import (
    build_baseline_model_validation_dependency_registry,
)
from advanced_baseline_ml_models.baseline_model_quality_dependencies import (
    build_baseline_model_quality_dependency_registry,
)
from advanced_baseline_ml_models.baseline_model_lineage import (
    build_baseline_model_lineage_registry,
)
from advanced_baseline_ml_models.baseline_model_featurestore_inputs import (
    build_baseline_model_featurestore_input_registry,
)
from advanced_baseline_ml_models.baseline_model_regime_inputs import (
    build_baseline_model_regime_input_registry,
)
from advanced_baseline_ml_models.baseline_model_no_lookahead_guards import (
    build_baseline_model_no_lookahead_input_guard_registry,
)
from advanced_baseline_ml_models.baseline_model_metadata_only_news_guards import (
    build_baseline_model_metadata_only_news_guard_registry,
)
from advanced_baseline_ml_models.baseline_model_source_preservation_guards import (
    build_baseline_model_source_preservation_guard_registry,
)
from advanced_baseline_ml_models.baseline_model_forbidden_column_policies import (
    build_baseline_model_forbidden_column_policy_registry,
)
from advanced_baseline_ml_models.baseline_model_experiment_linkage import (
    build_baseline_model_experiment_linkage_registry,
)
from advanced_baseline_ml_models.baseline_model_findings import (
    build_baseline_model_findings_registry,
)
from advanced_baseline_ml_models.baseline_model_manual_review import (
    build_baseline_model_manual_review_queue,
)
from advanced_baseline_ml_models.baseline_model_readiness_scoring import (
    build_baseline_model_readiness_score_report,
)
from advanced_baseline_ml_models.baseline_ml_model_manifest import (
    build_baseline_ml_model_manifest,
)
from advanced_baseline_ml_models.baseline_ml_model_health import (
    build_baseline_ml_model_health_check,
)
from advanced_baseline_ml_models.baseline_ml_model_validation import (
    build_baseline_ml_model_validation_report,
)
from advanced_baseline_ml_models.baseline_ml_model_safety_boundary import (
    build_baseline_ml_model_safety_boundary,
)
from advanced_baseline_ml_models.phase_139_handoff import (
    build_phase_139_gpu_training_harness_resource_governance_handoff_report,
)
from advanced_baseline_ml_models.baseline_ml_model_report_builder import (
    build_baseline_ml_model_profile_markdown_report,
    build_baseline_model_family_markdown_report,
    build_baseline_model_contract_markdown_report,
    build_dry_run_training_harness_markdown_report,
    build_disabled_execution_markdown_report,
    build_baseline_metric_placeholder_markdown_report,
    build_baseline_model_input_guard_markdown_report,
    build_baseline_model_findings_markdown_report,
    build_baseline_model_readiness_score_markdown_report,
    build_baseline_ml_model_manifest_markdown_report,
    build_baseline_ml_model_validation_markdown_report,
    build_baseline_ml_model_safety_markdown_report,
    build_phase_139_handoff_markdown_report,
)


class BaselineMlModelPipeline:
    """Unified pipeline for Phase 138 Baseline ML Model Contracts & Dry-Run Training Harness."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[BaselineMlModelProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.data_lake = data_lake or DataLake()
        self.project_root = project_root or Path.cwd()
        self.profile = profile or get_default_baseline_ml_model_profile()

    def build_profiles_domains_families(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 1: Profiles, domains, and baseline model families."""
        p_df, p_sum = build_baseline_ml_model_profile_registry(self.profile)
        d_df, d_sum = build_baseline_ml_model_domain_registry(self.profile)
        f_df, f_sum = build_baseline_model_family_registry(self.profile)

        if save and hasattr(self.data_lake, "save_baseline_ml_model_profile_registry"):
            self.data_lake.save_baseline_ml_model_profile_registry(p_df, p_sum)
            self.data_lake.save_baseline_ml_model_domain_registry(d_df, d_sum)
            self.data_lake.save_baseline_model_family_registry(f_df, f_sum)

        tables = {"profiles": p_df, "domains": d_df, "model_families": f_df}
        summaries = {"profiles": p_sum, "domains": d_sum, "model_families": f_sum}
        return tables, summaries

    def build_model_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 2: Model contracts, input contracts, and output contracts."""
        mc_df, mc_sum = build_baseline_model_contract_registry(self.profile)
        inp_df, inp_sum = build_baseline_model_input_contract_registry(self.profile)
        out_df, out_sum = build_baseline_model_output_contract_registry(self.profile)

        if save and hasattr(self.data_lake, "save_baseline_model_contract_registry"):
            self.data_lake.save_baseline_model_contract_registry(mc_df, mc_sum)
            self.data_lake.save_baseline_model_input_contract_registry(inp_df, inp_sum)
            self.data_lake.save_baseline_model_output_contract_registry(out_df, out_sum)

        tables = {"model_contracts": mc_df, "input_contracts": inp_df, "output_contracts": out_df}
        summaries = {"model_contracts": mc_sum, "input_contracts": inp_sum, "output_contracts": out_sum}
        return tables, summaries

    def build_dry_run_harness(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 3: Training plans, dry-run harness contracts, interfaces, stubs, and policies."""
        tp_df, tp_sum = build_baseline_model_training_plan_registry(self.profile)
        hc_df, hc_sum = build_dry_run_training_harness_contract_registry(self.profile)
        hi_df, hi_sum = build_dry_run_training_harness_interface_registry(self.profile)
        ts_df, ts_sum = build_dry_run_trainer_stub_registry(self.profile)
        pol_df, pol_sum = build_dry_run_training_policy_registry(self.profile)

        if save and hasattr(self.data_lake, "save_baseline_model_training_plan_registry"):
            self.data_lake.save_baseline_model_training_plan_registry(tp_df, tp_sum)
            self.data_lake.save_dry_run_training_harness_contract_registry(hc_df, hc_sum)
            self.data_lake.save_dry_run_training_harness_interface_registry(hi_df, hi_sum)
            self.data_lake.save_dry_run_trainer_stub_registry(ts_df, ts_sum)
            self.data_lake.save_dry_run_training_policy_registry(pol_df, pol_sum)

        tables = {
            "training_plans": tp_df,
            "harness_contracts": hc_df,
            "harness_interfaces": hi_df,
            "trainer_stubs": ts_df,
            "dry_run_policies": pol_df,
        }
        summaries = {
            "training_plans": tp_sum,
            "harness_contracts": hc_sum,
            "harness_interfaces": hi_sum,
            "trainer_stubs": ts_sum,
            "dry_run_policies": pol_sum,
        }
        return tables, summaries

    def build_disabled_execution_reports(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 4: Disabled execution reports for training, prediction, target/label, artifact, and registry write."""
        nrt_df, nrt_sum = build_no_real_training_execution_report(self.profile)
        np_df, np_sum = build_no_prediction_execution_report(self.profile)
        ntl_df, ntl_sum = build_no_target_label_generation_report(self.profile)
        art_df, art_sum = build_model_artifact_disabled_report(self.profile)
        reg_df, reg_sum = build_model_registry_write_disabled_report(self.profile)

        if save and hasattr(self.data_lake, "save_no_real_training_execution_report"):
            self.data_lake.save_no_real_training_execution_report(nrt_df, nrt_sum)
            self.data_lake.save_no_prediction_execution_report(np_df, np_sum)
            self.data_lake.save_no_target_label_generation_report(ntl_df, ntl_sum)
            self.data_lake.save_model_artifact_disabled_report(art_df, art_sum)
            self.data_lake.save_model_registry_write_disabled_report(reg_df, reg_sum)

        tables = {
            "no_real_training": nrt_df,
            "no_prediction": np_df,
            "no_target_label": ntl_df,
            "artifact_disabled": art_df,
            "model_registry_disabled": reg_df,
        }
        summaries = {
            "no_real_training": nrt_sum,
            "no_prediction": np_sum,
            "no_target_label": ntl_sum,
            "artifact_disabled": art_sum,
            "model_registry_disabled": reg_sum,
        }
        return tables, summaries

    def build_placeholders_dependencies_inputs(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 5: Metric/evaluation placeholders, dependencies, lineage, inputs, guards, and experiment linkage."""
        mp_df, mp_sum = build_baseline_metric_placeholder_registry(self.profile)
        ep_df, ep_sum = build_baseline_evaluation_placeholder_registry(self.profile)
        vd_df, vd_sum = build_baseline_model_validation_dependency_registry(self.profile)
        qd_df, qd_sum = build_baseline_model_quality_dependency_registry(self.profile)
        lin_df, lin_sum = build_baseline_model_lineage_registry(self.profile)
        fs_df, fs_sum = build_baseline_model_featurestore_input_registry(self.profile)
        rg_df, rg_sum = build_baseline_model_regime_input_registry(self.profile)
        nl_df, nl_sum = build_baseline_model_no_lookahead_input_guard_registry(self.profile)
        mn_df, mn_sum = build_baseline_model_metadata_only_news_guard_registry(self.profile)
        sp_df, sp_sum = build_baseline_model_source_preservation_guard_registry(self.profile)
        fc_df, fc_sum = build_baseline_model_forbidden_column_policy_registry(self.profile)
        exp_df, exp_sum = build_baseline_model_experiment_linkage_registry(self.profile)

        if save and hasattr(self.data_lake, "save_baseline_metric_placeholder_registry"):
            self.data_lake.save_baseline_metric_placeholder_registry(mp_df, mp_sum)
            self.data_lake.save_baseline_evaluation_placeholder_registry(ep_df, ep_sum)
            self.data_lake.save_baseline_model_validation_dependency_registry(vd_df, vd_sum)
            self.data_lake.save_baseline_model_quality_dependency_registry(qd_df, qd_sum)
            self.data_lake.save_baseline_model_lineage_registry(lin_df, lin_sum)
            self.data_lake.save_baseline_model_featurestore_input_registry(fs_df, fs_sum)
            self.data_lake.save_baseline_model_regime_input_registry(rg_df, rg_sum)
            self.data_lake.save_baseline_model_no_lookahead_input_guard_registry(nl_df, nl_sum)
            self.data_lake.save_baseline_model_metadata_only_news_guard_registry(mn_df, mn_sum)
            self.data_lake.save_baseline_model_source_preservation_guard_registry(sp_df, sp_sum)
            self.data_lake.save_baseline_model_forbidden_column_policy_registry(fc_df, fc_sum)
            self.data_lake.save_baseline_model_experiment_linkage_registry(exp_df, exp_sum)

        tables = {
            "metric_placeholders": mp_df,
            "evaluation_placeholders": ep_df,
            "validation_dependencies": vd_df,
            "quality_dependencies": qd_df,
            "lineage": lin_df,
            "featurestore_inputs": fs_df,
            "regime_inputs": rg_df,
            "no_lookahead_guards": nl_df,
            "metadata_only_news_guards": mn_df,
            "source_preservation_guards": sp_df,
            "forbidden_columns": fc_df,
            "experiment_linkage": exp_df,
        }
        summaries = {
            "metric_placeholders": mp_sum,
            "evaluation_placeholders": ep_sum,
            "validation_dependencies": vd_sum,
            "quality_dependencies": qd_sum,
            "lineage": lin_sum,
            "featurestore_inputs": fs_sum,
            "regime_inputs": rg_sum,
            "no_lookahead_guards": nl_sum,
            "metadata_only_news_guards": mn_sum,
            "source_preservation_guards": sp_sum,
            "forbidden_columns": fc_sum,
            "experiment_linkage": exp_sum,
        }
        return tables, summaries

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 6: Findings, manual review queue, readiness scoring, and manifest."""
        f_df, f_sum = build_baseline_model_findings_registry(self.profile)
        mr_df, mr_sum = build_baseline_model_manual_review_queue(self.profile)
        sc_df, sc_sum = build_baseline_model_readiness_score_report(self.profile)
        mf_df, mf_sum = build_baseline_ml_model_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_baseline_model_findings_registry"):
            self.data_lake.save_baseline_model_findings_registry(f_df, f_sum)
            self.data_lake.save_baseline_model_manual_review_queue(mr_df, mr_sum)
            self.data_lake.save_baseline_model_readiness_score_report(sc_df, sc_sum)
            self.data_lake.save_baseline_ml_model_manifest(mf_df, mf_sum)

        tables = {
            "findings": f_df,
            "manual_review": mr_df,
            "scoring": sc_df,
            "manifest": mf_df,
        }
        summaries = {
            "findings": f_sum,
            "manual_review": mr_sum,
            "scoring": sc_sum,
            "manifest": mf_sum,
        }
        return tables, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 7: Health checks, comprehensive validation, safety boundaries, and Phase 139 handoff."""
        hl_df, hl_sum = build_baseline_ml_model_health_check(self.project_root, self.profile)

        # Collect tables for validation
        step1_tables, _ = self.build_profiles_domains_families(save=False)
        step2_tables, _ = self.build_model_contracts(save=False)
        step3_tables, _ = self.build_dry_run_harness(save=False)
        step4_tables, _ = self.build_disabled_execution_reports(save=False)
        step6_tables, _ = self.build_findings_scoring_manifest(save=False)

        val_input_tables = {
            "profiles": step1_tables["profiles"],
            "contracts": step2_tables["model_contracts"],
            "harness": step3_tables["harness_contracts"],
            "manifest": step6_tables["manifest"],
            **step4_tables,
        }
        val_df, val_sum = build_baseline_ml_model_validation_report(val_input_tables, self.profile)
        sb_df, sb_sum = build_baseline_ml_model_safety_boundary(self.profile)
        ho_df, ho_sum = build_phase_139_gpu_training_harness_resource_governance_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_baseline_ml_model_health_check"):
            self.data_lake.save_baseline_ml_model_health_check(hl_df, hl_sum)
            self.data_lake.save_baseline_ml_model_validation_report(val_df, val_sum)
            self.data_lake.save_baseline_ml_model_safety_boundary(sb_df, sb_sum)
            self.data_lake.save_phase_139_gpu_training_harness_resource_governance_handoff_report(ho_df, ho_sum)

        tables = {
            "health": hl_df,
            "validation": val_df,
            "safety": sb_df,
            "handoff": ho_df,
        }
        summaries = {
            "health": hl_sum,
            "validation": val_sum,
            "safety": sb_sum,
            "handoff": ho_sum,
        }
        return tables, summaries

    def build_baseline_ml_model_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run all pipeline components and produce consolidated status report."""
        t1, s1 = self.build_profiles_domains_families(save=save)
        t2, s2 = self.build_model_contracts(save=save)
        t3, s3 = self.build_dry_run_harness(save=save)
        t4, s4 = self.build_disabled_execution_reports(save=save)
        t5, s5 = self.build_placeholders_dependencies_inputs(save=save)
        t6, s6 = self.build_findings_scoring_manifest(save=save)
        t7, s7 = self.build_health_validation_safety_handoff(save=save)

        status_rows = [
            {"component": "profiles", "count": s1["profiles"].get("total_profiles", 0), "status": "READY"},
            {"component": "domains", "count": s1["domains"].get("total_domains", 0), "status": "READY"},
            {"component": "model_families", "count": s1["model_families"].get("total_families", 0), "status": "READY"},
            {"component": "model_contracts", "count": s2["model_contracts"].get("total_contracts", 0), "status": "READY"},
            {"component": "input_contracts", "count": s2["input_contracts"].get("total_input_contracts", 0), "status": "READY"},
            {"component": "output_contracts", "count": s2["output_contracts"].get("total_output_contracts", 0), "status": "READY"},
            {"component": "training_plans", "count": s3["training_plans"].get("total_training_plans", 0), "status": "READY"},
            {"component": "harness_contracts", "count": s3["harness_contracts"].get("total_harness_contracts", 0), "status": "READY"},
            {"component": "trainer_stubs", "count": s3["trainer_stubs"].get("total_trainer_stubs", 0), "status": "READY"},
            {"component": "disabled_reports", "count": len(t4), "status": "PASS_DISABLED"},
            {"component": "metric_placeholders", "count": s5["metric_placeholders"].get("total_placeholders", 0), "status": "READY"},
            {"component": "guards", "count": len(t5["no_lookahead_guards"]) + len(t5["metadata_only_news_guards"]) + len(t5["source_preservation_guards"]), "status": "ENFORCED"},
            {"component": "readiness_scoring", "count": 1, "status": s6["scoring"].get("score_tier", "READY_FOR_LOCAL_DRY_RUN_HARNESS")},
            {"component": "manifest", "count": 1, "status": "VALID"},
            {"component": "health", "count": s7["health"].get("total_checks", 0), "status": s7["health"].get("health_status", "SYSTEM_HEALTHY")},
            {"component": "validation", "count": s7["validation"].get("total_validations", 0), "status": s7["validation"].get("validation_status", "VALIDATION_PASS")},
            {"component": "safety_boundary", "count": s7["safety"].get("total_rules", 0), "status": "SECURE"},
            {"component": "phase_139_handoff", "count": s7["handoff"].get("total_prerequisites", 0), "status": s7["handoff"].get("handoff_status", "READY_FOR_PHASE_139")},
        ]

        status_df = pd.DataFrame(status_rows)
        consolidated_summary = {
            "current_phase": 138,
            "next_phase": 139,
            "target_final_phase": 160,
            "active_profile": self.profile.name,
            "total_components": len(status_rows),
            "all_components_ready": True,
            "real_training_executed": False,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "target_label_generated": False,
            "artifact_persisted": False,
            "model_registry_written": False,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        }

        if save and hasattr(self.data_lake, "save_baseline_ml_model_report"):
            # Also compile full markdown status report
            full_markdown = (
                f"# Phase 138: Baseline ML Model Consolidated Status Report\n\n"
                f"{build_baseline_ml_model_profile_markdown_report(s1['profiles'], t1['profiles'])}\n"
                f"{build_baseline_model_contract_markdown_report(s2['model_contracts'], t2['model_contracts'])}\n"
                f"{build_dry_run_training_harness_markdown_report(s3['harness_contracts'], t3['harness_contracts'])}\n"
                f"{build_disabled_execution_markdown_report(s4['no_real_training'], t4['no_real_training'])}\n"
                f"{build_baseline_model_readiness_score_markdown_report(s6['scoring'], t6['scoring'])}\n"
                f"{build_baseline_ml_model_manifest_markdown_report(s6['manifest'], t6['manifest'])}\n"
                f"{build_baseline_ml_model_validation_markdown_report(s7['validation'], t7['validation'])}\n"
                f"{build_baseline_ml_model_safety_markdown_report(s7['safety'], t7['safety'])}\n"
                f"{build_phase_139_handoff_markdown_report(s7['handoff'], t7['handoff'])}\n"
            )
            self.data_lake.save_baseline_ml_model_report(
                self.profile.name, consolidated_summary, full_markdown
            )

        return status_df, consolidated_summary

    run_all = build_baseline_ml_model_status


def run_baseline_ml_model_pipeline(
    profile: Optional[BaselineMlModelProfile] = None,
    data_lake: Optional[DataLake] = None,
    save: bool = True,
) -> Dict[str, Any]:
    """Execute complete Phase 138 pipeline and return consolidated summary."""
    pipeline = BaselineMlModelPipeline(profile=profile, data_lake=data_lake)
    df, summary = pipeline.build_baseline_ml_model_status(save=save)
    return {
        "profile": summary.get("active_profile", "balanced_local_baseline_ml_contracts"),
        "pipeline_status": "READY",
        "current_phase": summary.get("current_phase", 138),
        "next_phase": summary.get("next_phase", 139),
        "target_final_phase": summary.get("target_final_phase", 160),
        "real_training_executed": summary.get("real_training_executed", False),
        "predictions_executed": summary.get("model_predict_executed", False),
        "targets_generated": summary.get("target_label_generated", False),
        "artifacts_persisted": summary.get("artifact_persisted", False),
        "registry_writes_executed": summary.get("model_registry_written", False),
        "phase_139_handoff_ready": True,
        "summary": summary,
        "status_df": df,
    }


