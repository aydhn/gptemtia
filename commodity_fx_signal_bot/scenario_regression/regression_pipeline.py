import pandas as pd
from pathlib import Path

from config.settings import Settings
from data.storage.data_lake import DataLake
from scenario_regression.regression_config import ScenarioRegressionProfile, get_default_scenario_regression_profile
from scenario_regression.regression_registry import ScenarioRegressionRegistry, build_default_regression_definitions, regression_definitions_to_dataframe
from scenario_regression.golden_outputs import build_golden_outputs_for_scenario, build_golden_output_manifest
from scenario_regression.snapshot_capture import capture_snapshots_for_scenario, build_snapshot_manifest
from scenario_regression.snapshot_compare import build_snapshot_diff_report
from scenario_regression.deterministic_replay import DeterministicReplayRunner
from scenario_regression.demo_workflow_regression import build_demo_workflow_regression_report
from scenario_regression.end_to_end_acceptance import build_end_to_end_demo_acceptance_report
from scenario_regression.drift_detection import build_scenario_drift_report
from scenario_regression.failure_register import build_failures_from_regression_results, regression_failures_to_dataframe, summarize_regression_failures
from scenario_regression.regression_quality import build_scenario_regression_quality_report
from scenario_regression.regression_report_builder import (
    build_regression_registry_markdown_report,
    build_golden_output_markdown_report,
    build_snapshot_comparison_markdown_report,
    build_deterministic_replay_markdown_report,
    build_demo_acceptance_markdown_report,
    build_regression_status_markdown_report
)
import reports.report_builder as rb

class ScenarioRegressionPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        project_root: Path,
        profile: ScenarioRegressionProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_scenario_regression_profile()

    def _get_dummy_scenarios(self) -> pd.DataFrame:
        return pd.DataFrame([{"scenario_id": "scen_1"}])

    def build_scenario_regression_registry(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        scenarios_df = self._get_dummy_scenarios()
        defs = build_default_regression_definitions(scenarios_df, self.profile)
        df = regression_definitions_to_dataframe(defs)

        summary = {"total_definitions": len(df)}
        if save:
            self.data_lake.save_scenario_regression_registry(df, summary)
            md = build_regression_registry_markdown_report(summary, df)
            txt = rb.build_scenario_regression_registry_text_report(summary, df)
            self.data_lake.save_scenario_regression_report("regression_registry", {"content": txt}, md)

        return df, summary

    def build_golden_output_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        expected_outputs_df = pd.DataFrame([{"scenario_id": "scen_1", "output_name": "test_out", "output_path": "test.csv"}])
        df, summary = build_golden_outputs_for_scenario("scen_1", expected_outputs_df, self.project_root)
        manifest = build_golden_output_manifest(df)

        if save:
            self.data_lake.save_golden_outputs(df, summary)
            self.data_lake.save_golden_output_manifest(manifest)
            md = build_golden_output_markdown_report(summary, df)
            txt = rb.build_golden_output_text_report(summary, df)
            self.data_lake.save_scenario_regression_report("golden_output", {"content": txt}, md)

        return df, summary

    def build_snapshot_comparison_report(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        paths = ["test.csv"]
        df, summary = capture_snapshots_for_scenario("scen_1", paths, self.profile)

        diff_df, diff_summary = build_snapshot_diff_report(pd.DataFrame(), df, self.profile)

        if save:
            self.data_lake.save_snapshot_manifest(df, summary)
            self.data_lake.save_snapshot_diff_report(diff_df, diff_summary)
            md = build_snapshot_comparison_markdown_report(diff_summary, diff_df)
            txt = rb.build_snapshot_comparison_text_report(diff_summary, diff_df)
            self.data_lake.save_scenario_regression_report("snapshot_comparison", {"content": txt}, md)

        return {"manifest": df, "diff": diff_df}, diff_summary

    def build_deterministic_replay_report(self, execute_safe_commands: bool = False, save: bool = True) -> tuple[pd.DataFrame, dict]:
        runner = DeterministicReplayRunner(self.project_root, self.profile)
        scen_df = self._get_dummy_scenarios()

        df, summary = runner.replay_all_scenarios(scen_df, pd.DataFrame(), pd.DataFrame(), execute_safe_commands)

        if save:
            self.data_lake.save_deterministic_replay_report(df, summary)
            md = build_deterministic_replay_markdown_report(summary, df)
            txt = rb.build_deterministic_replay_text_report(summary, df)
            self.data_lake.save_scenario_regression_report("deterministic_replay", {"content": txt}, md)

        return df, summary

    def build_demo_acceptance_report(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        workflow_df, workflow_summary = build_demo_workflow_regression_report(None, None, None, self.profile)
        acceptance_df, acceptance_summary = build_end_to_end_demo_acceptance_report(pd.DataFrame(), pd.DataFrame(), workflow_df, self.profile)

        if save:
            self.data_lake.save_demo_workflow_regression_report(workflow_df, workflow_summary)
            self.data_lake.save_end_to_end_demo_acceptance(acceptance_df, acceptance_summary)
            md = build_demo_acceptance_markdown_report(acceptance_summary, acceptance_df)
            txt = rb.build_demo_acceptance_text_report(acceptance_summary, acceptance_df)
            self.data_lake.save_scenario_regression_report("demo_acceptance", {"content": txt}, md)

        return {"workflow": workflow_df, "acceptance": acceptance_df}, acceptance_summary

    def build_scenario_regression_status(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"status": "ok", "component": "regression_pipeline"}])
        summary = {"status": "ok"}
        if save:
            md = build_regression_status_markdown_report(summary, df)
            txt = rb.build_scenario_regression_status_report(df, summary)
            self.data_lake.save_scenario_regression_report("regression_status", {"content": txt}, md)

        return df, summary
