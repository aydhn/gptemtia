import pytest
import pandas as pd
from experiments.experiment_report_builder import (
    build_experiment_disclaimer,
    build_hypothesis_registry_markdown_report,
    build_experiment_tracking_markdown_report,
    build_research_version_markdown_report,
    build_ablation_study_markdown_report,
    build_experiment_comparison_markdown_report,
    build_experiment_leaderboard_markdown_report
)

def test_disclaimer():
    d = build_experiment_disclaimer()
    assert "yatırım tavsiyesi değildir" in d

def test_build_reports():
    df = pd.DataFrame([{"col1": "A", "col2": 1}])

    md_hyp = build_hypothesis_registry_markdown_report({"total_hypotheses": 1}, df)
    assert "Hypothesis Registry" in md_hyp

    md_trk = build_experiment_tracking_markdown_report({"notes": "test"}, df)
    assert "Experiment Tracking" in md_trk

    md_ver = build_research_version_markdown_report({"k": "v"}, df)
    assert "Research Version" in md_ver

    md_abl = build_ablation_study_markdown_report({"total_studies": 1}, df)
    assert "Ablation Study" in md_abl

    md_cmp = build_experiment_comparison_markdown_report({"total_comparisons": 1}, df)
    assert "Experiment Comparison" in md_cmp

    md_ldr = build_experiment_leaderboard_markdown_report({"total_runs": 1}, df)
    assert "Experiment Leaderboard" in md_ldr
