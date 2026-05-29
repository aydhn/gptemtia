import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.scenario_registry import build_default_scenarios
from scenarios.expected_outputs import build_expected_output_contracts, validate_expected_outputs
from pathlib import Path

def test_expected_output_contracts():
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:2]

    df = build_expected_output_contracts(scenarios)
    assert not df.empty
    assert "validation_rule" in df.columns

    val_df, summary = validate_expected_outputs(scenarios[0].scenario_id, df, Path("."))
    assert not val_df.empty
    assert summary["total_checked"] > 0
