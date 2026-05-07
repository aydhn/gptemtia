import pytest
from validation.parameter_grid import (
    build_default_parameter_grid,
    build_profile_parameter_grid,
    validate_parameter_grid,
    generate_parameter_sets,
    summarize_parameter_sets
)

def test_build_default_parameter_grid():
    grid = build_default_parameter_grid()
    assert isinstance(grid, dict)
    assert "backtest_profile" in grid

def test_validate_parameter_grid():
    valid_grid = {"param1": [1, 2], "param2": ["a", "b"]}
    res = validate_parameter_grid(valid_grid)
    assert res["valid"] is True

    invalid_grid_1 = {"param1": []}
    res_1 = validate_parameter_grid(invalid_grid_1)
    assert res_1["valid"] is False

    invalid_grid_2 = {"param1": "not_a_list"}
    res_2 = validate_parameter_grid(invalid_grid_2)
    assert res_2["valid"] is False

def test_generate_parameter_sets():
    grid = {"p1": [1, 2], "p2": ["a", "b", "c"]}
    sets = generate_parameter_sets(grid, max_combinations=10)
    assert len(sets) == 6
    assert sets[0].parameters["p1"] == 1
    assert sets[0].parameters["p2"] == "a"

def test_generate_parameter_sets_max_limit():
    grid = {"p1": [1, 2, 3], "p2": ["a", "b", "c"]}
    sets = generate_parameter_sets(grid, max_combinations=5)
    assert len(sets) == 5

def test_generate_parameter_sets_empty():
    grid = {}
    sets = generate_parameter_sets(grid)
    assert len(sets) == 1
    assert sets[0].parameters == {}

def test_summarize_parameter_sets():
    grid = {"p1": [1, 2]}
    sets = generate_parameter_sets(grid)
    summary = summarize_parameter_sets(sets)
    assert summary["count"] == 2
    assert "p1" in summary["keys"]
