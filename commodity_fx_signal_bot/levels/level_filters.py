import pandas as pd
from levels.level_config import LevelProfile


def should_block_level_candidate(
    sizing_row: pd.Series, level_eval: dict, profile: LevelProfile
) -> tuple[bool, list[str]]:
    reasons = []

    if profile.block_on_sizing_rejection:
        sizing_label = sizing_row.get("sizing_label", "")
        if sizing_label == "sizing_rejected_candidate":
            reasons.append("sizing_rejection")

    rr = level_eval.get("reward_risk")
    if rr is not None and rr < profile.min_reward_risk:
        reasons.append("insufficient_reward_risk")

    stop_dist_pct = level_eval.get("stop_distance_pct")
    if stop_dist_pct is not None and stop_dist_pct > profile.max_stop_distance_pct:
        reasons.append("excessive_stop_distance")

    return len(reasons) > 0, reasons


def should_watchlist_level_candidate(
    sizing_row: pd.Series, level_eval: dict, profile: LevelProfile
) -> tuple[bool, list[str]]:
    reasons = []

    if profile.allow_watchlist_when_borderline:
        sizing_readiness = sizing_row.get("sizing_readiness_score", 0.0)
        if sizing_readiness < profile.min_sizing_readiness_score:
            reasons.append("low_sizing_readiness")

    return len(reasons) > 0, reasons


def infer_level_candidate_label(
    sizing_row: pd.Series, level_eval: dict, profile: LevelProfile
) -> str:
    is_blocked, block_reasons = should_block_level_candidate(
        sizing_row, level_eval, profile
    )
    if is_blocked:
        if "insufficient_reward_risk" in block_reasons:
            return "insufficient_reward_risk_candidate"
        if "excessive_stop_distance" in block_reasons:
            return "excessive_stop_distance_candidate"
        return "level_rejected_candidate"

    if "warnings" in level_eval and level_eval["warnings"]:
        if any("price" in w.lower() for w in level_eval["warnings"]):
            return "invalid_price_level_candidate"

    is_watchlist, _ = should_watchlist_level_candidate(sizing_row, level_eval, profile)
    if is_watchlist:
        return "level_watchlist_candidate"

    # Valid and not blocked/watchlist
    bias = sizing_row.get("directional_bias", "")
    if bias in ["neutral", "no_trade_candidate"]:
        return "level_zero_candidate"

    return "level_approved_candidate"


def filter_level_candidates_by_readiness(
    df: pd.DataFrame, min_readiness: float
) -> pd.DataFrame:
    if "stop_target_readiness_score" not in df.columns:
        return df
    return df[df["stop_target_readiness_score"] >= min_readiness].copy()


def filter_level_candidates_by_reward_risk(
    df: pd.DataFrame, min_reward_risk: float
) -> pd.DataFrame:
    if "reward_risk" not in df.columns:
        return df
    return df[df["reward_risk"] >= min_reward_risk].copy()


def rank_level_candidates(df: pd.DataFrame, top_n: int | None = None) -> pd.DataFrame:
    if (
        "reward_risk" not in df.columns
        or "stop_target_readiness_score" not in df.columns
    ):
        return df

    df_sorted = df.sort_values(
        by=["stop_target_readiness_score", "reward_risk"], ascending=[False, False]
    )
    if top_n is not None:
        return df_sorted.head(top_n).copy()
    return df_sorted.copy()
