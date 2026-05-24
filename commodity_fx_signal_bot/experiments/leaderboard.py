import pandas as pd
from experiments.experiment_config import ExperimentProfile

def calculate_leaderboard_score(row: pd.Series) -> float:
    score = 0.0
    weight = 0.0

    # Priority metrics
    if "quality_adjusted_score" in row and pd.notna(row["quality_adjusted_score"]):
        score += row["quality_adjusted_score"] * 0.4
        weight += 0.4
    if "validation_score" in row and pd.notna(row["validation_score"]):
        score += row["validation_score"] * 0.3
        weight += 0.3
    if "reproducibility_score" in row and pd.notna(row["reproducibility_score"]):
        score += row["reproducibility_score"] * 0.2
        weight += 0.2
    if "consensus_score" in row and pd.notna(row["consensus_score"]):
        score += row["consensus_score"] * 0.1
        weight += 0.1

    return score / weight if weight > 0 else 0.0

def assign_leaderboard_rank_labels(leaderboard_df: pd.DataFrame) -> pd.DataFrame:
    df = leaderboard_df.copy()
    if df.empty or "leaderboard_score" not in df.columns:
        df["rank_label"] = "insufficient_data_run"
        return df

    def get_label(score):
        if pd.isna(score):
            return "insufficient_data_run"
        if score >= 0.8:
            return "leading_research_run"
        elif score >= 0.6:
            return "strong_research_run"
        elif score >= 0.4:
            return "average_research_run"
        else:
            return "weak_research_run"

    df["rank_label"] = df["leaderboard_score"].apply(get_label)
    return df

def build_experiment_leaderboard(metric_df: pd.DataFrame, profile: ExperimentProfile) -> pd.DataFrame:
    if metric_df.empty:
        return pd.DataFrame()

    df = metric_df.copy()
    df["leaderboard_score"] = df.apply(calculate_leaderboard_score, axis=1)

    # Sort
    df = df.sort_values(by="leaderboard_score", ascending=False).reset_index(drop=True)

    # Filter
    df = df[df["leaderboard_score"] >= profile.min_quality_score]

    # Assign ranks
    df["rank"] = df.index + 1
    df = assign_leaderboard_rank_labels(df)

    # Truncate
    if len(df) > profile.max_runs_in_leaderboard:
        df = df.head(profile.max_runs_in_leaderboard)

    return df

def summarize_leaderboard(leaderboard_df: pd.DataFrame) -> dict:
    if leaderboard_df.empty:
        return {"total_runs": 0}

    return {
        "total_runs": len(leaderboard_df),
        "top_score": leaderboard_df["leaderboard_score"].max(),
        "median_score": leaderboard_df["leaderboard_score"].median(),
        "by_rank_label": leaderboard_df["rank_label"].value_counts().to_dict() if "rank_label" in leaderboard_df.columns else {}
    }
