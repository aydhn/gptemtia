import hashlib
from dataclasses import asdict, dataclass


@dataclass
class StrategyCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    strategy_id: str
    strategy_family: str
    strategy_status: str
    source_decision_id: str
    source_decision_label: str
    directional_bias: str
    candidate_type: str
    decision_score: float
    decision_confidence: float
    decision_quality_score: float
    strategy_selection_score: float
    strategy_fit_score: float
    regime_fit_score: float
    mtf_fit_score: float
    macro_fit_score: float
    asset_profile_fit_score: float
    conflict_penalty: float
    strategy_readiness_score: float
    passed_strategy_filters: bool
    block_reasons: list[str]
    watchlist_reasons: list[str]
    warnings: list[str]
    notes: str = ""


def build_strategy_id(
    symbol: str,
    timeframe: str,
    timestamp: str,
    strategy_family: str,
    source_decision_id: str,
) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{strategy_family}_{source_decision_id}"
    return hashlib.md5(raw.encode()).hexdigest()


def strategy_candidate_to_dict(candidate: StrategyCandidate) -> dict:
    return asdict(candidate)
