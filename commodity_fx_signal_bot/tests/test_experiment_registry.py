import pytest
from pathlib import Path
from experiments.experiment_registry import ExperimentRegistry, build_default_experiment_definitions
from experiments.experiment_models import ExperimentDefinition
from experiments.experiment_config import get_default_experiment_profile

def test_build_default_experiment_definitions():
    profile = get_default_experiment_profile()
    defs = build_default_experiment_definitions(profile)
    assert len(defs) > 0
    assert isinstance(defs[0], ExperimentDefinition)

def test_experiment_registry(tmp_path):
    registry = ExperimentRegistry(tmp_path)
    profile = get_default_experiment_profile()
    defs = build_default_experiment_definitions(profile)

    for ed in defs:
        registry.add_definition(ed)

    df = registry.load_definitions()
    assert len(df) == len(defs)

    e_id = defs[0].experiment_id
    e_dict = registry.get_definition(e_id)
    assert e_dict is not None
    assert e_dict["experiment_name"] == defs[0].experiment_name

    by_type = registry.list_by_type("ablation_experiment")
    assert not by_type.empty

    summary = registry.summarize()
    assert summary["total_definitions"] == len(defs)
    assert "ablation_experiment" in summary["by_type"]
