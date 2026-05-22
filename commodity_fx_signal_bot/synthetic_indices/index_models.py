import pandas as pd
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SyntheticIndexDefinition:
    index_id: str
    index_name: str
    index_type: str
    timeframe: str
    symbols: list[str]
    weights: dict[str, float]
    weighting_scheme: str
    base_value: float
    created_at_utc: str
    methodology: str
    warnings: list[str]

@dataclass
class SyntheticIndexSeries:
    index_id: str
    timeframe: str
    level_series: pd.Series
    return_series: pd.Series
    start_date: str | None
    end_date: str | None
    observation_count: int
    warnings: list[str]

@dataclass
class RelativeStrengthRecord:
    symbol: str
    timeframe: str
    window: int
    relative_to: str
    relative_return: float | None
    relative_rank: int | None
    relative_percentile: float | None
    relative_strength_label: str
    warnings: list[str]

@dataclass
class RotationRecord:
    symbol: str
    timeframe: str
    lookback: int
    rotation_score: float | None
    rotation_rank: int | None
    rotation_label: str
    previous_rank: int | None
    rank_delta: int | None
    warnings: list[str]

def build_synthetic_index_id(index_type: str, timeframe: str, symbols: list[str], weighting_scheme: str) -> str:
    sorted_symbols = sorted(symbols)
    symbol_hash = hash(tuple(sorted_symbols)) % 1000000
    return f"{index_type}_{timeframe}_{weighting_scheme}_{symbol_hash}"

def build_relative_strength_id(symbol: str, timeframe: str, window: int, relative_to: str) -> str:
    return f"rs_{symbol}_{timeframe}_{window}_vs_{relative_to}"

def build_rotation_id(symbol: str, timeframe: str, lookback: int) -> str:
    return f"rot_{symbol}_{timeframe}_{lookback}"

def synthetic_index_definition_to_dict(definition: SyntheticIndexDefinition) -> dict:
    return {
        "index_id": definition.index_id,
        "index_name": definition.index_name,
        "index_type": definition.index_type,
        "timeframe": definition.timeframe,
        "symbols": ",".join(definition.symbols),
        "weights": str(definition.weights),
        "weighting_scheme": definition.weighting_scheme,
        "base_value": definition.base_value,
        "created_at_utc": definition.created_at_utc,
        "methodology": definition.methodology,
        "warnings": str(definition.warnings),
    }

def synthetic_index_series_to_dict(series: SyntheticIndexSeries, include_values: bool = False) -> dict:
    d = {
        "index_id": series.index_id,
        "timeframe": series.timeframe,
        "start_date": series.start_date,
        "end_date": series.end_date,
        "observation_count": series.observation_count,
        "warnings": str(series.warnings),
    }
    if include_values:
        d["level_series"] = series.level_series.to_dict()
        d["return_series"] = series.return_series.to_dict()
    return d

def relative_strength_record_to_dict(record: RelativeStrengthRecord) -> dict:
    return {
        "symbol": record.symbol,
        "timeframe": record.timeframe,
        "window": record.window,
        "relative_to": record.relative_to,
        "relative_return": record.relative_return,
        "relative_rank": record.relative_rank,
        "relative_percentile": record.relative_percentile,
        "relative_strength_label": record.relative_strength_label,
        "warnings": str(record.warnings),
    }

def rotation_record_to_dict(record: RotationRecord) -> dict:
    return {
        "symbol": record.symbol,
        "timeframe": record.timeframe,
        "lookback": record.lookback,
        "rotation_score": record.rotation_score,
        "rotation_rank": record.rotation_rank,
        "rotation_label": record.rotation_label,
        "previous_rank": record.previous_rank,
        "rank_delta": record.rank_delta,
        "warnings": str(record.warnings),
    }

def normalize_index_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(weights.values())
    if total == 0:
        return {k: 1.0 / len(weights) for k in weights}
    return {k: v / total for k, v in weights.items()}
