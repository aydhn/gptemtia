import pytest
from pathlib import Path
from experiments.experiment_runner import ExperimentRunner
from experiments.experiment_models import ExperimentDefinition
from experiments.experiment_config import get_default_experiment_profile

class MockDataLake:
    pass

class MockSettings:
    pass

def test_experiment_runner(tmp_path):
    profile = get_default_experiment_profile()
    runner = ExperimentRunner(MockDataLake(), MockSettings(), profile, tmp_path)

    ed = ExperimentDefinition(
        experiment_id="exp_1",
        experiment_name="test",
        experiment_type="candidate_experiment",
        hypothesis_id=None,
        profile_name="test",
        timeframe="1d",
        symbols=["AAPL"],
        module_scope=["meta"],
        parameters={},
        baseline_experiment_id=None,
        created_at_utc="utc",
        notes="",
        warnings=[]
    )

    # Test dry run
    dry_manifest, _ = runner.run_experiment(ed, dry_run=True)
    assert dry_manifest.status == "experiment_dry_run"
    assert "live trade" not in str(dry_manifest.__dict__).lower()

    # Test collect
    col_manifest, _ = runner.collect_existing_outputs_as_run(ed)
    assert col_manifest.status == "experiment_completed"
