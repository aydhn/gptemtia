from dataclasses import dataclass, asdict
import hashlib
from typing import List, Dict


@dataclass
class DecisionCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    decision_id: str
    decision_label: str
    directional_bias: str
    candidate_type: str
    source_candidate_count: int
    top_source_candidate_score: float
    signal_score_component: float
    directional_consensus_component: float
    regime_confirmation_component: float
    mtf_confirmation_component: float
    macro_context_component: float
    asset_profile_fit_component: float
    quality_component: float
    risk_precheck_component: float
    conflict_score: float
    decision_score: float
    decision_confidence: float
    decision_quality_score: float
    strategy_readiness_score: float
    passed_decision_filters: bool
    no_trade_reasons: List[str]
    conflict_reasons: List[str]
    warnings: List[str]
    notes: str = ""


def decision_candidate_to_dict(candidate: DecisionCandidate) -> Dict:
    return asdict(candidate)


def build_decision_id(
    symbol: str,
    timeframe: str,
    timestamp: str,
    decision_label: str,
    candidate_type: str,
) -> str:
    seed = f"{symbol}_{timeframe}_{timestamp}_{decision_label}_{candidate_type}"
    return hashlib.md5(seed.encode()).hexdigest()
