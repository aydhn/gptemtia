from scenario_regression.regression_models import (
    build_regression_id, build_golden_output_id, build_snapshot_id, build_replay_id,
    ScenarioRegressionDefinition, scenario_regression_definition_to_dict
)

def test_id_builders():
    assert len(build_regression_id("scen1", "type1")) > 0
    assert len(build_golden_output_id("scen1", "out1")) > 0
    assert len(build_snapshot_id("scen1", "snap1")) > 0
    assert len(build_replay_id("scen1", "2024")) > 0

def test_dataclass_to_dict():
    d = ScenarioRegressionDefinition("r1", "s1", "t1", "n1", "d1", ["out1"], ["g1"], ["snp1"], True, ["w1"])
    dic = scenario_regression_definition_to_dict(d)
    assert dic["regression_id"] == "r1"
    assert "out1" in dic["expected_outputs"]
