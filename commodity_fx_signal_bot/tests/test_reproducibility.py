import pytest
from experiments.reproducibility import (
    build_reproducibility_manifest,
    validate_reproducibility_manifest,
    calculate_reproducibility_score,
    build_rerun_candidate_command,
    reproducibility_manifest_to_dataframe
)
from experiments.experiment_models import ExperimentDefinition, ExperimentRunManifest

def test_reproducibility_manifest():
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
    run = ExperimentRunManifest(
        run_id="run_1",
        experiment_id="exp_1",
        experiment_name="test",
        experiment_type="candidate_experiment",
        status="completed",
        profile_name="test",
        timeframe="1d",
        symbols=["AAPL"],
        started_at_utc="utc",
        finished_at_utc="utc",
        duration_seconds=10.0,
        produced_artifacts=[],
        metrics={},
        warnings=[]
    )
    version = {
        "version_id": "v1",
        "config_snapshot": {},
        "environment_snapshot": {},
        "git_snapshot": {"git_commit": "abc"}
    }
    art_man = {
        "artifacts": [{"exists": True}],
        "missing_required": []
    }

    man = build_reproducibility_manifest(ed, run, version, art_man)
    assert man["has_config_snapshot"] is True

    val = validate_reproducibility_manifest(man)
    assert val["valid"] is True

    score = calculate_reproducibility_score(man)
    assert 0.0 <= score <= 1.0
    assert score > 0.9  # Should be 1.0 based on perfect inputs

    cmd = build_rerun_candidate_command(man)
    assert "broker" not in cmd
    assert "live" not in cmd
    assert "run_experiment_tracking_report" in cmd

    df = reproducibility_manifest_to_dataframe(man)
    assert len(df) == 1
    assert "reproducibility_score" in df.columns
