from scenarios.scenario_models import (
    build_scenario_id, build_fixture_id, build_expected_output_id,
    build_dry_run_id, ScenarioDefinition, scenario_definition_to_dict
)

def test_build_ids_deterministic():
    s_id1 = build_scenario_id("test scenario", "test_type")
    s_id2 = build_scenario_id("test scenario", "test_type")
    assert s_id1 == s_id2
    assert s_id1.startswith("scn_test_type_test_scenario")

    f_id1 = build_fixture_id(s_id1, "my fixture")
    f_id2 = build_fixture_id(s_id1, "my fixture")
    assert f_id1 == f_id2
    assert f_id1.startswith(f"fix_{s_id1}_my_fixture")

def test_scenario_definition_to_dict():
    s = ScenarioDefinition(
        scenario_id="s1", scenario_name="n", scenario_type="t",
        status="st", safety_label="sf", description="d", symbols=[],
        timeframe="1d", modules=[], fixture_paths=[], expected_output_paths=[],
        command_sequence_ids=[], warnings=[]
    )
    d = scenario_definition_to_dict(s)
    assert d["scenario_id"] == "s1"
    assert "safety_label" in d
