import pytest
from pathlib import Path
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.scenario_registry import build_default_scenarios
from scenarios.fixture_generator import build_all_scenario_fixtures, build_fixture_manifest, validate_fixture_manifest

def test_build_fixtures(tmp_path):
    profile = get_default_scenario_profile()
    scenarios = build_default_scenarios(profile)[:2]

    df, summary = build_all_scenario_fixtures(scenarios, profile, tmp_path)
    assert not df.empty
    assert summary["synthetic_enforced"] is True
    assert df["synthetic"].all()

    manifest = build_fixture_manifest(df)
    assert manifest["total_fixtures"] == len(df)

    val = validate_fixture_manifest(manifest)
    assert val["is_valid"] is True
