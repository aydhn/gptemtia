import pytest
from experiments.ablation_studies import (
    build_ablation_id,
    build_default_ablation_studies,
    ablation_study_definition_to_dict,
    build_ablation_result_table,
    summarize_ablation_results
)
from experiments.experiment_config import get_default_experiment_profile

def test_build_ablation_id():
    a_id = build_ablation_id("test", ["c1", "c2"])
    assert a_id.startswith("abl_")

def test_build_default_ablation_studies():
    profile = get_default_experiment_profile()
    studies = build_default_ablation_studies(profile)
    assert len(studies) > 0

    d = ablation_study_definition_to_dict(studies[0])
    assert "ablation_id" in d

def test_ablation_result_table():
    baseline = {"quality_adjusted_score": 0.8, "other": "string"}
    abl_map = {
        "abl_1": {"study_name": "remove_ml", "quality_adjusted_score": 0.7}
    }

    df = build_ablation_result_table(baseline, abl_map)
    assert len(df) == 2
    assert "quality_adjusted_score_diff" in df.columns

    # Assert winner is not called live selection
    assert "winner" not in df.columns

    summary = summarize_ablation_results(df)
    assert summary["total_studies"] == 1
    assert "quality_adjusted_score" in summary["metrics_analyzed"]
