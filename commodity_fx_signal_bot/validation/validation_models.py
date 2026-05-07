"""
Data models for validation processes.
"""

import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class TimeSplit:
    """Represents a specific train/test split for walk-forward validation."""
    split_id: str
    train_start: str
    train_end: str
    test_start: str
    test_end: str
    train_bars: int
    test_bars: int
    split_index: int


@dataclass
class ValidationRunResult:
    """Represents the overall result of a validation run."""
    run_id: str
    symbol: str
    timeframe: str
    validation_profile: str
    parameter_set_id: str
    split_count: int
    train_summary: dict
    test_summary: dict
    walk_forward_summary: dict
    robustness_score: float
    overfitting_risk_score: float
    stability_score: float
    validation_status: str
    warnings: list[str]


@dataclass
class ParameterSet:
    """Represents a specific set of parameters to be evaluated."""
    parameter_set_id: str
    parameters: dict
    description: str = ""
    enabled: bool = True


def build_validation_run_id(symbol: str, timeframe: str, profile_name: str, parameter_set_id: str) -> str:
    """Builds a deterministic ID for a validation run."""
    components = [symbol, timeframe, profile_name, parameter_set_id]
    base_string = "_".join(str(c) for c in components)
    return hashlib.sha256(base_string.encode()).hexdigest()[:16]


def build_split_id(symbol: str, timeframe: str, split_index: int) -> str:
    """Builds a deterministic ID for a time split."""
    base_string = f"{symbol}_{timeframe}_split_{split_index}"
    return hashlib.sha256(base_string.encode()).hexdigest()[:12]


def build_parameter_set_id(parameters: dict) -> str:
    """Builds a deterministic ID for a parameter set based on its content."""
    # Sort keys to ensure consistent hashing
    param_str = json.dumps(parameters, sort_keys=True)
    return hashlib.sha256(param_str.encode()).hexdigest()[:12]


def time_split_to_dict(split: TimeSplit) -> dict[str, Any]:
    """Converts a TimeSplit to a dictionary."""
    return asdict(split)


def validation_run_result_to_dict(result: ValidationRunResult) -> dict[str, Any]:
    """Converts a ValidationRunResult to a dictionary."""
    return asdict(result)


def parameter_set_to_dict(parameter_set: ParameterSet) -> dict[str, Any]:
    """Converts a ParameterSet to a dictionary."""
    return asdict(parameter_set)
