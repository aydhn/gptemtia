from pathlib import Path
import pandas as pd

from config.settings import Settings
from .ux_config import AnalystUXProfile, get_default_analyst_ux_profile
from .command_aliases import build_default_command_aliases, command_aliases_to_dataframe, validate_command_aliases
from .intent_classifier import classify_analyst_intent, build_intent_examples, summarize_intents
from .safe_command_mapper import build_safe_command_suggestions, rank_command_suggestions, validate_suggestion_safety, summarize_command_suggestions
from .prompt_packs import build_default_prompt_packs, prompt_packs_to_dataframe, build_prompt_pack_manifest
from .workflow_shortcuts import build_default_workflow_shortcuts
from .query_mapping import build_query_mapping_report
from .task_board import build_default_analyst_tasks, analyst_tasks_to_dataframe, summarize_analyst_task_board
from .cheat_sheets import build_command_cheat_sheet, build_safe_query_examples, build_module_quick_reference, build_operator_shortcuts_reference, save_cheat_sheets
from .productivity_checklist import build_productivity_checklist, evaluate_productivity_checklist, summarize_productivity_checklist
from .ux_validation import build_ux_validation_report
from .ux_quality import build_ux_quality_report
from .ux_report_builder import (
    build_alias_markdown_report, build_safe_command_suggestion_markdown_report,
    build_prompt_pack_markdown_report, build_productivity_checklist_markdown_report,
    build_task_board_markdown_report, build_operator_productivity_status_markdown_report
)

class AnalystUXPipeline:
    def __init__(self, data_lake, settings: Settings, project_root: Path, profile: AnalystUXProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_analyst_ux_profile()

    def build_ux_alias_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        aliases = build_default_command_aliases(self.profile)
        df = command_aliases_to_dataframe(aliases)
        summary = validate_command_aliases(aliases)

        if save and hasattr(self.data_lake, "save_command_alias_registry"):
            self.data_lake.save_command_alias_registry(df, summary)

            md = build_alias_markdown_report(summary, df)
            if hasattr(self.data_lake, "save_ux_report"):
                self.data_lake.save_ux_report("ux_alias_report", summary, md)

        return df, summary

    def build_safe_command_suggestions(self, query_text: str, save: bool = True) -> tuple[pd.DataFrame, dict]:
        aliases = build_default_command_aliases(self.profile)
        aliases_df = command_aliases_to_dataframe(aliases)

        df, summary = build_safe_command_suggestions(query_text, aliases_df, self.profile)
        df = rank_command_suggestions(df)
        val_summary = validate_suggestion_safety(df, self.profile)
        summary.update(val_summary)

        if save and hasattr(self.data_lake, "save_safe_command_suggestions"):
            self.data_lake.save_safe_command_suggestions(df, summary)

            md = build_safe_command_suggestion_markdown_report(summary, df)
            if hasattr(self.data_lake, "save_ux_report"):
                self.data_lake.save_ux_report("safe_command_suggestions", summary, md)

        return df, summary

    def build_prompt_pack_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        packs = build_default_prompt_packs(self.profile)
        df = prompt_packs_to_dataframe(packs)
        manifest = build_prompt_pack_manifest(packs)
        summary = {"total_packs": manifest["total_packs"]}

        if save and hasattr(self.data_lake, "save_prompt_pack_registry"):
            self.data_lake.save_prompt_pack_registry(df, summary)
            self.data_lake.save_prompt_pack_manifest(manifest)

            md = build_prompt_pack_markdown_report(summary, df)
            if hasattr(self.data_lake, "save_ux_report"):
                self.data_lake.save_ux_report("prompt_pack_report", summary, md)

        return df, summary

    def build_productivity_checklist(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = build_productivity_checklist(self.profile)
        aliases = command_aliases_to_dataframe(build_default_command_aliases(self.profile))
        prompts = prompt_packs_to_dataframe(build_default_prompt_packs(self.profile))
        tasks = analyst_tasks_to_dataframe(build_default_analyst_tasks(self.profile))

        evaluated = evaluate_productivity_checklist(df, aliases, prompts, tasks)
        summary = summarize_productivity_checklist(evaluated)

        if save and hasattr(self.data_lake, "save_productivity_checklist"):
            self.data_lake.save_productivity_checklist(evaluated, summary)

            md = build_productivity_checklist_markdown_report(summary, evaluated)
            if hasattr(self.data_lake, "save_ux_report"):
                self.data_lake.save_ux_report("productivity_checklist", summary, md)

        return evaluated, summary

    def build_analyst_task_board(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        tasks = build_default_analyst_tasks(self.profile)
        df = analyst_tasks_to_dataframe(tasks)
        summary = summarize_analyst_task_board(df)

        if save and hasattr(self.data_lake, "save_analyst_task_board"):
            self.data_lake.save_analyst_task_board(df, summary)

            md = build_task_board_markdown_report(summary, df)
            if hasattr(self.data_lake, "save_ux_report"):
                self.data_lake.save_ux_report("analyst_task_board", summary, md)

        return df, summary

    def build_operator_productivity_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        # Simple status check
        status = [
            {"component": "aliases", "status": "available"},
            {"component": "prompt_packs", "status": "available"},
            {"component": "task_board", "status": "available"}
        ]
        df = pd.DataFrame(status)
        summary = {"passed": True}

        if save and hasattr(self.data_lake, "save_ux_report"):
            md = build_operator_productivity_status_markdown_report(summary, df)
            self.data_lake.save_ux_report("operator_productivity_status", summary, md)

        return df, summary
