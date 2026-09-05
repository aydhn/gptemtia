import re
from typing import Tuple, Dict, Any, List, Optional
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile
from advanced_feature_grid.feature_grid_models import FORBIDDEN_OUTPUT_WORDS


NAMING_CONVENTIONS = [
    {
        "indicator_name": "sma",
        "pattern": "sma_w{window}",
        "example": "sma_w20",
        "family": "moving_average",
    },
    {
        "indicator_name": "ema",
        "pattern": "ema_w{window}",
        "example": "ema_w50",
        "family": "moving_average",
    },
    {
        "indicator_name": "wma",
        "pattern": "wma_w{window}",
        "example": "wma_w20",
        "family": "moving_average",
    },
    {
        "indicator_name": "rsi",
        "pattern": "rsi_w{window}",
        "example": "rsi_w14",
        "family": "momentum",
    },
    {
        "indicator_name": "roc",
        "pattern": "roc_w{window}",
        "example": "roc_w10",
        "family": "momentum",
    },
    {
        "indicator_name": "atr",
        "pattern": "atr_w{window}",
        "example": "atr_w14",
        "family": "volatility",
    },
    {
        "indicator_name": "bollinger",
        "pattern": "bb_{band}_w{window}_std{num_std}",
        "example": "bb_width_w20_std2",
        "family": "range_channel",
    },
    {
        "indicator_name": "donchian",
        "pattern": "donchian_{channel}_w{window}",
        "example": "donchian_high_w20",
        "family": "range_channel",
    },
    {
        "indicator_name": "rolling_zscore",
        "pattern": "zscore_w{window}",
        "example": "zscore_w20",
        "family": "mean_reversion",
    },
    {
        "indicator_name": "realized_volatility",
        "pattern": "realized_vol_w{window}",
        "example": "realized_vol_w20",
        "family": "volatility",
    },
    {
        "indicator_name": "simple_return",
        "pattern": "return_w{window}",
        "example": "return_w5",
        "family": "return",
    },
]


def build_feature_grid_column_name(
    indicator_name: str,
    parameters: Dict[str, Any],
    prefix: Optional[str] = None,
    subcomponent: Optional[str] = None,
) -> str:
    parts = []
    if prefix:
        parts.append(prefix.strip().lower())

    base_indicator = indicator_name.strip().lower()
    if subcomponent:
        parts.append(f"{base_indicator}_{subcomponent.strip().lower()}")
    else:
        parts.append(base_indicator)

    # Sort parameters deterministically with window prioritized first
    def key_priority(k: str) -> int:
        if k in ("window", "w", "period", "n"):
            return 0
        if k in ("num_std", "std", "std_dev"):
            return 1
        return 2

    sorted_keys = sorted(parameters.keys(), key=lambda k: (key_priority(k), k))
    for k in sorted_keys:
        val = parameters[k]
        if isinstance(val, float):
            # Format float cleanly (e.g. 2.0 -> 2, 2.5 -> 2_5)
            val_str = str(val).replace(".", "_")
            if val_str.endswith("_0"):
                val_str = val_str[:-2]
        else:
            val_str = str(val)

        if k in ("window", "w", "period", "n"):
            parts.append(f"w{val_str}")
        elif k in ("num_std", "std", "std_dev"):
            parts.append(f"std{val_str}")
        else:
            parts.append(f"{k}_{val_str}")

    col_name = "_".join(parts)
    col_name = re.sub(r"[^a-zA-Z0-9_]+", "_", col_name)
    col_name = re.sub(r"_+", "_", col_name).strip("_").lower()
    return col_name


def validate_feature_grid_column_name(name: str) -> Dict[str, Any]:
    errors = []
    warnings = []

    if not name or not isinstance(name, str):
        return {
            "valid": False,
            "name": name,
            "errors": ["Kolon ismi boş veya string tipinde değil."],
            "warnings": [],
        }

    lower_name = name.lower()

    # Check snake_case
    if not re.match(r"^[a-z0-9_]+$", lower_name):
        errors.append(f"'{name}' geçerli snake_case formatında değil.")

    # Check forbidden words
    for fw in FORBIDDEN_OUTPUT_WORDS:
        # Check as whole token or part of token
        tokens = lower_name.split("_")
        if fw in tokens or fw in lower_name:
            errors.append(f"'{name}' yasaklı kelime içeriyor: '{fw}'. Sinyal/hedef kolonları yasaktır.")

    return {
        "valid": len(errors) == 0,
        "name": lower_name,
        "errors": errors,
        "warnings": warnings,
    }


def build_feature_grid_naming_registry(
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    df = pd.DataFrame(NAMING_CONVENTIONS)
    summary = summarize_feature_grid_naming(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_naming(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_rules": 0, "status": "EMPTY"}

    return {
        "total_rules": len(df),
        "total_families": df["family"].nunique() if "family" in df.columns else 0,
        "forbidden_words_count": len(FORBIDDEN_OUTPUT_WORDS),
        "naming_standard": "lowercase_snake_case",
        "status": "READY",
    }
