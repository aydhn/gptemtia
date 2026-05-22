from dataclasses import dataclass, asdict
from typing import Dict, Any, List

@dataclass
class FactorDefinition:
    factor_id: str
    factor_name: str
    factor_type: str
    description: str
    direction: str
    required_inputs: list[str]
    lookback_windows: list[int]
    methodology: str
    warnings: list[str]

@dataclass
class FactorScoreRecord:
    symbol: str
    timeframe: str
    timestamp: str
    factor_id: str
    raw_score: float | None
    normalized_score: float | None
    rank: int | None
    percentile: float | None
    bucket_label: str
    warnings: list[str]

@dataclass
class FactorBacktestResult:
    factor_id: str
    timeframe: str
    horizon: int
    top_bucket_return: float | None
    bottom_bucket_return: float | None
    spread_return: float | None
    hit_rate: float | None
    observation_count: int
    ic_proxy: float | None
    stability_score: float | None
    warnings: list[str]

@dataclass
class FactorNeutralBasket:
    basket_id: str
    timeframe: str
    symbols: list[str]
    weights: dict[str, float]
    neutralized_exposures: dict[str, float]
    methodology: str
    warnings: list[str]

def build_factor_id(factor_name: str, factor_type: str) -> str:
    return f"{factor_type}_{factor_name}".lower().replace(" ", "_")

def build_factor_neutral_basket_id(timeframe: str, symbols: list[str]) -> str:
    symbols_hash = "_".join(sorted(symbols))[:20]
    return f"neutral_basket_{timeframe}_{symbols_hash}"

def factor_definition_to_dict(definition: FactorDefinition) -> dict[str, Any]:
    return asdict(definition)

def factor_score_record_to_dict(record: FactorScoreRecord) -> dict[str, Any]:
    return asdict(record)

def factor_backtest_result_to_dict(result: FactorBacktestResult) -> dict[str, Any]:
    return asdict(result)

def factor_neutral_basket_to_dict(basket: FactorNeutralBasket) -> dict[str, Any]:
    return asdict(basket)

def normalize_factor_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(abs(w) for w in weights.values() if w is not None)
    if total == 0:
        return {k: 0.0 for k in weights.keys()}
    return {k: (w / total if w is not None else 0.0) for k, w in weights.items()}
