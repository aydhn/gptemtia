import pytest
from pathlib import Path
from experiments.experiment_pipeline import ExperimentTrackingPipeline
from experiments.experiment_config import get_default_experiment_profile

class MockDataLake:
    pass

class MockSettings:
    pass

def test_experiment_pipeline(tmp_path):
    profile = get_default_experiment_profile()
    pipeline = ExperimentTrackingPipeline(MockDataLake(), MockSettings(), tmp_path, profile)

    df_hyp, sum_hyp = pipeline.build_hypothesis_registry_report(save=False)
    assert not df_hyp.empty

    run_man, run_sum = pipeline.track_existing_research_run(
        experiment_name="test_exp",
        module_scope=["meta_research"],
        symbols=["AAPL"],
        save=False
    )
    assert run_man["status"] == "experiment_completed"

    df_ver, sum_ver = pipeline.build_research_version_report(save=False)
    assert not df_ver.empty

    df_abl, sum_abl = pipeline.build_ablation_study_report(save=False)
    assert not df_abl.empty

    df_cmp, sum_cmp = pipeline.build_experiment_comparison_report(save=False)
    assert not df_cmp.empty

    df_ld, sum_ld = pipeline.build_experiment_leaderboard(save=False)
    assert not df_ld.empty
