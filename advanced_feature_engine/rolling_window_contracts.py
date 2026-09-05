from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile

STANDARD_ROLLING_WINDOWS = [5, 10, 14, 20, 50, 100, 200]


def validate_rolling_window(window: int) -> Dict[str, Any]:
    if not isinstance(window, int):
        return {
            "valid": False,
            "window": window,
            "error": f"Rolling window must be an integer, got {type(window).__name__}",
        }
    if window < 2:
        return {
            "valid": False,
            "window": window,
            "error": f"Rolling window must be >= 2, got {window}",
        }
    return {
        "valid": True,
        "window": window,
        "is_standard": window in STANDARD_ROLLING_WINDOWS,
        "lookahead_safe": True,
    }


def build_rolling_window_contract_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[Dict[str, Any]] = []

    descriptions = {
        5: "Kısa vadeli mikro pencere (1 hafta yaklaşık)",
        10: "İki haftalık kısa vadeli momentum/volatilite penceresi",
        14: "RSI ve ATR standart salınım penceresi",
        20: "Bir aylık standart trend ve Bollinger bandı penceresi",
        50: "Orta vadeli çeyreklik trend referans penceresi",
        100: "Uzun vadeli altı aylık rejim referans penceresi",
        200: "Makro ve uzun vadeli yıllık trend referans penceresi",
    }

    for w in STANDARD_ROLLING_WINDOWS:
        records.append({
            "window_size": w,
            "description": descriptions.get(w, f"{w} barlık pencere"),
            "minimum_allowed": 2,
            "lookahead_bias_guarded": True,
            "warmup_nan_count": w - 1,
            "non_signal": True,
            "policy_note": "Yalnızca geçmiş ve mevcut barları kullanır ([t - window + 1 : t]); shift(-1) kesinlikle yasaktır.",
        })

    df = pd.DataFrame.from_records(records)
    summary = summarize_rolling_window_contracts(df)
    return df, summary


def summarize_rolling_window_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_standard_windows": len(df),
        "windows": df["window_size"].tolist() if not df.empty and "window_size" in df.columns else [],
        "min_window": int(df["window_size"].min()) if not df.empty and "window_size" in df.columns else 0,
        "max_window": int(df["window_size"].max()) if not df.empty and "window_size" in df.columns else 0,
        "all_lookahead_guarded": True,
        "non_signal": True,
    }
