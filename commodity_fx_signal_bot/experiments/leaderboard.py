import pandas as pd

from experiments.experiment_config import ExperimentProfile


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

def build_experiment_leaderboard(
    metric_df: pd.DataFrame, profile: ExperimentProfile
) -> pd.DataFrame:
    if metric_df.empty:
        return pd.DataFrame()

    df = metric_df.copy()

    score = pd.Series(0.0, index=df.index)
    weight = pd.Series(0.0, index=df.index)

    if "quality_adjusted_score" in df.columns:
        mask = df["quality_adjusted_score"].notna()
        score += df["quality_adjusted_score"].fillna(0.0) * mask * 0.4
        weight += mask * 0.4
    if "validation_score" in df.columns:
        mask = df["validation_score"].notna()
        score += df["validation_score"].fillna(0.0) * mask * 0.3
        weight += mask * 0.3
    if "reproducibility_score" in df.columns:
        mask = df["reproducibility_score"].notna()
        score += df["reproducibility_score"].fillna(0.0) * mask * 0.2
        weight += mask * 0.2
    if "consensus_score" in df.columns:
        mask = df["consensus_score"].notna()
        score += df["consensus_score"].fillna(0.0) * mask * 0.1
        weight += mask * 0.1

    df["leaderboard_score"] = (score / weight).fillna(0.0)

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
        "by_rank_label": leaderboard_df["rank_label"].value_counts().to_dict()
        if "rank_label" in leaderboard_df.columns
        else {}
    }
