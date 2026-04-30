import logging
from typing import Optional

import pandas as pd

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake

logger = logging.getLogger(__name__)

class FeatureStore:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def load_trend_features(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, feature_set_name="trend"):
            return self.data_lake.load_features(spec, timeframe, feature_set_name="trend")
        return pd.DataFrame()

    def load_trend_events(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, feature_set_name="trend_events"):
            return self.data_lake.load_features(spec, timeframe, feature_set_name="trend_events")
        return pd.DataFrame()

    def list_available_trend_features(self, spec: SymbolSpec) -> dict:
        features = self.data_lake.list_feature_timeframes(spec, feature_set_name="trend")
        events = self.data_lake.list_feature_timeframes(spec, feature_set_name="trend_events")
        return {
            "trend_features": features,
            "trend_events": events,
        }

    def load_volatility_features(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, feature_set_name="volatility"):
            return self.data_lake.load_features(spec, timeframe, feature_set_name="volatility")
        return pd.DataFrame()

    def load_volatility_events(self, spec: SymbolSpec, timeframe: str) -> pd.DataFrame:
        if self.data_lake.has_features(spec, timeframe, feature_set_name="volatility_events"):
            return self.data_lake.load_features(spec, timeframe, feature_set_name="volatility_events")
        return pd.DataFrame()

    def list_available_volatility_features(self, spec: SymbolSpec) -> dict:
        features = self.data_lake.list_feature_timeframes(spec, feature_set_name="volatility")
        events = self.data_lake.list_feature_timeframes(spec, feature_set_name="volatility_events")
        return {
            "volatility_features": features,
            "volatility_events": events,
        }
