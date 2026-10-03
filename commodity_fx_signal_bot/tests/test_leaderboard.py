import pytest
import pandas as pd
from experiments.leaderboard import (
    assign_leaderboard_rank_labels,
    build_experiment_leaderboard,
    summarize_leaderboard
)
from experiments.experiment_config import get_default_experiment_profile

def test_assign_leaderboard_rank_labels():
    df = pd.DataFrame([{"leaderboard_score": 0.9}, {"leaderboard_score": 0.5}])
    labeled = assign_leaderboard_rank_labels(df)
    assert labeled.iloc[0]["rank_label"] == "leading_research_run"
    assert labeled.iloc[1]["rank_label"] == "average_research_run"
    assert "leading_research_run" not in ["buy", "sell", "deploy"]

def test_build_experiment_leaderboard():
    df = pd.DataFrame([
        {"run_id": "r1", "quality_adjusted_score": 0.9},
        {"run_id": "r2", "quality_adjusted_score": 0.1}
    ])
    profile = get_default_experiment_profile()

    leaderboard = build_experiment_leaderboard(df, profile)
    assert len(leaderboard) == 1 # 0.1 < min_quality_score (0.4)
    assert "rank" in leaderboard.columns
    assert "rank_label" in leaderboard.columns

def test_summarize_leaderboard():
    df = pd.DataFrame([{"leaderboard_score": 0.8, "rank_label": "leading_research_run"}])
    summary = summarize_leaderboard(df)
    assert summary["total_runs"] == 1
    assert "leading_research_run" in summary["by_rank_label"]

def test_build_experiment_leaderboard_vectorized():
    df = pd.DataFrame([
        {"run_id": "r1", "quality_adjusted_score": 0.8, "validation_score": 0.9, "reproducibility_score": 1.0, "consensus_score": 0.7},
        {"run_id": "r2", "quality_adjusted_score": 0.5, "validation_score": 0.6, "reproducibility_score": 0.7, "consensus_score": 0.8}
    ])
    profile = get_default_experiment_profile()
    # profile is frozen, but min_quality_score is default 0.0 usually, wait, min_quality_score is 0.4. Let's just adjust the second run's score to be > 0.4

    leaderboard = build_experiment_leaderboard(df, profile)

    # 0.8*0.4 + 0.9*0.3 + 1.0*0.2 + 0.7*0.1 = 0.32 + 0.27 + 0.20 + 0.07 = 0.86
    # 0.1*0.4 + 0.2*0.3 + 0.3*0.2 + 0.4*0.1 = 0.04 + 0.06 + 0.06 + 0.04 = 0.20

    assert len(leaderboard) == 2
    assert abs(leaderboard[leaderboard["run_id"] == "r1"]["leaderboard_score"].iloc[0] - 0.86) < 1e-6
    # 0.5*0.4 + 0.6*0.3 + 0.7*0.2 + 0.8*0.1 = 0.2 + 0.18 + 0.14 + 0.08 = 0.60
    assert abs(leaderboard[leaderboard["run_id"] == "r2"]["leaderboard_score"].iloc[0] - 0.60) < 1e-6
