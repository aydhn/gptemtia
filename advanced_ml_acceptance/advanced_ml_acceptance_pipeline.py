# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Pipeline.

Coordinates generation of all Phase 145 acceptance registries, checkpoints,
boundaries, findings, readiness scores, manifests, health checks, validation reports,
and Phase 146 handoff documents.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_profile_registry import (
    build_advanced_ml_acceptance_profile_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_domain_registry import (
    build_advanced_ml_acceptance_domain_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_scope_registry import (
    build_advanced_ml_acceptance_scope_registry,
)
from advanced_ml_acceptance.advanced_ml_component_registry import (
    build_advanced_ml_component_registry,
)
from advanced_ml_acceptance.advanced_ml_component_checkpoints import (
    build_advanced_ml_component_acceptance_checkpoint_registry,
)
from advanced_ml_acceptance.phase_136_gpu_runtime_acceptance import (
    build_phase_136_gpu_runtime_acceptance_registry,
)
from advanced_ml_acceptance.phase_137_dataset_contract_acceptance import (
    build_phase_137_dataset_contract_acceptance_registry,
)
from advanced_ml_acceptance.phase_138_baseline_model_acceptance import (
    build_phase_138_baseline_model_acceptance_registry,
)
from advanced_ml_acceptance.phase_139_gpu_training_governance_acceptance import (
    build_phase_139_gpu_training_governance_acceptance_registry,
)
from advanced_ml_acceptance.phase_140_ensemble_candidate_acceptance import (
    build_phase_140_ensemble_candidate_acceptance_registry,
)
from advanced_ml_acceptance.phase_141_calibration_uncertainty_acceptance import (
    build_phase_141_calibration_uncertainty_acceptance_registry,
)
from advanced_ml_acceptance.phase_142_drift_monitoring_acceptance import (
    build_phase_142_drift_monitoring_acceptance_registry,
)
from advanced_ml_acceptance.phase_143_explainability_acceptance import (
    build_phase_143_explainability_acceptance_registry,
)
from advanced_ml_acceptance.phase_144_model_governance_acceptance import (
    build_phase_144_model_governance_acceptance_registry,
)
from advanced_ml_acceptance.advanced_ml_dependency_acceptance import (
    build_advanced_ml_dependency_acceptance_registry,
)
from advanced_ml_acceptance.advanced_ml_validation_evidence_summary import (
    build_advanced_ml_validation_evidence_summary_registry,
)
from advanced_ml_acceptance.advanced_ml_safety_boundary_acceptance import (
    build_advanced_ml_safety_boundary_acceptance_registry,
)
from advanced_ml_acceptance.advanced_ml_non_production_boundaries import (
    build_advanced_ml_non_production_boundary_registry,
)
from advanced_ml_acceptance.advanced_ml_manual_review_gates import (
    build_advanced_ml_manual_review_gate_registry,
)
from advanced_ml_acceptance.advanced_ml_go_no_go_boundaries import (
    build_advanced_ml_go_no_go_boundary_registry,
)
from advanced_ml_acceptance.advanced_ml_blockers import (
    build_advanced_ml_blocker_registry,
)
from advanced_ml_acceptance.advanced_ml_gaps import (
    build_advanced_ml_gap_registry,
)
from advanced_ml_acceptance.advanced_ml_warnings import (
    build_advanced_ml_warning_registry,
)
from advanced_ml_acceptance.advanced_ml_findings import (
    build_advanced_ml_findings_registry,
)
from advanced_ml_acceptance.advanced_ml_readiness_scoring import (
    build_advanced_ml_readiness_score_report,
)
from advanced_ml_acceptance.advanced_ml_acceptance_manifest import (
    build_advanced_ml_acceptance_manifest,
)
from advanced_ml_acceptance.advanced_ml_acceptance_health import (
    build_advanced_ml_acceptance_health_check,
)
from advanced_ml_acceptance.advanced_ml_acceptance_validation import (
    build_advanced_ml_acceptance_validation_report,
)
from advanced_ml_acceptance.advanced_ml_acceptance_safety_boundary import (
    build_advanced_ml_acceptance_safety_boundary,
)
from advanced_ml_acceptance.phase_146_handoff import (
    build_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_advanced_ml_acceptance_full_markdown_report,
)


class AdvancedMlAcceptancePipeline:
    """End-to-end pipeline orchestrator for Phase 145 Advanced ML block acceptance."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[AdvancedMlAcceptanceProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(".")
        self.profile = profile or get_default_advanced_ml_acceptance_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save profile, domain, and scope registries."""
        df_prof, s_prof = build_advanced_ml_acceptance_profile_registry(self.profile)
        df_dom, s_dom = build_advanced_ml_acceptance_domain_registry(self.profile)
        df_scp, s_scp = build_advanced_ml_acceptance_scope_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_acceptance_profile_registry"):
            self.data_lake.save_advanced_ml_acceptance_profile_registry(df_prof, s_prof)
            self.data_lake.save_advanced_ml_acceptance_domain_registry(df_dom, s_dom)
            self.data_lake.save_advanced_ml_acceptance_scope_registry(df_scp, s_scp)

        dfs = {"profiles": df_prof, "domains": df_dom, "scope": df_scp}
        summary = {"profiles": s_prof, "domains": s_dom, "scope": s_scp, "non_signal": True}
        return dfs, summary

    def build_components_checkpoints(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save component and checkpoint registries."""
        df_cmp, s_cmp = build_advanced_ml_component_registry(self.profile)
        df_chk, s_chk = build_advanced_ml_component_acceptance_checkpoint_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_component_registry"):
            self.data_lake.save_advanced_ml_component_registry(df_cmp, s_cmp)
            self.data_lake.save_advanced_ml_component_acceptance_checkpoint_registry(df_chk, s_chk)

        dfs = {"components": df_cmp, "checkpoints": df_chk}
        summary = {"components": s_cmp, "checkpoints": s_chk, "non_signal": True}
        return dfs, summary

    def build_phase_acceptance(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save Phase 136-144 acceptance registries."""
        df_136, s_136 = build_phase_136_gpu_runtime_acceptance_registry(self.profile)
        df_137, s_137 = build_phase_137_dataset_contract_acceptance_registry(self.profile)
        df_138, s_138 = build_phase_138_baseline_model_acceptance_registry(self.profile)
        df_139, s_139 = build_phase_139_gpu_training_governance_acceptance_registry(self.profile)
        df_140, s_140 = build_phase_140_ensemble_candidate_acceptance_registry(self.profile)
        df_141, s_141 = build_phase_141_calibration_uncertainty_acceptance_registry(self.profile)
        df_142, s_142 = build_phase_142_drift_monitoring_acceptance_registry(self.profile)
        df_143, s_143 = build_phase_143_explainability_acceptance_registry(self.profile)
        df_144, s_144 = build_phase_144_model_governance_acceptance_registry(self.profile)

        if save and hasattr(self.data_lake, "save_phase_136_gpu_runtime_acceptance_registry"):
            self.data_lake.save_phase_136_gpu_runtime_acceptance_registry(df_136, s_136)
            self.data_lake.save_phase_137_dataset_contract_acceptance_registry(df_137, s_137)
            self.data_lake.save_phase_138_baseline_model_acceptance_registry(df_138, s_138)
            self.data_lake.save_phase_139_gpu_training_governance_acceptance_registry(df_139, s_139)
            self.data_lake.save_phase_140_ensemble_candidate_acceptance_registry(df_140, s_140)
            self.data_lake.save_phase_141_calibration_uncertainty_acceptance_registry(df_141, s_141)
            self.data_lake.save_phase_142_drift_monitoring_acceptance_registry(df_142, s_142)
            self.data_lake.save_phase_143_explainability_acceptance_registry(df_143, s_143)
            self.data_lake.save_phase_144_model_governance_acceptance_registry(df_144, s_144)

        dfs = {
            "phase_136": df_136, "phase_137": df_137, "phase_138": df_138,
            "phase_139": df_139, "phase_140": df_140, "phase_141": df_141,
            "phase_142": df_142, "phase_143": df_143, "phase_144": df_144,
        }
        summary = {
            "phase_136": s_136, "phase_137": s_137, "phase_138": s_138,
            "phase_139": s_139, "phase_140": s_140, "phase_141": s_141,
            "phase_142": s_142, "phase_143": s_143, "phase_144": s_144,
            "non_signal": True,
        }
        return dfs, summary

    def build_dependency_evidence(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save dependency, evidence, and safety registries."""
        df_dep, s_dep = build_advanced_ml_dependency_acceptance_registry(self.profile)
        df_evd, s_evd = build_advanced_ml_validation_evidence_summary_registry(self.profile)
        df_sba, s_sba = build_advanced_ml_safety_boundary_acceptance_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_dependency_acceptance_registry"):
            self.data_lake.save_advanced_ml_dependency_acceptance_registry(df_dep, s_dep)
            self.data_lake.save_advanced_ml_validation_evidence_summary_registry(df_evd, s_evd)
            self.data_lake.save_advanced_ml_safety_boundary_acceptance_registry(df_sba, s_sba)

        dfs = {"dependencies": df_dep, "evidence": df_evd, "safety_acceptance": df_sba}
        summary = {"dependencies": s_dep, "evidence": s_evd, "safety_acceptance": s_sba, "non_signal": True}
        return dfs, summary

    def build_boundaries_gates(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save boundary and gate registries."""
        df_npb, s_npb = build_advanced_ml_non_production_boundary_registry(self.profile)
        df_mrg, s_mrg = build_advanced_ml_manual_review_gate_registry(self.profile)
        df_gng, s_gng = build_advanced_ml_go_no_go_boundary_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_non_production_boundary_registry"):
            self.data_lake.save_advanced_ml_non_production_boundary_registry(df_npb, s_npb)
            self.data_lake.save_advanced_ml_manual_review_gate_registry(df_mrg, s_mrg)
            self.data_lake.save_advanced_ml_go_no_go_boundary_registry(df_gng, s_gng)

        dfs = {"non_production_boundaries": df_npb, "manual_review_gates": df_mrg, "go_no_go": df_gng}
        summary = {"non_production_boundaries": s_npb, "manual_review_gates": s_mrg, "go_no_go": s_gng, "non_signal": True}
        return dfs, summary

    def build_blockers_gaps_warnings_findings(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save blockers, gaps, warnings, and findings."""
        df_blk, s_blk = build_advanced_ml_blocker_registry(self.profile)
        df_gap, s_gap = build_advanced_ml_gap_registry(self.profile)
        df_wrn, s_wrn = build_advanced_ml_warning_registry(self.profile)
        df_fnd, s_fnd = build_advanced_ml_findings_registry(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_blocker_registry"):
            self.data_lake.save_advanced_ml_blocker_registry(df_blk, s_blk)
            self.data_lake.save_advanced_ml_gap_registry(df_gap, s_gap)
            self.data_lake.save_advanced_ml_warning_registry(df_wrn, s_wrn)
            self.data_lake.save_advanced_ml_findings_registry(df_fnd, s_fnd)

        dfs = {"blockers": df_blk, "gaps": df_gap, "warnings": df_wrn, "findings": df_fnd}
        summary = {"blockers": s_blk, "gaps": s_gap, "warnings": s_wrn, "findings": s_fnd, "non_signal": True}
        return dfs, summary

    def build_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save readiness score and acceptance manifest."""
        df_scr, s_scr = build_advanced_ml_readiness_score_report(self.profile)
        df_mnf, s_mnf = build_advanced_ml_acceptance_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_readiness_score_report"):
            self.data_lake.save_advanced_ml_readiness_score_report(df_scr, s_scr)
            self.data_lake.save_advanced_ml_acceptance_manifest(df_mnf, s_mnf)

        dfs = {"scoring": df_scr, "manifest": df_mnf}
        summary = {"scoring": s_scr, "manifest": s_mnf, "non_signal": True}
        return dfs, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, validation, safety boundaries, and Phase 146 handoff."""
        df_hlt, s_hlt = build_advanced_ml_acceptance_health_check(self.project_root, self.profile)
        df_val, s_val = build_advanced_ml_acceptance_validation_report({}, self.profile)
        df_sft, s_sft = build_advanced_ml_acceptance_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_advanced_ml_acceptance_health_check"):
            self.data_lake.save_advanced_ml_acceptance_health_check(df_hlt, s_hlt)
            self.data_lake.save_advanced_ml_acceptance_validation_report(df_val, s_val)
            self.data_lake.save_advanced_ml_acceptance_safety_boundary(df_sft, s_sft)
            self.data_lake.save_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(df_hnd, s_hnd)

        dfs = {"health": df_hlt, "validation": df_val, "safety": df_sft, "handoff": df_hnd}
        summary = {"health": s_hlt, "validation": s_val, "safety": s_sft, "handoff": s_hnd, "non_signal": True}
        return dfs, summary

    def build_advanced_ml_acceptance_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Consolidate overall status across all sections."""
        components_dfs, _ = self.build_components_checkpoints(save=False)
        scoring_dfs, s_scr = self.build_scoring_manifest(save=False)
        handoff_dfs, s_hnd = self.build_health_validation_safety_handoff(save=False)

        records = [{
            "profile": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "components_registered": len(components_dfs.get("components", [])),
            "checkpoints_satisfied": len(components_dfs.get("checkpoints", [])),
            "readiness_score": s_scr["scoring"]["readiness_score"],
            "classification": s_scr["scoring"]["classification"],
            "phase_146_handoff_ready": s_hnd["handoff"]["all_satisfied"],
            "production_ready": False,
            "broker_ready": False,
            "live_trading_ready": False,
            "status": "ACCEPTED",
            "non_signal": True,
        }]

        df = pd.DataFrame(records)
        summary = {
            "active_profile": self.profile.profile_name,
            "current_phase": self.profile.current_phase,
            "target_final_phase": self.profile.target_final_phase,
            "next_phase": self.profile.next_phase,
            "readiness_score": s_scr["scoring"]["readiness_score"],
            "classification": s_scr["scoring"]["classification"],
            "status": "ACCEPTED",
            "non_signal": True,
        }

        if save and hasattr(self.data_lake, "save_advanced_ml_acceptance_report"):
            full_md = build_advanced_ml_acceptance_full_markdown_report(
                {"components": components_dfs["components"], "scoring": scoring_dfs["scoring"], "handoff": handoff_dfs["handoff"]},
                summary,
            )
            self.data_lake.save_advanced_ml_acceptance_report(
                self.profile.profile_name, summary, full_md
            )

        return df, summary
