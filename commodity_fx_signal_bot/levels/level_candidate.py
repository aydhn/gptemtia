from dataclasses import dataclass
import hashlib


@dataclass
class StopTargetLevelCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    level_id: str
    source_sizing_id: str
    source_risk_id: str
    source_rule_condition_id: str
    strategy_family: str
    condition_label: str
    directional_bias: str
    asset_class: str
    level_label: str
    level_method: str
    level_severity: str
    latest_close: float | None
    atr_value: float | None
    atr_pct: float | None
    theoretical_stop_level: float | None
    theoretical_target_level: float | None
    theoretical_invalidation_level: float | None
    stop_distance: float | None
    target_distance: float | None
    stop_distance_pct: float | None
    target_distance_pct: float | None
    reward_risk: float | None
    selected_rr_multiplier: float | None
    volatility_adjustment_factor: float
    sizing_readiness_score: float
    total_pretrade_risk_score: float
    stop_target_readiness_score: float
    stop_target_quality_score: float
    passed_level_filters: bool
    block_reasons: list[str]
    watchlist_reasons: list[str]
    warnings: list[str]
    notes: str = ""


def build_level_id(
    symbol: str, timeframe: str, timestamp: str, source_sizing_id: str
) -> str:
    raw = f"{symbol}_{timeframe}_{timestamp}_{source_sizing_id}"
    return "LVL_" + hashlib.sha256(raw.encode()).hexdigest()[:12]


def level_candidate_to_dict(candidate: StopTargetLevelCandidate) -> dict:
    return {
        "symbol": candidate.symbol,
        "timeframe": candidate.timeframe,
        "timestamp": candidate.timestamp,
        "level_id": candidate.level_id,
        "source_sizing_id": candidate.source_sizing_id,
        "source_risk_id": candidate.source_risk_id,
        "source_rule_condition_id": candidate.source_rule_condition_id,
        "strategy_family": candidate.strategy_family,
        "condition_label": candidate.condition_label,
        "directional_bias": candidate.directional_bias,
        "asset_class": candidate.asset_class,
        "level_label": candidate.level_label,
        "level_method": candidate.level_method,
        "level_severity": candidate.level_severity,
        "latest_close": candidate.latest_close,
        "atr_value": candidate.atr_value,
        "atr_pct": candidate.atr_pct,
        "theoretical_stop_level": candidate.theoretical_stop_level,
        "theoretical_target_level": candidate.theoretical_target_level,
        "theoretical_invalidation_level": candidate.theoretical_invalidation_level,
        "stop_distance": candidate.stop_distance,
        "target_distance": candidate.target_distance,
        "stop_distance_pct": candidate.stop_distance_pct,
        "target_distance_pct": candidate.target_distance_pct,
        "reward_risk": candidate.reward_risk,
        "selected_rr_multiplier": candidate.selected_rr_multiplier,
        "volatility_adjustment_factor": candidate.volatility_adjustment_factor,
        "sizing_readiness_score": candidate.sizing_readiness_score,
        "total_pretrade_risk_score": candidate.total_pretrade_risk_score,
        "stop_target_readiness_score": candidate.stop_target_readiness_score,
        "stop_target_quality_score": candidate.stop_target_quality_score,
        "passed_level_filters": candidate.passed_level_filters,
        "block_reasons": ",".join(candidate.block_reasons),
        "watchlist_reasons": ",".join(candidate.watchlist_reasons),
        "warnings": ",".join(candidate.warnings),
        "notes": candidate.notes,
    }


def build_level_candidate_from_evaluation(
    sizing_row, evaluation: dict, symbol: str, timeframe: str
) -> StopTargetLevelCandidate:
    # A dummy logic to assemble dataclass.
    # Real pipeline will extract real values.

    timestamp = str(sizing_row.name) if hasattr(sizing_row, "name") else ""
    source_sizing_id = sizing_row.get("sizing_id", "")
    level_id = build_level_id(symbol, timeframe, timestamp, source_sizing_id)

    return StopTargetLevelCandidate(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=timestamp,
        level_id=level_id,
        source_sizing_id=source_sizing_id,
        source_risk_id=sizing_row.get("source_risk_id", ""),
        source_rule_condition_id=sizing_row.get("source_rule_condition_id", ""),
        strategy_family=sizing_row.get("strategy_family", ""),
        condition_label=sizing_row.get("condition_label", ""),
        directional_bias=sizing_row.get("directional_bias", ""),
        asset_class=sizing_row.get("asset_class", ""),
        level_label=evaluation.get("level_label", "unknown_level_candidate"),
        level_method=evaluation.get("level_method", "unknown_level_method"),
        level_severity=evaluation.get("level_severity", "unknown"),
        latest_close=evaluation.get("latest_close"),
        atr_value=evaluation.get("atr_value"),
        atr_pct=evaluation.get("atr_pct"),
        theoretical_stop_level=evaluation.get("theoretical_stop_level"),
        theoretical_target_level=evaluation.get("theoretical_target_level"),
        theoretical_invalidation_level=evaluation.get("theoretical_invalidation_level"),
        stop_distance=evaluation.get("stop_distance"),
        target_distance=evaluation.get("target_distance"),
        stop_distance_pct=evaluation.get("stop_distance_pct"),
        target_distance_pct=evaluation.get("target_distance_pct"),
        reward_risk=evaluation.get("reward_risk"),
        selected_rr_multiplier=evaluation.get("selected_rr_multiplier"),
        volatility_adjustment_factor=evaluation.get(
            "volatility_adjustment_factor", 1.0
        ),
        sizing_readiness_score=sizing_row.get("sizing_readiness_score", 0.0),
        total_pretrade_risk_score=sizing_row.get("total_pretrade_risk_score", 0.0),
        stop_target_readiness_score=evaluation.get("stop_target_readiness_score", 0.0),
        stop_target_quality_score=evaluation.get("stop_target_quality_score", 0.0),
        passed_level_filters=evaluation.get("passed_level_filters", False),
        block_reasons=evaluation.get("block_reasons", []),
        watchlist_reasons=evaluation.get("watchlist_reasons", []),
        warnings=evaluation.get("warnings", []),
        notes=evaluation.get("notes", ""),
    )
