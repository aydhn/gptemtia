"""
Pipeline for the Command Center.
"""

from typing import Tuple, Dict
import pandas as pd
from pathlib import Path
from data.storage.data_lake import DataLake
from config.settings import Settings
from command_center.command_config import CommandCenterProfile, get_default_command_center_profile
from command_center.command_registry import build_default_command_registry, command_registry_to_dataframe
from command_center.command_safety import filter_safe_commands
from command_center.workflow_registry import build_default_workflows, workflows_to_dataframe
from command_center.runbook_registry import build_default_runbooks, runbooks_to_dataframe
from command_center.project_status import build_project_status_table, summarize_project_status
from command_center.consolidation import build_project_consolidation_summary, build_consolidation_table, build_phase_1_to_50_digest
from command_center.script_discovery import build_script_availability_matrix
from command_center.phase_coverage import build_phase_coverage_matrix
from command_center.module_health import build_module_health_table
from command_center.troubleshooting import build_troubleshooting_plan
from command_center.command_quality import build_command_center_quality_report
from command_center.command_report_builder import (
    build_command_catalog_markdown_report,
    build_guided_workflow_markdown_report,
    build_safe_runbook_markdown_report,
    build_project_status_markdown_report,
    build_project_consolidation_markdown_report,
    build_analyst_command_query_markdown_report
)
from reports.report_builder import (
    build_command_catalog_text_report,
    build_guided_workflow_text_report,
    build_safe_runbook_text_report,
    build_project_status_text_report,
    build_project_consolidation_text_report,
    build_analyst_command_query_text_report,
    build_command_center_status_report
)

class CommandCenterPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: CommandCenterProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_command_center_profile()

    def build_command_catalog_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        commands = build_default_command_registry(self.profile)
        safe_cmds, blocked_cmds = filter_safe_commands(commands)
        df = command_registry_to_dataframe(safe_cmds)

        summary = {
            "profile_name": self.profile.name,
            "total_commands": len(commands),
            "safe_commands": len(safe_cmds),
            "blocked_commands": len(blocked_cmds)
        }

        if save:
            self.data_lake.save_command_registry(df, summary)
            md = build_command_catalog_markdown_report(summary, df)
            txt = build_command_catalog_text_report(summary, df)

            md_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR / "command_catalog_report.md"
            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "command_catalog_report.txt"

            md_path.parent.mkdir(parents=True, exist_ok=True)
            txt_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)

        return df, summary

    def build_guided_workflow_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        commands = build_default_command_registry(self.profile)
        workflows = build_default_workflows(commands, self.profile)
        df = workflows_to_dataframe(workflows)

        summary = {
            "profile_name": self.profile.name,
            "total_workflows": len(workflows)
        }

        if save:
            self.data_lake.save_guided_workflows(df, summary)
            md = build_guided_workflow_markdown_report(summary, df)
            txt = build_guided_workflow_text_report(summary, df)

            md_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR / "guided_workflow_report.md"
            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "guided_workflow_report.txt"

            md_path.parent.mkdir(parents=True, exist_ok=True)
            txt_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)

        return df, summary

    def build_safe_runbook_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        commands = build_default_command_registry(self.profile)
        workflows = build_default_workflows(commands, self.profile)
        runbooks = build_default_runbooks(commands, workflows, self.profile)
        df = runbooks_to_dataframe(runbooks)

        summary = {
            "profile_name": self.profile.name,
            "total_runbooks": len(runbooks)
        }

        if save:
            self.data_lake.save_safe_runbooks(df, summary)
            md = build_safe_runbook_markdown_report(summary, df)
            txt = build_safe_runbook_text_report(summary, df)

            md_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR / "safe_runbook_report.md"
            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "safe_runbook_report.txt"

            md_path.parent.mkdir(parents=True, exist_ok=True)
            txt_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)

        return df, summary

    def build_project_status_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        status_df = build_project_status_table(self.project_root)
        health_df = build_module_health_table(status_df)
        summary = summarize_project_status(status_df)
        summary["profile_name"] = self.profile.name

        if save:
            self.data_lake.save_project_status(status_df, summary)
            self.data_lake.save_module_health(health_df, summary)

            md = build_project_status_markdown_report(summary, status_df)
            txt = build_project_status_text_report(summary, status_df)

            md_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR / "project_status_report.md"
            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "project_status_report.txt"

            md_path.parent.mkdir(parents=True, exist_ok=True)
            txt_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)

        return status_df, summary

    def build_project_consolidation_report(self, save: bool = True) -> Tuple[dict, dict]:
        status_df = build_project_status_table(self.project_root)
        health_df = build_module_health_table(status_df)
        script_df = build_script_availability_matrix(self.project_root)
        phase_df = build_phase_coverage_matrix(self.project_root)

        summary = build_project_consolidation_summary(status_df, health_df, phase_df, script_df)
        summary["profile_name"] = self.profile.name
        summary["phase_1_50_digest"] = build_phase_1_to_50_digest(self.project_root)

        consolidation_df = build_consolidation_table(summary)

        if save:
            # We mock the DataLake's project consolidation report save logic for now
            # but ideally it saves all the dataframes
            self.data_lake.save_script_availability_matrix(script_df, summary)
            self.data_lake.save_phase_coverage_matrix(phase_df, summary)

            md = build_project_consolidation_markdown_report(summary, consolidation_df)
            txt = build_project_consolidation_text_report(summary, consolidation_df)
            self.data_lake.save_project_consolidation_report(self.profile.name, summary, md)

            md_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR / "project_consolidation_report.md"
            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "project_consolidation_report.txt"

            md_path.parent.mkdir(parents=True, exist_ok=True)
            txt_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)

        # Return summary and a placeholder second dict for matching signature
        return summary, {"status": "success"}

    def build_analyst_command_query(self, query_text: str, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        commands = build_default_command_registry(self.profile)
        safe_cmds, _ = filter_safe_commands(commands)
        df, summary = build_troubleshooting_plan(query_text, safe_cmds, self.profile)
        summary["profile_name"] = self.profile.name

        if save:
            md = build_analyst_command_query_markdown_report(summary, df)
            txt = build_analyst_command_query_text_report(summary, df)

            md_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_MARKDOWN_DIR / "analyst_command_query_report.md"
            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "analyst_command_query_report.txt"
            csv_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_CSV_DIR / "analyst_command_query_results.csv"

            md_path.parent.mkdir(parents=True, exist_ok=True)
            txt_path.parent.mkdir(parents=True, exist_ok=True)
            csv_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)
            df.to_csv(csv_path, index=False)

        return df, summary

    def build_command_center_status(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        data = [
            {"component": "data_lake_command_center", "status": "exists" if self.data_lake.paths.LAKE_COMMAND_CENTER_DIR.exists() else "missing"},
            {"component": "reports_output_command_center", "status": "exists" if self.data_lake.paths.REPORTS_COMMAND_CENTER_DIR.exists() else "missing"}
        ]
        df = pd.DataFrame(data)
        summary = {"profile_name": self.profile.name, "components_checked": len(df)}

        if save:
            self.data_lake.save_command_center_status(df, summary)
            txt = build_command_center_status_report(df, summary)

            txt_path = self.data_lake.paths.REPORTS_COMMAND_CENTER_TXT_DIR / "command_center_status_report.txt"
            txt_path.parent.mkdir(parents=True, exist_ok=True)

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(txt)

        return df, summary
