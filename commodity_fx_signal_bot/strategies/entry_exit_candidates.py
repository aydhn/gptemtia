from dataclasses import dataclass, asdict
from typing import Any
import hashlib
import json
from .rule_config import StrategyRuleProfile


@dataclass
class EntryExitConditionCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    condition_id: str
    source_strategy_id: str
    source_decision_id: str
    strategy_family: str
    rule_id: str
    rule_group: str
    condition_label: str
    rule_status: str
    directional_bias: str
    candidate_type: str
    match_score: float
    confidence_score: float
    quality_score: float
    readiness_score: float
    conflict_score: float
    passed_rule_filters: bool
    passed_conditions: list[str]
    failed_conditions: list[str]
    required_failures: list[str]
    block_reasons: list[str]
    warnings: list[str]
    notes: str = ""


def build_condition_id(
    symbol: str, timeframe: str, timestamp: str, rule_id: str, source_strategy_id: str
) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{rule_id}_{source_strategy_id}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def entry_exit_candidate_to_dict(
    candidate: EntryExitConditionCandidate,
) -> dict[str, Any]:
    return asdict(candidate)


def infer_rule_status_from_result(
    result: dict,
    profile: StrategyRuleProfile,
    base_confidence: float = 0.5,
    base_quality: float = 0.5,
    base_readiness: float = 0.5,
    conflict: float = 0.0,
) -> str:

    if result.get("required_conditions_failed", 0) > 0:
        return "blocked_candidate"

    match_score = result.get("match_score", 0.0)

    if match_score < profile.min_match_score:
        return "partial_match_candidate"

    if conflict > profile.max_conflict_score:
        return "conflict_blocked"

    if base_confidence < profile.min_confidence:
        return "insufficient_context"

    if base_quality < profile.min_quality_score:
        return "insufficient_quality"

    if base_readiness < profile.min_readiness_score:
        return "wait_candidate"

    if result.get("matched", False):
        return "matched_candidate"

    return "unknown"
