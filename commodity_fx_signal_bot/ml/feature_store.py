import pandas as pd
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


class FeatureStore:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_mtf_features(
        self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "mtf"):
            return self.data_lake.load_features(spec, timeframe, "mtf")
        return pd.DataFrame()

    def load_mtf_events(
        self, spec: SymbolSpec, timeframe: str, profile_name: str | None = None
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "mtf_events"):
            return self.data_lake.load_features(spec, timeframe, "mtf_events")
        return pd.DataFrame()

    def list_available_mtf_features(self, spec: SymbolSpec) -> dict:
        return {
            "mtf": self.data_lake.list_feature_timeframes(spec, "mtf"),
            "mtf_events": self.data_lake.list_feature_timeframes(spec, "mtf_events"),
        }

    def load_regime_features(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime"):
            return self.data_lake.load_features(spec, timeframe, "regime")
        return pd.DataFrame()

    def load_regime_events(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime_events"):
            return self.data_lake.load_features(spec, timeframe, "regime_events")
        return pd.DataFrame()

    def list_available_regime_features(self, spec: SymbolSpec) -> dict:
        return {
            "regime": self.data_lake.list_feature_timeframes(spec, "regime"),
            "regime_events": self.data_lake.list_feature_timeframes(
                spec, "regime_events"
            ),
        }

    def load_macro_features(self) -> pd.DataFrame:
        """Load macro features from the data lake."""
        try:
            return self.data_lake.load_feature_set("macro", "macro_features")
        except Exception:
            return pd.DataFrame()

    def load_macro_events(self) -> pd.DataFrame:
        """Load macro events from the data lake."""
        try:
            return self.data_lake.load_feature_set("macro_events", "macro_events")
        except Exception:
            return pd.DataFrame()

    def load_benchmark_features(self) -> pd.DataFrame:
        """Load benchmark features from the data lake."""
        try:
            return self.data_lake.load_feature_set("benchmarks", "benchmark_features")
        except Exception:
            return pd.DataFrame()

    def list_available_macro_features(self) -> dict:
        """List available macro and benchmark features."""
        features = {}

        macro_df = self.load_macro_features()
        if not macro_df.empty:
            features["macro_features"] = list(macro_df.columns)

        events_df = self.load_macro_events()
        if not events_df.empty:
            features["macro_events"] = list(events_df.columns)

        benchmarks_df = self.load_benchmark_features()
        if not benchmarks_df.empty:
            features["benchmarks"] = list(benchmarks_df.columns)

        return features

    def load_asset_profile_features(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "asset_profiles"):
            return self.data_lake.load_features(spec, timeframe, "asset_profiles")
        return pd.DataFrame()

    def load_asset_profile_events(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "asset_profile_events"):
            return self.data_lake.load_features(spec, timeframe, "asset_profile_events")
        return pd.DataFrame()

    def load_group_features(self, asset_class: str, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_group_features(asset_class, timeframe):
            return self.data_lake.load_group_features(asset_class, timeframe)
        return pd.DataFrame()

    def list_available_asset_profile_features(self, spec: SymbolSpec) -> dict:
        return {
            "asset_profiles": self.data_lake.list_feature_timeframes(
                spec, "asset_profiles"
            ),
            "asset_profile_events": self.data_lake.list_feature_timeframes(
                spec, "asset_profile_events"
            ),
        }

    def list_available_group_features(self, asset_class: str) -> dict:
        return {
            "group_features": self.data_lake.list_group_feature_timeframes(asset_class)
        }
