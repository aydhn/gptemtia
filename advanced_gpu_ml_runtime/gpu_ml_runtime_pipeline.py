"""Phase 136: GPU ML Runtime Pipeline.

Orchestrates local hardware discovery, runtime capability inspection,
safety contracts, input contracts, scoring, validation, and Phase 137 handoff.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_labels import (
    GPU_ML_RUNTIME_DOMAIN,
    RUNTIME_READY,
)
from advanced_gpu_ml_runtime.gpu_ml_runtime_profile_registry import build_gpu_ml_runtime_profile_registry
from advanced_gpu_ml_runtime.gpu_ml_runtime_domain_registry import build_gpu_ml_runtime_domain_registry
from advanced_gpu_ml_runtime.local_hardware_discovery import build_local_hardware_discovery_report
from advanced_gpu_ml_runtime.gpu_capability_registry import build_gpu_capability_registry
from advanced_gpu_ml_runtime.cpu_capability_registry import build_cpu_capability_registry
from advanced_gpu_ml_runtime.memory_capability_registry import build_memory_capability_registry
from advanced_gpu_ml_runtime.cuda_availability import build_cuda_availability_report
from advanced_gpu_ml_runtime.torch_runtime_capability import build_torch_runtime_capability_report
from advanced_gpu_ml_runtime.sklearn_runtime_capability import build_sklearn_runtime_capability_report
from advanced_gpu_ml_runtime.numpy_pandas_runtime_capability import build_numpy_pandas_runtime_capability_report
from advanced_gpu_ml_runtime.optional_ml_dependency_registry import build_optional_ml_dependency_registry
from advanced_gpu_ml_runtime.accelerator_backend_registry import build_accelerator_backend_registry
from advanced_gpu_ml_runtime.ml_runtime_environment_snapshot import build_ml_runtime_environment_snapshot
from advanced_gpu_ml_runtime.ml_runtime_safety_contracts import build_ml_runtime_safety_contract_registry
from advanced_gpu_ml_runtime.ml_experiment_permission_policies import build_ml_experiment_permission_policy_registry
from advanced_gpu_ml_runtime.ml_training_disabled_policies import build_ml_training_disabled_policy_registry
from advanced_gpu_ml_runtime.ml_inference_disabled_policies import build_ml_inference_disabled_policy_registry
from advanced_gpu_ml_runtime.ml_target_label_disabled_policies import build_ml_target_label_disabled_policy_registry
from advanced_gpu_ml_runtime.ml_artifact_governance_placeholders import build_ml_artifact_governance_placeholder_registry
from advanced_gpu_ml_runtime.regime_metadata_ml_input_contracts import build_regime_metadata_ml_input_contract_registry
from advanced_gpu_ml_runtime.featurestore_ml_input_contracts import build_featurestore_ml_input_contract_registry
from advanced_gpu_ml_runtime.no_lookahead_ml_input_contracts import build_no_lookahead_ml_input_contract_registry
from advanced_gpu_ml_runtime.metadata_only_news_ml_input_contracts import build_metadata_only_news_ml_input_contract_registry
from advanced_gpu_ml_runtime.source_preservation_ml_input_contracts import build_source_preservation_ml_input_contract_registry
from advanced_gpu_ml_runtime.ml_runtime_findings import build_ml_runtime_findings_registry
from advanced_gpu_ml_runtime.ml_runtime_manual_review import build_ml_runtime_manual_review_queue
from advanced_gpu_ml_runtime.ml_runtime_readiness_scoring import build_ml_runtime_readiness_score_report
from advanced_gpu_ml_runtime.gpu_ml_runtime_manifest import build_gpu_ml_runtime_manifest
from advanced_gpu_ml_runtime.gpu_ml_runtime_health import build_gpu_ml_runtime_health_check
from advanced_gpu_ml_runtime.gpu_ml_runtime_validation import build_gpu_ml_runtime_validation_report
from advanced_gpu_ml_runtime.gpu_ml_runtime_safety_boundary import build_gpu_ml_runtime_safety_boundary
from advanced_gpu_ml_runtime.phase_137_handoff import build_phase_137_advanced_ml_dataset_experiment_handoff_report
from advanced_gpu_ml_runtime.gpu_ml_runtime_report_builder import (
    build_gpu_ml_runtime_profile_markdown_report,
    build_local_hardware_discovery_markdown_report,
    build_gpu_capability_markdown_report,
    build_runtime_dependency_capability_markdown_report,
    build_ml_runtime_safety_contract_markdown_report,
    build_ml_input_contract_markdown_report,
    build_ml_runtime_findings_markdown_report,
    build_ml_runtime_readiness_score_markdown_report,
    build_gpu_ml_runtime_manifest_markdown_report,
    build_gpu_ml_runtime_validation_markdown_report,
    build_gpu_ml_runtime_safety_markdown_report,
    build_phase_137_handoff_markdown_report,
)


class GpuMlRuntimePipeline:
    """Unified pipeline for Phase 136 GPU Acceleration and ML Runtime Foundation."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[GpuMlRuntimeProfile] = None,
    ):
        self.settings = settings or get_settings()
        self.data_lake = data_lake or DataLake()
        self.project_root = project_root or Path.cwd()
        self.profile = profile or get_gpu_ml_runtime_profile()

    def build_profiles_domains(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 1: Build profile and domain registries."""
        p_df, p_sum = build_gpu_ml_runtime_profile_registry(self.profile)
        d_df, d_sum = build_gpu_ml_runtime_domain_registry(self.profile)

        if save:
            self.data_lake.save_gpu_ml_runtime_profile_registry(p_df, p_sum)
            self.data_lake.save_gpu_ml_runtime_domain_registry(d_df, d_sum)

        tables = {"profiles": p_df, "domains": d_df}
        summaries = {"profiles": p_sum, "domains": d_sum}
        return tables, summaries

    def build_hardware_capabilities(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 2: Build local hardware discovery, GPU, CPU, and memory capabilities."""
        hw_df, hw_sum = build_local_hardware_discovery_report(self.profile)
        gpu_df, gpu_sum = build_gpu_capability_registry(self.profile)
        cpu_df, cpu_sum = build_cpu_capability_registry(self.profile)
        mem_df, mem_sum = build_memory_capability_registry(self.profile)

        if save:
            self.data_lake.save_local_hardware_discovery_report(hw_df, hw_sum)
            self.data_lake.save_gpu_capability_registry(gpu_df, gpu_sum)
            self.data_lake.save_cpu_capability_registry(cpu_df, cpu_sum)
            self.data_lake.save_memory_capability_registry(mem_df, mem_sum)

        tables = {"hardware": hw_df, "gpu": gpu_df, "cpu": cpu_df, "memory": mem_df}
        summaries = {"hardware": hw_sum, "gpu": gpu_sum, "cpu": cpu_sum, "memory": mem_sum}
        return tables, summaries

    def build_dependency_capabilities(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 3: Build CUDA, PyTorch, scikit-learn, numpy/pandas, optional dependencies, and snapshot."""
        cuda_df, cuda_sum = build_cuda_availability_report(self.profile)
        torch_df, torch_sum = build_torch_runtime_capability_report(self.profile)
        sk_df, sk_sum = build_sklearn_runtime_capability_report(self.profile)
        np_pd_df, np_pd_sum = build_numpy_pandas_runtime_capability_report(self.profile)
        opt_df, opt_sum = build_optional_ml_dependency_registry(self.profile)
        acc_df, acc_sum = build_accelerator_backend_registry(self.profile)
        snap_df, snap_sum = build_ml_runtime_environment_snapshot(self.profile)

        if save:
            self.data_lake.save_cuda_availability_report(cuda_df, cuda_sum)
            self.data_lake.save_torch_runtime_capability_report(torch_df, torch_sum)
            self.data_lake.save_sklearn_runtime_capability_report(sk_df, sk_sum)
            self.data_lake.save_numpy_pandas_runtime_capability_report(np_pd_df, np_pd_sum)
            self.data_lake.save_optional_ml_dependency_registry(opt_df, opt_sum)
            self.data_lake.save_accelerator_backend_registry(acc_df, acc_sum)
            self.data_lake.save_ml_runtime_environment_snapshot(snap_df, snap_sum)

        tables = {
            "cuda": cuda_df,
            "torch": torch_df,
            "sklearn": sk_df,
            "numpy_pandas": np_pd_df,
            "optional_dependencies": opt_df,
            "accelerator_backends": acc_df,
            "environment_snapshot": snap_df,
        }
        summaries = {
            "cuda": cuda_sum,
            "torch": torch_sum,
            "sklearn": sk_sum,
            "numpy_pandas": np_pd_sum,
            "optional_dependencies": opt_sum,
            "accelerator_backends": acc_sum,
            "environment_snapshot": snap_sum,
        }
        return tables, summaries

    def build_safety_permissions(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 4: Build safety contracts, permissions, disabled policies, and governance placeholders."""
        safe_df, safe_sum = build_ml_runtime_safety_contract_registry(self.profile)
        perm_df, perm_sum = build_ml_experiment_permission_policy_registry(self.profile)
        train_df, train_sum = build_ml_training_disabled_policy_registry(self.profile)
        infer_df, infer_sum = build_ml_inference_disabled_policy_registry(self.profile)
        target_df, target_sum = build_ml_target_label_disabled_policy_registry(self.profile)
        gov_df, gov_sum = build_ml_artifact_governance_placeholder_registry(self.profile)

        if save:
            self.data_lake.save_ml_runtime_safety_contract_registry(safe_df, safe_sum)
            self.data_lake.save_ml_experiment_permission_policy_registry(perm_df, perm_sum)
            self.data_lake.save_ml_training_disabled_policy_registry(train_df, train_sum)
            self.data_lake.save_ml_inference_disabled_policy_registry(infer_df, infer_sum)
            self.data_lake.save_ml_target_label_disabled_policy_registry(target_df, target_sum)
            self.data_lake.save_ml_artifact_governance_placeholder_registry(gov_df, gov_sum)

        tables = {
            "safety_contracts": safe_df,
            "permission_policies": perm_df,
            "training_disabled": train_df,
            "inference_disabled": infer_df,
            "target_label_disabled": target_df,
            "artifact_governance": gov_df,
        }
        summaries = {
            "safety_contracts": safe_sum,
            "permission_policies": perm_sum,
            "training_disabled": train_sum,
            "inference_disabled": infer_sum,
            "target_label_disabled": target_sum,
            "artifact_governance": gov_sum,
        }
        return tables, summaries

    def build_ml_input_contracts(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 5: Build regime metadata, FeatureStore, no-lookahead, news, and source preservation input contracts."""
        reg_df, reg_sum = build_regime_metadata_ml_input_contract_registry(self.profile)
        fs_df, fs_sum = build_featurestore_ml_input_contract_registry(self.profile)
        nl_df, nl_sum = build_no_lookahead_ml_input_contract_registry(self.profile)
        news_df, news_sum = build_metadata_only_news_ml_input_contract_registry(self.profile)
        sp_df, sp_sum = build_source_preservation_ml_input_contract_registry(self.profile)

        if save:
            self.data_lake.save_regime_metadata_ml_input_contract_registry(reg_df, reg_sum)
            self.data_lake.save_featurestore_ml_input_contract_registry(fs_df, fs_sum)
            self.data_lake.save_no_lookahead_ml_input_contract_registry(nl_df, nl_sum)
            self.data_lake.save_metadata_only_news_ml_input_contract_registry(news_df, news_sum)
            self.data_lake.save_source_preservation_ml_input_contract_registry(sp_df, sp_sum)

        tables = {
            "regime_metadata_inputs": reg_df,
            "featurestore_inputs": fs_df,
            "no_lookahead_inputs": nl_df,
            "metadata_only_news_inputs": news_df,
            "source_preservation_inputs": sp_df,
        }
        summaries = {
            "regime_metadata_inputs": reg_sum,
            "featurestore_inputs": fs_sum,
            "no_lookahead_inputs": nl_sum,
            "metadata_only_news_inputs": news_sum,
            "source_preservation_inputs": sp_sum,
        }
        return tables, summaries

    def build_findings_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 6: Build findings, manual review queue, readiness scoring, and manifest."""
        find_df, find_sum = build_ml_runtime_findings_registry(self.profile)
        rev_df, rev_sum = build_ml_runtime_manual_review_queue(self.profile)
        score_df, score_sum = build_ml_runtime_readiness_score_report(self.profile)
        man_df, man_sum = build_gpu_ml_runtime_manifest(self.profile)

        if save:
            self.data_lake.save_ml_runtime_findings_registry(find_df, find_sum)
            self.data_lake.save_ml_runtime_manual_review_queue(rev_df, rev_sum)
            self.data_lake.save_ml_runtime_readiness_score_report(score_df, score_sum)
            self.data_lake.save_gpu_ml_runtime_manifest(man_df, man_sum)

        tables = {
            "findings": find_df,
            "manual_review": rev_df,
            "readiness_score": score_df,
            "manifest": man_df,
        }
        summaries = {
            "findings": find_sum,
            "manual_review": rev_sum,
            "readiness_score": score_sum,
            "manifest": man_sum,
        }
        return tables, summaries

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Step 7: Build health check, validation report, safety boundary, and Phase 137 handoff."""
        health_df, health_sum = build_gpu_ml_runtime_health_check(self.project_root, self.profile)

        p_df, _ = build_gpu_ml_runtime_profile_registry(self.profile)
        gpu_df, _ = build_gpu_capability_registry(self.profile)
        safe_df, _ = build_ml_runtime_safety_contract_registry(self.profile)
        inp_df, _ = build_regime_metadata_ml_input_contract_registry(self.profile)
        man_df, man_sum = build_gpu_ml_runtime_manifest(self.profile)

        val_tables = {
            "profiles": p_df,
            "gpu_capability": gpu_df,
            "safety_contracts": safe_df,
            "input_contracts": inp_df,
            "manifest": man_df,
        }
        val_df, val_sum = build_gpu_ml_runtime_validation_report(val_tables, self.profile)
        bound_df, bound_sum = build_gpu_ml_runtime_safety_boundary(self.profile)
        handoff_df, handoff_sum = build_phase_137_advanced_ml_dataset_experiment_handoff_report(self.profile)

        if save:
            self.data_lake.save_gpu_ml_runtime_health_check(health_df, health_sum)
            self.data_lake.save_gpu_ml_runtime_validation_report(val_df, val_sum)
            self.data_lake.save_gpu_ml_runtime_safety_boundary(bound_df, bound_sum)
            self.data_lake.save_phase_137_advanced_ml_dataset_experiment_handoff_report(handoff_df, handoff_sum)

            # Save full composite JSON report and Markdown
            composite_report = {
                "profile": self.profile.profile_name,
                "current_phase": 136,
                "next_phase": 137,
                "health": health_sum,
                "validation": val_sum,
                "safety": bound_sum,
                "handoff": handoff_sum,
                "non_signal": True,
            }
            md_content = (
                build_gpu_ml_runtime_manifest_markdown_report(man_sum, man_df)
                + "\n\n"
                + build_phase_137_handoff_markdown_report(handoff_sum, handoff_df)
            )
            self.data_lake.save_gpu_ml_runtime_report(self.profile.profile_name, composite_report, md_content)

        tables = {
            "health": health_df,
            "validation": val_df,
            "safety_boundary": bound_df,
            "handoff": handoff_df,
        }
        summaries = {
            "health": health_sum,
            "validation": val_sum,
            "safety_boundary": bound_sum,
            "handoff": handoff_sum,
        }
        return tables, summaries

    def build_gpu_ml_runtime_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run full end-to-end execution and return master status."""
        self.build_profiles_domains(save=save)
        self.build_hardware_capabilities(save=save)
        self.build_dependency_capabilities(save=save)
        self.build_safety_permissions(save=save)
        self.build_ml_input_contracts(save=save)
        f_tables, f_sums = self.build_findings_scoring_manifest(save=save)
        h_tables, h_sums = self.build_health_validation_safety_handoff(save=save)

        manifest_df = f_tables["manifest"]
        score_df = f_tables["readiness_score"]
        val_sum = h_sums["validation"]
        handoff_sum = h_sums["handoff"]

        readiness_score = float(score_df.iloc[0]["metric_value"]) if not score_df.empty else 0.0

        rows = [
            {
                "subsystem": "advanced_gpu_ml_runtime",
                "current_phase": 136,
                "target_final_phase": 160,
                "next_phase": 137,
                "active_profile": self.profile.profile_name,
                "readiness_score": readiness_score,
                "validation_passed": val_sum.get("all_passed", True),
                "handoff_ready": handoff_sum.get("all_satisfied", True),
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "status_label": RUNTIME_READY,
            }
        ]

        status_df = pd.DataFrame(rows)
        status_sum: Dict[str, Any] = {
            "domain": GPU_ML_RUNTIME_DOMAIN,
            "current_phase": 136,
            "next_phase": 137,
            "target_final_phase": 160,
            "active_profile": self.profile.profile_name,
            "readiness_score": readiness_score,
            "validation_passed": val_sum.get("all_passed", True),
            "handoff_ready": handoff_sum.get("all_satisfied", True),
            "status": "READY",
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        }
        return status_df, status_sum

    run = build_gpu_ml_runtime_status
