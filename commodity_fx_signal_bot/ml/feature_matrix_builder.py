import pandas as pd
import numpy as np
import logging
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

logger = logging.getLogger(__name__)

class FeatureMatrixBuilder:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_feature_set(
        self,
        spec: SymbolSpec,
        timeframe: str,
        feature_set_name: str,
    ) -> tuple[pd.DataFrame, dict]:
        """Loads a specific feature set."""
        try:
             # Map abstract feature set names to data lake loading methods
             # This is a simplified mapping; real implementation would use appropriate methods
             if feature_set_name == "technical":
                  df = self.data_lake.load_technical_indicators(spec.symbol, timeframe)
             elif feature_set_name == "momentum":
                  df = self.data_lake.load_momentum_features(spec.symbol, timeframe)
             elif feature_set_name == "trend":
                  df = self.data_lake.load_trend_features(spec.symbol, timeframe)
             elif feature_set_name == "volatility":
                  df = self.data_lake.load_volatility_features(spec.symbol, timeframe)
             elif feature_set_name == "price_action":
                  df = self.data_lake.load_price_action_features(spec.symbol, timeframe)
             elif feature_set_name == "regime":
                  df = self.data_lake.load_regime_features(spec.symbol, timeframe)
             else:
                  # Fallback/mock for tests and unsupported sets right now
                  logger.warning(f"Feature set loader not implemented for: {feature_set_name}")
                  return pd.DataFrame(), {"warnings": [f"Feature set loader not implemented: {feature_set_name}"]}

             if df is None:
                  return pd.DataFrame(), {"warnings": [f"Feature set returned None: {feature_set_name}"]}

             return df, {}

        except Exception as e:
             logger.error(f"Error loading feature set {feature_set_name}: {str(e)}")
             return pd.DataFrame(), {"warnings": [f"Error loading {feature_set_name}: {str(e)}"]}

    def load_feature_sets(
        self,
        spec: SymbolSpec,
        timeframe: str,
        feature_sets: tuple[str, ...],
    ) -> tuple[dict[str, pd.DataFrame], dict]:
        """Load multiple feature sets."""
        loaded_sets = {}
        missing_sets = []
        warnings = []

        for fs in feature_sets:
            df, summary = self.load_feature_set(spec, timeframe, fs)
            if df.empty:
                missing_sets.append(fs)
            else:
                loaded_sets[fs] = df
            if summary.get("warnings"):
                warnings.extend(summary["warnings"])

        return loaded_sets, {
            "loaded_feature_sets": list(loaded_sets.keys()),
            "missing_feature_sets": missing_sets,
            "warnings": warnings
        }

    def build_feature_matrix(
        self,
        spec: SymbolSpec,
        timeframe: str,
        feature_sets: tuple[str, ...],
    ) -> tuple[pd.DataFrame, dict]:
        """Combine feature sets into a single prefixed matrix."""
        # Start with OHLCV as base index
        ohlcv = self.data_lake.load_processed_ohlcv(spec.symbol, timeframe)
        if ohlcv is None or ohlcv.empty:
            return pd.DataFrame(), {"warnings": ["OHLCV data is missing or empty"]}

        base_df = pd.DataFrame(index=ohlcv.index)
        # Include base OHLCV features? Often good practice to include returns or normalized price

        loaded_sets, summary = self.load_feature_sets(spec, timeframe, feature_sets)

        feature_dfs = []
        for fs_name, fs_df in loaded_sets.items():
            # Apply prefix
            prefixed_df = fs_df.copy()
            prefixed_df.columns = [f"{fs_name}__{c}" for c in fs_df.columns]
            feature_dfs.append(prefixed_df)

        if not feature_dfs:
            return base_df, summary

        # Join all
        matrix = base_df.join(feature_dfs, how='left')

        summary["input_columns"] = list(matrix.columns)

        # Clean exclusions
        exclude_patterns = [
             "target_", "_id", "source_", "notes", "warnings", "block_reasons",
             "watchlist_reasons", "conflict_reasons", "no_trade_reasons"
        ]

        cols_to_drop = []
        for col in matrix.columns:
            if any(pattern in col.lower() for pattern in exclude_patterns):
                cols_to_drop.append(col)

        matrix = matrix.drop(columns=cols_to_drop)

        # Drop duplicates if any
        matrix = matrix.loc[:, ~matrix.columns.duplicated()]

        # Convert inf to nan
        matrix = matrix.replace([np.inf, -np.inf], np.nan)

        summary["output_columns"] = list(matrix.columns)
        summary["dropped_columns"] = cols_to_drop

        categorical_cols = list(matrix.select_dtypes(include=['object', 'category']).columns)
        numeric_cols = list(matrix.select_dtypes(include=[np.number]).columns)

        summary["categorical_columns"] = categorical_cols
        summary["numeric_columns"] = numeric_cols

        return matrix, summary

    def clean_feature_matrix(
        self,
        X: pd.DataFrame,
        max_nan_ratio: float = 0.35,
    ) -> tuple[pd.DataFrame, dict]:
        """Remove columns with too many NaNs."""
        nan_ratios = X.isna().mean()
        cols_to_drop = nan_ratios[nan_ratios > max_nan_ratio].index.tolist()

        X_clean = X.drop(columns=cols_to_drop)

        return X_clean, {
             "total_nan_ratio": float(X.isna().mean().mean()) if not X.empty else 0.0,
             "columns_dropped_due_to_nans": cols_to_drop,
             "warnings": [f"Dropped {len(cols_to_drop)} columns due to high NaN ratio"] if cols_to_drop else []
        }
