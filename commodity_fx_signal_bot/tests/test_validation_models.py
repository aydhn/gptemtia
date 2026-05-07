from validation.validation_models import (
    build_validation_run_id,
    build_split_id,
    build_parameter_set_id,
    TimeSplit,
    time_split_to_dict,
)

def test_build_validation_run_id_deterministic():
    id1 = build_validation_run_id("AAPL", "1d", "prof1", "param1")
    id2 = build_validation_run_id("AAPL", "1d", "prof1", "param1")
    assert id1 == id2
    assert len(id1) > 0

def test_build_split_id_deterministic():
    id1 = build_split_id("AAPL", "1d", 1)
    id2 = build_split_id("AAPL", "1d", 1)
    assert id1 == id2
    assert len(id1) > 0

def test_build_parameter_set_id_deterministic():
    id1 = build_parameter_set_id({"a": 1, "b": 2})
    id2 = build_parameter_set_id({"b": 2, "a": 1})
    assert id1 == id2
    assert len(id1) > 0

def test_dataclass_to_dict():
    split = TimeSplit("id1", "2020-01-01", "2020-12-31", "2021-01-01", "2021-06-30", 252, 126, 1)
    split_dict = time_split_to_dict(split)
    assert "split_id" in split_dict
    assert split_dict["split_index"] == 1
