import pytest
from pathlib import Path
from experiments.research_versioning import (
    build_research_version_id,
    capture_config_snapshot,
    capture_environment_snapshot,
    capture_git_snapshot,
    build_research_version_record,
    research_version_record_to_dataframe
)
from experiments.experiment_models import ExperimentDefinition

class MockSettings:
    def __init__(self):
        self.normal_setting = "value"
        self.telegram_bot_token = "secret123"

class MockDataLake:
    pass

def test_build_research_version_id():
    v_id = build_research_version_id(["meta", "factor"], "1d", ["AAPL"], "2023-01-01T00:00:00Z")
    assert v_id.startswith("rver_")

def test_capture_config_snapshot():
    settings = MockSettings()
    snap = capture_config_snapshot(settings)
    assert snap["normal_setting"] == "value"
    assert snap["telegram_bot_token"] == "***MASKED***"

def test_capture_environment_snapshot():
    env = capture_environment_snapshot()
    assert "python_version" in env
    assert isinstance(env, dict)

def test_capture_git_snapshot(tmp_path):
    git = capture_git_snapshot(tmp_path)
    assert "git_commit" in git

def test_build_research_version_record(tmp_path):
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
        created_at_utc="2023-01-01T00:00:00Z",
        notes="",
        warnings=[]
    )
    dl = MockDataLake()
    settings = MockSettings()

    rec = build_research_version_record(ed, dl, settings, tmp_path)
    assert "version_id" in rec
    assert "config_hash" in rec
    assert "git_snapshot" in rec

    df = research_version_record_to_dataframe(rec)
    assert len(df) == 1
    assert "version_id" in df.columns
