import pandas as pd
import numpy as np
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


class UniverseReturnsBuilder:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_close_prices(
        self,
        specs: list[SymbolSpec],
        timeframe: str,
    ) -> tuple[pd.DataFrame, dict]:
        close_series = {}
        warnings = []

        for spec in specs:
            try:
                df = self.data_lake.load_processed_ohlcv(spec.symbol, timeframe)
                if df is not None and not df.empty and 'close' in df.columns:
                    close_series[spec.symbol] = df['close']
                else:
                    warnings.append(f"Missing or invalid close data for {spec.symbol}")
            except Exception as e:
                warnings.append(f"Error loading {spec.symbol}: {e}")

        if not close_series:
            return pd.DataFrame(), {"warnings": warnings}

        close_df = pd.DataFrame(close_series)

        # Check index issues
        if close_df.index.has_duplicates:
            warnings.append("Duplicate index found. Taking last.")
            close_df = close_df[~close_df.index.duplicated(keep='last')]

        if not close_df.index.is_monotonic_increasing:
            warnings.append("Index not monotonic increasing. Sorting.")
            close_df = close_df.sort_index()

        return close_df, {"warnings": warnings}

    def build_returns_matrix(
        self,
        close_df: pd.DataFrame,
        method: str = "log",
    ) -> tuple[pd.DataFrame, dict]:
        warnings = []

        if close_df.empty:
            return pd.DataFrame(), {"warnings": ["Empty close_df."]}

        if method == "log":
            returns_df = np.log(close_df / close_df.shift(1))
        elif method == "simple":
            returns_df = close_df.pct_change()
        else:
            warnings.append(f"Invalid method {method}, using log returns.")
            returns_df = np.log(close_df / close_df.shift(1))

        returns_df = returns_df.dropna(how='all')

        return returns_df, {"warnings": warnings, "method": method}

    def align_universe_returns(
        self,
        returns_df: pd.DataFrame,
        min_observations: int = 120,
    ) -> tuple[pd.DataFrame, dict]:
        warnings = []

        if returns_df.empty:
            return pd.DataFrame(), {"warnings": ["Empty returns_df."]}

        valid_counts = returns_df.count()
        valid_symbols = valid_counts[valid_counts >= min_observations].index.tolist()

        dropped = set(returns_df.columns) - set(valid_symbols)
        if dropped:
            warnings.append(f"Dropped symbols due to insufficient data (<{min_observations}): {list(dropped)}")

        aligned_df = returns_df[valid_symbols].dropna(how='all')

        return aligned_df, {"warnings": warnings}
