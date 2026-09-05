from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_technical_indicators.technical_indicator_config import TechnicalIndicatorProfile
from advanced_technical_indicators.technical_indicator_models import (
    IndicatorParameterContract,
    build_indicator_parameter_id,
)

PARAMETER_CONTRACTS_DATA = [
    {"indicator": "sma", "param": "window", "type": "int", "default": 20, "min": 2, "max": 1000, "allowed": []},
    {"indicator": "ema", "param": "window", "type": "int", "default": 20, "min": 2, "max": 1000, "allowed": []},
    {"indicator": "wma", "param": "window", "type": "int", "default": 20, "min": 2, "max": 1000, "allowed": []},
    {"indicator": "dema", "param": "window", "type": "int", "default": 20, "min": 2, "max": 1000, "allowed": []},
    {"indicator": "tema", "param": "window", "type": "int", "default": 20, "min": 2, "max": 1000, "allowed": []},
    {"indicator": "rsi", "param": "window", "type": "int", "default": 14, "min": 2, "max": 500, "allowed": []},
    {"indicator": "cmo", "param": "window", "type": "int", "default": 14, "min": 2, "max": 500, "allowed": []},
    {"indicator": "roc", "param": "window", "type": "int", "default": 10, "min": 1, "max": 500, "allowed": []},
    {"indicator": "momentum", "param": "window", "type": "int", "default": 10, "min": 1, "max": 500, "allowed": []},
    {"indicator": "atr", "param": "window", "type": "int", "default": 14, "min": 2, "max": 500, "allowed": []},
    {"indicator": "bollinger_bands", "param": "window", "type": "int", "default": 20, "min": 2, "max": 500, "allowed": []},
    {"indicator": "bollinger_bands", "param": "num_std", "type": "float", "default": 2.0, "min": 0.5, "max": 5.0, "allowed": []},
    {"indicator": "donchian_channel", "param": "window", "type": "int", "default": 20, "min": 2, "max": 500, "allowed": []},
    {"indicator": "stochastic", "param": "k_window", "type": "int", "default": 14, "min": 2, "max": 500, "allowed": []},
    {"indicator": "stochastic", "param": "d_window", "type": "int", "default": 3, "min": 1, "max": 100, "allowed": []},
    {"indicator": "williams_r", "param": "window", "type": "int", "default": 14, "min": 2, "max": 500, "allowed": []},
    {"indicator": "cci", "param": "window", "type": "int", "default": 20, "min": 2, "max": 500, "allowed": []},
    {"indicator": "macd", "param": "fast", "type": "int", "default": 12, "min": 2, "max": 200, "allowed": []},
    {"indicator": "macd", "param": "slow", "type": "int", "default": 26, "min": 3, "max": 500, "allowed": []},
    {"indicator": "macd", "param": "signal_window", "type": "int", "default": 9, "min": 1, "max": 100, "allowed": []},
    {"indicator": "rolling_zscore", "param": "window", "type": "int", "default": 20, "min": 2, "max": 500, "allowed": []},
]


def validate_indicator_window(window: int, min_window: int = 2, max_window: int = 1000) -> Dict[str, Any]:
    if not isinstance(window, int):
        return {"valid": False, "error": f"Window must be an integer, got {type(window).__name__}"}
    if window < min_window:
        return {"valid": False, "error": f"Window ({window}) < min_window ({min_window})"}
    if window > max_window:
        return {"valid": False, "error": f"Window ({window}) > max_window ({max_window})"}
    return {"valid": True, "error": None}


def validate_indicator_parameters(indicator_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
    errors = []
    for k, v in parameters.items():
        if "window" in k or k in ("fast", "slow", "k_window", "d_window", "signal_window"):
            res = validate_indicator_window(v, min_window=1 if k in ("signal_window", "d_window", "window") else 2)
            if not res["valid"]:
                errors.append(f"{k}: {res['error']}")
        elif k == "num_std":
            if not isinstance(v, (int, float)) or v <= 0:
                errors.append(f"num_std must be positive float, got {v}")
    return {"valid": len(errors) == 0, "errors": errors}


def build_indicator_parameter_contract_registry(
    profile: TechnicalIndicatorProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    items = []
    for c in PARAMETER_CONTRACTS_DATA:
        item = IndicatorParameterContract(
            parameter_id=build_indicator_parameter_id(c["indicator"], c["param"]),
            indicator_name=c["indicator"],
            parameter_name=c["param"],
            parameter_type=c["type"],
            default_value=c["default"],
            min_value=c["min"],
            max_value=c["max"],
            allowed_values=c["allowed"],
            validation_note=f"Bounded range [{c['min']}, {c['max']}]",
            manual_review_required=False,
        )
        items.append(item.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "total_parameter_contracts": len(df),
        "total_indicators_covered": len(df["indicator_name"].unique()),
        "status": "READY",
        "current_phase": profile.current_phase,
    }
    return df, summary


def summarize_indicator_parameter_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_contracts": len(df),
        "indicators": sorted(list(df["indicator_name"].unique())) if not df.empty else [],
    }
