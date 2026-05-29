import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.scenario_registry import build_default_scenarios
from scenarios.demo_command_sequences import (
    build_all_demo_command_sequences, validate_demo_command_sequence, _is_safe
)

def test_demo_command_sequences():
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:2]

    df, summary = build_all_demo_command_sequences(scenarios, profile)
    assert not df.empty
    assert "command" in df.columns
    assert "is_safe" in df.columns

    val = validate_demo_command_sequence(df)
    assert val["is_valid"] is True

def test_is_safe_command():
    assert _is_safe("python -m scripts.run_governance_status") is True
    assert _is_safe("python -m main --live") is False
    assert _is_safe("send_broker_order") is False
