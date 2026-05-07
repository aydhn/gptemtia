import pandas as pd
import logging

logger = logging.getLogger(__name__)


def filter_backtest_eligible_level_candidates(level_df: pd.DataFrame) -> pd.DataFrame:
    if level_df.empty:
        return pd.DataFrame()

    df = level_df.copy()

    # Needs passed_level_filters
    if "passed_level_filters" in df.columns:
        df = df[df["passed_level_filters"] == True]

    # Valid stop/target
    if (
        "theoretical_stop_level" in df.columns
        and "theoretical_target_level" in df.columns
    ):
        df = df[
            df["theoretical_stop_level"].notna()
            & df["theoretical_target_level"].notna()
        ]

    # Bias
    if "directional_bias" in df.columns:
        df = df[
            df["directional_bias"].isin(["long_bias_candidate", "short_bias_candidate"])
        ]

    return df


def infer_candidate_direction(row: pd.Series) -> str:
    bias = row.get("directional_bias", "")
    if bias == "long_bias_candidate":
        return "long"
    elif bias == "short_bias_candidate":
        return "short"
    return "unknown"


def infer_candidate_entry_context(row: pd.Series) -> dict:
    return {
        "level_id": row.get("candidate_id", ""),
        "bias": row.get("directional_bias", ""),
        "stop": row.get("theoretical_stop_level", None),
        "target": row.get("theoretical_target_level", None),
    }


def build_candidate_events(level_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    eligible = filter_backtest_eligible_level_candidates(level_df)
    summary = {
        "input_count": len(level_df),
        "eligible_count": len(eligible),
        "rejected_count": len(level_df) - len(eligible),
    }
    return eligible, summary
