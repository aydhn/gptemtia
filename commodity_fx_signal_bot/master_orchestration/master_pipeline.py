"""
Master orchestration execution pipeline.
"""

import pandas as pd
from pathlib import Path
import logging

from config.settings import Settings
from config.paths import DOCS_MASTER_ORCHESTRATION, REPORTS_MASTER_ORCHESTRATION_CSV, REPORTS_MASTER_ORCHESTRATION_MARKDOWN, REPORTS_MASTER_ORCHESTRATION_TXT, REPORTS_MASTER_ORCHESTRATION_JSON
from data.storage.data_lake import DataLake
from master_orchestration.master_config import MasterOrchestrationProfile, get_default_master_orchestration_profile
from master_orchestration.layer_map import build_orchestration_layer_map, build_layer_dependency_table, summarize_layer_map
from master_orchestration.dependency_mapper import build_module_dependency_map, build_report_dependency_map, build_datalake_dependency_map, build_cross_layer_dependency_summary
from master_orchestration.command_graph import build_master_command_registry, build_command_dependency_graph, summarize_command_graph
from master_orchestration.operating_modes import build_operating_mode_registry, summarize_operating_modes
from master_orchestration.master_command_plan import build_offline_master_command_plan, build_master_dry_run_execution_plan
from master_orchestration.safe_meta_runner import SafeMetaRunner, build_meta_runner_registry
from master_orchestration.run_order_planner import build_daily_offline_operating_plan, build_weekly_offline_operating_plan, build_monthly_maintenance_plan, build_full_audit_run_plan, summarize_run_order_plans
from master_orchestration.handoff_checklists import build_operator_handoff_checklist, build_codex_handoff_checklist, build_analyst_handoff_checklist, evaluate_handoff_checklist, summarize_handoff_checklists
from master_orchestration.operational_playbook import build_full_operational_playbook
from master_orchestration.consolidation_matrix import build_phase_1_60_consolidation_matrix, build_phase_1_60_executive_digest, summarize_phase_1_60_consolidation
from master_orchestration.safety_boundary_report import build_master_safety_boundary_report, scan_master_plan_for_forbidden_terms
from master_orchestration.master_status import build_master_orchestration_status, summarize_master_status
from master_orchestration.master_quality import build_master_quality_report
from master_orchestration.master_report_builder import (
    build_orchestration_map_markdown_report,
    build_master_command_plan_markdown_report,
    build_master_dry_run_markdown_report,
    build_operational_playbook_markdown_report,
    build_phase_1_60_consolidation_markdown_report,
    build_master_safety_boundary_markdown_report,
    build_master_status_markdown_report
)

logger = logging.getLogger(__name__)

class MasterOrchestrationPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: MasterOrchestrationProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_master_orchestration_profile()
        self.runner = SafeMetaRunner(project_root, self.profile)

    def build_orchestration_map(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        logger.info(f"Building orchestration map with profile: {self.profile.name}")
        layer_df = build_orchestration_layer_map(self.profile)
        layer_summary = summarize_layer_map(layer_df)

        mod_dep_df = build_module_dependency_map(self.project_root, layer_df)
        rep_dep_df = build_report_dependency_map(self.project_root)
        dl_dep_df = build_datalake_dependency_map(self.project_root)
        dep_summary = build_cross_layer_dependency_summary(mod_dep_df, rep_dep_df, dl_dep_df)

        cmd_reg_df = build_master_command_registry(self.project_root, self.profile)
        cmd_dep_df = build_command_dependency_graph(cmd_reg_df)
        cmd_summary = summarize_command_graph(cmd_reg_df, cmd_dep_df)

        summary = {**layer_summary, **dep_summary, **cmd_summary}

        if save:
            self.data_lake.save_orchestration_layer_map(layer_df, summary)
            self.data_lake.save_module_dependency_map(mod_dep_df)
            self.data_lake.save_report_dependency_map(rep_dep_df)
            self.data_lake.save_datalake_dependency_map(dl_dep_df)
            self.data_lake.save_master_command_registry(cmd_reg_df)
            self.data_lake.save_command_dependency_graph(cmd_dep_df)

            md_report = build_orchestration_map_markdown_report(summary, layer_df)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "master_orchestration_map_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

        dfs = {
            "layer_map": layer_df,
            "module_dependency": mod_dep_df,
            "report_dependency": rep_dep_df,
            "datalake_dependency": dl_dep_df,
            "command_registry": cmd_reg_df,
            "command_graph": cmd_dep_df
        }
        return dfs, summary

    def build_offline_master_command_plan(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        logger.info(f"Building offline master command plan with profile: {self.profile.name}")
        cmd_reg_df = build_master_command_registry(self.project_root, self.profile)
        plan_df, summary = build_offline_master_command_plan(cmd_reg_df, self.profile)

        mode_reg_df = build_operating_mode_registry(self.profile)
        mode_summary = summarize_operating_modes(mode_reg_df)
        summary.update(mode_summary)

        if save:
            self.data_lake.save_offline_master_command_plan(plan_df, summary)
            self.data_lake.save_operating_mode_registry(mode_reg_df)

            md_report = build_master_command_plan_markdown_report(summary, plan_df)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "offline_master_command_plan_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

        return plan_df, summary

    def build_master_dry_run_plan(self, operating_mode: str | None = None, save: bool = True) -> tuple[pd.DataFrame, dict]:
        logger.info(f"Building master dry run plan for mode: {operating_mode or 'all'}")
        cmd_reg_df = build_master_command_registry(self.project_root, self.profile)
        plan_df, _ = build_master_dry_run_execution_plan(cmd_reg_df, operating_mode or "all", self.profile)

        # Meta runner validation and execution
        validation = self.runner.validate_plan(plan_df)
        dry_run_df, summary = self.runner.dry_run_plan(plan_df)

        meta_reg_df = build_meta_runner_registry(cmd_reg_df, self.profile)

        summary["validation"] = validation

        if save:
            self.data_lake.save_master_dry_run_execution_plan(dry_run_df, summary)
            self.data_lake.save_meta_runner_registry(meta_reg_df)

            md_report = build_master_dry_run_markdown_report(summary, dry_run_df)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "master_dry_run_plan_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

        return dry_run_df, summary

    def build_operational_playbook(self, save: bool = True) -> tuple[str, dict]:
        logger.info(f"Building operational playbook with profile: {self.profile.name}")

        cmd_reg_df = build_master_command_registry(self.project_root, self.profile)
        mode_reg_df = build_operating_mode_registry(self.profile)
        plan_df, _ = build_offline_master_command_plan(cmd_reg_df, self.profile)

        playbook_text, summary = build_full_operational_playbook(self.profile, mode_reg_df, plan_df)

        # Run order plans
        daily_df, _ = build_daily_offline_operating_plan(cmd_reg_df, self.profile)
        weekly_df, _ = build_weekly_offline_operating_plan(cmd_reg_df, self.profile)
        monthly_df, _ = build_monthly_maintenance_plan(cmd_reg_df, self.profile)

        # Handoffs
        op_handoff = evaluate_handoff_checklist(build_operator_handoff_checklist(self.profile))
        codex_handoff = evaluate_handoff_checklist(build_codex_handoff_checklist(self.profile))
        analyst_handoff = evaluate_handoff_checklist(build_analyst_handoff_checklist(self.profile))

        if save:
            self.data_lake.save_operational_playbook(playbook_text, summary)

            self.data_lake.save_run_order_plan("daily_offline_operating", daily_df)
            self.data_lake.save_run_order_plan("weekly_offline_operating", weekly_df)
            self.data_lake.save_run_order_plan("monthly_maintenance", monthly_df)

            self.data_lake.save_handoff_checklist("operator", op_handoff)
            self.data_lake.save_handoff_checklist("codex", codex_handoff)
            self.data_lake.save_handoff_checklist("analyst", analyst_handoff)

            md_report = build_operational_playbook_markdown_report(summary, playbook_text)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "operational_playbook_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

            docs_path = DOCS_MASTER_ORCHESTRATION / "OPERATIONAL_PLAYBOOK.md"
            docs_path.parent.mkdir(parents=True, exist_ok=True)
            docs_path.write_text(playbook_text, encoding="utf-8")

        return playbook_text, summary

    def build_phase_1_60_consolidation(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        logger.info(f"Building Phase 1-60 consolidation with profile: {self.profile.name}")
        matrix_df = build_phase_1_60_consolidation_matrix(self.project_root, self.profile)
        summary = summarize_phase_1_60_consolidation(matrix_df)

        digest_text, digest_summary = build_phase_1_60_executive_digest(matrix_df, self.profile)
        summary.update(digest_summary)

        if save:
            self.data_lake.save_phase_1_60_consolidation_matrix(matrix_df, summary)
            self.data_lake.save_phase_1_60_executive_digest(digest_text)

            md_report = build_phase_1_60_consolidation_markdown_report(summary, matrix_df)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "phase_1_60_executive_digest.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

        return matrix_df, summary

    def build_master_safety_boundary_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        logger.info(f"Building master safety boundary report with profile: {self.profile.name}")
        cmd_reg_df = build_master_command_registry(self.project_root, self.profile)
        plan_df, _ = build_offline_master_command_plan(cmd_reg_df, self.profile)

        safety_df, summary = build_master_safety_boundary_report(self.project_root, plan_df, self.profile)
        forbidden_df, forbidden_summary = scan_master_plan_for_forbidden_terms(plan_df, self.profile)
        summary.update(forbidden_summary)

        if save:
            self.data_lake.save_master_safety_boundary_report(safety_df, summary)
            if not forbidden_df.empty:
                # Assuming data lake has a method or just generic save
                # Use a custom save or just to_parquet here since we don't have a dedicated method
                path = self.data_lake.LAKE_MASTER_ORCHESTRATION_SAFETY / f"master_forbidden_terms_scan_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.parquet"
                forbidden_df.to_parquet(path, index=False)

            md_report = build_master_safety_boundary_markdown_report(summary, safety_df)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "master_safety_boundary_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

        return safety_df, summary

    def build_master_operational_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        logger.info("Building master operational status")
        status_df = build_master_orchestration_status(self.project_root)
        summary = summarize_master_status(status_df)

        if save:
            # We don't have a direct DL method for this, just write it
            md_report = build_master_status_markdown_report(summary, status_df)
            md_path = REPORTS_MASTER_ORCHESTRATION_MARKDOWN / "master_operational_status_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_report, encoding="utf-8")

            # also generate master quality report and save it
            quality = build_master_quality_report(summary, status_df)
            self.data_lake.save_master_quality(self.profile.name, quality)

            # Save master orchestration report
            self.data_lake.save_master_orchestration_report(self.profile.name, summary, md_report)

        return status_df, summary
