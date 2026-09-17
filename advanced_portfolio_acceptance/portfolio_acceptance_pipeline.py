# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Pipeline.

Coordinates generation of all Phase 157 acceptance registries, checkpoints,
boundaries, findings, readiness scores, manifests, health checks, validation reports,
and Phase 158 handoff documents.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
    get_default_portfolio_acceptance_profile,
)
from .portfolio_acceptance_profile_registry import (
    build_portfolio_acceptance_profile_registry,
)
from .portfolio_acceptance_domain_registry import (
    build_portfolio_acceptance_domain_registry,
)
from .portfolio_acceptance_scope_registry import (
    build_portfolio_acceptance_scope_registry,
)
from .portfolio_acceptance_component_registry import (
    build_portfolio_acceptance_component_registry,
)
from .portfolio_acceptance_component_checkpoints import (
    build_portfolio_acceptance_component_checkpoint_registry,
)
from .phase_153_portfolio_construction_acceptance import (
    build_phase_153_portfolio_construction_acceptance_registry,
)
from .phase_154_portfolio_optimization_acceptance import (
    build_phase_154_portfolio_optimization_acceptance_registry,
)
from .phase_155_risk_reporting_acceptance import (
    build_phase_155_risk_reporting_acceptance_registry,
)
from .phase_156_portfolio_scenario_control_acceptance import (
    build_phase_156_portfolio_scenario_control_acceptance_registry,
)
from .portfolio_acceptance_dependencies import (
    build_portfolio_acceptance_dependency_registry,
)
from .portfolio_acceptance_validation_evidence import (
    build_portfolio_acceptance_validation_evidence_registry,
)
from .portfolio_acceptance_safety_boundary_registry import (
    build_portfolio_acceptance_safety_boundary_registry,
)
from .portfolio_acceptance_non_production_boundaries import (
    build_portfolio_acceptance_non_production_boundary_registry,
)
from .portfolio_acceptance_manual_review_gates import (
    build_portfolio_acceptance_manual_review_gate_registry,
)
from .portfolio_acceptance_go_no_go_boundaries import (
    build_portfolio_acceptance_go_no_go_boundary_registry,
)
from .portfolio_acceptance_blockers import (
    build_portfolio_acceptance_blocker_registry,
)
from .portfolio_acceptance_gaps import (
    build_portfolio_acceptance_gap_registry,
)
from .portfolio_acceptance_warnings import (
    build_portfolio_acceptance_warning_registry,
)
from .portfolio_acceptance_findings import (
    build_portfolio_acceptance_findings_registry,
)
from .portfolio_acceptance_readiness_scoring import (
    build_portfolio_acceptance_readiness_score_report,
)
from .portfolio_acceptance_manifest import (
    build_portfolio_acceptance_manifest,
)
from .portfolio_acceptance_health import (
    build_portfolio_acceptance_health_check,
)
from .portfolio_acceptance_validation import (
    build_portfolio_acceptance_validation_report,
)
from .portfolio_acceptance_safety_boundary import (
    build_portfolio_acceptance_safety_boundary,
)
from .phase_158_handoff import (
    build_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report,
)
from .portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_full_markdown_report,
)


class PortfolioAcceptancePipeline:
    """End-to-end pipeline orchestrator for Phase 157 Portfolio Acceptance block."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[PortfolioAcceptanceProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(".")
        self.profile = profile or get_default_portfolio_acceptance_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save profile, domain, and scope registries."""
        df_prof, s_prof = build_portfolio_acceptance_profile_registry(self.profile)
        df_dom, s_dom = build_portfolio_acceptance_domain_registry(self.profile)
        df_scp, s_scp = build_portfolio_acceptance_scope_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_profile_registry"):
            self.data_lake.save_portfolio_acceptance_profile_registry(df_prof, s_prof)
            self.data_lake.save_portfolio_acceptance_domain_registry(df_dom, s_dom)
            self.data_lake.save_portfolio_acceptance_scope_registry(df_scp, s_scp)

        dfs = {"profiles": df_prof, "domains": df_dom, "scope": df_scp}
        summary = {"profiles": s_prof, "domains": s_dom, "scope": s_scp, "non_signal": True}
        return dfs, summary

    def build_components_checkpoints(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save component and checkpoint registries."""
        df_cmp, s_cmp = build_portfolio_acceptance_component_registry(self.profile)
        df_chk, s_chk = build_portfolio_acceptance_component_checkpoint_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_component_registry"):
            self.data_lake.save_portfolio_acceptance_component_registry(df_cmp, s_cmp)
            self.data_lake.save_portfolio_acceptance_component_checkpoint_registry(df_chk, s_chk)

        dfs = {"components": df_cmp, "checkpoints": df_chk}
        summary = {"components": s_cmp, "checkpoints": s_chk, "non_signal": True}
        return dfs, summary

    def build_phase_acceptance(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save Phase 153-156 acceptance registries."""
        df_153, s_153 = build_phase_153_portfolio_construction_acceptance_registry(self.profile)
        df_154, s_154 = build_phase_154_portfolio_optimization_acceptance_registry(self.profile)
        df_155, s_155 = build_phase_155_risk_reporting_acceptance_registry(self.profile)
        df_156, s_156 = build_phase_156_portfolio_scenario_control_acceptance_registry(self.profile)

        if save and hasattr(self.data_lake, "save_phase_153_portfolio_construction_acceptance_registry"):
            self.data_lake.save_phase_153_portfolio_construction_acceptance_registry(df_153, s_153)
            self.data_lake.save_phase_154_portfolio_optimization_acceptance_registry(df_154, s_154)
            self.data_lake.save_phase_155_risk_reporting_acceptance_registry(df_155, s_155)
            self.data_lake.save_phase_156_portfolio_scenario_control_acceptance_registry(df_156, s_156)

        dfs = {
            "phase_153": df_153,
            "phase_154": df_154,
            "phase_155": df_155,
            "phase_156": df_156,
        }
        summary = {
            "phase_153": s_153,
            "phase_154": s_154,
            "phase_155": s_155,
            "phase_156": s_156,
            "non_signal": True,
        }
        return dfs, summary

    def build_dependency_evidence(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save dependency, evidence, and safety boundary registries."""
        df_dep, s_dep = build_portfolio_acceptance_dependency_registry(self.profile)
        df_evd, s_evd = build_portfolio_acceptance_validation_evidence_registry(self.profile)
        df_sba, s_sba = build_portfolio_acceptance_safety_boundary_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_dependency_registry"):
            self.data_lake.save_portfolio_acceptance_dependency_registry(df_dep, s_dep)
            self.data_lake.save_portfolio_acceptance_validation_evidence_registry(df_evd, s_evd)
            self.data_lake.save_portfolio_acceptance_safety_boundary_registry(df_sba, s_sba)

        dfs = {"dependencies": df_dep, "evidence": df_evd, "safety_registry": df_sba}
        summary = {"dependencies": s_dep, "evidence": s_evd, "safety_registry": s_sba, "non_signal": True}
        return dfs, summary

    def build_boundaries_gates(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save boundary and manual review gate registries."""
        df_npb, s_npb = build_portfolio_acceptance_non_production_boundary_registry(self.profile)
        df_mrg, s_mrg = build_portfolio_acceptance_manual_review_gate_registry(self.profile)
        df_gng, s_gng = build_portfolio_acceptance_go_no_go_boundary_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_non_production_boundary_registry"):
            self.data_lake.save_portfolio_acceptance_non_production_boundary_registry(df_npb, s_npb)
            self.data_lake.save_portfolio_acceptance_manual_review_gate_registry(df_mrg, s_mrg)
            self.data_lake.save_portfolio_acceptance_go_no_go_boundary_registry(df_gng, s_gng)

        dfs = {"non_production_boundaries": df_npb, "manual_review_gates": df_mrg, "go_no_go": df_gng}
        summary = {"non_production_boundaries": s_npb, "manual_review_gates": s_mrg, "go_no_go": s_gng, "non_signal": True}
        return dfs, summary

    def build_blockers_gaps_warnings_findings(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save blockers, gaps, warnings, and findings."""
        df_blk, s_blk = build_portfolio_acceptance_blocker_registry(self.profile)
        df_gap, s_gap = build_portfolio_acceptance_gap_registry(self.profile)
        df_wrn, s_wrn = build_portfolio_acceptance_warning_registry(self.profile)
        df_fnd, s_fnd = build_portfolio_acceptance_findings_registry(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_blocker_registry"):
            self.data_lake.save_portfolio_acceptance_blocker_registry(df_blk, s_blk)
            self.data_lake.save_portfolio_acceptance_gap_registry(df_gap, s_gap)
            self.data_lake.save_portfolio_acceptance_warning_registry(df_wrn, s_wrn)
            self.data_lake.save_portfolio_acceptance_findings_registry(df_fnd, s_fnd)

        dfs = {"blockers": df_blk, "gaps": df_gap, "warnings": df_wrn, "findings": df_fnd}
        summary = {"blockers": s_blk, "gaps": s_gap, "warnings": s_wrn, "findings": s_fnd, "non_signal": True}
        return dfs, summary

    def build_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save readiness score and acceptance manifest."""
        df_scr, s_scr = build_portfolio_acceptance_readiness_score_report(self.profile)
        df_mnf, s_mnf = build_portfolio_acceptance_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_readiness_score_report"):
            self.data_lake.save_portfolio_acceptance_readiness_score_report(df_scr, s_scr)
            self.data_lake.save_portfolio_acceptance_manifest(df_mnf, s_mnf)

        dfs = {"scoring": df_scr, "manifest": df_mnf}
        summary = {"scoring": s_scr, "manifest": s_mnf, "non_signal": True}
        return dfs, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, validation report, safety boundary, and Phase 158 handoff report."""
        dfs_prof, _ = self.build_profiles_domains_scope(save=False)
        dfs_comp, _ = self.build_components_checkpoints(save=False)
        dfs_ph, _ = self.build_phase_acceptance(save=False)
        dfs_bnd, _ = self.build_boundaries_gates(save=False)
        dfs_scr, _ = self.build_scoring_manifest(save=False)

        eval_tables = {
            "profiles": dfs_prof["profiles"],
            "checkpoints": dfs_comp["checkpoints"],
            "phase_153": dfs_ph["phase_153"],
            "phase_154": dfs_ph["phase_154"],
            "phase_155": dfs_ph["phase_155"],
            "phase_156": dfs_ph["phase_156"],
            "go_no_go": dfs_bnd["go_no_go"],
            "manifest": dfs_scr["manifest"],
        }

        df_hlth, s_hlth = build_portfolio_acceptance_health_check(self.project_root, self.profile)
        df_val, s_val = build_portfolio_acceptance_validation_report(eval_tables, self.profile)
        df_sft, s_sft = build_portfolio_acceptance_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_portfolio_acceptance_health_check"):
            self.data_lake.save_portfolio_acceptance_health_check(df_hlth, s_hlth)
            self.data_lake.save_portfolio_acceptance_validation_report(df_val, s_val)
            self.data_lake.save_portfolio_acceptance_safety_boundary(df_sft, s_sft)
            self.data_lake.save_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report(df_hnd, s_hnd)

        dfs = {
            "health": df_hlth,
            "validation": df_val,
            "safety": df_sft,
            "handoff": df_hnd,
        }
        summary = {
            "health": s_hlth,
            "validation": s_val,
            "safety": s_sft,
            "handoff": s_hnd,
            "non_signal": True,
        }
        return dfs, summary

    def build_portfolio_acceptance_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run full end-to-end acceptance status pipeline and optionally persist all reports."""
        dfs_prof, s_prof = self.build_profiles_domains_scope(save=save)
        dfs_cmp, s_cmp = self.build_components_checkpoints(save=save)
        dfs_ph, s_ph = self.build_phase_acceptance(save=save)
        dfs_dep, s_dep = self.build_dependency_evidence(save=save)
        dfs_bnd, s_bnd = self.build_boundaries_gates(save=save)
        dfs_fnd, s_fnd = self.build_blockers_gaps_warnings_findings(save=save)
        dfs_scr, s_scr = self.build_scoring_manifest(save=save)
        dfs_hvs, s_hvs = self.build_health_validation_safety_handoff(save=save)

        status_records = [
            {"domain": "profiles_domains_scope", "status": "READY", "items": len(dfs_prof["profiles"])},
            {"domain": "components_checkpoints", "status": "READY", "items": len(dfs_cmp["components"])},
            {"domain": "phase_acceptance", "status": "READY", "items": 4},
            {"domain": "dependency_evidence", "status": "READY", "items": len(dfs_dep["dependencies"])},
            {"domain": "boundaries_gates", "status": "READY", "items": len(dfs_bnd["manual_review_gates"])},
            {"domain": "blockers_gaps_findings", "status": "READY", "items": len(dfs_fnd["findings"])},
            {"domain": "scoring_manifest", "status": "READY", "score": s_scr["scoring"]["readiness_score"]},
            {"domain": "health_validation_handoff", "status": "READY", "handoff_ready": s_hvs["handoff"]["handoff_ready"]},
        ]
        status_df = pd.DataFrame(status_records)

        full_tables = {
            "components": dfs_cmp["components"],
            "checkpoints": dfs_cmp["checkpoints"],
            "phase_153": dfs_ph["phase_153"],
            "phase_154": dfs_ph["phase_154"],
            "phase_155": dfs_ph["phase_155"],
            "phase_156": dfs_ph["phase_156"],
            "dependencies": dfs_dep["dependencies"],
            "evidence": dfs_dep["evidence"],
            "findings": dfs_fnd["findings"],
            "scoring": dfs_scr["scoring"],
            "manifest": dfs_scr["manifest"],
            "health": dfs_hvs["health"],
            "validation": dfs_hvs["validation"],
            "safety": dfs_hvs["safety"],
            "handoff": dfs_hvs["handoff"],
        }
        full_summary = {
            "active_profile": self.profile.profile_name,
            "readiness_score": s_scr["scoring"]["readiness_score"],
            "classification": s_scr["scoring"]["classification"],
            "meets_threshold": s_scr["scoring"]["meets_threshold"],
            "handoff_ready": s_hvs["handoff"]["handoff_ready"],
            "status": "ACCEPTED",
            "non_signal": True,
        }

        full_md = build_portfolio_acceptance_full_markdown_report(full_tables, full_summary)

        if save:
            out_dir = Path("reports/output/advanced_portfolio_acceptance")
            out_dir.mkdir(parents=True, exist_ok=True)
            with open(out_dir / "portfolio_acceptance_report.md", "w", encoding="utf-8") as f:
                f.write(full_md)
            if hasattr(self.data_lake, "save_portfolio_acceptance_report"):
                self.data_lake.save_portfolio_acceptance_report(
                    self.profile.profile_name,
                    full_summary,
                    full_md,
                )

        return status_df, full_summary
