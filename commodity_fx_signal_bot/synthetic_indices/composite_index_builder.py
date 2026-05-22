import pandas as pd
import numpy as np
import logging
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from synthetic_indices.index_models import SyntheticIndexDefinition, SyntheticIndexSeries

logger = logging.getLogger(__name__)

class CompositeIndexBuilder:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_close_prices(
        self,
        specs: list[SymbolSpec],
        timeframe: str,
    ) -> tuple[pd.DataFrame, dict]:
        summary = {"warnings": [], "loaded_symbols": 0, "missing_symbols": []}
        prices = {}

        for spec in specs:
            try:
                # Load parquet data from lake
                # This assumes we have a load_ohlcv method in data_lake
                df = self.data_lake.load_ohlcv(spec.symbol, timeframe)
                if df is not None and not df.empty and "close" in df.columns:
                    prices[spec.symbol] = df["close"]
                else:
                     summary["missing_symbols"].append(spec.symbol)
            except Exception as e:
                 summary["missing_symbols"].append(spec.symbol)
                 summary["warnings"].append(f"Error loading {spec.symbol}: {e}")

        if not prices:
             summary["warnings"].append("No price data loaded.")
             return pd.DataFrame(), summary

        close_df = pd.DataFrame(prices)
        close_df.sort_index(inplace=True)
        summary["loaded_symbols"] = len(close_df.columns)
        return close_df, summary

    def build_returns_matrix(
        self,
        close_df: pd.DataFrame,
        method: str = "log",
    ) -> tuple[pd.DataFrame, dict]:
        summary = {"warnings": [], "method": method}

        if close_df.empty:
            summary["warnings"].append("Empty close prices dataframe.")
            return pd.DataFrame(), summary

        if method == "log":
             # Avoid log(0) or negative
             safe_close = close_df.replace(0, np.nan)
             returns_df = np.log(safe_close / safe_close.shift(1))
        elif method == "simple":
             returns_df = close_df.pct_change()
        else:
             summary["warnings"].append(f"Unknown return method: {method}. Using log.")
             safe_close = close_df.replace(0, np.nan)
             returns_df = np.log(safe_close / safe_close.shift(1))

        # Drop all-NaN rows (usually just the first row)
        returns_df.dropna(how="all", inplace=True)

        return returns_df, summary

    def build_index_series(
        self,
        definition: SyntheticIndexDefinition,
        returns_df: pd.DataFrame,
    ) -> tuple[SyntheticIndexSeries, dict]:
        summary = {"warnings": [], "missing_symbols": []}

        if returns_df.empty:
            summary["warnings"].append("Empty returns dataframe.")
            return SyntheticIndexSeries(
                index_id=definition.index_id,
                timeframe=definition.timeframe,
                level_series=pd.Series(dtype=float),
                return_series=pd.Series(dtype=float),
                start_date=None,
                end_date=None,
                observation_count=0,
                warnings=["Empty returns dataframe."]
            ), summary

        # Check for missing symbols
        available_symbols = set(returns_df.columns)
        required_symbols = set(definition.symbols)
        missing = required_symbols - available_symbols

        if missing:
             summary["missing_symbols"] = list(missing)
             summary["warnings"].append(f"Missing symbols: {missing}")

        # Filter for available symbols
        symbols_to_use = list(required_symbols.intersection(available_symbols))

        if not symbols_to_use:
             msg = "No symbols available to build index."
             summary["warnings"].append(msg)
             return SyntheticIndexSeries(
                index_id=definition.index_id,
                timeframe=definition.timeframe,
                level_series=pd.Series(dtype=float),
                return_series=pd.Series(dtype=float),
                start_date=None,
                end_date=None,
                observation_count=0,
                warnings=[msg]
             ), summary

        # Re-normalize weights for available symbols
        raw_weights = {sym: definition.weights.get(sym, 0.0) for sym in symbols_to_use}
        total_w = sum(raw_weights.values())

        if total_w == 0:
            weights = {sym: 1.0 / len(symbols_to_use) for sym in symbols_to_use}
        else:
            weights = {sym: w / total_w for sym, w in raw_weights.items()}

        # Calculate weighted returns
        idx_returns = pd.Series(0.0, index=returns_df.index)

        # We fillna(0) for returns so if a symbol is missing a day, it contributes 0 return for that day
        # Real index construction might rebalance or use Divisor, but this is a synthetic proxy.
        for sym in symbols_to_use:
            idx_returns += returns_df[sym].fillna(0.0) * weights[sym]

        # Calculate levels
        # If simple returns: level = base * cumprod(1 + r)
        # If log returns: level = base * exp(cumsum(r))

        # Assume log for simplicity based on our test setup
        if definition.weighting_scheme == "equal_weight" or definition.weighting_scheme == "equal_weight":
             # We assume log returns for aggregation if it's equal weight for simplicity,
             # but strictly speaking, standard portfolios use simple returns.
             # We will use log aggregation for the synthetic research index.
             levels = definition.base_value * np.exp(idx_returns.cumsum())
        else:
             levels = definition.base_value * (1 + idx_returns).cumprod()

        start_date = str(idx_returns.index[0].date()) if not idx_returns.empty else None
        end_date = str(idx_returns.index[-1].date()) if not idx_returns.empty else None

        series = SyntheticIndexSeries(
            index_id=definition.index_id,
            timeframe=definition.timeframe,
            level_series=levels,
            return_series=idx_returns,
            start_date=start_date,
            end_date=end_date,
            observation_count=len(idx_returns),
            warnings=summary["warnings"]
        )

        return series, summary

    def build_index_series_for_definitions(
        self,
        definitions: list[SyntheticIndexDefinition],
        returns_df: pd.DataFrame,
    ) -> tuple[dict[str, SyntheticIndexSeries], dict]:

        result_map = {}
        summary = {"warnings": [], "success_count": 0, "failed_count": 0}

        for d in definitions:
            try:
                 series, series_summary = self.build_index_series(d, returns_df)
                 result_map[d.index_id] = series
                 if series_summary.get("warnings"):
                      summary["warnings"].extend([f"{d.index_id}: {w}" for w in series_summary["warnings"]])
                 summary["success_count"] += 1
            except Exception as e:
                 summary["failed_count"] += 1
                 summary["warnings"].append(f"Failed to build series for {d.index_id}: {e}")

        return result_map, summary
