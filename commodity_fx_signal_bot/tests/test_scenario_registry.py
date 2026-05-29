import pytest
from pathlib import Path
from scenarios.scenario_registry import ScenarioRegistry, build_default_scenarios, scenario_definitions_to_dataframe
from scenarios.scenario_config import get_default_scenario_profile

def test_default_scenarios_not_empty():
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)
    assert len(scenarios) > 0
    assert scenarios[0].safety_label == "synthetic_offline_only"

def test_scenario_registry(tmp_path):
    registry = ScenarioRegistry(tmp_path)
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)
    for s in scenarios:
        registry.add_scenario(s)

    assert len(registry.scenarios) == len(scenarios)
    df = registry.load_scenarios()
    assert not df.empty
    assert "scenario_id" in df.columns

    s1 = registry.get_scenario(scenarios[0].scenario_id)
    assert s1 is not None
    assert s1["scenario_id"] == scenarios[0].scenario_id

    type_df = registry.list_by_type("symbol_research_scenario")
    assert not type_df.empty
