import pytest
from pathlib import Path
from scenarios.scenario_pipeline import ScenarioPipeline
from config.settings import Settings
from scenarios.scenario_config import get_default_scenario_profile

class MockDataLake:
    def __init__(self):
        self.saved_scenarios = False
    def save_scenario_registry(self, df, summary):
        self.saved_scenarios = True
    def save_scenario_sample_data_manifest(self, df, summary): pass
    def save_scenario_fixtures(self, df, summary): pass
    def save_scenario_expected_outputs(self, df, summary): pass
    def save_scenario_workflow_packs(self, df, summary): pass
    def save_demo_command_sequences(self, df, summary): pass
    def save_scenario_dry_run_results(self, df, summary): pass
    def save_scenario_validation_report(self, df, summary): pass
    def save_case_studies(self, df, summary): pass
    def save_module_demo_flows(self, df, summary): pass
    def save_end_to_end_demo_report(self, name, report): pass

def test_scenario_pipeline():
    dl = MockDataLake()
    s = Settings()
    p = get_default_scenario_profile()

    pipeline = ScenarioPipeline(data_lake=dl, settings=s, project_root=Path("."), profile=p)
    df, summ = pipeline.build_scenario_registry_report(save=True)

    assert not df.empty
    assert dl.saved_scenarios is True
