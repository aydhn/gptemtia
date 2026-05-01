import pandas as pd
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


class MTFFeatureLoader:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_feature_set(
        self,
        spec: SymbolSpec,
        timeframe: str,
        feature_set_name: str,
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, feature_set_name):
            return self.data_lake.load_features(spec, timeframe, feature_set_name)
        return pd.DataFrame()

    def load_context_features(
        self,
        spec: SymbolSpec,
        timeframes: tuple[str, ...],
        feature_sets: tuple[str, ...],
    ) -> dict[str, dict[str, pd.DataFrame]]:
        result = {}
        for tf in timeframes:
            result[tf] = {}
            for fset in feature_sets:
                df = self.load_feature_set(spec, tf, fset)
                if not df.empty:
                    result[tf][fset] = df
        return result

    def load_best_available_base_frame(
        self,
        spec: SymbolSpec,
        base_timeframe: str,
        preferred_feature_sets: tuple[str, ...],
    ) -> tuple[pd.DataFrame, dict]:
        summary = {"missing": []}
        best_df = pd.DataFrame()

        for fset in preferred_feature_sets:
            df = self.load_feature_set(spec, base_timeframe, fset)
            if not df.empty:
                if best_df.empty:
                    best_df = df
                else:
                    # Merge if possible or just use the first valid one as base
                    pass
            else:
                summary["missing"].append(fset)

        if best_df.empty:
            # Fallback to OHLCV processed
            if self.data_lake.has_processed_ohlcv(spec, base_timeframe):
                best_df = self.data_lake.load_processed_ohlcv(spec, base_timeframe)
            else:
                summary["missing"].append("processed_ohlcv")

        return best_df, summary
