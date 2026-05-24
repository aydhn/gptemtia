import pytest
import pandas as pd
from experiments.leaderboard import (
    calculate_leaderboard_score,
    assign_leaderboard_rank_labels,
    build_experiment_leaderboard,
    summarize_leaderboard
)
from experiments.experiment_config import get_default_experiment_profile

def test_calculate_leaderboard_score():
    row = pd.Series({
        "quality_adjusted_score": 0.8,
        "validation_score": 0.9,
        "reproducibility_score": 1.0,
        "consensus_score": 0.7
    })
    score = calculate_leaderboard_score(row)
    assert 0.0 <= score <= 1.0
    assert score > 0.8 # It's a weighted average

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
