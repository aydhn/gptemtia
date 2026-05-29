"""
Orchestrator pipeline for generating scenarios and reports.
"""

import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, Optional
import json

from config.settings import Settings
from data.storage.data_lake import DataLake
from scenarios.scenario_config import ScenarioProfile, get_default_scenario_profile
from scenarios.scenario_registry import ScenarioRegistry, build_default_scenarios, scenario_definitions_to_dataframe
from scenarios.sample_data_builder import build_sample_data_pack, save_sample_data_pack
from scenarios.fixture_generator import build_all_scenario_fixtures, build_fixture_manifest
from scenarios.expected_outputs import build_expected_output_contracts, validate_expected_outputs, summarize_expected_outputs
from scenarios.workflow_packs import build_default_workflow_packs
from scenarios.demo_command_sequences import build_all_demo_command_sequences, summarize_demo_command_sequences
from scenarios.scenario_executor import ScenarioDryRunExecutor, summarize_scenario_dry_runs
from scenarios.scenario_validation import build_scenario_validation_report
from scenarios.case_studies import build_default_case_studies, case_studies_to_dataframe
from scenarios.module_demo_flows import build_all_module_demo_flows, summarize_module_demo_flows
from scenarios.end_to_end_demo import build_end_to_end_offline_demo_plan, build_end_to_end_demo_expected_outputs, build_end_to_end_demo_report, summarize_end_to_end_demo
from scenarios.scenario_quality import build_scenario_quality_report
from scenarios.scenario_report_builder import (
    build_scenario_registry_markdown_report,
    build_sample_data_markdown_report,
    build_scenario_dry_run_markdown_report,
    build_case_study_markdown_report,
    build_demo_workflow_markdown_report,
    build_end_to_end_demo_markdown_report
)


class ScenarioPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: Optional[ScenarioProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root

        if profile is None:
            self.profile = get_default_scenario_profile()
        else:
            self.profile = profile

        from config.paths import DATA_SCENARIOS_REGISTRY_DIR
        self.registry = ScenarioRegistry(DATA_SCENARIOS_REGISTRY_DIR)

        # Load defaults
        self._initialize_registry()

    def _initialize_registry(self):
        """Initializes the registry with default scenarios."""
        defaults = build_default_scenarios(self.profile)
        for s in defaults:
            self.registry.add_scenario(s)

    def build_scenario_registry_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        """Builds and optionally saves the scenario registry report."""
        df = self.registry.load_scenarios()
        summary = self.registry.summarize()

        if save:
            md = build_scenario_registry_markdown_report(summary, df)
            # data lake methods added later
            self.data_lake.save_scenario_registry(df, summary)

        return df, summary

    def build_sample_data_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        """Builds synthetic sample data and returns the manifest."""
        data_pack, _ = build_sample_data_pack(self.profile)

        if not save:
            return pd.DataFrame(), {"warnings": ["Did not save sample data because save=False."]}

        from config.paths import DATA_SCENARIOS_SAMPLE_DATA_DIR
        manifest_df, summary = save_sample_data_pack(data_pack, DATA_SCENARIOS_SAMPLE_DATA_DIR)

        self.data_lake.save_scenario_sample_data_manifest(manifest_df, summary)
        return manifest_df, summary

    def build_scenario_dry_run_report(
        self,
        scenario_id: Optional[str] = None,
        execute_safe_commands: bool = False,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, dict]:
        """Builds a scenario dry run report."""
        # Need sequences
        scenarios = list(self.registry.scenarios.values())
        if scenario_id:
            scenarios = [s for s in scenarios if s.scenario_id == scenario_id]

        cmd_df, _ = build_all_demo_command_sequences(scenarios, self.profile)

        executor = ScenarioDryRunExecutor(self.project_root, self.profile)
        dry_run_df, summary = executor.dry_run_all_scenarios(scenarios, cmd_df, execute_safe_commands)

        if save:
            self.data_lake.save_scenario_dry_run_results(dry_run_df, summary)

        return dry_run_df, summary

    def build_case_study_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        """Builds the synthetic case studies."""
        case_studies = build_default_case_studies(self.profile)
        df = case_studies_to_dataframe(case_studies)
        summary = {"total": len(case_studies)}

        if save:
            self.data_lake.save_case_studies(df, summary)

        return df, summary

    def build_demo_workflow_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        """Builds workflow packs and module flows."""
        wf_df, wf_summary = build_default_workflow_packs(self.profile)
        mod_df, mod_summary = build_all_module_demo_flows(self.profile)

        # We'll just return workflows for simplicity here, but save both
        if save:
            self.data_lake.save_scenario_workflow_packs(wf_df, wf_summary)
            self.data_lake.save_module_demo_flows(mod_df, mod_summary)

            # Save command sequences too
            scenarios = list(self.registry.scenarios.values())
            cmd_df, cmd_sum = build_all_demo_command_sequences(scenarios, self.profile)
            self.data_lake.save_demo_command_sequences(cmd_df, cmd_sum)

        return wf_df, wf_summary

    def build_end_to_end_demo_report(self, save: bool = True) -> Tuple[Dict[str, pd.DataFrame], dict]:
        """Builds the E2E offline demo report."""
        plan_df = build_end_to_end_offline_demo_plan(self.profile)
        exp_df = build_end_to_end_demo_expected_outputs(self.profile)
        summary = summarize_end_to_end_demo(plan_df)

        json_str, report_dict = build_end_to_end_demo_report(plan_df, exp_df)

        if save:
            # We save the report dict
            self.data_lake.save_end_to_end_demo_report("end_to_end_offline_demo", report_dict)

        return {"plan": plan_df, "expected": exp_df}, summary

    def build_scenario_status(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        """Builds a high level status of the scenarios system."""
        # Simple status check
        status = []
        try:
            reg = self.data_lake.load_scenario_registry()
            status.append({"component": "registry", "status": "exists", "count": len(reg) if not reg.empty else 0})
        except:
            status.append({"component": "registry", "status": "missing", "count": 0})

        df = pd.DataFrame(status)
        summary = {"total_components": len(status)}

        if save:
            pass # Usually just outputs via standard save_report but we'll implement later

        return df, summary
