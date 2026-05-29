import pytest
from pathlib import Path
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.scenario_registry import build_default_scenarios
from scenarios.demo_command_sequences import build_all_demo_command_sequences
from scenarios.scenario_executor import ScenarioDryRunExecutor

def test_scenario_executor():
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:2]
    cmd_df, _ = build_all_demo_command_sequences(scenarios, profile)

    executor = ScenarioDryRunExecutor(Path("."), profile)
    df, summary = executor.dry_run_all_scenarios(scenarios, cmd_df, execute_safe_commands=False)

    assert not df.empty
    assert summary["total_runs"] == len(scenarios)
    assert df["validation_passed"].all()
