import pandas as pd
from typing import Tuple, List, Dict, Any, Optional
from sizing.sizing_config import SizingProfile
from sizing.sizing_models import safe_positive_float


def should_block_sizing(
    risk_row: pd.Series, sizing_eval: Dict[str, Any], profile: SizingProfile
) -> Tuple[bool, List[str]]:
    """Determines if sizing should be blocked for a candidate."""
    reasons = []

    # Check risk precheck label if available
    risk_label = risk_row.get("risk_label", "")
    if profile.block_on_risk_rejection and risk_label == "risk_rejected_candidate":
        reasons.append("Risk precheck returned rejection.")

    # Check risk readiness
    readiness = safe_positive_float(
        sizing_eval.get(
            "risk_readiness_score", risk_row.get("risk_readiness_score", 0.0)
        )
    )
    if readiness is not None and readiness < profile.min_risk_readiness_score:
        reasons.append(
            f"Risk readiness score ({readiness}) is below minimum ({profile.min_risk_readiness_score})."
        )

    # Check total pretrade risk
    pretrade_risk = safe_positive_float(
        sizing_eval.get(
            "total_pretrade_risk_score", risk_row.get("total_pretrade_risk_score", 0.0)
        )
    )
    if pretrade_risk is not None and pretrade_risk > profile.max_total_pretrade_risk:
        reasons.append(
            f"Total pretrade risk ({pretrade_risk}) is above maximum ({profile.max_total_pretrade_risk})."
        )

    # Check budget constraints
    capped_amount = sizing_eval.get(
        "capped_theoretical_risk_amount",
        sizing_eval.get("theoretical_risk_amount", 1.0),
    )
    if capped_amount <= 0:
        reasons.append("Capped theoretical risk amount is zero or negative.")

    # Check exposure constraints
    exposure_eval = sizing_eval.get("exposure_eval", {})
    if not exposure_eval.get("symbol_limit_passed", True):
        reasons.append("Symbol exposure limit exceeded.")
    if not exposure_eval.get("asset_class_limit_passed", True):
        reasons.append("Asset class exposure limit exceeded.")

    # Check theoretical notional
    notional = sizing_eval.get("adjusted_theoretical_notional")
    if notional is None or notional <= 0:
        reasons.append("Adjusted theoretical notional is zero, negative, or invalid.")

    return len(reasons) > 0, reasons


def should_watchlist_sizing(
    risk_row: pd.Series, sizing_eval: Dict[str, Any], profile: SizingProfile
) -> Tuple[bool, List[str]]:
    """Determines if a sizing candidate should be placed on a watchlist (borderline conditions)."""
    if not profile.allow_watchlist_for_borderline:
        return False, []

    reasons = []

    risk_label = risk_row.get("risk_label", "")
    if risk_label == "risk_watchlist_candidate":
        reasons.append("Source risk candidate was on watchlist.")

    # Check readiness borderline
    readiness = safe_positive_float(
        sizing_eval.get(
            "risk_readiness_score", risk_row.get("risk_readiness_score", 0.0)
        )
    )
    if readiness is not None and profile.min_risk_readiness_score <= readiness < (
        profile.min_risk_readiness_score + 0.1
    ):
        reasons.append("Risk readiness is borderline.")

    # Check pretrade risk borderline
    pretrade_risk = safe_positive_float(
        sizing_eval.get(
            "total_pretrade_risk_score", risk_row.get("total_pretrade_risk_score", 0.0)
        )
    )
    if (
        pretrade_risk is not None
        and (profile.max_total_pretrade_risk - 0.1)
        < pretrade_risk
        <= profile.max_total_pretrade_risk
    ):
        reasons.append("Total pretrade risk is borderline.")

    return len(reasons) > 0, reasons


def infer_sizing_candidate_label(
    risk_row: pd.Series, sizing_eval: Dict[str, Any], profile: SizingProfile
) -> str:
    """Infers the final sizing candidate label based on blocking and watchlist logic."""
    blocked, _ = should_block_sizing(risk_row, sizing_eval, profile)
    if blocked:
        return "sizing_rejected_candidate"

    watchlist, _ = should_watchlist_sizing(risk_row, sizing_eval, profile)
    if watchlist:
        return "sizing_watchlist_candidate"

    return "sizing_approved_candidate"


def filter_sizing_candidates_by_readiness(
    df: pd.DataFrame, min_readiness: float
) -> pd.DataFrame:
    """Filters a sizing pool dataframe by minimum readiness score."""
    if df.empty or "sizing_readiness_score" not in df.columns:
        return df
    return df[df["sizing_readiness_score"] >= min_readiness].copy()


def filter_sizing_candidates_by_label(df: pd.DataFrame, label: str) -> pd.DataFrame:
    """Filters a sizing pool dataframe by sizing label."""
    if df.empty or "sizing_label" not in df.columns:
        return df
    return df[df["sizing_label"] == label].copy()


def rank_sizing_candidates(
    df: pd.DataFrame, top_n: Optional[int] = None
) -> pd.DataFrame:
    """Ranks sizing candidates by their sizing readiness score."""
    if df.empty or "sizing_readiness_score" not in df.columns:
        return df

    ranked = df.sort_values(by="sizing_readiness_score", ascending=False)
    if top_n is not None:
        ranked = ranked.head(top_n)
    return ranked.copy()
