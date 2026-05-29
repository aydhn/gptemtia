import re

def update_paths():
    with open('commodity_fx_signal_bot/config/paths.py', 'r') as f:
        content = f.read()

    if "scenario_regression_dir =" in content:
        print("Already updated paths")
        return

    # Find the right place to insert variables (around end of Phase 50)
    insert_idx = content.find("LAKE_RESEARCH_REPORTS_DIR = LAKE_DIR / \"research_reports\"")

    new_paths_vars = """
# Phase 57: Scenario Regression
LAKE_SCENARIO_REGRESSION_DIR = LAKE_DIR / "scenario_regression"
LAKE_SCENARIO_REGRESSION_REGISTRY_DIR = LAKE_SCENARIO_REGRESSION_DIR / "registry"
LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR = LAKE_SCENARIO_REGRESSION_DIR / "golden_outputs"
LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR = LAKE_SCENARIO_REGRESSION_DIR / "snapshots"
LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR = LAKE_SCENARIO_REGRESSION_DIR / "snapshot_diffs"
LAKE_SCENARIO_REGRESSION_REPLAY_DIR = LAKE_SCENARIO_REGRESSION_DIR / "replay"
LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR = LAKE_SCENARIO_REGRESSION_DIR / "fixture_reproducibility"
LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR = LAKE_SCENARIO_REGRESSION_DIR / "output_contracts"
LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR = LAKE_SCENARIO_REGRESSION_DIR / "demo_workflows"
LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR = LAKE_SCENARIO_REGRESSION_DIR / "end_to_end_acceptance"
LAKE_SCENARIO_REGRESSION_DRIFT_DIR = LAKE_SCENARIO_REGRESSION_DIR / "drift"
LAKE_SCENARIO_REGRESSION_FAILURES_DIR = LAKE_SCENARIO_REGRESSION_DIR / "failures"
LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR = LAKE_SCENARIO_REGRESSION_DIR / "checklists"
LAKE_SCENARIO_REGRESSION_QUALITY_DIR = LAKE_SCENARIO_REGRESSION_DIR / "quality"

REPORTS_SCENARIO_REGRESSION_DIR = REPORTS_DIR / "scenario_regression"
REPORTS_SCENARIO_REGRESSION_CSV_DIR = REPORTS_SCENARIO_REGRESSION_DIR / "csv"
REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR = REPORTS_SCENARIO_REGRESSION_DIR / "markdown"
REPORTS_SCENARIO_REGRESSION_TXT_DIR = REPORTS_SCENARIO_REGRESSION_DIR / "txt"
REPORTS_SCENARIO_REGRESSION_JSON_DIR = REPORTS_SCENARIO_REGRESSION_DIR / "json"

DOCS_SCENARIO_REGRESSION_DIR = PROJECT_ROOT / "docs" / "generated" / "scenario_regression"
"""
    content = content[:insert_idx] + new_paths_vars + "\n" + content[insert_idx:]

    # Add attributes to Paths class
    insert_idx = content.find("self.REPORTS_COMMAND_CENTER_JSON_DIR = REPORTS_COMMAND_CENTER_JSON_DIR")
    insert_idx = content.find("\n", insert_idx) + 1

    new_paths_attrs = """
        # Phase 57: Scenario Regression
        self.scenario_regression_dir = LAKE_SCENARIO_REGRESSION_DIR
        self.scenario_regression_registry_dir = LAKE_SCENARIO_REGRESSION_REGISTRY_DIR
        self.scenario_regression_golden_outputs_dir = LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR
        self.scenario_regression_snapshots_dir = LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR
        self.scenario_regression_snapshot_diffs_dir = LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR
        self.scenario_regression_replay_dir = LAKE_SCENARIO_REGRESSION_REPLAY_DIR
        self.scenario_regression_fixture_reproducibility_dir = LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR
        self.scenario_regression_output_contracts_dir = LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR
        self.scenario_regression_demo_workflows_dir = LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR
        self.scenario_regression_end_to_end_acceptance_dir = LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR
        self.scenario_regression_drift_dir = LAKE_SCENARIO_REGRESSION_DRIFT_DIR
        self.scenario_regression_failures_dir = LAKE_SCENARIO_REGRESSION_FAILURES_DIR
        self.scenario_regression_checklists_dir = LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR
        self.scenario_regression_quality_dir = LAKE_SCENARIO_REGRESSION_QUALITY_DIR

        self.reports_scenario_regression_dir = REPORTS_SCENARIO_REGRESSION_DIR
        self.reports_scenario_regression_csv_dir = REPORTS_SCENARIO_REGRESSION_CSV_DIR
        self.reports_scenario_regression_markdown_dir = REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR
        self.reports_scenario_regression_txt_dir = REPORTS_SCENARIO_REGRESSION_TXT_DIR
        self.reports_scenario_regression_json_dir = REPORTS_SCENARIO_REGRESSION_JSON_DIR

        self.docs_scenario_regression_dir = DOCS_SCENARIO_REGRESSION_DIR
"""
    content = content[:insert_idx] + new_paths_attrs + content[insert_idx:]

    # Add directories to ensure_project_directories
    insert_idx = content.find("LAKE_COMMAND_CENTER_QUALITY_DIR,")
    insert_idx = content.find("\n", insert_idx) + 1

    new_dirs = """
        LAKE_SCENARIO_REGRESSION_DIR,
        LAKE_SCENARIO_REGRESSION_REGISTRY_DIR,
        LAKE_SCENARIO_REGRESSION_GOLDEN_OUTPUTS_DIR,
        LAKE_SCENARIO_REGRESSION_SNAPSHOTS_DIR,
        LAKE_SCENARIO_REGRESSION_SNAPSHOT_DIFFS_DIR,
        LAKE_SCENARIO_REGRESSION_REPLAY_DIR,
        LAKE_SCENARIO_REGRESSION_FIXTURE_REPRODUCIBILITY_DIR,
        LAKE_SCENARIO_REGRESSION_OUTPUT_CONTRACTS_DIR,
        LAKE_SCENARIO_REGRESSION_DEMO_WORKFLOWS_DIR,
        LAKE_SCENARIO_REGRESSION_END_TO_END_ACCEPTANCE_DIR,
        LAKE_SCENARIO_REGRESSION_DRIFT_DIR,
        LAKE_SCENARIO_REGRESSION_FAILURES_DIR,
        LAKE_SCENARIO_REGRESSION_CHECKLISTS_DIR,
        LAKE_SCENARIO_REGRESSION_QUALITY_DIR,
        REPORTS_SCENARIO_REGRESSION_DIR,
        REPORTS_SCENARIO_REGRESSION_CSV_DIR,
        REPORTS_SCENARIO_REGRESSION_MARKDOWN_DIR,
        REPORTS_SCENARIO_REGRESSION_TXT_DIR,
        REPORTS_SCENARIO_REGRESSION_JSON_DIR,
        DOCS_SCENARIO_REGRESSION_DIR,
"""
    content = content[:insert_idx] + new_dirs + content[insert_idx:]

    with open('commodity_fx_signal_bot/config/paths.py', 'w') as f:
        f.write(content)

update_paths()
