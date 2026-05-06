import hashlib
import pandas as pd
from dataclasses import dataclass, asdict


@dataclass
class RiskPrecheckCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    risk_id: str
    source_rule_condition_id: str
    source_strategy_id: str
    strategy_family: str
    condition_label: str
    directional_bias: str
    risk_label: str
    risk_severity: str
    volatility_risk_score: float
    gap_risk_score: float
    liquidity_risk_score: float
    data_quality_risk_score: float
    regime_risk_score: float
    mtf_risk_score: float
    macro_risk_score: float
    asset_profile_risk_score: float
    conflict_risk_score: float
    total_pretrade_risk_score: float
    risk_readiness_score: float
    passed_risk_precheck: bool
    blocking_reasons: list[str]
    watchlist_reasons: list[str]
    warnings: list[str]
    notes: str = ""


def build_risk_id(
    symbol: str, timeframe: str, timestamp: str, source_rule_condition_id: str
) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{source_rule_condition_id}"
    return hashlib.md5(raw.encode()).hexdigest()


def risk_candidate_to_dict(candidate: RiskPrecheckCandidate) -> dict:
    return asdict(candidate)


def build_risk_candidate_from_evaluation(
    rule_row: pd.Series,
    evaluation: dict,
    symbol: str,
    timeframe: str,
    risk_label: str,
    risk_severity: str,
) -> RiskPrecheckCandidate:
    timestamp = str(
        rule_row.name
        if isinstance(rule_row.name, (pd.Timestamp, str))
        else rule_row.get("timestamp", "")
    )
    source_rule_condition_id = str(
        rule_row.get("rule_condition_id", rule_row.get("decision_id", ""))
    )
    comp = evaluation.get("component_dict", {})
    return RiskPrecheckCandidate(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=timestamp,
        risk_id=build_risk_id(symbol, timeframe, timestamp, source_rule_condition_id),
        source_rule_condition_id=source_rule_condition_id,
        source_strategy_id=str(rule_row.get("strategy_id", "")),
        strategy_family=str(rule_row.get("strategy_family", "")),
        condition_label=str(rule_row.get("condition_label", "")),
        directional_bias=str(rule_row.get("directional_bias", "")),
        risk_label=risk_label,
        risk_severity=risk_severity,
        volatility_risk_score=comp.get("volatility", 0.0),
        gap_risk_score=comp.get("gap", 0.0),
        liquidity_risk_score=comp.get("liquidity", 0.0),
        data_quality_risk_score=comp.get("data_quality", 0.0),
        regime_risk_score=comp.get("regime", 0.0),
        mtf_risk_score=comp.get("mtf", 0.0),
        macro_risk_score=comp.get("macro", 0.0),
        asset_profile_risk_score=comp.get("asset_profile", 0.0),
        conflict_risk_score=comp.get("conflict", 0.0),
        total_pretrade_risk_score=evaluation.get("total_pretrade_risk_score", 0.0),
        risk_readiness_score=evaluation.get("risk_readiness_score", 0.0),
        passed_risk_precheck=evaluation.get("passed_risk_precheck", False),
        blocking_reasons=evaluation.get("blocking_reasons", []),
        watchlist_reasons=evaluation.get("watchlist_reasons", []),
        warnings=evaluation.get("warnings", []),
        notes="",
    )
