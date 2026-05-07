from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
import hashlib
import pandas as pd
from sizing.sizing_models import safe_positive_float

@dataclass
class SizingCandidate:
    symbol: str
    timeframe: str
    timestamp: str
    sizing_id: str
    source_risk_id: str
    source_rule_condition_id: str
    strategy_family: str
    condition_label: str
    directional_bias: str
    asset_class: str
    sizing_label: str
    sizing_method: str
    sizing_severity: str
    theoretical_account_equity: float
    theoretical_risk_amount: float
    capped_theoretical_risk_amount: float
    latest_close: Optional[float]
    atr_value: Optional[float]
    atr_pct: Optional[float]
    volatility_adjustment_factor: float
    risk_adjustment_factor: float
    combined_adjustment_factor: float
    theoretical_units: float
    adjusted_theoretical_units: float
    theoretical_notional: Optional[float]
    adjusted_theoretical_notional: Optional[float]
    total_pretrade_risk_score: float
    risk_readiness_score: float
    sizing_readiness_score: float
    sizing_quality_score: float
    passed_sizing_filters: bool
    block_reasons: List[str]
    watchlist_reasons: List[str]
    warnings: List[str]
    notes: str = ""

def build_sizing_id(symbol: str, timeframe: str, timestamp: str, source_risk_id: str) -> str:
    """Generates a deterministic sizing candidate ID."""
    raw = f"{symbol}_{timeframe}_{timestamp}_{source_risk_id}"
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16]

def sizing_candidate_to_dict(candidate: SizingCandidate) -> Dict[str, Any]:
    return asdict(candidate)

def build_sizing_candidate_from_evaluation(
    risk_row: pd.Series,
    evaluation: Dict[str, Any],
    symbol: str,
    timeframe: str
) -> SizingCandidate:
    """Builds a SizingCandidate dataclass from evaluation context."""

    timestamp = str(risk_row.name) if isinstance(risk_row.name, (pd.Timestamp, str)) else str(risk_row.get("timestamp", ""))
    source_risk_id = risk_row.get("risk_id", "")
    sizing_id = build_sizing_id(symbol, timeframe, timestamp, source_risk_id)

    # Calculate a proxy for sizing readiness
    risk_readiness = safe_positive_float(risk_row.get("risk_readiness_score", 0.0)) or 0.0
    combined_adj = evaluation.get("combined_adjustment_factor", 1.0)
    sizing_readiness_score = risk_readiness * combined_adj

    sizing_quality_score = 1.0
    if len(evaluation.get("block_reasons", [])) > 0:
        sizing_quality_score -= 0.5
    if len(evaluation.get("warnings", [])) > 0:
        sizing_quality_score -= 0.1 * len(evaluation.get("warnings", []))
    sizing_quality_score = max(0.0, min(1.0, sizing_quality_score))

    return SizingCandidate(
        symbol=symbol,
        timeframe=timeframe,
        timestamp=timestamp,
        sizing_id=sizing_id,
        source_risk_id=source_risk_id,
        source_rule_condition_id=risk_row.get("source_rule_condition_id", ""),
        strategy_family=risk_row.get("strategy_family", ""),
        condition_label=risk_row.get("condition_label", ""),
        directional_bias=risk_row.get("directional_bias", ""),
        asset_class=risk_row.get("asset_class", ""),
        sizing_label=evaluation.get("sizing_label", "unknown_sizing_candidate"),
        sizing_method=evaluation.get("sizing_method", "unknown_sizing_method"),
        sizing_severity=evaluation.get("sizing_severity", "unknown"),
        theoretical_account_equity=evaluation.get("theoretical_account_equity", 0.0),
        theoretical_risk_amount=evaluation.get("theoretical_risk_amount", 0.0),
        capped_theoretical_risk_amount=evaluation.get("capped_theoretical_risk_amount", 0.0),
        latest_close=evaluation.get("latest_close"),
        atr_value=evaluation.get("atr_value"),
        atr_pct=evaluation.get("atr_pct"),
        volatility_adjustment_factor=evaluation.get("volatility_adjustment_factor", 1.0),
        risk_adjustment_factor=evaluation.get("risk_adjustment_factor", 1.0),
        combined_adjustment_factor=combined_adj,
        theoretical_units=evaluation.get("theoretical_units", 0.0),
        adjusted_theoretical_units=evaluation.get("adjusted_theoretical_units", 0.0),
        theoretical_notional=evaluation.get("theoretical_notional"),
        adjusted_theoretical_notional=evaluation.get("adjusted_theoretical_notional"),
        total_pretrade_risk_score=safe_positive_float(risk_row.get("total_pretrade_risk_score", 0.0)) or 0.0,
        risk_readiness_score=risk_readiness,
        sizing_readiness_score=sizing_readiness_score,
        sizing_quality_score=sizing_quality_score,
        passed_sizing_filters=evaluation.get("passed_sizing_filters", False),
        block_reasons=evaluation.get("block_reasons", []),
        watchlist_reasons=evaluation.get("watchlist_reasons", []),
        warnings=evaluation.get("warnings", []),
        notes=evaluation.get("notes", "")
    )
