import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.scenario_registry import build_default_scenarios
from scenarios.scenario_validation import (
    validate_scenario_definition, build_scenario_validation_report
)

def test_scenario_validation():
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:2]

    val = validate_scenario_definition(scenarios[0], profile)
    assert val["is_valid"] is True

def test_invalid_safety_label():
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:1]
    scenarios[0].safety_label = "invalid_label"

    val = validate_scenario_definition(scenarios[0], profile)
    assert val["is_valid"] is False

def test_build_validation_report():
    from scenarios.scenario_registry import scenario_definitions_to_dataframe
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:2]
    df = scenario_definitions_to_dataframe(scenarios)

    report_df, summary = build_scenario_validation_report(df)
    assert not report_df.empty
    assert summary["passed"] == len(scenarios)
