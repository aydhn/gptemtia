from dataclasses import dataclass, asdict
import hashlib


@dataclass
class SignalCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    candidate_id: str
    candidate_type: str
    directional_bias: str
    primary_event_group: str
    active_events: list[str]
    event_count: int
    event_strength_score: float
    category_confluence_score: float
    trend_context_score: float
    regime_context_score: float
    mtf_context_score: float
    macro_context_score: float
    asset_profile_context_score: float
    data_quality_score: float
    conflict_score: float
    risk_precheck_score: float
    candidate_score: float
    confidence_score: float
    quality_score: float
    passed_pre_filters: bool
    warnings: list[str]
    notes: str = ""


def build_candidate_id(
    symbol: str,
    timeframe: str,
    timestamp: str,
    candidate_type: str,
    directional_bias: str,
) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{candidate_type}_{directional_bias}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()[:16]


def signal_candidate_to_dict(candidate: SignalCandidate) -> dict:
    return asdict(candidate)
