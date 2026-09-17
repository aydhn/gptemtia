# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Pipeline.

Coordinates generation of all Phase 152 acceptance registries, checkpoints,
boundaries, findings, readiness scores, manifests, health checks, validation reports,
and Phase 153 handoff documents.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import pandas as pd

from config.settings import Settings, get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
    get_default_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_profile_registry import (
    build_backtest_acceptance_profile_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_domain_registry import (
    build_backtest_acceptance_domain_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_scope_registry import (
    build_backtest_acceptance_scope_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_component_registry import (
    build_backtest_acceptance_component_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_component_checkpoints import (
    build_backtest_acceptance_component_checkpoint_registry,
)
from advanced_backtest_acceptance.phase_146_realistic_backtest_acceptance import (
    build_phase_146_realistic_backtest_acceptance_registry,
)
from advanced_backtest_acceptance.phase_147_walk_forward_oos_acceptance import (
    build_phase_147_walk_forward_oos_acceptance_registry,
)
from advanced_backtest_acceptance.phase_148_stress_testing_acceptance import (
    build_phase_148_stress_testing_acceptance_registry,
)
from advanced_backtest_acceptance.phase_149_monte_carlo_acceptance import (
    build_phase_149_monte_carlo_acceptance_registry,
)
from advanced_backtest_acceptance.phase_150_backtest_governance_acceptance import (
    build_phase_150_backtest_governance_acceptance_registry,
)
from advanced_backtest_acceptance.phase_151_benchmark_evaluation_acceptance import (
    build_phase_151_benchmark_evaluation_acceptance_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_dependencies import (
    build_backtest_acceptance_dependency_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_validation_evidence import (
    build_backtest_acceptance_validation_evidence_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_safety_boundary_registry import (
    build_backtest_acceptance_safety_boundary_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_non_production_boundaries import (
    build_backtest_acceptance_non_production_boundary_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_manual_review_gates import (
    build_backtest_acceptance_manual_review_gate_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_go_no_go_boundaries import (
    build_backtest_acceptance_go_no_go_boundary_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_blockers import (
    build_backtest_acceptance_blocker_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_gaps import (
    build_backtest_acceptance_gap_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_warnings import (
    build_backtest_acceptance_warning_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_findings import (
    build_backtest_acceptance_findings_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_readiness_scoring import (
    build_backtest_acceptance_readiness_score_report,
)
from advanced_backtest_acceptance.backtest_acceptance_manifest import (
    build_backtest_acceptance_manifest,
)
from advanced_backtest_acceptance.backtest_acceptance_health import (
    build_backtest_acceptance_health_check,
)
from advanced_backtest_acceptance.backtest_acceptance_validation import (
    build_backtest_acceptance_validation_report,
)
from advanced_backtest_acceptance.backtest_acceptance_safety_boundary import (
    build_backtest_acceptance_safety_boundary,
)
from advanced_backtest_acceptance.phase_153_handoff import (
    build_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report,
)
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_backtest_acceptance_full_markdown_report,
)


class BacktestAcceptancePipeline:
    """End-to-end pipeline orchestrator for Phase 152 Backtest Acceptance block."""

    def __init__(
        self,
        data_lake: Optional[DataLake] = None,
        settings: Optional[Settings] = None,
        project_root: Optional[Path] = None,
        profile: Optional[BacktestAcceptanceProfile] = None,
    ):
        self.data_lake = data_lake or DataLake()
        self.settings = settings or get_settings()
        self.project_root = project_root or Path(".")
        self.profile = profile or get_default_backtest_acceptance_profile()

    def build_profiles_domains_scope(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save profile, domain, and scope registries."""
        df_prof, s_prof = build_backtest_acceptance_profile_registry(self.profile)
        df_dom, s_dom = build_backtest_acceptance_domain_registry(self.profile)
        df_scp, s_scp = build_backtest_acceptance_scope_registry(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_profile_registry"):
            self.data_lake.save_backtest_acceptance_profile_registry(df_prof, s_prof)
            self.data_lake.save_backtest_acceptance_domain_registry(df_dom, s_dom)
            self.data_lake.save_backtest_acceptance_scope_registry(df_scp, s_scp)

        dfs = {"profiles": df_prof, "domains": df_dom, "scope": df_scp}
        summary = {"profiles": s_prof, "domains": s_dom, "scope": s_scp, "non_signal": True}
        return dfs, summary

    def build_components_checkpoints(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save component and checkpoint registries."""
        df_cmp, s_cmp = build_backtest_acceptance_component_registry(self.profile)
        df_chk, s_chk = build_backtest_acceptance_component_checkpoint_registry(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_component_registry"):
            self.data_lake.save_backtest_acceptance_component_registry(df_cmp, s_cmp)
            self.data_lake.save_backtest_acceptance_component_checkpoint_registry(df_chk, s_chk)

        dfs = {"components": df_cmp, "checkpoints": df_chk}
        summary = {"components": s_cmp, "checkpoints": s_chk, "non_signal": True}
        return dfs, summary

    def build_phase_acceptance(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save Phase 146-151 acceptance registries."""
        df_146, s_146 = build_phase_146_realistic_backtest_acceptance_registry(self.profile)
        df_147, s_147 = build_phase_147_walk_forward_oos_acceptance_registry(self.profile)
        df_148, s_148 = build_phase_148_stress_testing_acceptance_registry(self.profile)
        df_149, s_149 = build_phase_149_monte_carlo_acceptance_registry(self.profile)
        df_150, s_150 = build_phase_150_backtest_governance_acceptance_registry(self.profile)
        df_151, s_151 = build_phase_151_benchmark_evaluation_acceptance_registry(self.profile)

        if save and hasattr(self.data_lake, "save_phase_146_realistic_backtest_acceptance_registry"):
            self.data_lake.save_phase_146_realistic_backtest_acceptance_registry(df_146, s_146)
            self.data_lake.save_phase_147_walk_forward_oos_acceptance_registry(df_147, s_147)
            self.data_lake.save_phase_148_stress_testing_acceptance_registry(df_148, s_148)
            self.data_lake.save_phase_149_monte_carlo_acceptance_registry(df_149, s_149)
            self.data_lake.save_phase_150_backtest_governance_acceptance_registry(df_150, s_150)
            self.data_lake.save_phase_151_benchmark_evaluation_acceptance_registry(df_151, s_151)

        dfs = {
            "phase_146": df_146, "phase_147": df_147, "phase_148": df_148,
            "phase_149": df_149, "phase_150": df_150, "phase_151": df_151,
        }
        summary = {
            "phase_146": s_146, "phase_147": s_147, "phase_148": s_148,
            "phase_149": s_149, "phase_150": s_150, "phase_151": s_151,
            "non_signal": True,
        }
        return dfs, summary

    def build_dependency_evidence(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save dependency, evidence, and safety boundary registries."""
        df_dep, s_dep = build_backtest_acceptance_dependency_registry(self.profile)
        df_evd, s_evd = build_backtest_acceptance_validation_evidence_registry(self.profile)
        df_sba, s_sba = build_backtest_acceptance_safety_boundary_registry(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_dependency_registry"):
            self.data_lake.save_backtest_acceptance_dependency_registry(df_dep, s_dep)
            self.data_lake.save_backtest_acceptance_validation_evidence_registry(df_evd, s_evd)
            self.data_lake.save_backtest_acceptance_safety_boundary_registry(df_sba, s_sba)

        dfs = {"dependencies": df_dep, "evidence": df_evd, "safety_registry": df_sba}
        summary = {"dependencies": s_dep, "evidence": s_evd, "safety_registry": s_sba, "non_signal": True}
        return dfs, summary

    def build_boundaries_gates(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save boundary and manual review gate registries."""
        df_npb, s_npb = build_backtest_acceptance_non_production_boundary_registry(self.profile)
        df_mrg, s_mrg = build_backtest_acceptance_manual_review_gate_registry(self.profile)
        df_gng, s_gng = build_backtest_acceptance_go_no_go_boundary_registry(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_non_production_boundary_registry"):
            self.data_lake.save_backtest_acceptance_non_production_boundary_registry(df_npb, s_npb)
            self.data_lake.save_backtest_acceptance_manual_review_gate_registry(df_mrg, s_mrg)
            self.data_lake.save_backtest_acceptance_go_no_go_boundary_registry(df_gng, s_gng)

        dfs = {"non_production_boundaries": df_npb, "manual_review_gates": df_mrg, "go_no_go": df_gng}
        summary = {"non_production_boundaries": s_npb, "manual_review_gates": s_mrg, "go_no_go": s_gng, "non_signal": True}
        return dfs, summary

    def build_blockers_gaps_warnings_findings(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save blockers, gaps, warnings, and findings."""
        df_blk, s_blk = build_backtest_acceptance_blocker_registry(self.profile)
        df_gap, s_gap = build_backtest_acceptance_gap_registry(self.profile)
        df_wrn, s_wrn = build_backtest_acceptance_warning_registry(self.profile)
        df_fnd, s_fnd = build_backtest_acceptance_findings_registry(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_blocker_registry"):
            self.data_lake.save_backtest_acceptance_blocker_registry(df_blk, s_blk)
            self.data_lake.save_backtest_acceptance_gap_registry(df_gap, s_gap)
            self.data_lake.save_backtest_acceptance_warning_registry(df_wrn, s_wrn)
            self.data_lake.save_backtest_acceptance_findings_registry(df_fnd, s_fnd)

        dfs = {"blockers": df_blk, "gaps": df_gap, "warnings": df_wrn, "findings": df_fnd}
        summary = {"blockers": s_blk, "gaps": s_gap, "warnings": s_wrn, "findings": s_fnd, "non_signal": True}
        return dfs, summary

    def build_scoring_manifest(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build and optionally save readiness score and acceptance manifest."""
        df_scr, s_scr = build_backtest_acceptance_readiness_score_report(self.profile)
        df_mnf, s_mnf = build_backtest_acceptance_manifest(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_readiness_score_report"):
            self.data_lake.save_backtest_acceptance_readiness_score_report(df_scr, s_scr)
            self.data_lake.save_backtest_acceptance_manifest(df_mnf, s_mnf)

        dfs = {"scoring": df_scr, "manifest": df_mnf}
        summary = {"scoring": s_scr, "manifest": s_mnf, "non_signal": True}
        return dfs, summary

    def build_health_validation_safety_handoff(
        self, save: bool = True
    ) -> Tuple[Dict[str, pd.DataFrame], Dict[str, Any]]:
        """Build health check, validation, safety boundaries, and Phase 153 handoff."""
        df_hlt, s_hlt = build_backtest_acceptance_health_check(self.project_root, self.profile)
        df_val, s_val = build_backtest_acceptance_validation_report({}, self.profile)
        df_sft, s_sft = build_backtest_acceptance_safety_boundary(self.profile)
        df_hnd, s_hnd = build_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report(self.profile)

        if save and hasattr(self.data_lake, "save_backtest_acceptance_health_check"):
            self.data_lake.save_backtest_acceptance_health_check(df_hlt, s_hlt)
            self.data_lake.save_backtest_acceptance_validation_report(df_val, s_val)
            self.data_lake.save_backtest_acceptance_safety_boundary(df_sft, s_sft)
            self.data_lake.save_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report(df_hnd, s_hnd)

        dfs = {"health": df_hlt, "validation": df_val, "safety": df_sft, "handoff": df_hnd}
        summary = {"health": s_hlt, "validation": s_val, "safety": s_sft, "handoff": s_hnd, "non_signal": True}
        return dfs, summary

    def build_backtest_acceptance_status(
        self, save: bool = True
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Consolidate overall status across all sections and write reports."""
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
            "phase_153_handoff_ready": s_hnd["handoff"]["all_satisfied"],
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

        if save and hasattr(self.data_lake, "save_backtest_acceptance_report"):
            full_md = build_backtest_acceptance_full_markdown_report(
                {
                    "components": components_dfs["components"],
                    "scoring": scoring_dfs["scoring"],
                    "handoff": handoff_dfs["handoff"],
                },
                summary,
            )
            self.data_lake.save_backtest_acceptance_report(
                self.profile.profile_name, summary, full_md
            )

        return df, summary
