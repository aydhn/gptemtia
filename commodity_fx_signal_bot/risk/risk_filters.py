import pandas as pd
from typing import Tuple, List, Dict, Optional
from risk.risk_config import RiskPrecheckProfile


def should_block_for_risk(
    evaluation: Dict, profile: RiskPrecheckProfile
) -> Tuple[bool, List[str]]:
    reasons = list(evaluation.get("blocking_reasons", []))
    if evaluation.get("total_pretrade_risk_score", 0) > profile.max_total_pretrade_risk:
        reasons.append(
            f"Total risk {evaluation.get('total_pretrade_risk_score')} > max {profile.max_total_pretrade_risk}"
        )
    if evaluation.get("risk_readiness_score", 1.0) < profile.min_readiness_score:
        reasons.append(
            f"Readiness {evaluation.get('risk_readiness_score')} < min {profile.min_readiness_score}"
        )
    return len(reasons) > 0, reasons


def should_watchlist_for_risk(
    evaluation: Dict, profile: RiskPrecheckProfile
) -> Tuple[bool, List[str]]:
    reasons = []
    total_risk = evaluation.get("total_pretrade_risk_score", 0)
    if profile.allow_watchlist_when_borderline:
        if (
            profile.max_total_pretrade_risk - 0.1
            <= total_risk
            <= profile.max_total_pretrade_risk
        ):
            reasons.append(f"Total risk {total_risk} is borderline high")
    return len(reasons) > 0, reasons


def infer_risk_candidate_label(evaluation: Dict, profile: RiskPrecheckProfile) -> str:
    block, _ = should_block_for_risk(evaluation, profile)
    if block:
        reasons = " ".join(evaluation.get("blocking_reasons", [])).lower()
        if profile.block_on_invalid_data_quality and "data quality grade" in reasons:
            return "invalid_data_risk_candidate"
        if profile.block_on_extreme_volatility and (
            "atr" in reasons or "range shock" in reasons
        ):
            return "extreme_volatility_risk_candidate"
        if profile.block_on_high_conflict and "conflict" in reasons:
            return "high_conflict_risk_candidate"
        return "risk_rejection_candidate"
    watchlist, _ = should_watchlist_for_risk(evaluation, profile)
    if watchlist:
        return "risk_watchlist_candidate"
    if evaluation.get("warnings"):
        return "risk_warning_candidate"
    return "risk_approval_candidate"


def filter_risk_candidates_by_readiness(
    df: pd.DataFrame, min_readiness: float
) -> pd.DataFrame:
    return (
        df[df["risk_readiness_score"] >= min_readiness]
        if not df.empty and "risk_readiness_score" in df.columns
        else df
    )


def filter_risk_candidates_by_total_risk(
    df: pd.DataFrame, max_total_risk: float
) -> pd.DataFrame:
    return (
        df[df["total_pretrade_risk_score"] <= max_total_risk]
        if not df.empty and "total_pretrade_risk_score" in df.columns
        else df
    )


def rank_risk_candidates(df: pd.DataFrame, top_n: Optional[int] = None) -> pd.DataFrame:
    if df.empty or "risk_readiness_score" not in df.columns:
        return df
    ranked = df.sort_values(by="risk_readiness_score", ascending=False)
    return ranked.head(top_n) if top_n is not None else ranked
