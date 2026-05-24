import pytest
from experiments.experiment_models import (
    ResearchHypothesis,
    ExperimentDefinition,
    ExperimentRunManifest,
    ExperimentComparison,
    build_hypothesis_id,
    build_experiment_id,
    build_experiment_run_id,
    build_experiment_comparison_id,
    research_hypothesis_to_dict,
    experiment_definition_to_dict,
    experiment_run_manifest_to_dict,
    experiment_comparison_to_dict,
    sanitize_experiment_name
)

def test_build_hypothesis_id():
    h_id = build_hypothesis_id("Trend test", "1d", "meta_research")
    assert h_id.startswith("hyp_")

    h_id2 = build_hypothesis_id("Trend test", "1d", "meta_research")
    assert h_id == h_id2

def test_build_experiment_id():
    e_id = build_experiment_id("Trend Test!!", "candidate_experiment", "1d")
    assert e_id.startswith("exp_trend_test__")

def test_build_experiment_run_id():
    r_id = build_experiment_run_id("exp_123", "2023-01-01T00:00:00Z")
    assert r_id.startswith("run_")

def test_sanitize_experiment_name():
    sanitized = sanitize_experiment_name("Test-Name 123!")
    assert sanitized == "test_name_123_"

def test_to_dict_methods():
    h = ResearchHypothesis(
        hypothesis_id="h1",
        title="t1",
        description="d",
        hypothesis_status="hypothesis_proposed",
        target_module="meta",
        target_symbols=["A"],
        timeframe="1d",
        expected_effect="none",
        success_metrics=["a"],
        created_at_utc="utc",
        updated_at_utc=None,
        notes="",
        warnings=[]
    )
    d = research_hypothesis_to_dict(h)
    assert d["hypothesis_id"] == "h1"
    assert d["target_symbols"] == ["A"]
