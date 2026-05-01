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

    def load_regime_features(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime"):
            return self.data_lake.load_features(spec, timeframe, "regime")
        return pd.DataFrame()

    def load_regime_events(
        self, spec: SymbolSpec, timeframe: str
    ) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, "regime_events"):
            return self.data_lake.load_features(spec, timeframe, "regime_events")
        return pd.DataFrame()

    def list_available_regime_features(self, spec: SymbolSpec) -> dict:
        return {
            "regime": self.data_lake.list_feature_timeframes(spec, "regime"),
            "regime_events": self.data_lake.list_feature_timeframes(spec, "regime_events"),
        }
