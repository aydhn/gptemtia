from typing import Tuple, List
from .decision_config import DecisionProfile


def should_mark_neutral(
    directional_consensus_score: float,
    bullish_bearish_balance: float,
    neutral_zone_threshold: float = 0.15,
) -> bool:
    if directional_consensus_score < 0.5:
        return True
    if bullish_bearish_balance < neutral_zone_threshold:
        return True
    return False


def should_mark_no_trade(
    quality_score: float,
    conflict_score: float,
    strategy_readiness_score: float,
    profile: DecisionProfile,
) -> Tuple[bool, List[str]]:
    reasons = []

    if quality_score < profile.min_quality:
        reasons.append(
            f"Quality score {quality_score:.2f} below minimum {profile.min_quality}"
        )

    if conflict_score > profile.max_conflict:
        reasons.append(
            f"Conflict score {conflict_score:.2f} above maximum {profile.max_conflict}"
        )

    if strategy_readiness_score < profile.min_strategy_readiness:
        reasons.append(
            f"Readiness score {strategy_readiness_score:.2f} below minimum {profile.min_strategy_readiness}"
        )

    return len(reasons) > 0, reasons


def should_mark_watchlist(
    decision_score: float,
    quality_score: float,
    conflict_score: float,
    profile: DecisionProfile,
) -> Tuple[bool, List[str]]:
    reasons = []

    if decision_score < profile.min_signal_score:
        reasons.append("Decision score too low for trading, adding to watchlist")

    return len(reasons) > 0, reasons


def build_no_trade_reasons(
    components: dict[str, float],
    conflict_summary: dict,
    profile: DecisionProfile,
) -> List[str]:
    reasons = []

    if conflict_summary.get("blocking_conflict"):
        reasons.append("Blocking conflict detected")
        reasons.extend(conflict_summary.get("conflict_reasons", []))

    # Check components against profile if needed

    return list(set(reasons))
