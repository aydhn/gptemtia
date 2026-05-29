"""
Sample data builder for generating synthetic offline data packs.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, Tuple
from datetime import datetime, timedelta

from scenarios.scenario_config import ScenarioProfile

class SampleDataBuilderError(Exception):
    pass


def _generate_synthetic_prices(rows: int, seed: int, start_price: float, volatility: float, trend: float) -> np.ndarray:
    """Helper to generate a random walk."""
    np.random.seed(seed)
    returns = np.random.normal(loc=trend, scale=volatility, size=rows)
    prices = start_price * np.exp(np.cumsum(returns))
    return np.maximum(prices, 0.0001)


def build_synthetic_ohlcv(symbol: str, rows: int, seed: int = 42, regime: str = "mixed") -> pd.DataFrame:
    """Builds a completely synthetic OHLCV DataFrame."""
    np.random.seed(seed)

    end_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    dates = [end_date - timedelta(days=x) for x in range(rows - 1, -1, -1)]

    # Base parameters based on regime
    start_price = 100.0
    volatility = 0.02
    trend = 0.0

    if regime == "trend_up":
        trend = 0.002
    elif regime == "trend_down":
        trend = -0.002
    elif regime == "mean_reversion":
        volatility = 0.01
    elif regime == "volatile":
        volatility = 0.05
    elif regime == "calm":
        volatility = 0.005

    closes = _generate_synthetic_prices(rows, seed, start_price, volatility, trend)

    # Generate OHLC
    highs = closes * (1 + np.abs(np.random.normal(0, volatility/2, rows)))
    lows = closes * (1 - np.abs(np.random.normal(0, volatility/2, rows)))
    opens = (highs + lows) / 2

    # Add some noise to make open different from previous close
    opens[1:] = closes[:-1] * (1 + np.random.normal(0, volatility/4, rows-1))

    # Ensure High is highest and Low is lowest
    highs = np.maximum(np.maximum(opens, closes), highs)
    lows = np.minimum(np.minimum(opens, closes), lows)

    volumes = np.random.lognormal(mean=10, sigma=1, size=rows)

    df = pd.DataFrame({
        "timestamp": dates,
        "open": opens,
        "high": highs,
        "low": lows,
        "close": closes,
        "volume": volumes,
        "symbol": symbol,
        "synthetic": True,
        "regime_label": regime
    })

    df.set_index("timestamp", inplace=True)
    return df


def build_synthetic_macro_series(name: str, rows: int, seed: int = 42) -> pd.DataFrame:
    """Builds synthetic macroeconomic data (like interest rates or GDP)."""
    np.random.seed(seed)
    end_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    dates = [end_date - timedelta(days=x) for x in range(rows - 1, -1, -1)]

    values = _generate_synthetic_prices(rows, seed, start_price=5.0, volatility=0.01, trend=0.0)

    df = pd.DataFrame({
        "timestamp": dates,
        "value": values,
        "series_name": name,
        "synthetic": True
    })
    df.set_index("timestamp", inplace=True)
    return df


def build_synthetic_inflation_series(country: str, rows: int, seed: int = 42) -> pd.DataFrame:
    """Builds synthetic inflation data."""
    return build_synthetic_macro_series(f"{country}_inflation", rows, seed)


def build_synthetic_fx_series(symbol: str, rows: int, seed: int = 42) -> pd.DataFrame:
    """Builds synthetic FX OHLCV data."""
    return build_synthetic_ohlcv(symbol, rows, seed, regime="mean_reversion")


def build_synthetic_benchmark_series(name: str, rows: int, seed: int = 42) -> pd.DataFrame:
    """Builds synthetic benchmark index data."""
    return build_synthetic_macro_series(f"benchmark_{name}", rows, seed)


def build_sample_data_pack(profile: ScenarioProfile) -> Tuple[Dict[str, pd.DataFrame], dict]:
    """Generates a full pack of synthetic data for a profile."""
    data_pack = {}
    rows = min(profile.max_rows_per_symbol, 200) # Reasonable default for sample data

    symbols_to_generate = ["GC=F", "CL=F", "SI=F", "HG=F", "USDTRY=X"]

    for i, symbol in enumerate(symbols_to_generate[:profile.max_symbols]):
        if "=" in symbol:
            # Assume FX or similar
            data_pack[symbol] = build_synthetic_fx_series(symbol, rows, seed=profile.random_seed + i)
        else:
            # Assume Commodity
            data_pack[symbol] = build_synthetic_ohlcv(symbol, rows, seed=profile.random_seed + i, regime="trend_up")

    # Macro and Benchmark
    data_pack["macro_US_IR"] = build_synthetic_macro_series("US_Interest_Rate", rows, profile.random_seed)
    data_pack["inflation_US"] = build_synthetic_inflation_series("US", rows, profile.random_seed)
    data_pack["benchmark_SPY"] = build_synthetic_benchmark_series("SPY", rows, profile.random_seed)

    summary = {
        "profile": profile.name,
        "total_series_generated": len(data_pack),
        "rows_per_series": rows,
        "synthetic_flag_enforced": True,
        "real_market_download_attempted": False,
        "warnings": ["This is entirely synthetic data for offline scenarios. No real market data used."]
    }

    return data_pack, summary


def save_sample_data_pack(data_pack: Dict[str, pd.DataFrame], output_dir: Path) -> Tuple[pd.DataFrame, dict]:
    """Saves the generated sample data pack to CSV files and returns a manifest."""
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_records = []

    for name, df in data_pack.items():
        file_path = output_dir / f"synthetic_{name.replace('=', '_')}.csv"
        df.to_csv(file_path)

        manifest_records.append({
            "series_name": name,
            "path": str(file_path),
            "rows": len(df),
            "synthetic": True,
            "saved_at_utc": datetime.utcnow().isoformat()
        })

    manifest_df = pd.DataFrame(manifest_records)
    summary = {
        "files_saved": len(manifest_records),
        "output_dir": str(output_dir),
        "warnings": ["Data is synthetic. Do not use for live trading."]
    }

    return manifest_df, summary
